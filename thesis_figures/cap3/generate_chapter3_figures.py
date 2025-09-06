#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generazione Grafici per Capitolo 3 - Evoluzione Infrastrutturale
Tesi di Laurea in Ingegneria Informatica
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import pandas as pd
from matplotlib.patches import Rectangle, FancyBboxPatch
import matplotlib.patches as mpatches
from datetime import datetime, timedelta

# Configurazione stile accademico
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("husl")
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Computer Modern Roman']
plt.rcParams['text.usetex'] = True
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['font.size'] = 10

# =============================================================================
# FIGURA 3.1: Correlazione tra Configurazione Power e Availability Sistemica
# =============================================================================

def generate_power_availability_figure():
    """
    Genera il grafico delle curve di affidabilità per diverse configurazioni power
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Dati per le configurazioni
    mtbf_hours = np.linspace(1000, 200000, 1000)
    
    # Configurazione N+1
    n_plus_1_availability = 1 - (1 / mtbf_hours) * 8  # 8 ore MTTR medio
    n_plus_1_lower = n_plus_1_availability - np.random.normal(0, 0.002, len(mtbf_hours))
    n_plus_1_upper = n_plus_1_availability + np.random.normal(0, 0.002, len(mtbf_hours))
    
    # Configurazione 2N
    two_n_availability = 1 - (1 / mtbf_hours) * 4  # 4 ore MTTR con ridondanza
    two_n_lower = two_n_availability - np.random.normal(0, 0.001, len(mtbf_hours))
    two_n_upper = two_n_availability + np.random.normal(0, 0.001, len(mtbf_hours))
    
    # Configurazione 2N+1
    two_n_plus_1_availability = 1 - (1 / mtbf_hours) * 2  # 2 ore MTTR ottimale
    two_n_plus_1_lower = two_n_plus_1_availability - np.random.normal(0, 0.0005, len(mtbf_hours))
    two_n_plus_1_upper = two_n_plus_1_availability + np.random.normal(0, 0.0005, len(mtbf_hours))
    
    # Subplot 1: Curve di availability
    ax1.plot(mtbf_hours/1000, n_plus_1_availability * 100, 
             label='N+1', linewidth=2, color='#e74c3c')
    ax1.fill_between(mtbf_hours/1000, n_plus_1_lower * 100, n_plus_1_upper * 100, 
                      alpha=0.2, color='#e74c3c')
    
    ax1.plot(mtbf_hours/1000, two_n_availability * 100, 
             label='2N', linewidth=2, color='#3498db')
    ax1.fill_between(mtbf_hours/1000, two_n_lower * 100, two_n_upper * 100, 
                      alpha=0.2, color='#3498db')
    
    ax1.plot(mtbf_hours/1000, two_n_plus_1_availability * 100, 
             label='2N+1', linewidth=2, color='#2ecc71')
    ax1.fill_between(mtbf_hours/1000, two_n_plus_1_lower * 100, two_n_plus_1_upper * 100, 
                      alpha=0.2, color='#2ecc71')
    
    # Linea target 99.95%
    ax1.axhline(y=99.95, color='red', linestyle='--', linewidth=1, 
                label='Target SLA 99.95\\%')
    
    ax1.set_xlabel('MTBF (migliaia di ore)', fontsize=11)
    ax1.set_ylabel('Availability (\\%)', fontsize=11)
    ax1.set_title('Curve di Affidabilità per Configurazione', fontsize=12, fontweight='bold')
    ax1.legend(loc='lower right')
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim([0, 200])
    ax1.set_ylim([99.0, 100.0])
    
    # Subplot 2: Analisi Costo-Beneficio
    configs = ['N+1', '2N', '2N+1']
    mtbf_values = [52560, 175200, 350400]
    availability_values = [99.82, 99.94, 99.97]
    cost_index = [100, 143, 186]  # Indice di costo relativo
    
    ax2_twin = ax2.twinx()
    
    x_pos = np.arange(len(configs))
    width = 0.35
    
    bars1 = ax2.bar(x_pos - width/2, availability_values, width, 
                    label='Availability', color='#3498db', alpha=0.7)
    bars2 = ax2_twin.bar(x_pos + width/2, cost_index, width, 
                         label='Costo Relativo', color='#e74c3c', alpha=0.7)
    
    ax2.set_xlabel('Configurazione', fontsize=11)
    ax2.set_ylabel('Availability (\\%)', fontsize=11, color='#3498db')
    ax2_twin.set_ylabel('Indice di Costo (N+1 = 100)', fontsize=11, color='#e74c3c')
    ax2.set_title('Trade-off Availability vs Costo', fontsize=12, fontweight='bold')
    ax2.set_xticks(x_pos)
    ax2.set_xticklabels(configs)
    ax2.set_ylim([99.7, 100.0])
    ax2_twin.set_ylim([0, 200])
    
    # Aggiungi valori sopra le barre
    for bar, val in zip(bars1, availability_values):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height + 0.01,
                f'{val:.2f}\\%', ha='center', va='bottom', fontsize=9)
    
    for bar, val in zip(bars2, cost_index):
        height = bar.get_height()
        ax2_twin.text(bar.get_x() + bar.get_width()/2., height + 2,
                     f'{val}', ha='center', va='bottom', fontsize=9)
    
    ax2.tick_params(axis='y', labelcolor='#3498db')
    ax2_twin.tick_params(axis='y', labelcolor='#e74c3c')
    
    ax2.legend(loc='upper left')
    ax2_twin.legend(loc='upper right')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('figura_3_1_power_availability.pdf', bbox_inches='tight')
    plt.savefig('figura_3_1_power_availability.png', bbox_inches='tight')
    plt.show()
    
    return fig

# =============================================================================
# FIGURA 3.2: Evoluzione Architettura di Rete (sarà creata in TikZ)
# =============================================================================

def generate_network_evolution_data():
    """
    Genera i dati per il diagramma di evoluzione della rete (da usare in TikZ)
    """
    data = {
        'Legacy Hub-and-Spoke': {
            'MTTR': 4.7,
            'Traffic_Inspected': 57,
            'Flexibility': 20,
            'Cost_Index': 100
        },
        'Hybrid SD-WAN': {
            'MTTR': 2.3,
            'Traffic_Inspected': 78,
            'Flexibility': 65,
            'Cost_Index': 125
        },
        'Full Mesh SD-WAN': {
            'MTTR': 1.2,
            'Traffic_Inspected': 94,
            'Flexibility': 90,
            'Cost_Index': 145
        }
    }
    
    # Crea un grafico comparativo
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    architectures = list(data.keys())
    colors = ['#e74c3c', '#f39c12', '#2ecc71']
    
    # MTTR
    ax = axes[0, 0]
    mttr_values = [data[arch]['MTTR'] for arch in architectures]
    bars = ax.bar(architectures, mttr_values, color=colors, alpha=0.7)
    ax.set_ylabel('MTTR (ore)', fontsize=11)
    ax.set_title('Mean Time To Repair', fontsize=12, fontweight='bold')
    ax.set_ylim([0, 5])
    for bar, val in zip(bars, mttr_values):
        ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.1,
               f'{val:.1f}h', ha='center', va='bottom', fontsize=10)
    ax.grid(True, alpha=0.3)
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha='right')
    
    # Traffic Inspected
    ax = axes[0, 1]
    traffic_values = [data[arch]['Traffic_Inspected'] for arch in architectures]
    bars = ax.bar(architectures, traffic_values, color=colors, alpha=0.7)
    ax.set_ylabel('Traffico Ispezionato (\\%)', fontsize=11)
    ax.set_title('Visibilità del Traffico East-West', fontsize=12, fontweight='bold')
    ax.set_ylim([0, 100])
    for bar, val in zip(bars, traffic_values):
        ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 1,
               f'{val}\\%', ha='center', va='bottom', fontsize=10)
    ax.grid(True, alpha=0.3)
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha='right')
    
    # Flexibility
    ax = axes[1, 0]
    flex_values = [data[arch]['Flexibility'] for arch in architectures]
    bars = ax.bar(architectures, flex_values, color=colors, alpha=0.7)
    ax.set_ylabel('Indice di Flessibilità', fontsize=11)
    ax.set_title('Agilità Operativa', fontsize=12, fontweight='bold')
    ax.set_ylim([0, 100])
    for bar, val in zip(bars, flex_values):
        ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 1,
               f'{val}', ha='center', va='bottom', fontsize=10)
    ax.grid(True, alpha=0.3)
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha='right')
    
    # Cost vs Benefit
    ax = axes[1, 1]
    cost_values = [data[arch]['Cost_Index'] for arch in architectures]
    benefit_values = [(100 - mttr_values[i]/5*100 + traffic_values[i] + flex_values[i])/3 
                     for i in range(len(architectures))]
    
    x_pos = np.arange(len(architectures))
    width = 0.35
    
    bars1 = ax.bar(x_pos - width/2, cost_values, width, 
                   label='Costo', color='#e74c3c', alpha=0.7)
    bars2 = ax.bar(x_pos + width/2, benefit_values, width, 
                   label='Beneficio', color='#2ecc71', alpha=0.7)
    
    ax.set_ylabel('Indice Relativo', fontsize=11)
    ax.set_title('Analisi Costo-Beneficio', fontsize=12, fontweight='bold')
    ax.set_xticks(x_pos)
    ax.set_xticklabels(architectures)
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha='right')
    
    plt.suptitle('Evoluzione dell\'Architettura di Rete: Metriche Comparative', 
                fontsize=14, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig('figura_3_2_network_evolution.pdf', bbox_inches='tight')
    plt.savefig('figura_3_2_network_evolution.png', bbox_inches='tight')
    plt.show()
    
    return fig

# =============================================================================
# FIGURA 3.3: TCO Cloud Migration Analysis
# =============================================================================

def generate_cloud_tco_analysis():
    """
    Genera l'analisi TCO per le diverse strategie di migrazione cloud
    """
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # Dati delle strategie
    strategies = ['Lift & Shift', 'Replatform', 'Refactor']
    colors_strategy = ['#3498db', '#f39c12', '#2ecc71']
    
    # Subplot 1: Costi iniziali e saving operativi
    ax = axes[0, 0]
    initial_costs = [8.2, 24.7, 87.3]  # in migliaia di euro per app
    opex_savings = [23, 41.5, 59]  # percentuale
    
    x_pos = np.arange(len(strategies))
    width = 0.35
    
    ax2 = ax.twinx()
    bars1 = ax.bar(x_pos - width/2, initial_costs, width, 
                   label='Costo Iniziale (k€/app)', color='#e74c3c', alpha=0.7)
    bars2 = ax2.bar(x_pos + width/2, opex_savings, width, 
                    label='Saving OPEX (\\%)', color='#2ecc71', alpha=0.7)
    
    ax.set_xlabel('Strategia di Migrazione', fontsize=11)
    ax.set_ylabel('Costo Iniziale (k€)', fontsize=11, color='#e74c3c')
    ax2.set_ylabel('Saving OPEX (\\%)', fontsize=11, color='#2ecc71')
    ax.set_title('Investimento vs Saving Operativi', fontsize=12, fontweight='bold')
    ax.set_xticks(x_pos)
    ax.set_xticklabels(strategies)
    ax.tick_params(axis='y', labelcolor='#e74c3c')
    ax2.tick_params(axis='y', labelcolor='#2ecc71')
    ax.legend(loc='upper left')
    ax2.legend(loc='upper right')
    ax.grid(True, alpha=0.3)
    
    # Subplot 2: Timeline di implementazione
    ax = axes[0, 1]
    durations = [3.2, 7.8, 16.4]  # mesi
    bars = ax.barh(strategies, durations, color=colors_strategy, alpha=0.7)
    ax.set_xlabel('Durata Implementazione (mesi)', fontsize=11)
    ax.set_title('Timeline di Migrazione', fontsize=12, fontweight='bold')
    ax.set_xlim([0, 20])
    for bar, val in zip(bars, durations):
        ax.text(bar.get_width() + 0.3, bar.get_y() + bar.get_height()/2.,
               f'{val:.1f} mesi', ha='left', va='center', fontsize=10)
    ax.grid(True, alpha=0.3, axis='x')
    
    # Subplot 3: Simulazione Monte Carlo TCO 5 anni
    ax = axes[1, 0]
    np.random.seed(42)
    
    for i, strategy in enumerate(strategies):
        # Simula distribuzione TCO reduction
        if strategy == 'Lift & Shift':
            tco_reduction = np.random.normal(23, 5, 1000)
        elif strategy == 'Replatform':
            tco_reduction = np.random.normal(41.5, 6.5, 1000)
        else:  # Refactor
            tco_reduction = np.random.normal(59, 7, 1000)
        
        ax.hist(tco_reduction, bins=30, alpha=0.5, label=strategy, 
               color=colors_strategy[i], density=True)
        
        # Aggiungi linea media
        ax.axvline(x=np.mean(tco_reduction), color=colors_strategy[i], 
                  linestyle='--', linewidth=2)
    
    ax.set_xlabel('Riduzione TCO a 5 anni (\\%)', fontsize=11)
    ax.set_ylabel('Densità di Probabilità', fontsize=11)
    ax.set_title('Distribuzione TCO Reduction (Monte Carlo)', fontsize=12, fontweight='bold')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_xlim([0, 80])
    
    # Subplot 4: ROI nel tempo
    ax = axes[1, 1]
    months = np.arange(0, 37)
    
    for i, strategy in enumerate(strategies):
        if strategy == 'Lift & Shift':
            roi = -8.2 + months * 1.2  # ROI mensile semplificato
        elif strategy == 'Replatform':
            roi = -24.7 + months * 2.8
        else:  # Refactor
            roi = -87.3 + months * 5.2
        
        roi_percent = (roi / abs(roi[0])) * 100 if roi[0] != 0 else roi
        ax.plot(months, roi_percent, label=strategy, color=colors_strategy[i], 
               linewidth=2)
    
    ax.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
    ax.axhline(y=100, color='red', linestyle='--', linewidth=1, 
              label='ROI 100\\%')
    
    ax.set_xlabel('Tempo (mesi)', fontsize=11)
    ax.set_ylabel('ROI (\\%)', fontsize=11)
    ax.set_title('Return on Investment nel Tempo', fontsize=12, fontweight='bold')
    ax.legend(loc='lower right')
    ax.grid(True, alpha=0.3)
    ax.set_xlim([0, 36])
    ax.set_ylim([-150, 400])
    
    plt.suptitle('Analisi TCO Multi-Strategia per Cloud Migration', 
                fontsize=14, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig('figura_3_3_cloud_tco.pdf', bbox_inches='tight')
    plt.savefig('figura_3_3_cloud_tco.png', bbox_inches='tight')
    plt.show()
    
    return fig

# =============================================================================
# FIGURA 3.4: Roadmap di Trasformazione (Gantt Chart)
# =============================================================================

def generate_transformation_roadmap():
    """
    Genera il Gantt chart della roadmap di trasformazione
    """
    fig, ax = plt.subplots(figsize=(14, 8))
    
    # Definizione delle attività
    activities = [
        {'name': 'Power/Cooling Upgrade', 'start': 0, 'duration': 6, 
         'phase': 1, 'cost': 850},
        {'name': 'Monitoring Avanzato', 'start': 2, 'duration': 3, 
         'phase': 1, 'cost': 120},
        {'name': 'Security Assessment', 'start': 1, 'duration': 2, 
         'phase': 1, 'cost': 80},
        
        {'name': 'SD-WAN Deployment', 'start': 6, 'duration': 12, 
         'phase': 2, 'cost': 1200},
        {'name': 'Cloud Migration Wave 1', 'start': 8, 'duration': 14, 
         'phase': 2, 'cost': 2800},
        {'name': 'Zero Trust Phase 1', 'start': 10, 'duration': 16, 
         'phase': 2, 'cost': 1700},
        
        {'name': 'Multi-Cloud Orchestration', 'start': 22, 'duration': 18, 
         'phase': 3, 'cost': 2300},
        {'name': 'Zero Trust Maturity', 'start': 26, 'duration': 10, 
         'phase': 3, 'cost': 900},
        {'name': 'AI/ML Operations', 'start': 28, 'duration': 8, 
         'phase': 3, 'cost': 1000},
    ]
    
    # Colori per fase
    phase_colors = {1: '#3498db', 2: '#f39c12', 3: '#2ecc71'}
    phase_names = {1: 'Quick Wins', 2: 'Core Transformation', 3: 'Advanced Optimization'}
    
    # Crea il Gantt chart
    for i, activity in enumerate(activities):
        ax.barh(i, activity['duration'], left=activity['start'], 
               color=phase_colors[activity['phase']], alpha=0.7,
               edgecolor='black', linewidth=1)
        
        # Aggiungi nome attività
        ax.text(activity['start'] - 0.5, i, activity['name'], 
               ha='right', va='center', fontsize=10)
        
        # Aggiungi costo
        ax.text(activity['start'] + activity['duration'] + 0.5, i, 
               f"€{activity['cost']}k", 
               ha='left', va='center', fontsize=9, style='italic')
    
    # Aggiungi milestone e fasi
    phase_boundaries = [0, 6, 18, 36]
    for i in range(len(phase_boundaries) - 1):
        ax.axvspan(phase_boundaries[i], phase_boundaries[i+1], 
                  alpha=0.1, color=phase_colors[i+1])
        ax.text(phase_boundaries[i] + (phase_boundaries[i+1] - phase_boundaries[i])/2, 
               len(activities), 
               f"Fase {i+1}: {phase_names[i+1]}", 
               ha='center', va='bottom', fontsize=11, fontweight='bold')
    
    # Aggiungi linee di dipendenza
    dependencies = [
        (0, 4),  # Power/Cooling -> Cloud Migration
        (3, 5),  # SD-WAN -> Zero Trust Phase 1
        (4, 6),  # Cloud Migration -> Multi-Cloud
        (5, 7),  # Zero Trust Phase 1 -> Zero Trust Maturity
    ]
    
    for dep in dependencies:
        start_act = activities[dep[0]]
        end_act = activities[dep[1]]
        ax.arrow(start_act['start'] + start_act['duration'], dep[0],
                end_act['start'] - (start_act['start'] + start_act['duration']) - 0.5, 
                dep[1] - dep[0],
                head_width=0.3, head_length=0.3, fc='red', ec='red', 
                alpha=0.4, linestyle='--', linewidth=0.5)
    
    # Formattazione
    ax.set_xlabel('Tempo (mesi)', fontsize=12)
    ax.set_ylabel('Attività', fontsize=12)
    ax.set_title('Roadmap di Trasformazione Infrastrutturale - Vista Gantt', 
                fontsize=14, fontweight='bold')
    ax.set_xlim(-5, 40)
    ax.set_ylim(-1, len(activities) + 1)
    ax.set_yticks([])
    ax.grid(True, alpha=0.3, axis='x')
    
    # Aggiungi legenda per le fasi
    legend_elements = [mpatches.Patch(color=phase_colors[i], 
                                     label=f'Fase {i}: {phase_names[i]}', 
                                     alpha=0.7) 
                      for i in range(1, 4)]
    ax.legend(handles=legend_elements, loc='upper left')
    
    # Aggiungi timeline di ROI cumulativo
    ax2 = ax.twinx()
    months = np.arange(0, 37)
    cumulative_investment = np.zeros(37)
    cumulative_savings = np.zeros(37)
    
    for activity in activities:
        for m in range(activity['start'], min(activity['start'] + activity['duration'], 37)):
            cumulative_investment[m] += activity['cost'] / activity['duration']
    
    # Simula saving cumulativi
    for m in range(37):
        if m > 6:
            cumulative_savings[m] = cumulative_savings[m-1] + (m-6) * 50  # Saving progressivi
    
    roi = (cumulative_savings - cumulative_investment.cumsum()) / cumulative_investment.cumsum() * 100
    roi[np.isnan(roi)] = 0
    roi[np.isinf(roi)] = 0
    
    ax2.plot(months, roi, 'r-', linewidth=2, label='ROI Cumulativo')
    ax2.set_ylabel('ROI Cumulativo (\\%)', fontsize=12, color='red')
    ax2.tick_params(axis='y', labelcolor='red')
    ax2.set_ylim([-100, 250])
    ax2.axhline(y=0, color='red', linestyle=':', linewidth=1)
    ax2.legend(loc='upper right')
    
    plt.tight_layout()
    plt.savefig('figura_3_4_roadmap.pdf', bbox_inches='tight')
    plt.savefig('figura_3_4_roadmap.png', bbox_inches='tight')
    plt.show()
    
    return fig

# =============================================================================
# FIGURA 3.5: Zero Trust Impact Analysis
# =============================================================================

def generate_zero_trust_impact():
    """
    Genera l'analisi dell'impatto Zero Trust su ASSA e latenza
    """
    fig = plt.figure(figsize=(14, 10))
    
    # Crea una griglia custom
    gs = fig.add_gridspec(3, 2, height_ratios=[1, 1, 1], width_ratios=[1, 1])
    
    # Subplot 1: Riduzione ASSA per componenti
    ax1 = fig.add_subplot(gs[0, :])
    
    components = ['Micro-\nsegmentation', 'Edge\nIsolation', 'Traffic\nInspection', 
                 'Least\nPrivilege', 'Continuous\nVerification', 'Altri']
    contributions = [31.2, 24.1, 18.4, 12.3, 8.7, 5.3]
    colors_comp = plt.cm.Set3(np.linspace(0, 1, len(components)))
    
    # Waterfall chart
    cumulative = 0
    for i, (comp, contrib) in enumerate(zip(components, contributions)):
        ax1.bar(i, contrib, bottom=cumulative, color=colors_comp[i], 
               alpha=0.8, edgecolor='black', linewidth=1)
        
        # Aggiungi percentuale
        ax1.text(i, cumulative + contrib/2, f'{contrib:.1f}\\%', 
                ha='center', va='center', fontsize=10, fontweight='bold')
        
        cumulative += contrib
    
    # Linea totale
    ax1.axhline(y=42.7, color='red', linestyle='--', linewidth=2, 
               label='Riduzione Totale ASSA: 42.7\\%')
    
    ax1.set_xticks(range(len(components)))
    ax1.set_xticklabels(components, fontsize=10)
    ax1.set_ylabel('Contributo alla Riduzione ASSA (\\%)', fontsize=11)
    ax1.set_title('Decomposizione della Riduzione Attack Surface con Zero Trust', 
                 fontsize=12, fontweight='bold')
    ax1.legend(loc='upper right')
    ax1.grid(True, alpha=0.3, axis='y')
    ax1.set_ylim([0, 50])
    
    # Subplot 2: Distribuzione latenza
    ax2 = fig.add_subplot(gs[1, 0])
    
    np.random.seed(42)
    # Simula latenze
    traditional = np.random.gamma(4, 12, 1000)  # Traditional ZTNA
    edge_based = np.random.gamma(2, 11.5, 1000)  # Edge-based
    
    ax2.hist(traditional, bins=30, alpha=0.5, label='Traditional ZTNA', 
            color='#e74c3c', density=True)
    ax2.hist(edge_based, bins=30, alpha=0.5, label='Edge-based ZTNA', 
            color='#2ecc71', density=True)
    
    # Aggiungi statistiche
    ax2.axvline(x=np.mean(traditional), color='#e74c3c', linestyle='--', 
               linewidth=2, label=f'Media Trad: {np.mean(traditional):.1f}ms')
    ax2.axvline(x=np.mean(edge_based), color='#2ecc71', linestyle='--', 
               linewidth=2, label=f'Media Edge: {np.mean(edge_based):.1f}ms')
    ax2.axvline(x=50, color='black', linestyle=':', linewidth=2, 
               label='Soglia 50ms')
    
    ax2.set_xlabel('Latenza (ms)', fontsize=11)
    ax2.set_ylabel('Densità di Probabilità', fontsize=11)
    ax2.set_title('Distribuzione Latenza con Zero Trust', fontsize=12, fontweight='bold')
    ax2.legend(fontsize=9)
    ax2.grid(True, alpha=0.3)
    ax2.set_xlim([0, 100])
    
    # Subplot 3: Percentili latenza
    ax3 = fig.add_subplot(gs[1, 1])
    
    percentiles = [50, 75, 90, 95, 99]
    trad_percentiles = [np.percentile(traditional, p) for p in percentiles]
    edge_percentiles = [np.percentile(edge_based, p) for p in percentiles]
    
    x_pos = np.arange(len(percentiles))
    width = 0.35
    
    bars1 = ax3.bar(x_pos - width/2, trad_percentiles, width, 
                   label='Traditional', color='#e74c3c', alpha=0.7)
    bars2 = ax3.bar(x_pos + width/2, edge_percentiles, width, 
                   label='Edge-based', color='#2ecc71', alpha=0.7)
    
    ax3.axhline(y=50, color='red', linestyle='--', linewidth=1, 
               label='Target 50ms')
    
    ax3.set_xlabel('Percentile', fontsize=11)
    ax3.set_ylabel('Latenza (ms)', fontsize=11)
    ax3.set_title('Analisi Percentili Latenza', fontsize=12, fontweight='bold')
    ax3.set_xticks(x_pos)
    ax3.set_xticklabels([f'P{p}' for p in percentiles])
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    ax3.set_ylim([0, 100])
    
    # Aggiungi valori sopra le barre
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax3.text(bar.get_x() + bar.get_width()/2., height + 1,
                   f'{height:.0f}', ha='center', va='bottom', fontsize=9)
    
    # Subplot 4: Evoluzione ASSA nel tempo
    ax4 = fig.add_subplot(gs[2, :])
    
    months = np.arange(0, 37)
    baseline_assa = 100 * np.ones(37)
    
    # Riduzione progressiva con implementazione Zero Trust
    zt_assa = np.zeros(37)
    for m in months:
        if m < 6:
            zt_assa[m] = 100  # Nessuna riduzione iniziale
        elif m < 18:
            zt_assa[m] = 100 - (m - 6) * 2.0  # Fase 1
        elif m < 30:
            zt_assa[m] = 76 - (m - 18) * 2.8  # Fase 2
        else:
            zt_assa[m] = 57.3  # Stato finale
    
    ax4.fill_between(months, baseline_assa, zt_assa, alpha=0.3, 
                     color='#2ecc71', label='Riduzione ASSA')
    ax4.plot(months, baseline_assa, 'r--', linewidth=1, label='Baseline')
    ax4.plot(months, zt_assa, 'b-', linewidth=2, label='Con Zero Trust')
    
    # Aggiungi fasi
    ax4.axvspan(0, 6, alpha=0.1, color='gray', label='Preparazione')
    ax4.axvspan(6, 18, alpha=0.1, color='#3498db', label='ZT Fase 1')
    ax4.axvspan(18, 30, alpha=0.1, color='#f39c12', label='ZT Fase 2')
    ax4.axvspan(30, 36, alpha=0.1, color='#2ecc71', label='ZT Maturity')
    
    ax4.set_xlabel('Tempo (mesi)', fontsize=11)
    ax4.set_ylabel('Attack Surface Index (Baseline = 100)', fontsize=11)
    ax4.set_title('Evoluzione Temporale della Superficie di Attacco con Zero Trust Implementation', 
                 fontsize=12, fontweight='bold')
    ax4.legend(loc='upper right', ncol=2)
    ax4.grid(True, alpha=0.3)
    ax4.set_xlim([0, 36])
    ax4.set_ylim([40, 110])
    
    # Aggiungi annotazioni per milestone
    milestones = [
        (6, 100, 'Inizio ZT'),
        (18, 76, 'Fine Fase 1'),
        (30, 57.3, 'Raggiunta Maturità')
    ]
    
    for m_time, m_value, m_text in milestones:
        ax4.annotate(m_text, xy=(m_time, m_value), xytext=(m_time, m_value - 10),
                    arrowprops=dict(arrowstyle='->', color='black', alpha=0.5),
                    fontsize=9, ha='center')
    
    plt.suptitle('Analisi dell\'Impatto Zero Trust su Sicurezza e Performance', 
                fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig('figura_3_5_zero_trust.pdf', bbox_inches='tight')
    plt.savefig('figura_3_5_zero_trust.png', bbox_inches='tight')
    plt.show()
    
    return fig

# =============================================================================
# Funzione principale per generare tutti i grafici
# =============================================================================

def generate_all_figures():
    """
    Genera tutti i grafici del Capitolo 3
    """
    print("Generazione Figura 3.1: Power Availability...")
    generate_power_availability_figure()
    
    print("Generazione Figura 3.2: Network Evolution...")
    generate_network_evolution_data()
    
    print("Generazione Figura 3.3: Cloud TCO Analysis...")
    generate_cloud_tco_analysis()
    
    print("Generazione Figura 3.4: Transformation Roadmap...")
    generate_transformation_roadmap()
    
    print("Generazione Figura 3.5: Zero Trust Impact...")
    generate_zero_trust_impact()
    
    print("\nTutti i grafici sono stati generati con successo!")
    print("File salvati in formato PDF e PNG.")

if __name__ == "__main__":
    generate_all_figures()