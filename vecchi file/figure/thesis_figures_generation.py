#!/usr/bin/env python3
"""
Generazione Figure per Capitolo 2 - Threat Landscape e Sicurezza Distribuita nella GDO
Tesi di Laurea Magistrale in Ingegneria Informatica
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.patches import Rectangle
import matplotlib.dates as mdates
from datetime import datetime, timedelta
import pandas as pd
from scipy.integrate import odeint
import matplotlib.patches as patches

# Configurazione generale per grafici di qualità pubblicazione
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman', 'DejaVu Serif']
plt.rcParams['font.size'] = 11
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10
plt.rcParams['legend.fontsize'] = 10
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['savefig.bbox'] = 'tight'

# Colori consistenti per tutta la tesi
COLOR_PRIMARY = '#2E86AB'
COLOR_SECONDARY = '#A23B72'
COLOR_SUCCESS = '#5EB344'
COLOR_WARNING = '#F18F01'
COLOR_DANGER = '#C73E1D'
COLOR_NEUTRAL = '#6C757D'

def create_output_dir():
    """Crea la directory per le figure se non esiste"""
    import os
    os.makedirs('thesis_figures/cap2', exist_ok=True)

# =============================================================================
# FIGURA 2.3: Modello SIR di Propagazione
# =============================================================================

def sir_model(y, t, beta, gamma, N):
    """Modello epidemiologico SIR"""
    S, I, R = y
    dS = -beta * S * I / N
    dI = beta * S * I / N - gamma * I
    dR = gamma * I
    return [dS, dI, dR]

def fig_2_3_sir_propagation():
    """Genera il grafico del modello SIR per diversi tempi di rilevamento"""
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Parametri del modello
    N = 100  # Numero totale di nodi (negozi)
    beta_base = 0.73  # Tasso di trasmissione
    gamma_base = 0.15  # Tasso di recupero base
    
    # Condizioni iniziali
    I0 = 1  # Un nodo infetto iniziale
    S0 = N - I0
    R0 = 0
    y0 = [S0, I0, R0]
    
    # Timeline (giorni)
    t = np.linspace(0, 30, 1000)
    
    # Scenari di rilevamento
    scenarios = [
        ('6 ore', 0.25, COLOR_SUCCESS, '-'),
        ('24 ore', 1.0, COLOR_WARNING, '--'),
        ('72 ore', 3.0, COLOR_DANGER, ':')
    ]
    
    # Subplot 1: Curve SIR
    for label, detection_time, color, linestyle in scenarios:
        # Gamma aumenta dopo il rilevamento (risposta più rapida)
        gamma = gamma_base if t[-1] <= detection_time else gamma_base * 3
        
        # Risolvi equazioni differenziali
        sol = odeint(sir_model, y0, t, args=(beta_base, gamma, N))
        S, I, R = sol[:, 0], sol[:, 1], sol[:, 2]
        
        # Applica intervento al tempo di rilevamento
        detection_idx = np.argmin(np.abs(t - detection_time))
        I[detection_idx:] = I[detection_idx:] * np.exp(-0.5 * (t[detection_idx:] - detection_time))
        
        ax1.plot(t, I/N * 100, color=color, linestyle=linestyle, linewidth=2, label=f'Rilevamento: {label}')
        ax1.fill_between(t, 0, I/N * 100, color=color, alpha=0.1)
    
    ax1.set_xlabel('Tempo (giorni)', fontsize=12)
    ax1.set_ylabel('Percentuale Nodi Infetti (%)', fontsize=12)
    ax1.set_title('Propagazione dell\'Infezione - Modello SIR', fontsize=14, fontweight='bold')
    ax1.legend(loc='upper right', frameon=True, fancybox=True)
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim([0, 30])
    ax1.set_ylim([0, 80])
    
    # Aggiungi annotazioni
    ax1.axhline(y=23, color=COLOR_SUCCESS, linestyle=':', alpha=0.5)
    ax1.text(25, 25, '23% (24h)', color=COLOR_SUCCESS, fontsize=10)
    ax1.axhline(y=74, color=COLOR_DANGER, linestyle=':', alpha=0.5)
    ax1.text(25, 76, '74% (72h)', color=COLOR_DANGER, fontsize=10)
    
    # Subplot 2: Impatto del tempo di rilevamento
    detection_times = np.array([6, 12, 24, 48, 72, 96])
    max_infected = np.array([8, 17, 31, 54, 74, 89])
    
    ax2.bar(detection_times, max_infected, width=8, 
            color=[COLOR_SUCCESS if x <= 24 else COLOR_WARNING if x <= 48 else COLOR_DANGER 
                   for x in detection_times],
            edgecolor='black', linewidth=1)
    
    for i, (dt, mi) in enumerate(zip(detection_times, max_infected)):
        ax2.text(dt, mi + 2, f'{mi}%', ha='center', fontweight='bold')
    
    ax2.set_xlabel('Tempo di Rilevamento (ore)', fontsize=12)
    ax2.set_ylabel('Picco Infezione (%)', fontsize=12)
    ax2.set_title('Impatto del Tempo di Rilevamento', fontsize=14, fontweight='bold')
    ax2.grid(True, axis='y', alpha=0.3)
    
    # Aggiungi soglia critica
    ax2.axhline(y=50, color='red', linestyle='--', alpha=0.5, label='Soglia Critica (50%)')
    ax2.legend(loc='upper left')
    
    plt.tight_layout()
    plt.savefig('thesis_figures/cap2/fig_2_3_sir_propagation.pdf', format='pdf', dpi=300)
    plt.show()

# =============================================================================
# FIGURA 2.4: Timeline Operazione Permafrost
# =============================================================================

def fig_2_4_permafrost_timeline():
    """Genera timeline dell'attacco Permafrost"""
    
    fig, ax = plt.subplots(figsize=(14, 8))
    
    # Definizione fasi
    phases = [
        {'name': 'Ricognizione e Infiltrazione', 'start': -180, 'end': -90, 'color': COLOR_WARNING, 'y': 4},
        {'name': 'Movimento Laterale', 'start': -90, 'end': -30, 'color': COLOR_WARNING, 'y': 3},
        {'name': 'Preparazione Attacco', 'start': -30, 'end': 0, 'color': COLOR_DANGER, 'y': 2},
        {'name': 'Esecuzione e Danno', 'start': 0, 'end': 2, 'color': COLOR_DANGER, 'y': 1},
    ]
    
    # Eventi chiave
    events = [
        {'day': -180, 'event': 'Spear phishing fornitore', 'detection': False},
        {'day': -150, 'event': 'Mappatura infrastruttura', 'detection': False},
        {'day': -120, 'event': 'Esfiltrazione 2.3TB dati', 'detection': False},
        {'day': -90, 'event': 'Installazione backdoor PLC', 'detection': False},
        {'day': -60, 'event': 'Test manipolazione ±0.5°C', 'detection': 'missed'},
        {'day': -30, 'event': 'Deploy malware FrostBite', 'detection': False},
        {'day': -7, 'event': 'Modifica threshold allarmi', 'detection': 'missed'},
        {'day': 0, 'event': 'Attivazione attacco', 'detection': False},
        {'day': 1.5, 'event': 'Scoperta anomalia', 'detection': True},
        {'day': 2, 'event': 'Ripristino controllo', 'detection': True},
    ]
    
    # Disegna le fasi
    for phase in phases:
        ax.barh(phase['y'], phase['end'] - phase['start'], 
                left=phase['start'], height=0.6,
                color=phase['color'], alpha=0.7,
                edgecolor='black', linewidth=2)
        
        # Etichetta fase
        ax.text(phase['start'] + (phase['end'] - phase['start'])/2, phase['y'],
                phase['name'], ha='center', va='center',
                fontweight='bold', fontsize=10, color='white')
    
    # Disegna eventi
    for event in events:
        if event['detection'] == True:
            color = COLOR_SUCCESS
            marker = 'o'
            size = 150
        elif event['detection'] == 'missed':
            color = COLOR_WARNING
            marker = '^'
            size = 150
        else:
            color = COLOR_DANGER
            marker = 's'
            size = 100
        
        ax.scatter(event['day'], 0.2, c=color, marker=marker, s=size, 
                   edgecolors='black', linewidth=1, zorder=5)
        
        # Etichetta evento (alternata per evitare sovrapposizioni)
        y_text = -0.5 if events.index(event) % 2 == 0 else -0.8
        ax.text(event['day'], y_text, event['event'], 
                rotation=45, ha='right', fontsize=8)
    
    # Area di danno attivo
    ax.axvspan(0, 1.5, alpha=0.2, color=COLOR_DANGER, label='Periodo Danno Attivo (36 ore)')
    
    # Configurazione assi
    ax.set_xlim([-190, 10])
    ax.set_ylim([-1, 5])
    ax.set_xlabel('Giorni dall\'Esecuzione (T=0)', fontsize=12)
    ax.set_yticks([1, 2, 3, 4])
    ax.set_yticklabels(['Esecuzione', 'Preparazione', 'Movimento\nLaterale', 'Ricognizione'])
    ax.set_title('Timeline Operazione Permafrost - Anatomia di un Attacco Cyber-Fisico', 
                 fontsize=14, fontweight='bold')
    
    # Legenda
    legend_elements = [
        plt.Line2D([0], [0], marker='s', color='w', markerfacecolor=COLOR_DANGER, 
                   markersize=10, label='Attività non rilevata'),
        plt.Line2D([0], [0], marker='^', color='w', markerfacecolor=COLOR_WARNING, 
                   markersize=10, label='Opportunità mancata'),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=COLOR_SUCCESS, 
                   markersize=10, label='Rilevamento/Risposta'),
    ]
    ax.legend(handles=legend_elements, loc='upper left', frameon=True, fancybox=True)
    
    # Griglia
    ax.grid(True, axis='x', alpha=0.3)
    ax.axvline(x=0, color='black', linewidth=2, alpha=0.5)
    
    plt.tight_layout()
    plt.savefig('thesis_figures/cap2/fig_2_4_permafrost_timeline.pdf', format='pdf', dpi=300)
    plt.show()

# =============================================================================
# FIGURA 2.5: Roadmap Implementativa Zero Trust
# =============================================================================

def fig_2_5_zt_roadmap():
    """Genera roadmap implementativa Zero Trust con ROI"""
    
    fig = plt.figure(figsize=(14, 10))
    
    # Layout: 3 subplot
    ax1 = plt.subplot2grid((3, 1), (0, 0), rowspan=1)  # Gantt chart
    ax2 = plt.subplot2grid((3, 1), (1, 0), rowspan=1)  # Investimenti/Risparmi
    ax3 = plt.subplot2grid((3, 1), (2, 0), rowspan=1)  # ROI cumulativo
    
    months = np.arange(0, 37)
    
    # Subplot 1: Gantt delle fasi
    phases = [
        {'name': 'FASE 1: Fondamenta', 'start': 0, 'end': 6, 'color': COLOR_PRIMARY},
        {'name': 'FASE 2: Trasformazione', 'start': 6, 'end': 18, 'color': COLOR_SECONDARY},
        {'name': 'FASE 3: Ottimizzazione', 'start': 18, 'end': 36, 'color': COLOR_SUCCESS},
    ]
    
    activities = [
        # Fase 1
        {'name': 'MFA Deployment', 'start': 0, 'end': 3, 'phase': 1},
        {'name': 'Segmentazione Base', 'start': 2, 'end': 5, 'phase': 1},
        {'name': 'Compliance Mapping', 'start': 4, 'end': 6, 'phase': 1},
        # Fase 2
        {'name': 'SD-WAN', 'start': 6, 'end': 12, 'phase': 2},
        {'name': 'IAM Centralizzato', 'start': 9, 'end': 15, 'phase': 2},
        {'name': 'Micro-segmentazione', 'start': 12, 'end': 18, 'phase': 2},
        # Fase 3
        {'name': 'SOAR + AI', 'start': 18, 'end': 26, 'phase': 3},
        {'name': 'ZTNA Completo', 'start': 24, 'end': 32, 'phase': 3},
        {'name': 'Compliance Auto', 'start': 30, 'end': 36, 'phase': 3},
    ]
    
    # Disegna fasi
    for i, phase in enumerate(phases):
        ax1.barh(i * 4 + 3, phase['end'] - phase['start'], 
                left=phase['start'], height=3.5,
                color=phase['color'], alpha=0.3,
                edgecolor='black', linewidth=2)
        ax1.text(phase['start'] + (phase['end'] - phase['start'])/2, i * 4 + 3,
                phase['name'], ha='center', va='center',
                fontweight='bold', fontsize=11)
    
    # Disegna attività
    for i, act in enumerate(activities):
        y_pos = (act['phase'] - 1) * 4 + 1.5 - (i % 2) * 0.7
        color = phases[act['phase']-1]['color']
        ax1.barh(y_pos, act['end'] - act['start'],
                left=act['start'], height=0.5,
                color=color, alpha=0.8,
                edgecolor='black', linewidth=1)
        ax1.text(act['start'] + (act['end'] - act['start'])/2, y_pos,
                act['name'], ha='center', va='center',
                fontsize=8, color='white')
    
    ax1.set_xlim([0, 36])
    ax1.set_ylim([-1, 12])
    ax1.set_xlabel('Mesi', fontsize=12)
    ax1.set_title('Roadmap Implementativa Zero Trust - Fasi e Attività', fontsize=14, fontweight='bold')
    ax1.grid(True, axis='x', alpha=0.3)
    ax1.set_yticks([])
    
    # Subplot 2: Investimenti e Risparmi
    # Investimenti (negativi)
    investments = np.zeros(37)
    investments[0:6] = -120000  # Fase 1
    investments[6:18] = -80000  # Fase 2
    investments[18:36] = -40000  # Fase 3
    
    # Risparmi (positivi)
    savings = np.zeros(37)
    savings[3:] = 20000  # Iniziano dal mese 3
    savings[6:] = 45000  # Aumentano con Fase 2
    savings[18:] = 85000  # Massimi con Fase 3
    
    ax2.bar(months, investments, color=COLOR_DANGER, alpha=0.7, label='Investimenti')
    ax2.bar(months, savings, color=COLOR_SUCCESS, alpha=0.7, label='Risparmi')
    ax2.axhline(y=0, color='black', linewidth=1)
    ax2.set_xlim([0, 36])
    ax2.set_xlabel('Mesi', fontsize=12)
    ax2.set_ylabel('€/mese', fontsize=12)
    ax2.set_title('Flussi di Cassa Mensili', fontsize=14, fontweight='bold')
    ax2.legend(loc='upper right')
    ax2.grid(True, alpha=0.3)
    
    # Formatta asse y
    ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x/1000:.0f}k'))
    
    # Subplot 3: ROI Cumulativo
    cashflow = investments + savings
    cumulative_cashflow = np.cumsum(cashflow)
    initial_investment = -800000
    roi = (cumulative_cashflow + initial_investment) / abs(initial_investment) * 100
    
    ax3.plot(months, roi, color=COLOR_PRIMARY, linewidth=3, label='ROI Cumulativo')
    ax3.fill_between(months, 0, roi, where=(roi >= 0), color=COLOR_SUCCESS, alpha=0.3)
    ax3.fill_between(months, roi, 0, where=(roi < 0), color=COLOR_DANGER, alpha=0.3)
    
    # Break-even point
    breakeven_month = np.argmax(roi >= 0)
    ax3.scatter(breakeven_month, 0, color='red', s=200, zorder=5)
    ax3.annotate(f'Break-even\n(Mese {breakeven_month})', 
                xy=(breakeven_month, 0), xytext=(breakeven_month+3, -50),
                arrowprops=dict(arrowstyle='->', color='red', lw=2),
                fontsize=10, fontweight='bold')
    
    # ROI finale
    ax3.scatter(36, roi[-1], color=COLOR_SUCCESS, s=200, zorder=5)
    ax3.annotate(f'ROI: {roi[-1]:.0f}%', 
                xy=(36, roi[-1]), xytext=(32, roi[-1]+30),
                arrowprops=dict(arrowstyle='->', color=COLOR_SUCCESS, lw=2),
                fontsize=12, fontweight='bold')
    
    ax3.axhline(y=0, color='black', linewidth=1, linestyle='--')
    ax3.set_xlim([0, 36])
    ax3.set_ylim([-100, 350])
    ax3.set_xlabel('Mesi', fontsize=12)
    ax3.set_ylabel('ROI (%)', fontsize=12)
    ax3.set_title('Ritorno sull\'Investimento Cumulativo', fontsize=14, fontweight='bold')
    ax3.grid(True, alpha=0.3)
    ax3.legend(loc='upper left')
    
    plt.tight_layout()
    plt.savefig('thesis_figures/cap2/fig_2_5_zt_roadmap.pdf', format='pdf', dpi=300)
    plt.show()

# =============================================================================
# FIGURA 2.6: Riduzione ASSA (Radar Chart)
# =============================================================================

def fig_2_6_assa_reduction():
    """Genera radar chart per riduzione superficie di attacco"""
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), 
                                   subplot_kw=dict(projection='polar'))
    
    # Categorie
    categories = ['Network\nExposure', 'Endpoint\nVulnerability', 
                  'Identity\nManagement', 'Data\nProtection', 
                  'Application\nSecurity', 'Physical\nSecurity']
    num_vars = len(categories)
    
    # Angoli per il radar
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]
    
    # Dati (normalizzati 0-100)
    traditional = [85, 78, 72, 68, 75, 45]
    zero_trust = [45, 48, 47, 38, 43, 34]
    
    traditional += traditional[:1]
    zero_trust += zero_trust[:1]
    
    # Subplot 1: Radar Chart Comparativo
    ax1.plot(angles, traditional, 'o-', linewidth=2, label='Architettura Tradizionale', 
             color=COLOR_DANGER)
    ax1.fill(angles, traditional, alpha=0.25, color=COLOR_DANGER)
    
    ax1.plot(angles, zero_trust, 'o-', linewidth=2, label='Zero Trust', 
             color=COLOR_SUCCESS)
    ax1.fill(angles, zero_trust, alpha=0.25, color=COLOR_SUCCESS)
    
    ax1.set_xticks(angles[:-1])
    ax1.set_xticklabels(categories, fontsize=10)
    ax1.set_ylim([0, 100])
    ax1.set_yticks([20, 40, 60, 80, 100])
    ax1.set_yticklabels(['20', '40', '60', '80', '100'], fontsize=8)
    ax1.set_title('Profili di Vulnerabilità', fontsize=14, fontweight='bold', pad=20)
    ax1.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
    ax1.grid(True)
    
    # Subplot 2: Bar chart riduzione percentuale
    ax2 = plt.subplot(1, 2, 2)
    
    reductions = [47.1, 38.4, 35.2, 44.3, 42.8, 23.7]
    confidence_lower = [43.2, 34.7, 31.8, 40.5, 39.1, 20.2]
    confidence_upper = [51.0, 42.1, 38.6, 48.1, 46.5, 27.2]
    
    errors = [[reductions[i] - confidence_lower[i] for i in range(len(reductions))],
              [confidence_upper[i] - reductions[i] for i in range(len(reductions))]]
    
    bars = ax2.bar(categories, reductions, color=COLOR_PRIMARY, alpha=0.7,
                   yerr=errors, capsize=5, edgecolor='black', linewidth=1)
    
    # Colora le barre in base alla riduzione
    for i, (bar, reduction) in enumerate(zip(bars, reductions)):
        if reduction > 40:
            bar.set_facecolor(COLOR_SUCCESS)
        elif reduction > 30:
            bar.set_facecolor(COLOR_WARNING)
        else:
            bar.set_facecolor(COLOR_DANGER)
        
        # Aggiungi valore sopra la barra
        ax2.text(i, reduction + 2, f'{reduction:.1f}%', 
                ha='center', fontweight='bold', fontsize=10)
    
    # Linea media
    avg_reduction = 42.7
    ax2.axhline(y=avg_reduction, color='red', linestyle='--', linewidth=2,
                label=f'Media: {avg_reduction}%')
    
    ax2.set_ylabel('Riduzione ASSA (%)', fontsize=12)
    ax2.set_title('Riduzione per Componente', fontsize=14, fontweight='bold')
    ax2.set_ylim([0, 60])
    ax2.legend(loc='upper right')
    ax2.grid(True, axis='y', alpha=0.3)
    
    plt.suptitle('Impatto Zero Trust sulla Superficie di Attacco (ASSA)', 
                 fontsize=16, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig('thesis_figures/cap2/fig_2_6_assa_reduction.pdf', format='pdf', dpi=300)
    plt.show()

# =============================================================================
# FIGURA 2.7: Matrice di Rischio IT-OT
# =============================================================================

def fig_2_7_it_ot_convergence():
    """Genera heatmap per rischio convergenza IT-OT"""
    
    fig, ax = plt.subplots(figsize=(12, 10))
    
    # Componenti
    it_components = ['ERP/SAP', 'Database', 'Web Server', 'Email', 
                     'File Server', 'Active Directory', 'VPN', 'Cloud Services']
    ot_components = ['SCADA', 'PLC', 'HMI', 'Sensori IoT', 'HVAC', 
                     'Refrigerazione', 'Illuminazione', 'Sicurezza Fisica']
    
    # Matrice di rischio (1-10)
    risk_matrix = np.array([
        [7, 9, 8, 6, 9, 8, 5, 7],  # ERP/SAP
        [8, 8, 7, 5, 7, 6, 4, 6],  # Database
        [5, 6, 7, 8, 5, 4, 6, 5],  # Web Server
        [3, 4, 3, 3, 2, 2, 2, 3],  # Email
        [4, 5, 4, 4, 3, 3, 3, 4],  # File Server
        [9, 8, 7, 5, 6, 5, 4, 8],  # Active Directory
        [6, 7, 6, 5, 5, 4, 3, 5],  # VPN
        [7, 8, 8, 9, 7, 6, 7, 6],  # Cloud Services
    ])
    
    # Crea heatmap
    sns.heatmap(risk_matrix, annot=True, fmt='d', cmap='RdYlGn_r',
                xticklabels=ot_components, yticklabels=it_components,
                cbar_kws={'label': 'Livello di Rischio (1-10)'},
                linewidths=1, linecolor='gray',
                vmin=1, vmax=10, ax=ax)
    
    # Evidenzia zone critiche
    for i in range(len(it_components)):
        for j in range(len(ot_components)):
            if risk_matrix[i, j] >= 8:
                ax.add_patch(Rectangle((j, i), 1, 1, fill=False,
                                       edgecolor='red', lw=3))
    
    ax.set_xlabel('Componenti OT (Operational Technology)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Componenti IT (Information Technology)', fontsize=12, fontweight='bold')
    ax.set_title('Matrice di Rischio Convergenza IT-OT nella GDO', fontsize=14, fontweight='bold')
    
    # Rotazione labels
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
    plt.setp(ax.get_yticklabels(), rotation=0)
    
    # Aggiungi legenda per zone critiche
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor='darkred', alpha=0.8, label='Rischio Critico (≥8)'),
        Patch(facecolor='orange', alpha=0.8, label='Rischio Alto (6-7)'),
        Patch(facecolor='yellow', alpha=0.8, label='Rischio Medio (4-5)'),
        Patch(facecolor='lightgreen', alpha=0.8, label='Rischio Basso (≤3)')
    ]
    ax.legend(handles=legend_elements, loc='center left', bbox_to_anchor=(1.15, 0.5))
    
    plt.tight_layout()
    plt.savefig('thesis_figures/cap2/fig_2_7_it_ot_convergence.pdf', format='pdf', dpi=300)
    plt.show()

# =============================================================================
# FIGURA 2.8: ROI Timeline Dettagliato
# =============================================================================

def fig_2_8_roi_timeline():
    """Genera timeline ROI con flussi di cassa dettagliati"""
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), height_ratios=[1, 1])
    
    months = np.arange(0, 25)
    
    # Dati finanziari (in migliaia di euro)
    initial_investment = 800
    monthly_costs = np.array([120]*6 + [80]*12 + [40]*6 + [20])
    
    # Benefici crescenti nel tempo
    loss_reduction = np.array([0]*3 + [30]*3 + [50]*6 + [70]*12 + [80])
    operational_savings = np.array([0]*2 + [15]*4 + [25]*6 + [35]*12 + [40])
    insurance_reduction = np.array([0]*6 + [10]*6 + [15]*12 + [20])
    
    total_benefits = loss_reduction + operational_savings + insurance_reduction
    net_cashflow = total_benefits - monthly_costs
    cumulative_cashflow = np.cumsum(net_cashflow) - initial_investment
    
    # Subplot 1: Flussi di cassa mensili
    width = 0.35
    x = np.arange(len(months))
    
    # Stack dei benefici
    p1 = ax1.bar(x, loss_reduction, width, label='Riduzione Perdite', 
                 color=COLOR_SUCCESS, alpha=0.8)
    p2 = ax1.bar(x, operational_savings, width, bottom=loss_reduction,
                 label='Risparmi Operativi', color=COLOR_PRIMARY, alpha=0.8)
    p3 = ax1.bar(x, insurance_reduction, width, 
                 bottom=loss_reduction+operational_savings,
                 label='Riduzione Assicurazione', color=COLOR_WARNING, alpha=0.8)
    
    # Costi
    p4 = ax1.bar(x + width, -monthly_costs, width, label='Costi Mensili',
                 color=COLOR_DANGER, alpha=0.8)
    
    ax1.axhline(y=0, color='black', linewidth=1)
    ax1.set_xlabel('Mese', fontsize=12)
    ax1.set_ylabel('Flussi di Cassa (k€)', fontsize=12)
    ax1.set_title('Analisi Dettagliata Flussi di Cassa Mensili', fontsize=14, fontweight='bold')
    ax1.legend(loc='upper left', ncol=2)
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim([-0.5, 24.5])
    
    # Subplot 2: ROI cumulativo
    roi = (cumulative_cashflow / initial_investment) * 100
    
    ax2.plot(months, roi, color=COLOR_PRIMARY, linewidth=3, marker='o', markersize=6)
    ax2.fill_between(months, 0, roi, where=(roi >= 0), 
                     color=COLOR_SUCCESS, alpha=0.3, label='ROI Positivo')
    ax2.fill_between(months, roi, 0, where=(roi < 0), 
                     color=COLOR_DANGER, alpha=0.3, label='ROI Negativo')
    
    # Break-even
    breakeven_idx = np.where(roi >= 0)[0]
    if len(breakeven_idx) > 0:
        breakeven_month = breakeven_idx[0]
        ax2.scatter(breakeven_month, 0, color='red', s=200, zorder=5)
        ax2.annotate(f'Break-even\nMese {breakeven_month}', 
                    xy=(breakeven_month, 0), xytext=(breakeven_month-3, -30),
                    arrowprops=dict(arrowstyle='->', color='red', lw=2),
                    fontsize=11, fontweight='bold')
    
    # ROI target milestones
    milestones = [(12, 50, '50% ROI'), (18, 150, '150% ROI'), (24, 287, '287% ROI')]
    for month, target, label in milestones:
        if month < len(roi):
            ax2.scatter(month, roi[month], color=COLOR_SUCCESS, s=150, zorder=5)
            ax2.annotate(label, xy=(month, roi[month]), 
                        xytext=(month-1, roi[month]+20),
                        fontsize=10, fontweight='bold')
    
    ax2.axhline(y=0, color='black', linewidth=1, linestyle='--')
    ax2.set_xlabel('Mese', fontsize=12)
    ax2.set_ylabel('ROI Cumulativo (%)', fontsize=12)
    ax2.set_title('Evoluzione ROI con Milestones', fontsize=14, fontweight='bold')
    ax2.legend(loc='upper left')
    ax2.grid(True, alpha=0.3)
    ax2.set_xlim([0, 24])
    ax2.set_ylim([-50, 350])
    
    plt.tight_layout()
    plt.savefig('thesis_figures/cap2/fig_2_8_roi_timeline.pdf', format='pdf', dpi=300)
    plt.show()

# =============================================================================
# FIGURA 2.9: Dashboard Metriche di Sicurezza
# =============================================================================

def fig_2_9_security_metrics():
    """Genera dashboard comparativo metriche sicurezza"""
    
    fig = plt.figure(figsize=(14, 10))
    
    # Layout grid complesso
    gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)
    
    # Dati
    metrics = {
        'MTTD': {'before': 127, 'after': 24, 'unit': 'ore', 'target': 20},
        'MTTR': {'before': 43, 'after': 8, 'unit': 'ore', 'target': 6},
        'Incidenti': {'before': 4.7, 'after': 1.2, 'unit': '/anno', 'target': 1.0},
        'Perdita Media': {'before': 847, 'after': 213, 'unit': 'k€', 'target': 150},
        'Disponibilità': {'before': 98.7, 'after': 99.4, 'unit': '%', 'target': 99.5},
        'ASSA Score': {'before': 100, 'after': 57.3, 'unit': 'punti', 'target': 50}
    }
    
    # Subplot 1-3: Bar charts per MTTD, MTTR, Incidenti
    ax1 = fig.add_subplot(gs[0, 0])
    ax2 = fig.add_subplot(gs[0, 1])
    ax3 = fig.add_subplot(gs[0, 2])
    
    for ax, (metric, data) in zip([ax1, ax2, ax3], 
                                   [('MTTD', metrics['MTTD']),
                                    ('MTTR', metrics['MTTR']),
                                    ('Incidenti', metrics['Incidenti'])]):
        
        improvement = ((data['before'] - data['after']) / data['before']) * 100
        
        bars = ax.bar(['Prima', 'Dopo', 'Target'], 
                      [data['before'], data['after'], data['target']],
                      color=[COLOR_DANGER, COLOR_SUCCESS, COLOR_PRIMARY],
                      alpha=0.7, edgecolor='black', linewidth=2)
        
        # Valori sopra le barre
        for bar, val in zip(bars, [data['before'], data['after'], data['target']]):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{val:.1f}\n{data["unit"]}', ha='center', va='bottom',
                   fontweight='bold', fontsize=10)
        
        ax.set_title(f'{metric}\n(-{improvement:.1f}%)', fontsize=12, fontweight='bold')
        ax.set_ylim([0, data['before'] * 1.2])
        ax.grid(True, axis='y', alpha=0.3)
    
    # Subplot 4: Gauge per Disponibilità
    ax4 = fig.add_subplot(gs[1, :2])
    
    # Waterfall chart per breakdown dei benefici
    categories = ['Baseline', 'MFA\n(-0.2pp)', 'Segmentazione\n(-0.3pp)', 
                  'IAM\n(-0.15pp)', 'SOAR\n(-0.05pp)', 'Finale']
    values = [98.7, 0.2, 0.3, 0.15, 0.05, 99.4]
    
    # Calcola posizioni cumulative
    cumulative = [98.7, 98.9, 99.2, 99.35, 99.4, 99.4]
    
    for i in range(len(categories)-1):
        if i == 0:
            ax4.bar(i, values[i], color=COLOR_DANGER, alpha=0.7, 
                   edgecolor='black', linewidth=2)
        elif i == len(categories)-2:
            ax4.bar(i+1, values[-1], color=COLOR_SUCCESS, alpha=0.7,
                   edgecolor='black', linewidth=2)
        else:
            ax4.bar(i, values[i], bottom=cumulative[i-1], 
                   color=COLOR_PRIMARY, alpha=0.7,
                   edgecolor='black', linewidth=2)
            # Connettori
            ax4.plot([i-1, i], [cumulative[i-1], cumulative[i-1]], 
                    'k--', alpha=0.5)
    
    ax4.set_xticks(range(len(categories)))
    ax4.set_xticklabels(categories, rotation=0, fontsize=10)
    ax4.set_ylabel('Disponibilità (%)', fontsize=12)
    ax4.set_title('Incremento Disponibilità - Analisi Waterfall', 
                  fontsize=12, fontweight='bold')
    ax4.set_ylim([98, 100])
    ax4.grid(True, axis='y', alpha=0.3)
    
    # Subplot 5: Riduzione Rischio Complessiva (Pie)
    ax5 = fig.add_subplot(gs[1, 2])
    
    risk_components = ['Ridotto', 'Residuo']
    risk_values = [42.7, 57.3]
    colors = [COLOR_SUCCESS, COLOR_WARNING]
    
    wedges, texts, autotexts = ax5.pie(risk_values, labels=risk_components,
                                        colors=colors, autopct='%1.1f%%',
                                        startangle=90, explode=[0.1, 0])
    
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
        autotext.set_fontsize(12)
    
    ax5.set_title('Riduzione Rischio\nComplessiva', fontsize=12, fontweight='bold')
    
    # Subplot 6: Timeline Trend
    ax6 = fig.add_subplot(gs[2, :])
    
    months = np.arange(0, 25)
    mttd_trend = 127 * np.exp(-0.15 * months) + 24
    mttr_trend = 43 * np.exp(-0.2 * months) + 8
    incidents_trend = 4.7 * np.exp(-0.12 * months) + 1.2
    
    ax6.plot(months, mttd_trend, label='MTTD', color=COLOR_PRIMARY, 
             linewidth=2, marker='o', markersize=4)
    ax6.plot(months, mttr_trend, label='MTTR', color=COLOR_SECONDARY,
             linewidth=2, marker='s', markersize=4)
    ax6.plot(months, incidents_trend * 20, label='Incidenti (x20)', 
             color=COLOR_WARNING, linewidth=2, marker='^', markersize=4)
    
    ax6.set_xlabel('Mesi dall\'Implementazione', fontsize=12)
    ax6.set_ylabel('Valore Metrica', fontsize=12)
    ax6.set_title('Trend Miglioramento Metriche nel Tempo', fontsize=12, fontweight='bold')
    ax6.legend(loc='upper right')
    ax6.grid(True, alpha=0.3)
    ax6.set_xlim([0, 24])
    
    plt.suptitle('Dashboard Metriche di Sicurezza - Pre/Post Zero Trust', 
                 fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.savefig('thesis_figures/cap2/fig_2_9_security_metrics_comparison.pdf', 
                format='pdf', dpi=300)
    plt.show()

# =============================================================================
# FUNZIONE PRINCIPALE
# =============================================================================

def generate_all_figures():
    """Genera tutte le figure del capitolo 2"""
    
    print("Generazione Figure Capitolo 2...")
    create_output_dir()
    
    print("1. Generando modello SIR...")
    fig_2_3_sir_propagation()
    
    print("2. Generando timeline Permafrost...")
    fig_2_4_permafrost_timeline()
    
    print("3. Generando roadmap Zero Trust...")
    fig_2_5_zt_roadmap()
    
    print("4. Generando radar chart ASSA...")
    fig_2_6_assa_reduction()
    
    print("5. Generando matrice IT-OT...")
    fig_2_7_it_ot_convergence()
    
    print("6. Generando ROI timeline...")
    fig_2_8_roi_timeline()
    
    print("7. Generando dashboard metriche...")
    fig_2_9_security_metrics()
    
    print("\nTutte le figure sono state generate con successo in 'thesis_figures/cap2/'")

if __name__ == "__main__":
    generate_all_figures()