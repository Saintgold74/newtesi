#!/bin/bash

echo "=== ANALISI COMPLETA USO TERMINI GLOSSARIO ===" > rapporto_glossario.txt
echo "" >> rapporto_glossario.txt

# Termini più importanti da controllare
IMPORTANT_TERMS=(
    "gdo" "gist" "ai" "zerotrust" "edge" "pci-dss" "gdpr" "nis2" 
    "tco" "roi" "pos" "iot" "siem" "soc" "malware" "ransomware"
    "phishing" "hvac" "rfid" "microservizi" "container" "kubernetes"
)

echo "1. TERMINI CON USO CORRETTO \gls{}: " >> rapporto_glossario.txt
echo "" >> rapporto_glossario.txt

for term in "${IMPORTANT_TERMS[@]}"; do
    count=$(grep -r "\gls{$term}" capitoli/ | wc -l)
    if [ $count -gt 0 ]; then
        echo "✓ $term: $count occorrenze" >> rapporto_glossario.txt
    fi
done

echo "" >> rapporto_glossario.txt
echo "2. TERMINI MAI USATI CON \gls{}: " >> rapporto_glossario.txt
echo "" >> rapporto_glossario.txt

for term in "${IMPORTANT_TERMS[@]}"; do
    count=$(grep -r "\gls{$term}" capitoli/ | wc -l)
    if [ $count -eq 0 ]; then
        echo "✗ $term: mai usato con \gls{}" >> rapporto_glossario.txt
    fi
done

echo "" >> rapporto_glossario.txt
echo "3. TERMINI USATI COME TESTO NORMALE (ESEMPI):" >> rapporto_glossario.txt
echo "" >> rapporto_glossario.txt

# Cerca termini usati come testo normale
echo "--- 'Zero Trust' (dovrebbe essere \gls{zerotrust}):" >> rapporto_glossario.txt
grep -n "Zero Trust" capitoli/*.tex | grep -v "\gls{zerotrust}" | head -3 >> rapporto_glossario.txt

echo "" >> rapporto_glossario.txt
echo "--- 'GDO' (dovrebbe essere \gls{gdo}):" >> rapporto_glossario.txt
grep -n "GDO" capitoli/*.tex | grep -v "\gls{gdo}" | head -3 >> rapporto_glossario.txt

echo "" >> rapporto_glossario.txt
echo "--- 'IoT' (dovrebbe essere \gls{iot}):" >> rapporto_glossario.txt
grep -n "IoT" capitoli/*.tex | grep -v "\gls{iot}" | head -3 >> rapporto_glossario.txt

echo "" >> rapporto_glossario.txt
echo "--- 'Machine Learning' o 'ML' (dovrebbe essere \gls{ml}):" >> rapporto_glossario.txt
grep -n -E "Machine Learning|[^{]ML[^}]" capitoli/*.tex | grep -v "\gls{ml}" | head -3 >> rapporto_glossario.txt

echo "" >> rapporto_glossario.txt
echo "--- 'Artificial Intelligence' o 'AI' (dovrebbe essere \gls{ai}):" >> rapporto_glossario.txt
grep -n -E "Artificial Intelligence|[^{]AI[^}]" capitoli/*.tex | grep -v "\gls{ai}" | head -3 >> rapporto_glossario.txt

