#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Figura 3.5 SEMPLIFICATA - Zero Trust Impact Analysis
Versione ottimizzata per leggibilità in tesi
Solo 3 elementi essenziali: Riduzione ASSA, Confronto Latenze, Timeline
"""

import matplotlib
matplotlib.rcParams['text.usetex'] = False

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import warnings
warnings.filterwarnings('ignore')

# Configurazione stile minimalista
plt.rcParams.update({
    'text.usetex': False,
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'DejaVu Sans'],
    'font.size': 11,
    'figure.dpi': 100,
    'savefig.dpi': 300,
    'axes.unicode_minus': False,
    'axes.spines.top': False,
    'axes.spines.right': False
})

def generate_zero_trust_simplified():
    """
    Genera figura 3.5 semplificata con solo elementi essenziali
    """
    print("Generando Figura 3.5 SEMPLIFICATA...")
    
    # Crea figura con layout 2x1
    fig = plt.figure(figsize=(12, 8))
    
    # ========== PARTE SUPERIORE: Due grafici affiancati ==========
    
    # --- Subplot 1: Composizione Riduzione ASSA (semplificato) ---
    ax1 = plt.subplot(2, 2, 1)
    
    components = ['Micro-\nsegmentation', 'Edge\nIsolation', 'Traffic\nInspection', 
                 'Least\nPrivilege', 'Altri']
    values = [31.2, 24.1, 18.4, 12.3, 14.0]  # Accorpato Continuous Verification in Altri
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
    
    # Bar chart orizzontale pulito
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
    
    # Rimuovi spine superiore e destra
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    
    # Aggiungi totale come testo
    ax1.text(0.98, 0.05, f'TOTALE: 42.7%', 
            transform=ax1.transAxes, fontsize=12, fontweight='bold',
            ha='right', color='darkred',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.3))
    
    # --- Subplot 2: Confronto Latenze (semplificato) ---
    ax2 = plt.subplot(2, 2, 2)
    
    # Dati per il confronto
    categories = ['Media', 'P95', 'P99']
    traditional = [49.2, 95, 105]
    edge_based = [23.3, 46, 56]
    
    x = np.arange(len(categories))
    width = 0.35
    
    # Barre affiancate
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
    
    # Rimuovi spine superiore e destra
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    
    # Grid leggero solo su y
    ax2.yaxis.grid(True, alpha=0.3, linestyle='--')
    ax2.set_axisbelow(True)
    
    # ========== PARTE INFERIORE: Timeline a larghezza piena ==========
    ax3 = plt.subplot(2, 1, 2)
    
    months = np.arange(0, 37)
    baseline_assa = 100 * np.ones(37)
    
    # Calcolo progressione Zero Trust (semplificato)
    zt_assa = np.zeros(37)
    for m in months:
        if m < 6:
            zt_assa[m] = 100  # Preparazione
        elif m < 18:
            # Fase 1: riduzione lineare
            zt_assa[m] = 100 - (m - 6) * 2.0
        elif m < 30:
            # Fase 2: riduzione più lenta
            zt_assa[m] = 76 - (m - 18) * 1.5
        else:
            # Maturità: valore stabile
            zt_assa[m] = 57.3
    
    # Area di riduzione con colore uniforme
    ax3.fill_between(months, baseline_assa, zt_assa, 
                     where=(zt_assa <= baseline_assa),
                     interpolate=True, alpha=0.3, 
                     color='lightgreen', label='Riduzione ASSA Cumulativa')
    
    # Linee principali più spesse
    ax3.plot(months, baseline_assa, 'r--', linewidth=2.5, 
            label='Baseline senza Zero Trust', alpha=0.8)
    ax3.plot(months, zt_assa, 'b-', linewidth=3, 
            label='Implementazione Zero Trust', alpha=0.9)
    
    # Fasi come testo invece di background colorato
    phase_info = [
        (3, 95, 'FASE 0:\nPreparazione'),
        (12, 95, 'FASE 1:\nImplementazione\nCore'),
        (24, 95, 'FASE 2:\nOttimizzazione'),
        (33, 95, 'MATURITÀ')
    ]
    
    for x, y, text in phase_info:
        ax3.text(x, y, text, ha='center', va='top', 
                fontsize=10, color='gray', style='italic')
    
    # Linee verticali per separare le fasi (sottili)
    for x in [6, 18, 30]:
        ax3.axvline(x=x, color='gray', linestyle=':', alpha=0.4, linewidth=1)
    
    # Milestone principali con marker più grandi
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
    
    # Box con risultati finali (più compatto)
    result_text = "RISULTATI:\n• Riduzione ASSA: 42.7%\n• Tempo: 30 mesi\n• Latenza <50ms: 94%"
    ax3.text(0.98, 0.35, result_text, transform=ax3.transAxes,
            fontsize=11, va='top', ha='right',
            bbox=dict(boxstyle='round,pad=0.5', 
                     facecolor='lightyellow', edgecolor='black', linewidth=1.5))
    
    # Formattazione asse
    ax3.set_xlabel('Tempo (mesi)', fontsize=12, fontweight='bold')
    ax3.set_ylabel('Attack Surface Index\n(Baseline = 100)', fontsize=12, fontweight='bold')
    ax3.set_title('Roadmap Implementazione Zero Trust e Riduzione Attack Surface', 
                 fontsize=13, fontweight='bold', pad=15)
    ax3.legend(loc='upper right', fontsize=11, framealpha=0.95)
    ax3.set_xlim([-1, 37])
    ax3.set_ylim([50, 105])
    
    # Grid sottile
    ax3.grid(True, alpha=0.2, linestyle='--')
    ax3.set_axisbelow(True)
    
    # Rimuovi spine superiore e destra
    ax3.spines['top'].set_visible(False)
    ax3.spines['right'].set_visible(False)
    
    # Titolo generale più sobrio
    fig.suptitle('Analisi dell\'Impatto Zero Trust: Sicurezza e Performance', 
                fontsize=14, fontweight='bold', y=0.98)
    
    # Layout ottimizzato
    plt.subplots_adjust(left=0.10, right=0.95, top=0.93, bottom=0.08, 
                       hspace=0.35, wspace=0.35)
    
    # Salva
    plt.savefig('figura_3_5_semplificata.pdf', bbox_inches='tight', dpi=300)
    plt.savefig('figura_3_5_semplificata.png', bbox_inches='tight', dpi=300)
    print("  ✓ Figura 3.5 SEMPLIFICATA salvata con successo!")
    
    plt.show()
    plt.close()

if __name__ == "__main__":
    print("=" * 60)
    print("GENERAZIONE FIGURA 3.5 SEMPLIFICATA PER TESI")
    print("=" * 60)
    generate_zero_trust_simplified()
    print("=" * 60)
    print("Layout semplificato per massima leggibilità")
    print("\nCaratteristiche:")
    print("  • Solo 3 elementi essenziali")
    print("  • Font più grandi per leggibilità")
    print("  • Colori sobri e professionali")
    print("  • Informazioni raggruppate logicamente")
    print("\nFile generati:")
    print("  - figura_3_5_semplificata.pdf")
    print("  - figura_3_5_semplificata.png")
    print("=" * 60)