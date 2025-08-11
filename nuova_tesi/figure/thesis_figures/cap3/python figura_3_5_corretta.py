#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Figura 3.5 CORRETTA - Zero Trust Impact Analysis
Versione pulita e professionale
"""

import matplotlib
matplotlib.rcParams['text.usetex'] = False

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import warnings
warnings.filterwarnings('ignore')

# Configurazione stile
plt.rcParams.update({
    'text.usetex': False,
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'DejaVu Sans'],
    'font.size': 10,
    'figure.dpi': 100,
    'savefig.dpi': 300,
    'axes.unicode_minus': False
})

def generate_zero_trust_impact_corrected():
    """
    Genera l'analisi dell'impatto Zero Trust - VERSIONE CORRETTA
    """
    print("Generando Figura 3.5 (versione corretta)...")
    
    # Crea figura con layout migliorato
    fig = plt.figure(figsize=(15, 11))
    
    # ========== SUBPLOT 1: Waterfall Chart ASSA Reduction ==========
    ax1 = plt.subplot(3, 2, (1, 2))  # Occupa le prime 2 colonne
    
    components = ['Micro-\nsegmentation', 'Edge\nIsolation', 'Traffic\nInspection', 
                 'Least\nPrivilege', 'Continuous\nVerification', 'Altri']
    contributions = [31.2, 24.1, 18.4, 12.3, 8.7, 5.3]
    
    # Colori per ogni componente
    colors = ['#4CAF50', '#2196F3', '#FF9800', '#9C27B0', '#00BCD4', '#FFC107']
    
    # Crea il waterfall chart corretto
    cumulative = 0
    x_positions = np.arange(len(components))
    
    for i, (comp, contrib, color) in enumerate(zip(components, contributions, colors)):
        # Barra dal valore cumulativo precedente
        bar = ax1.bar(x_positions[i], contrib, bottom=cumulative, 
                     color=color, alpha=0.7, edgecolor='black', 
                     linewidth=1.5, width=0.8)
        
        # Etichetta con percentuale DENTRO la barra
        ax1.text(x_positions[i], cumulative + contrib/2, 
                f'{contrib:.1f}%', 
                ha='center', va='center', 
                fontsize=11, fontweight='bold', color='white',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='black', alpha=0.5))
        
        # Aggiorna cumulativo
        cumulative += contrib
    
    # Linea del totale
    ax1.axhline(y=42.7, color='red', linestyle='--', linewidth=2.5, alpha=0.8)
    ax1.text(len(components)-0.5, 42.7, 'Totale: 42.7%', 
            ha='left', va='center', fontsize=11, fontweight='bold',
            color='red', bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8))
    
    # Formattazione
    ax1.set_xticks(x_positions)
    ax1.set_xticklabels(components, fontsize=10, rotation=0)
    ax1.set_ylabel('Riduzione ASSA Cumulativa (%)', fontsize=12, fontweight='bold')
    ax1.set_title('Decomposizione della Riduzione Attack Surface con Zero Trust', 
                 fontsize=13, fontweight='bold', pad=15)
    ax1.set_ylim([0, 50])
    ax1.grid(True, alpha=0.3, axis='y', linestyle='--')
    ax1.set_axisbelow(True)
    
    # Aggiungi box informativo
    info_text = "Ogni componente contribuisce\nalla riduzione totale del 42.7%"
    ax1.text(0.02, 0.98, info_text, transform=ax1.transAxes,
            fontsize=9, va='top', ha='left',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='lightblue', alpha=0.3))
    
    # ========== SUBPLOT 2: Distribuzione Latenza ==========
    ax2 = plt.subplot(3, 2, 3)
    
    np.random.seed(42)
    traditional = np.random.gamma(4, 12, 1000)
    edge_based = np.random.gamma(2, 11.5, 1000)
    
    # Istogrammi con bins più definiti
    n_bins = 40
    ax2.hist(traditional, bins=n_bins, alpha=0.6, label='Traditional ZTNA', 
            color='#e74c3c', density=True, edgecolor='darkred', linewidth=0.5)
    ax2.hist(edge_based, bins=n_bins, alpha=0.6, label='Edge-based ZTNA', 
            color='#2ecc71', density=True, edgecolor='darkgreen', linewidth=0.5)
    
    # Linee medie più evidenti
    mean_trad = np.mean(traditional)
    mean_edge = np.mean(edge_based)
    
    ax2.axvline(x=mean_trad, color='#e74c3c', linestyle='--', linewidth=2.5, alpha=0.8)
    ax2.axvline(x=mean_edge, color='#2ecc71', linestyle='--', linewidth=2.5, alpha=0.8)
    ax2.axvline(x=50, color='black', linestyle=':', linewidth=2, alpha=0.7)
    
    # Annotazioni più chiare
    ax2.text(mean_trad + 2, ax2.get_ylim()[1]*0.9, f'μ = {mean_trad:.1f}ms', 
            fontsize=10, color='#e74c3c', fontweight='bold')
    ax2.text(mean_edge - 8, ax2.get_ylim()[1]*0.9, f'μ = {mean_edge:.1f}ms', 
            fontsize=10, color='#2ecc71', fontweight='bold')
    ax2.text(52, ax2.get_ylim()[1]*0.5, 'Target\n50ms', 
            fontsize=10, color='black', fontweight='bold')
    
    ax2.set_xlabel('Latenza (ms)', fontsize=11, fontweight='bold')
    ax2.set_ylabel('Densità di Probabilità', fontsize=11, fontweight='bold')
    ax2.set_title('Distribuzione Latenza: Traditional vs Edge-based', 
                 fontsize=12, fontweight='bold')
    ax2.legend(loc='upper right', fontsize=10, framealpha=0.9)
    ax2.grid(True, alpha=0.3, linestyle='--')
    ax2.set_xlim([0, 100])
    
    # ========== SUBPLOT 3: Percentili Latenza ==========
    ax3 = plt.subplot(3, 2, 4)
    
    percentiles = [50, 75, 90, 95, 99]
    trad_percentiles = [np.percentile(traditional, p) for p in percentiles]
    edge_percentiles = [np.percentile(edge_based, p) for p in percentiles]
    
    x_pos = np.arange(len(percentiles))
    width = 0.35
    
    # Barre con pattern
    bars1 = ax3.bar(x_pos - width/2, trad_percentiles, width, 
                   label='Traditional', color='#e74c3c', alpha=0.8,
                   edgecolor='darkred', linewidth=1.5)
    bars2 = ax3.bar(x_pos + width/2, edge_percentiles, width, 
                   label='Edge-based', color='#2ecc71', alpha=0.8,
                   edgecolor='darkgreen', linewidth=1.5)
    
    # Linea target
    ax3.axhline(y=50, color='red', linestyle='--', linewidth=2, alpha=0.7)
    ax3.text(ax3.get_xlim()[1]*0.98, 52, 'Target 50ms', 
            ha='right', va='bottom', fontsize=10, color='red', fontweight='bold')
    
    # Valori sopra le barre
    for bar, val in zip(bars1, trad_percentiles):
        height = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width()/2., height + 1,
               f'{height:.0f}', ha='center', va='bottom', 
               fontsize=9, fontweight='bold', color='#e74c3c')
    
    for bar, val in zip(bars2, edge_percentiles):
        height = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width()/2., height + 1,
               f'{height:.0f}', ha='center', va='bottom', 
               fontsize=9, fontweight='bold', color='#2ecc71')
    
    ax3.set_xlabel('Percentile', fontsize=11, fontweight='bold')
    ax3.set_ylabel('Latenza (ms)', fontsize=11, fontweight='bold')
    ax3.set_title('Analisi Percentili: Garanzie di Performance', 
                 fontsize=12, fontweight='bold')
    ax3.set_xticks(x_pos)
    ax3.set_xticklabels([f'P{p}' for p in percentiles], fontsize=10)
    ax3.legend(loc='upper left', fontsize=10, framealpha=0.9)
    ax3.grid(True, alpha=0.3, axis='y', linestyle='--')
    ax3.set_ylim([0, 105])
    
    # ========== SUBPLOT 4: Timeline Evolution (bottom, full width) ==========
    ax4 = plt.subplot(3, 1, 3)  # Occupa tutta la larghezza in basso
    
    months = np.arange(0, 37)
    baseline_assa = 100 * np.ones(37)
    
    # Calcolo progressione Zero Trust
    zt_assa = np.zeros(37)
    for m in months:
        if m < 6:
            zt_assa[m] = 100  # Preparazione
        elif m < 18:
            zt_assa[m] = 100 - (m - 6) * 2.0  # Fase 1
        elif m < 30:
            zt_assa[m] = 76 - (m - 18) * 1.5  # Fase 2
        else:
            zt_assa[m] = 57.3  # Maturità
    
    # Area di riduzione
    ax4.fill_between(months, baseline_assa, zt_assa, 
                     where=(zt_assa < baseline_assa),
                     interpolate=True, alpha=0.4, 
                     color='#2ecc71', label='Riduzione ASSA Raggiunta')
    
    # Linee principali
    ax4.plot(months, baseline_assa, 'r--', linewidth=2, 
            label='Baseline (No Zero Trust)', alpha=0.7)
    ax4.plot(months, zt_assa, 'b-', linewidth=3, 
            label='Con Zero Trust', alpha=0.9)
    
    # Fasi colorate come background
    phase_colors = ['#f0f0f0', '#e3f2fd', '#fff3e0', '#e8f5e9']
    phase_labels = ['Preparazione', 'ZT Fase 1', 'ZT Fase 2', 'ZT Maturity']
    phase_boundaries = [0, 6, 18, 30, 36]
    
    for i in range(len(phase_boundaries) - 1):
        ax4.axvspan(phase_boundaries[i], phase_boundaries[i+1], 
                   alpha=0.2, color=phase_colors[i])
        # Etichette fasi in alto
        mid_point = (phase_boundaries[i] + phase_boundaries[i+1]) / 2
        ax4.text(mid_point, 105, phase_labels[i], 
                ha='center', va='center', fontsize=10, 
                fontweight='bold', color='gray')
    
    # Milestone con annotazioni migliorate
    milestones = [
        (6, 100, 'Avvio\nImplementazione', 'bottom'),
        (18, 76, 'Completamento\nFase 1', 'top'),
        (30, 57.3, 'Raggiunta\nMaturità ZT', 'top')
    ]
    
    for m_time, m_value, m_text, va_pos in milestones:
        if va_pos == 'top':
            y_text = m_value + 5
            arrow_props = dict(arrowstyle='->', color='black', alpha=0.6, lw=1.5)
        else:
            y_text = m_value - 8
            arrow_props = dict(arrowstyle='->', color='black', alpha=0.6, lw=1.5)
        
        ax4.annotate(m_text, xy=(m_time, m_value), 
                    xytext=(m_time, y_text),
                    arrowprops=arrow_props,
                    fontsize=9, ha='center', fontweight='bold',
                    bbox=dict(boxstyle='round,pad=0.3', 
                             facecolor='yellow', alpha=0.3))
    
    # KPI Box
    kpi_text = (f"Riduzione Finale ASSA: 42.7%\n"
               f"Tempo Completamento: 30 mesi\n"
               f"Investment Protection: 57.3% del baseline")
    ax4.text(0.98, 0.25, kpi_text, transform=ax4.transAxes,
            fontsize=10, va='top', ha='right',
            bbox=dict(boxstyle='round,pad=0.5', 
                     facecolor='white', edgecolor='black', alpha=0.9))
    
    ax4.set_xlabel('Tempo (mesi)', fontsize=12, fontweight='bold')
    ax4.set_ylabel('Attack Surface Index\n(Baseline = 100)', fontsize=12, fontweight='bold')
    ax4.set_title('Evoluzione Temporale: Roadmap Zero Trust e Riduzione Attack Surface', 
                 fontsize=13, fontweight='bold', pad=15)
    ax4.legend(loc='upper right', fontsize=10, framealpha=0.9)
    ax4.grid(True, alpha=0.3, linestyle='--')
    ax4.set_xlim([0, 36])
    ax4.set_ylim([40, 110])
    
    # Titolo generale della figura
    fig.suptitle('Zero Trust Impact Analysis: Security Enhancement e Performance Optimization', 
                fontsize=15, fontweight='bold', y=0.98)
    
    # Adjust layout
    plt.subplots_adjust(left=0.08, right=0.95, top=0.94, bottom=0.06, 
                       hspace=0.4, wspace=0.3)
    
    # Salva figura
    plt.savefig('figura_3_5_zero_trust_corrected.pdf', bbox_inches='tight', dpi=300)
    plt.savefig('figura_3_5_zero_trust_corrected.png', bbox_inches='tight', dpi=300)
    print("  ✓ Figura 3.5 corretta salvata con successo!")
    
    plt.show()
    plt.close()

if __name__ == "__main__":
    print("=" * 60)
    print("GENERAZIONE FIGURA 3.5 CORRETTA")
    print("=" * 60)
    generate_zero_trust_impact_corrected()
    print("=" * 60)
    print("File generati:")
    print("  - figura_3_5_zero_trust_corrected.pdf")
    print("  - figura_3_5_zero_trust_corrected.png")
    print("=" * 60)