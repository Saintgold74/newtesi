#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GENERAZIONE COMPLETA GRAFICI CAPITOLO 3 - VERSIONE FINALE
Include la Figura 3.5 semplificata per leggibilità ottimale
Tutte e 5 le figure pronte per la tesi
"""

import matplotlib
# FORZA la disabilitazione di LaTeX prima di importare pyplot
matplotlib.rcParams['text.usetex'] = False
matplotlib.rcParams['text.latex.preamble'] = ''

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import pandas as pd
from matplotlib.patches import Rectangle, FancyBboxPatch
import matplotlib.patches as mpatches
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# Pulizia cache matplotlib
import os
import shutil
matplotlib_cachedir = matplotlib.get_cachedir()
if os.path.exists(matplotlib_cachedir):
    try:
        shutil.rmtree(matplotlib_cachedir)
        print(f"Cache matplotlib pulita: {matplotlib_cachedir}")
    except:
        pass

# Configurazione stile SENZA LaTeX
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("husl")

# DISABILITA COMPLETAMENTE LaTeX
plt.rcParams.update({
    'text.usetex': False,
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'DejaVu Sans', 'Liberation Sans'],
    'font.size': 10,
    'figure.dpi': 100,
    'savefig.dpi': 300,
    'axes.unicode_minus': False
})

print("=" * 70)
print("GENERAZIONE GRAFICI CAPITOLO 3 - VERSIONE FINALE")
print("=" * 70)
print(f"Configurazione: LaTeX={plt.rcParams['text.usetex']}, Font={plt.rcParams['font.family']}")
print("-" * 70)

# =============================================================================
# FIGURA 3.1: Correlazione tra Configurazione Power e Availability Sistemica
# =============================================================================

def generate_power_availability_figure():
    """
    Genera il grafico delle curve di affidabilità per diverse configurazioni power
    """
    print("\n[1/5] Generando Figura 3.1: Power Availability...")
    
    fig = plt.figure(figsize=(12, 5))
    ax1 = plt.subplot(1, 2, 1)
    ax2 = plt.subplot(1, 2, 2)
    
    # Dati per le configurazioni
    mtbf_hours = np.linspace(1000, 200000, 1000)
    
    # Configurazione N+1
    n_plus_1_availability = 1 - (1 / mtbf_hours) * 8
    n_plus_1_lower = n_plus_1_availability - np.abs(np.random.normal(0, 0.002, len(mtbf_hours)))
    n_plus_1_upper = n_plus_1_availability + np.abs(np.random.normal(0, 0.002, len(mtbf_hours)))
    
    # Configurazione 2N
    two_n_availability = 1 - (1 / mtbf_hours) * 4
    two_n_lower = two_n_availability - np.abs(np.random.normal(0, 0.001, len(mtbf_hours)))
    two_n_upper = two_n_availability + np.abs(np.random.normal(0, 0.001, len(mtbf_hours)))
    
    # Configurazione 2N+1
    two_n_plus_1_availability = 1 - (1 / mtbf_hours) * 2
    two_n_plus_1_lower = two_n_plus_1_availability - np.abs(np.random.normal(0, 0.0005, len(mtbf_hours)))
    two_n_plus_1_upper = two_n_plus_1_availability + np.abs(np.random.normal(0, 0.0005, len(mtbf_hours)))
    
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
    
    ax1.axhline(y=99.95, color='red', linestyle='--', linewidth=1, 
                label='Target SLA 99.95%')
    
    ax1.set_xlabel('MTBF (migliaia di ore)', fontsize=11)
    ax1.set_ylabel('Availability (%)', fontsize=11)
    ax1.set_title('Curve di Affidabilità per Configurazione', fontsize=12, fontweight='bold')
    ax1.legend(loc='lower right')
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim([0, 200])
    ax1.set_ylim([99.0, 100.0])
    
    # Subplot 2: Analisi Costo-Beneficio
    configs = ['N+1', '2N', '2N+1']
    availability_values = [99.82, 99.94, 99.97]
    cost_index = [100, 143, 186]
    
    ax2_twin = ax2.twinx()
    
    x_pos = np.arange(len(configs))
    width = 0.35
    
    bars1 = ax2.bar(x_pos - width/2, availability_values, width, 
                    label='Availability', color='#3498db', alpha=0.7)
    bars2 = ax2_twin.bar(x_pos + width/2, cost_index, width, 
                         label='Costo Relativo', color='#e74c3c', alpha=0.7)
    
    ax2.set_xlabel('Configurazione', fontsize=11)
    ax2.set_ylabel('Availability (%)', fontsize=11, color='#3498db')
    ax2_twin.set_ylabel('Indice di Costo (N+1 = 100)', fontsize=11, color='#e74c3c')
    ax2.set_title('Trade-off Availability vs Costo', fontsize=12, fontweight='bold')
    ax2.set_xticks(x_pos)
    ax2.set_xticklabels(configs)
    ax2.set_ylim([99.7, 100.0])
    ax2_twin.set_ylim([0, 200])
    
    for bar, val in zip(bars1, availability_values):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height + 0.01,
                f'{val:.2f}%', ha='center', va='bottom', fontsize=9)
    
    for bar, val in zip(bars2, cost_index):
        height = bar.get_height()
        ax2_twin.text(bar.get_x() + bar.get_width()/2., height + 2,
                     f'{val}', ha='center', va='bottom', fontsize=9)
    
    ax2.tick_params(axis='y', labelcolor='#3498db')
    ax2_twin.tick_params(axis='y', labelcolor='#e74c3c')
    ax2.legend(loc='upper left')
    ax2_twin.legend(loc='upper right')
    ax2.grid(True, alpha=0.3)
    
    plt.subplots_adjust(left=0.08, right=0.95, top=0.93, bottom=0.12, wspace=0.3)
    plt.savefig('figura_3_1_power_availability.pdf', bbox_inches='tight', dpi=300)
    plt.savefig('figura_3_1_power_availability.png', bbox_inches='tight', dpi=300)
    plt.close()
    print("      ✓ Figura 3.1 completata")

# =============================================================================
# FIGURA 3.2: Evoluzione Architettura di Rete
# =============================================================================

def generate_network_evolution_data():
    """
    Genera i dati per il diagramma di evoluzione della rete
    """
    print("\n[2/5] Generando Figura 3.2: Network Evolution...")
    
    data = {
        'Legacy\nHub-Spoke': {
            'MTTR': 4.7,
            'Traffic_Inspected': 57,
            'Flexibility': 20,
            'Cost_Index': 100
        },
        'Hybrid\nSD-WAN': {
            'MTTR': 2.3,
            'Traffic_Inspected': 78,
            'Flexibility': 65,
            'Cost_Index': 125
        },
        'Full Mesh\nSD-WAN': {
            'MTTR': 1.2,
            'Traffic_Inspected': 94,
            'Flexibility': 90,
            'Cost_Index': 145
        }
    }
    
    fig = plt.figure(figsize=(12, 10))
    ax1 = plt.subplot(2, 2, 1)
    ax2 = plt.subplot(2, 2, 2)
    ax3 = plt.subplot(2, 2, 3)
    ax4 = plt.subplot(2, 2, 4)
    
    architectures = list(data.keys())
    colors = ['#e74c3c', '#f39c12', '#2ecc71']
    
    # MTTR
    mttr_values = [data[arch]['MTTR'] for arch in architectures]
    bars = ax1.bar(range(len(architectures)), mttr_values, color=colors, alpha=0.7)
    ax1.set_ylabel('MTTR (ore)', fontsize=11)
    ax1.set_title('Mean Time To Repair', fontsize=12, fontweight='bold')
    ax1.set_ylim([0, 5])
    ax1.set_xticks(range(len(architectures)))
    ax1.set_xticklabels(architectures, rotation=0, ha='center')
    for bar, val in zip(bars, mttr_values):
        ax1.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.1,
               f'{val:.1f}h', ha='center', va='bottom', fontsize=10)
    ax1.grid(True, alpha=0.3)
    
    # Traffic Inspected
    traffic_values = [data[arch]['Traffic_Inspected'] for arch in architectures]
    bars = ax2.bar(range(len(architectures)), traffic_values, color=colors, alpha=0.7)
    ax2.set_ylabel('Traffico Ispezionato (%)', fontsize=11)
    ax2.set_title('Visibilità del Traffico East-West', fontsize=12, fontweight='bold')
    ax2.set_ylim([0, 100])
    ax2.set_xticks(range(len(architectures)))
    ax2.set_xticklabels(architectures, rotation=0, ha='center')
    for bar, val in zip(bars, traffic_values):
        ax2.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 1,
               f'{val}%', ha='center', va='bottom', fontsize=10)
    ax2.grid(True, alpha=0.3)
    
    # Flexibility
    flex_values = [data[arch]['Flexibility'] for arch in architectures]
    bars = ax3.bar(range(len(architectures)), flex_values, color=colors, alpha=0.7)
    ax3.set_ylabel('Indice di Flessibilità', fontsize=11)
    ax3.set_title('Agilità Operativa', fontsize=12, fontweight='bold')
    ax3.set_ylim([0, 100])
    ax3.set_xticks(range(len(architectures)))
    ax3.set_xticklabels(architectures, rotation=0, ha='center')
    for bar, val in zip(bars, flex_values):
        ax3.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 1,
               f'{val}', ha='center', va='bottom', fontsize=10)
    ax3.grid(True, alpha=0.3)
    
    # Cost vs Benefit
    cost_values = [data[arch]['Cost_Index'] for arch in architectures]
    benefit_values = [(100 - mttr_values[i]/5*100 + traffic_values[i] + flex_values[i])/3 
                     for i in range(len(architectures))]
    
    x_pos = np.arange(len(architectures))
    width = 0.35
    
    bars1 = ax4.bar(x_pos - width/2, cost_values, width, 
                   label='Costo', color='#e74c3c', alpha=0.7)
    bars2 = ax4.bar(x_pos + width/2, benefit_values, width, 
                   label='Beneficio', color='#2ecc71', alpha=0.7)
    
    ax4.set_ylabel('Indice Relativo', fontsize=11)
    ax4.set_title('Analisi Costo-Beneficio', fontsize=12, fontweight='bold')
    ax4.set_xticks(x_pos)
    ax4.set_xticklabels(architectures, rotation=0, ha='center')
    ax4.legend()
    ax4.grid(True, alpha=0.3)
    
    plt.suptitle('Evoluzione Architettura di Rete: Metriche Comparative', 
                fontsize=14, fontweight='bold', y=0.98)
    plt.subplots_adjust(left=0.08, right=0.95, top=0.93, bottom=0.08, hspace=0.3, wspace=0.3)
    plt.savefig('figura_3_2_network_evolution.pdf', bbox_inches='tight', dpi=300)
    plt.savefig('figura_3_2_network_evolution.png', bbox_inches='tight', dpi=300)
    plt.close()
    print("      ✓ Figura 3.2 completata")

# =============================================================================
# FIGURA 3.3: TCO Cloud Migration Analysis
# =============================================================================

def generate_cloud_tco_analysis():
    """
    Genera l'analisi TCO per le diverse strategie di migrazione cloud
    """
    print("\n[3/5] Generando Figura 3.3: Cloud TCO Analysis...")
    
    fig = plt.figure(figsize=(14, 10))
    ax1 = plt.subplot(2, 2, 1)
    ax2 = plt.subplot(2, 2, 2)
    ax3 = plt.subplot(2, 2, 3)
    ax4 = plt.subplot(2, 2, 4)
    
    strategies = ['Lift-and-Shift', 'Replatform', 'Refactor']
    colors_strategy = ['#3498db', '#f39c12', '#2ecc71']
    
    # Subplot 1: Costi iniziali e saving operativi
    initial_costs = [8.2, 24.7, 87.3]
    opex_savings = [23, 41.5, 59]
    
    x_pos = np.arange(len(strategies))
    width = 0.35
    
    ax1_twin = ax1.twinx()
    
    bars1 = ax1.bar(x_pos - width/2, initial_costs, width, 
                   label='Costo Iniziale', color='#e74c3c', alpha=0.7)
    bars2 = ax1_twin.bar(x_pos + width/2, opex_savings, width, 
                        label='Saving OPEX (%)', color='#2ecc71', alpha=0.7)
    
    ax1.set_xlabel('Strategia di Migrazione', fontsize=11)
    ax1.set_ylabel('Costo Iniziale (k EUR)', fontsize=11, color='#e74c3c')
    ax1_twin.set_ylabel('Saving OPEX (%)', fontsize=11, color='#2ecc71')
    ax1.set_title('Investimento vs Saving Operativi', fontsize=12, fontweight='bold')
    ax1.set_xticks(x_pos)
    ax1.set_xticklabels(strategies, rotation=15, ha='right')
    ax1.tick_params(axis='y', labelcolor='#e74c3c')
    ax1_twin.tick_params(axis='y', labelcolor='#2ecc71')
    ax1.legend(loc='upper left', fontsize=9)
    ax1_twin.legend(loc='upper right', fontsize=9)
    ax1.grid(True, alpha=0.3)
    
    # Subplot 2: Timeline
    durations = [3.2, 7.8, 16.4]
    bars = ax2.barh(range(len(strategies)), durations, color=colors_strategy, alpha=0.7)
    ax2.set_xlabel('Durata Implementazione (mesi)', fontsize=11)
    ax2.set_title('Timeline di Migrazione', fontsize=12, fontweight='bold')
    ax2.set_xlim([0, 20])
    ax2.set_yticks(range(len(strategies)))
    ax2.set_yticklabels(strategies)
    for i, (bar, val) in enumerate(zip(bars, durations)):
        ax2.text(bar.get_width() + 0.3, bar.get_y() + bar.get_height()/2.,
                f'{val:.1f} mesi', ha='left', va='center', fontsize=10)
    ax2.grid(True, alpha=0.3, axis='x')
    
    # Subplot 3: Monte Carlo
    np.random.seed(42)
    
    for i, strategy in enumerate(strategies):
        if strategy == 'Lift-and-Shift':
            tco_reduction = np.random.normal(23, 5, 1000)
        elif strategy == 'Replatform':
            tco_reduction = np.random.normal(41.5, 6.5, 1000)
        else:
            tco_reduction = np.random.normal(59, 7, 1000)
        
        ax3.hist(tco_reduction, bins=30, alpha=0.5, label=strategy, 
                color=colors_strategy[i], density=True)
        ax3.axvline(x=np.mean(tco_reduction), color=colors_strategy[i], 
                   linestyle='--', linewidth=2)
    
    ax3.set_xlabel('Riduzione TCO a 5 anni (%)', fontsize=11)
    ax3.set_ylabel('Densità di Probabilità', fontsize=11)
    ax3.set_title('Distribuzione TCO (Monte Carlo)', fontsize=12, fontweight='bold')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    ax3.set_xlim([0, 80])
    
    # Subplot 4: ROI nel tempo
    months = np.arange(0, 37)
    
    for i, strategy in enumerate(strategies):
        if strategy == 'Lift-and-Shift':
            roi = -8.2 + months * 1.2
        elif strategy == 'Replatform':
            roi = -24.7 + months * 2.8
        else:
            roi = -87.3 + months * 5.2
        
        roi_percent = (roi / abs(roi[0])) * 100 if roi[0] != 0 else roi
        ax4.plot(months, roi_percent, label=strategy, 
                color=colors_strategy[i], linewidth=2)
    
    ax4.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
    ax4.axhline(y=100, color='red', linestyle='--', linewidth=1, 
               label='ROI 100%')
    
    ax4.set_xlabel('Tempo (mesi)', fontsize=11)
    ax4.set_ylabel('ROI (%)', fontsize=11)
    ax4.set_title('Return on Investment nel Tempo', fontsize=12, fontweight='bold')
    ax4.legend(loc='lower right')
    ax4.grid(True, alpha=0.3)
    ax4.set_xlim([0, 36])
    ax4.set_ylim([-150, 400])
    
    fig.suptitle('Analisi TCO Multi-Strategia per Cloud Migration', 
                fontsize=14, fontweight='bold', y=0.98)
    plt.subplots_adjust(left=0.1, right=0.95, top=0.93, bottom=0.07, hspace=0.3, wspace=0.4)
    plt.savefig('figura_3_3_cloud_tco.pdf', bbox_inches='tight', dpi=300)
    plt.savefig('figura_3_3_cloud_tco.png', bbox_inches='tight', dpi=300)
    plt.close()
    print("      ✓ Figura 3.3 completata")

# =============================================================================
# FIGURA 3.4: Roadmap di Trasformazione (Gantt Chart)
# =============================================================================

def generate_transformation_roadmap():
    """
    Genera il Gantt chart della roadmap di trasformazione
    """
    print("\n[4/5] Generando Figura 3.4: Transformation Roadmap...")
    
    fig, ax = plt.subplots(figsize=(14, 8))
    
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
    
    phase_colors = {1: '#3498db', 2: '#f39c12', 3: '#2ecc71'}
    phase_names = {1: 'Quick Wins', 2: 'Core Transformation', 3: 'Advanced Optimization'}
    
    for i, activity in enumerate(activities):
        ax.barh(i, activity['duration'], left=activity['start'], 
               color=phase_colors[activity['phase']], alpha=0.7,
               edgecolor='black', linewidth=1)
        
        ax.text(activity['start'] - 0.5, i, activity['name'], 
               ha='right', va='center', fontsize=10)
        
        ax.text(activity['start'] + activity['duration'] + 0.5, i, 
               f"EUR {activity['cost']}k", 
               ha='left', va='center', fontsize=9, style='italic')
    
    phase_boundaries = [0, 6, 18, 36]
    for i in range(len(phase_boundaries) - 1):
        ax.axvspan(phase_boundaries[i], phase_boundaries[i+1], 
                  alpha=0.1, color=phase_colors[i+1])
        ax.text(phase_boundaries[i] + (phase_boundaries[i+1] - phase_boundaries[i])/2, 
               len(activities), 
               f"Fase {i+1}: {phase_names[i+1]}", 
               ha='center', va='bottom', fontsize=11, fontweight='bold')
    
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
    
    ax.set_xlabel('Tempo (mesi)', fontsize=12)
    ax.set_ylabel('Attività', fontsize=12)
    ax.set_title('Roadmap di Trasformazione Infrastrutturale - Vista Gantt', 
                fontsize=14, fontweight='bold')
    ax.set_xlim(-5, 40)
    ax.set_ylim(-1, len(activities) + 1)
    ax.set_yticks([])
    ax.grid(True, alpha=0.3, axis='x')
    
    legend_elements = [mpatches.Patch(color=phase_colors[i], 
                                     label=f'Fase {i}: {phase_names[i]}', 
                                     alpha=0.7) 
                      for i in range(1, 4)]
    ax.legend(handles=legend_elements, loc='upper left')
    
    # ROI Timeline
    ax2 = ax.twinx()
    months = np.arange(0, 37)
    cumulative_investment = np.zeros(37)
    cumulative_savings = np.zeros(37)
    
    for activity in activities:
        for m in range(activity['start'], min(activity['start'] + activity['duration'], 37)):
            cumulative_investment[m] += activity['cost'] / activity['duration']
    
    for m in range(37):
        if m > 6:
            cumulative_savings[m] = cumulative_savings[m-1] + (m-6) * 50
    
    roi = np.zeros_like(cumulative_investment)
    cumsum = cumulative_investment.cumsum()
    non_zero_mask = cumsum > 0
    roi[non_zero_mask] = (cumulative_savings[non_zero_mask] - cumsum[non_zero_mask]) / cumsum[non_zero_mask] * 100
    
    ax2.plot(months, roi, 'r-', linewidth=2, label='ROI Cumulativo')
    ax2.set_ylabel('ROI Cumulativo (%)', fontsize=12, color='red')
    ax2.tick_params(axis='y', labelcolor='red')
    ax2.set_ylim([-100, 250])
    ax2.axhline(y=0, color='red', linestyle=':', linewidth=1)
    ax2.legend(loc='upper right')
    
    plt.subplots_adjust(left=0.15, right=0.9, top=0.92, bottom=0.08)
    plt.savefig('figura_3_4_roadmap.pdf', bbox_inches='tight', dpi=300)
    plt.savefig('figura_3_4_roadmap.png', bbox_inches='tight', dpi=300)
    plt.close()
    print("      ✓ Figura 3.4 completata")

# =============================================================================
# FIGURA 3.5 SEMPLIFICATA: Zero Trust Impact Analysis
# =============================================================================

def generate_zero_trust_impact():
    """
    Genera figura 3.5 semplificata per massima leggibilità
    """
    print("\n[5/5] Generando Figura 3.5: Zero Trust Impact (versione semplificata)...")
    
    # Crea figura con layout 2x1
    fig = plt.figure(figsize=(12, 8))
    
    # ========== PARTE SUPERIORE: Due grafici affiancati ==========
    
    # --- Subplot 1: Composizione Riduzione ASSA ---
    ax1 = plt.subplot(2, 2, 1)
    
    components = ['Micro-\nsegmentation', 'Edge\nIsolation', 'Traffic\nInspection', 
                 'Least\nPrivilege', 'Altri']
    values = [31.2, 24.1, 18.4, 12.3, 14.0]
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
    
    # Bar chart orizzontale
    y_pos = np.arange(len(components))
    bars = ax1.barh(y_pos, values, color=colors, alpha=0.8, height=0.6)
    
    # Valori a destra delle barre
    for i, (bar, val) in enumerate(zip(bars, values)):
        width = bar.get_width()
        ax1.text(width + 1, bar.get_y() + bar.get_height()/2,
                f'{val:.1f}%', ha='left', va='center', 
                fontsize=11, fontweight='bold')
    
    ax1.set_yticks(y_pos)
    ax1.set_yticklabels(components, fontsize=11)
    ax1.set_xlabel('Contributo (%)', fontsize=12)
    ax1.set_title('Componenti della Riduzione ASSA', fontsize=13, fontweight='bold', pad=15)
    ax1.set_xlim([0, 35])
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    
    # Totale come testo
    ax1.text(0.98, 0.05, f'TOTALE: 42.7%', 
            transform=ax1.transAxes, fontsize=12, fontweight='bold',
            ha='right', color='darkred',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.3))
    
    # --- Subplot 2: Confronto Latenze ---
    ax2 = plt.subplot(2, 2, 2)
    
    categories = ['Media', 'P95', 'P99']
    traditional = [49.2, 95, 105]
    edge_based = [23.3, 46, 56]
    
    x = np.arange(len(categories))
    width = 0.35
    
    bars1 = ax2.bar(x - width/2, traditional, width, label='Traditional ZTNA',
                   color='#e74c3c', alpha=0.8)
    bars2 = ax2.bar(x + width/2, edge_based, width, label='Edge-based ZTNA',
                   color='#2ecc71', alpha=0.8)
    
    # Linea target 50ms
    ax2.axhline(y=50, color='darkblue', linestyle='--', linewidth=2, alpha=0.7)
    ax2.text(2.2, 52, 'Target\n50ms', fontsize=10, color='darkblue', fontweight='bold')
    
    # Valori sopra le barre
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            if height > 100:
                y_pos = height - 5
                color = 'white'
            else:
                y_pos = height + 2
                color = 'black'
            ax2.text(bar.get_x() + bar.get_width()/2., y_pos,
                   f'{height:.0f}', ha='center', va='center' if height > 100 else 'bottom',
                   fontsize=10, fontweight='bold', color=color)
    
    ax2.set_xlabel('Metrica', fontsize=12)
    ax2.set_ylabel('Latenza (ms)', fontsize=12)
    ax2.set_title('Performance Comparison', fontsize=13, fontweight='bold', pad=15)
    ax2.set_xticks(x)
    ax2.set_xticklabels(categories, fontsize=11)
    ax2.legend(loc='upper left', fontsize=10, framealpha=0.9)
    ax2.set_ylim([0, 120])
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax2.yaxis.grid(True, alpha=0.3, linestyle='--')
    ax2.set_axisbelow(True)
    
    # ========== PARTE INFERIORE: Timeline a larghezza piena ==========
    ax3 = plt.subplot(2, 1, 2)
    
    months = np.arange(0, 37)
    baseline_assa = 100 * np.ones(37)
    
    # Calcolo progressione Zero Trust
    zt_assa = np.zeros(37)
    for m in months:
        if m < 6:
            zt_assa[m] = 100
        elif m < 18:
            zt_assa[m] = 100 - (m - 6) * 2.0
        elif m < 30:
            zt_assa[m] = 76 - (m - 18) * 1.5
        else:
            zt_assa[m] = 57.3
    
    # Area di riduzione
    ax3.fill_between(months, baseline_assa, zt_assa, 
                     where=(zt_assa <= baseline_assa),
                     interpolate=True, alpha=0.3, 
                     color='lightgreen', label='Riduzione ASSA Cumulativa')
    
    # Linee principali
    ax3.plot(months, baseline_assa, 'r--', linewidth=2.5, 
            label='Baseline senza Zero Trust', alpha=0.8)
    ax3.plot(months, zt_assa, 'b-', linewidth=3, 
            label='Implementazione Zero Trust', alpha=0.9)
    
    # Fasi come testo
    phase_info = [
        (3, 95, 'FASE 0:\nPreparazione'),
        (12, 95, 'FASE 1:\nImplementazione\nCore'),
        (24, 95, 'FASE 2:\nOttimizzazione'),
        (33, 95, 'MATURITÀ')
    ]
    
    for x, y, text in phase_info:
        ax3.text(x, y, text, ha='center', va='top', 
                fontsize=10, color='gray', style='italic')
    
    # Linee verticali per fasi
    for x in [6, 18, 30]:
        ax3.axvline(x=x, color='gray', linestyle=':', alpha=0.4, linewidth=1)
    
    # Milestone principali
    milestones = [
        (6, 100, 'Start', 'green'),
        (18, 76, '−24%', 'orange'),
        (30, 57.3, '−42.7%', 'red')
    ]
    
    for m_time, m_value, m_text, m_color in milestones:
        ax3.plot(m_time, m_value, 'o', markersize=10, color=m_color, 
                zorder=5, markeredgecolor='black', markeredgewidth=1.5)
        ax3.text(m_time, m_value - 5, m_text, ha='center', 
                fontsize=11, fontweight='bold')
    
    # Box risultati finali
    result_text = "RISULTATI:\n• Riduzione ASSA: 42.7%\n• Tempo: 30 mesi\n• Latenza <50ms: 94%"
    ax3.text(0.98, 0.35, result_text, transform=ax3.transAxes,
            fontsize=11, va='top', ha='right',
            bbox=dict(boxstyle='round,pad=0.5', 
                     facecolor='lightyellow', edgecolor='black', linewidth=1.5))
    
    ax3.set_xlabel('Tempo (mesi)', fontsize=12, fontweight='bold')
    ax3.set_ylabel('Attack Surface Index\n(Baseline = 100)', fontsize=12, fontweight='bold')
    ax3.set_title('Roadmap Implementazione Zero Trust e Riduzione Attack Surface', 
                 fontsize=13, fontweight='bold', pad=15)
    ax3.legend(loc='upper right', fontsize=11, framealpha=0.95)
    ax3.set_xlim([-1, 37])
    ax3.set_ylim([50, 105])
    ax3.grid(True, alpha=0.2, linestyle='--')
    ax3.set_axisbelow(True)
    ax3.spines['top'].set_visible(False)
    ax3.spines['right'].set_visible(False)
    
    # Titolo generale
    fig.suptitle('Analisi dell\'Impatto Zero Trust: Sicurezza e Performance', 
                fontsize=14, fontweight='bold', y=0.98)
    
    # Layout ottimizzato
    plt.subplots_adjust(left=0.10, right=0.95, top=0.93, bottom=0.08, 
                       hspace=0.35, wspace=0.35)
    
    plt.savefig('figura_3_5_zero_trust.pdf', bbox_inches='tight', dpi=300)
    plt.savefig('figura_3_5_zero_trust.png', bbox_inches='tight', dpi=300)
    plt.close()
    print("      ✓ Figura 3.5 completata (versione semplificata)")

# =============================================================================
# Funzione principale per generare tutti i grafici
# =============================================================================

def generate_all_figures():
    """
    Genera tutti i grafici del Capitolo 3
    """
    
    functions = [
        ("Power Availability", generate_power_availability_figure),
        ("Network Evolution", generate_network_evolution_data),
        ("Cloud TCO Analysis", generate_cloud_tco_analysis),
        ("Transformation Roadmap", generate_transformation_roadmap),
        ("Zero Trust Impact", generate_zero_trust_impact)
    ]
    
    results = []
    
    for name, func in functions:
        try:
            func()
            results.append((name, True))
        except Exception as e:
            print(f"      ✗ Errore in {name}: {e}")
            results.append((name, False))
            plt.close('all')
    
    print("\n" + "=" * 70)
    print("RIEPILOGO GENERAZIONE:")
    print("-" * 70)
    
    success_count = sum(1 for _, success in results if success)
    
    for i, (name, success) in enumerate(results, 1):
        status = "✓" if success else "✗"
        print(f"  {status} Figura 3.{i}: {name}")
    
    print("-" * 70)
    
    if success_count == len(functions):
        print("✅ SUCCESSO COMPLETO!")
        print(f"   Tutte le {len(functions)} figure sono state generate correttamente.")
        print("\n📁 File generati nella directory corrente:")
        for i in range(1, 6):
            if i == 5:
                print(f"   • figura_3_5_zero_trust.pdf/.png (versione semplificata)")
            else:
                print(f"   • figura_3_{i}_*.pdf/.png")
    else:
        print(f"⚠️  GENERAZIONE PARZIALE: {success_count}/{len(functions)} figure completate")
        print("   Verificare gli errori sopra riportati.")
    
    print("=" * 70)
    
    return success_count == len(functions)

if __name__ == "__main__":
    success = generate_all_figures()
    if success:
        print("\n✨ Grafici pronti per l'inserimento nella tesi!")
    else:
        print("\n⚠️  Alcuni grafici non sono stati generati. Verificare gli errori.")