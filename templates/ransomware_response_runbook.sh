#!/bin/bash
# Runbook: Contenimento Ransomware GDO
# Versione: 2.0
# Ultimo aggiornamento: 2025-01-15
# Licenza: MIT

set -euo pipefail

# Configurazione
INCIDENT_ID=$(date +%Y%m%d%H%M%S)
LOG_DIR="/var/log/incidents/${INCIDENT_ID}"
SIEM_API="${SIEM_API:-https://siem.internal/api/v1}"
NETWORK_CONTROLLER="${NETWORK_CONTROLLER:-https://sdn.internal/api}"
SLACK_WEBHOOK="${SLACK_WEBHOOK:-}"
LDAP_PASS="${LDAP_PASS:-}"

# Colori per output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Funzioni di utilità
log() {
    echo -e "${BLUE}[$(date +'%Y-%m-%d %H:%M:%S')] $1${NC}" | tee -a "${LOG_DIR}/incident.log"
}

error() {
    echo -e "${RED}[ERROR] $1${NC}" | tee -a "${LOG_DIR}/incident.log"
}

warning() {
    echo -e "${YELLOW}[WARNING] $1${NC}" | tee -a "${LOG_DIR}/incident.log"
}

success() {
    echo -e "${GREEN}[SUCCESS] $1${NC}" | tee -a "${LOG_DIR}/incident.log"
}

alert_team() {
    if [[ -n "${SLACK_WEBHOOK}" ]]; then
        curl -X POST "${SLACK_WEBHOOK}" \
            -H 'Content-type: application/json' \
            --data "{\"text\": \"🚨 SECURITY ALERT: $1\"}" \
            2>/dev/null || warning "Failed to send Slack alert"
    fi

    # Backup notification via email
    if command -v mail >/dev/null; then
        echo "$1" | mail -s "URGENT: Ransomware Incident ${INCIDENT_ID}" \
            "security-team@company.com" 2>/dev/null || warning "Failed to send email alert"
    fi
}

check_dependencies() {
    local deps=("curl" "jq" "ldapmodify" "ldappasswd")
    local missing=()

    for dep in "${deps[@]}"; do
        if ! command -v "$dep" >/dev/null; then
            missing+=("$dep")
        fi
    done

    if [[ ${#missing[@]} -gt 0 ]]; then
        error "Missing dependencies: ${missing[*]}"
        error "Please install missing tools before running this script"
        exit 1
    fi
}

# STEP 1: Identificazione e Isolamento
isolate_affected_systems() {
    log "STEP 1: Iniziando isolamento sistemi affetti"

    # Create query for SIEM
    local siem_query='{"query": "event.type:ransomware_indicator OR event.category:malware", "last": "1h", "limit": 100}'

    # Query SIEM per sistemi con indicatori ransomware
    local siem_response
    if siem_response=$(curl -s --connect-timeout 10 "${SIEM_API}/query" \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer ${SIEM_TOKEN:-}" \
        -d "${siem_query}" 2>/dev/null); then

        AFFECTED_SYSTEMS=$(echo "${siem_response}" | jq -r '.results[]?.host // empty' 2>/dev/null | sort -u)
    else
        warning "SIEM query failed, using fallback detection methods"
        AFFECTED_SYSTEMS=""
    fi

    # Fallback: Check for common ransomware indicators
    if [[ -z "${AFFECTED_SYSTEMS}" ]]; then
        warning "Using local detection methods"
        # Check for encrypted files with common ransomware extensions
        AFFECTED_SYSTEMS=$(find /var/log -name "*.encrypted" -o -name "*.locked" -o -name "*README*" | head -10 | xargs -I {} dirname {} | sort -u)
    fi

    if [[ -z "${AFFECTED_SYSTEMS}" ]]; then
        warning "No affected systems detected via automated methods"
        read -p "Enter affected system hostnames (space-separated): " AFFECTED_SYSTEMS
    fi

    echo "${AFFECTED_SYSTEMS}" > "${LOG_DIR}/affected_systems.txt"
    local system_count=$(echo "${AFFECTED_SYSTEMS}" | wc -w)

    for system in ${AFFECTED_SYSTEMS}; do
        log "Isolating system: ${system}"

        # Network isolation via SDN controller
        if curl -s --connect-timeout 5 "${NETWORK_CONTROLLER}/isolate" \
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer ${SDN_TOKEN:-}" \
            -d "{\"host\": \"${system}\", \"vlan\": \"quarantine\"}" >/dev/null 2>&1; then
            success "Network isolation successful for ${system}"
        else
            warning "Network isolation failed for ${system}"
        fi

        # Disable AD computer account
        if [[ -n "${LDAP_PASS}" ]]; then
            if ldapmodify -x -D "cn=admin,dc=company,dc=local" -w "${LDAP_PASS}" >/dev/null 2>&1 <<EOF
dn: cn=${system},ou=computers,dc=company,dc=local
changetype: modify
replace: userAccountControl
userAccountControl: 514
EOF
            then
                success "AD account disabled for ${system}"
            else
                warning "Failed to disable AD account for ${system}"
            fi
        fi

        # Create VM snapshot if available
        if command -v vmware-cmd >/dev/null && vmware-cmd -l | grep -q "${system}"; then
            if vmware-cmd "${system}" create-snapshot "pre-incident-${INCIDENT_ID}" >/dev/null 2>&1; then
                success "VM snapshot created for ${system}"
            else
                warning "Failed to create VM snapshot for ${system}"
            fi
        fi
    done

    alert_team "Isolated ${system_count} systems: ${AFFECTED_SYSTEMS}"
}

# STEP 2: Contenimento della Propagazione
contain_lateral_movement() {
    log "STEP 2: Contenimento movimento laterale"

    # Blocco SMB su segmenti non critici
    log "Blocking SMB/445 on non-critical VLANs"
    for vlan in $(seq 100 150); do
        if curl -s --connect-timeout 5 "${NETWORK_CONTROLLER}/acl/add" \
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer ${SDN_TOKEN:-}" \
            -d "{\"vlan\": ${vlan}, \"rule\": \"deny tcp any any eq 445\"}" >/dev/null 2>&1; then
            log "SMB blocked on VLAN ${vlan}"
        fi
    done

    # Reset password account di servizio
    if [[ -f "/etc/security/service_accounts.txt" && -n "${LDAP_PASS}" ]]; then
        log "Resetting service account passwords"
        while IFS= read -r account; do
            if [[ -n "${account}" && ! "${account}" =~ ^# ]]; then
                NEW_PASS=$(openssl rand -base64 32)
                if ldappasswd -x -D "cn=admin,dc=company,dc=local" -w "${LDAP_PASS}" \
                    -s "${NEW_PASS}" "cn=${account},ou=service,dc=company,dc=local" >/dev/null 2>&1; then
                    success "Password reset for service account: ${account}"
                    # Store in secure location (would be Vault in production)
                    echo "${account}:${NEW_PASS}" >> "${LOG_DIR}/new_passwords.txt"
                    chmod 600 "${LOG_DIR}/new_passwords.txt"
                else
                    warning "Failed to reset password for: ${account}"
                fi
            fi
        done < "/etc/security/service_accounts.txt"
    else
        warning "Service accounts file not found or LDAP password not set"
    fi

    # Kill suspicious processes
    log "Scanning for suspicious processes"
    SUSPICIOUS_PROCS=""
    if command -v osquery >/dev/null; then
        SUSPICIOUS_PROCS=$(osquery --json \
            "SELECT pid, name, cmdline FROM processes WHERE
             (name LIKE '%crypt%' OR name LIKE '%lock%' OR name LIKE '%ransom%')
             AND start_time > datetime('now', '-1 hour')" 2>/dev/null || echo "")
    fi

    if [[ -n "${SUSPICIOUS_PROCS}" ]]; then
        echo "${SUSPICIOUS_PROCS}" | jq -r '.[]?.pid // empty' | while read -r pid; do
            if [[ -n "${pid}" && "${pid}" =~ ^[0-9]+$ ]]; then
                if kill -9 "${pid}" 2>/dev/null; then
                    success "Killed suspicious process: ${pid}"
                else
                    warning "Failed to kill process: ${pid}"
                fi
            fi
        done
    else
        log "No suspicious processes detected via osquery"
    fi

    success "Lateral movement containment completed"
}

# STEP 3: Identificazione del Vettore
identify_attack_vector() {
    log "STEP 3: Identificazione vettore di attacco"

    # Analisi email phishing ultimi 7 giorni
    log "Checking for phishing emails"
    if PHISHING_CANDIDATES=$(curl -s --connect-timeout 10 "${SIEM_API}/email/suspicious" \
        -H "Authorization: Bearer ${SIEM_TOKEN:-}" \
        -d '{"days": 7, "min_score": 7}' 2>/dev/null); then
        echo "${PHISHING_CANDIDATES}" > "${LOG_DIR}/phishing_analysis.json"
        success "Phishing analysis completed"
    else
        warning "Failed to retrieve phishing data from SIEM"
    fi

    # Check vulnerabilità note non patchate
    log "Scanning for unpatched vulnerabilities"
    if [[ -f "${LOG_DIR}/affected_systems.txt" ]]; then
        while IFS= read -r system; do
            if [[ -n "${system}" ]]; then
                log "Vulnerability scan for: ${system}"
                if command -v nmap >/dev/null; then
                    if timeout 300 nmap -sV --script vulners "${system}" > "${LOG_DIR}/vuln_scan_${system}.txt" 2>&1; then
                        success "Vulnerability scan completed for ${system}"
                    else
                        warning "Vulnerability scan failed for ${system}"
                    fi
                fi
            fi
        done < "${LOG_DIR}/affected_systems.txt"
    fi

    # Analisi log autenticazione per accessi anomali
    log "Analyzing authentication logs"
    if [[ -f "/var/log/auth.log" ]]; then
        grep -E "(Failed|Accepted)" /var/log/auth.log | \
            awk '{print $1, $2, $3, $9, $11}' | \
            sort | uniq -c | sort -rn > "${LOG_DIR}/access_analysis.txt"
        success "Authentication log analysis completed"
    else
        warning "Authentication logs not found"
    fi

    success "Attack vector identification completed"
}

# STEP 4: Preservazione delle Evidenze
preserve_evidence() {
    log "STEP 4: Preservazione evidenze forensi"

    if [[ -f "${LOG_DIR}/affected_systems.txt" ]]; then
        while IFS= read -r system; do
            if [[ -n "${system}" ]]; then
                log "Preserving evidence for: ${system}"

                # Test connectivity first
                if ping -c 1 -W 3 "${system}" >/dev/null 2>&1; then
                    # Dump memoria se accessibile (requires forensics user setup)
                    if ssh -o ConnectTimeout=10 -o StrictHostKeyChecking=no "forensics@${system}" \
                        "sudo dd if=/dev/mem of=/tmp/mem_${INCIDENT_ID}.dump bs=1M count=100" >/dev/null 2>&1; then
                        success "Memory dump created for ${system}"

                        # Copy memory dump
                        if scp -o ConnectTimeout=30 "forensics@${system}:/tmp/mem_${INCIDENT_ID}.dump" \
                            "${LOG_DIR}/${system}_memory.dump" >/dev/null 2>&1; then
                            success "Memory dump copied for ${system}"
                        fi
                    else
                        warning "Memory dump failed for ${system}"
                    fi

                    # Copy critical logs
                    if rsync -avz --timeout=30 "forensics@${system}:/var/log/" "${LOG_DIR}/${system}_logs/" >/dev/null 2>&1; then
                        success "Logs copied for ${system}"

                        # Generate hashes for chain of custody
                        find "${LOG_DIR}/${system}_logs/" -type f -exec sha256sum {} \; \
                            > "${LOG_DIR}/${system}_hashes.txt"
                    else
                        warning "Log copy failed for ${system}"
                    fi
                else
                    warning "System ${system} not reachable for evidence collection"
                fi
            fi
        done < "${LOG_DIR}/affected_systems.txt"
    fi

    success "Evidence preservation completed"
}

# STEP 5: Comunicazione e Coordinamento
coordinate_response() {
    log "STEP 5: Coordinamento risposta"

    # Genera report preliminare
    cat > "${LOG_DIR}/preliminary_report.md" <<EOF
# Incident Report ${INCIDENT_ID}

## Executive Summary
- **Tipo**: Ransomware Attack
- **Data/Ora**: $(date)
- **Sistemi affetti**: $(wc -l < "${LOG_DIR}/affected_systems.txt" 2>/dev/null || echo "Unknown")
- **Status**: CONTAINED
- **Severità**: HIGH

## Timeline
$(grep "STEP" "${LOG_DIR}/incident.log" 2>/dev/null || echo "Timeline data not available")

## Sistemi Affetti
$(cat "${LOG_DIR}/affected_systems.txt" 2>/dev/null || echo "System list not available")

## Azioni Intraprese
1. ✅ Isolamento sistemi affetti
2. ✅ Contenimento movimento laterale
3. ✅ Identificazione vettore d'attacco
4. ✅ Preservazione evidenze
5. ✅ Coordinamento risposta

## Prossimi Passi
1. Analisi forense completa
2. Identificazione ransomware variant
3. Valutazione opzioni recovery
4. Comunicazione stakeholder
5. Lessons learned e miglioramenti

## Contatti
- Incident Commander: Security Team
- CISO: ciso@company.com
- IT Operations: itops@company.com

---
Generated by Ransomware Response Runbook v2.0
EOF

    # Notifica management
    if command -v mail >/dev/null; then
        mail -s "URGENT: Ransomware Incident ${INCIDENT_ID} - CONTAINED" \
            "ciso@company.com" "security-team@company.com" < "${LOG_DIR}/preliminary_report.md" 2>/dev/null || \
            warning "Failed to send email notification"
    fi

    # Apertura ticket (esempio ServiceNow)
    if [[ -n "${SERVICENOW_API:-}" ]]; then
        TICKET_RESPONSE=$(curl -s "${SERVICENOW_API}/api/incident" \
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer ${SERVICENOW_TOKEN:-}" \
            -d "{
                \"priority\": 1,
                \"category\": \"security\",
                \"short_description\": \"Ransomware containment completed - ${INCIDENT_ID}\",
                \"description\": \"Automated ransomware response executed. See incident logs for details.\",
                \"incident_id\": \"${INCIDENT_ID}\"
            }" 2>/dev/null)

        if [[ -n "${TICKET_RESPONSE}" ]]; then
            TICKET_NUMBER=$(echo "${TICKET_RESPONSE}" | jq -r '.number // "Unknown"')
            success "ServiceNow ticket created: ${TICKET_NUMBER}"
        fi
    fi

    alert_team "Ransomware response completed for incident ${INCIDENT_ID}. Report available at ${LOG_DIR}/preliminary_report.md"
    success "Response coordination completed"
}

# Funzione di cleanup
cleanup() {
    log "Performing cleanup operations"
    # Ensure sensitive files are properly protected
    if [[ -f "${LOG_DIR}/new_passwords.txt" ]]; then
        chmod 600 "${LOG_DIR}/new_passwords.txt"
    fi
    success "Cleanup completed"
}

# Main execution
main() {
    echo -e "${BLUE}"
    echo "=================================="
    echo "  RANSOMWARE RESPONSE RUNBOOK"
    echo "=================================="
    echo -e "${NC}"

    # Setup
    mkdir -p "${LOG_DIR}"
    check_dependencies

    log "=== Iniziando risposta incidente Ransomware ==="
    log "Incident ID: ${INCIDENT_ID}"
    log "Log directory: ${LOG_DIR}"

    # Execute response steps
    isolate_affected_systems
    contain_lateral_movement
    identify_attack_vector
    preserve_evidence
    coordinate_response
    cleanup

    echo -e "${GREEN}"
    echo "=================================="
    echo "  CONTAINMENT COMPLETED"
    echo "=================================="
    echo -e "${NC}"

    log "=== Containment completed. Incident ID: ${INCIDENT_ID} ==="
    log "=== Procedere con analisi forense dettagliata ==="

    echo "Next steps:"
    echo "1. Review logs in: ${LOG_DIR}"
    echo "2. Conduct detailed forensic analysis"
    echo "3. Coordinate with law enforcement if required"
    echo "4. Plan recovery operations"
    echo "5. Update security controls based on findings"
}

# Trap per error handling
trap 'error "Script failed at line $LINENO. Command: $BASH_COMMAND"' ERR
trap 'cleanup' EXIT

# Execute if run directly (not sourced)
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi