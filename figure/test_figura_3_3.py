#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generazione Grafici per Capitolo 3 - VERSIONE NO LATEX
Fix definitivo per errori LaTeX
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

# Pulizia cache matplotlib (importante!)
import os
import shutil
matplotlib_cachedir = matplotlib.get_cachedir()
if os.path.exists(matplotlib_cachedir):
    try:
        shutil.rmtree(matplotlib_cachedir)
        print(f"Cache matplotlib pulita: {matplotlib_cachedir}")
    except:
        print("Impossibile pulire la cache, continuando...")

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
    'axes.unicode_minus': False  # Usa il segno meno corretto
})

print("Configurazione matplotlib:")
print(f"  text.usetex: {plt.rcParams['text.usetex']}")
print(f"  font.family: {plt.rcParams['font.family']}")
print("")

# =============================================================================
# FIGURA 3.3: TCO Cloud Migration Analysis - VERSIONE CORRETTA
# =============================================================================

def generate_cloud_tco_analysis_fixed():
    """
    Genera l'analisi TCO - VERSIONE SENZA LATEX E SENZA CARATTERI PROBLEMATICI
    """
    print("Generazione Figura 3.3 (versione corretta)...")
    
    # Crea figura con gestione errori
    try:
        fig = plt.figure(figsize=(14, 10))
        
        # Crea subplots manualmente per evitare problemi
        ax1 = plt.subplot(2, 2, 1)
        ax2 = plt.subplot(2, 2, 2)
        ax3 = plt.subplot(2, 2, 3)
        ax4 = plt.subplot(2, 2, 4)
        
        # Dati delle strategie - NESSUN CARATTERE SPECIALE
        strategies = ['Lift-and-Shift', 'Replatform', 'Refactor']
        colors_strategy = ['#3498db', '#f39c12', '#2ecc71']
        
        # ===== Subplot 1: Costi iniziali e saving operativi =====
        initial_costs = [8.2, 24.7, 87.3]
        opex_savings = [23, 41.5, 59]
        
        x_pos = np.arange(len(strategies))
        width = 0.35
        
        # Crea secondo asse Y
        ax1_twin = ax1.twinx()
        
        # Barre per costi iniziali
        bars1 = ax1.bar(x_pos - width/2, initial_costs, width, 
                       label='Costo Iniziale', color='#e74c3c', alpha=0.7)
        
        # Barre per savings
        bars2 = ax1_twin.bar(x_pos + width/2, opex_savings, width, 
                            label='Saving OPEX (%)', color='#2ecc71', alpha=0.7)
        
        # Configurazione assi
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
        
        # ===== Subplot 2: Timeline =====
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
        
        # ===== Subplot 3: Monte Carlo =====
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
        
        # ===== Subplot 4: ROI nel tempo =====
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
        
        # Titolo generale
        fig.suptitle('Analisi TCO Multi-Strategia per Cloud Migration', 
                    fontsize=14, fontweight='bold', y=0.98)
        
        # Adjust layout manualmente invece di tight_layout
        plt.subplots_adjust(left=0.1, right=0.95, top=0.93, bottom=0.07, 
                           hspace=0.3, wspace=0.4)
        
        # Salva figure
        plt.savefig('figura_3_3_cloud_tco.pdf', bbox_inches='tight', dpi=300)
        plt.savefig('figura_3_3_cloud_tco.png', bbox_inches='tight', dpi=300)
        print("  Figura 3.3 salvata con successo!")
        plt.close()
        
        return True
        
    except Exception as e:
        print(f"  ERRORE in Figura 3.3: {e}")
        plt.close('all')
        return False

# =============================================================================
# TEST SINGOLO FIGURA 3.3
# =============================================================================

def test_figura_3_3():
    """
    Test solo della figura problematica
    """
    print("=" * 60)
    print("TEST FIGURA 3.3 - VERSIONE CORRETTA")
    print("=" * 60)
    
    success = generate_cloud_tco_analysis_fixed()
    
    if success:
        print("\n✓ Figura 3.3 generata correttamente!")
        print("  File creati:")
        print("  - figura_3_3_cloud_tco.pdf")
        print("  - figura_3_3_cloud_tco.png")
    else:
        print("\n✗ Errore nella generazione della Figura 3.3")
        print("  Verificare i messaggi di errore sopra")
    
    print("=" * 60)

# =============================================================================
# VERSIONE SEMPLIFICATA DI TUTTE LE FIGURE
# =============================================================================

def generate_all_figures_safe():
    """
    Genera tutte le figure con gestione errori robusta
    """
    print("=" * 60)
    print("GENERAZIONE SICURA DI TUTTE LE FIGURE")
    print("=" * 60)
    
    figures = [
        ("Figura 3.1: Power Availability", generate_figure_3_1),
        ("Figura 3.2: Network Evolution", generate_figure_3_2),
        ("Figura 3.3: Cloud TCO Analysis", generate_cloud_tco_analysis_fixed),
        ("Figura 3.4: Transformation Roadmap", generate_figure_3_4),
        ("Figura 3.5: Zero Trust Impact", generate_figure_3_5)
    ]
    
    results = []
    
    for name, func in figures:
        print(f"\nGenerazione {name}...")
        try:
            func()
            print(f"  ✓ {name} completata")
            results.append((name, True))
        except Exception as e:
            print(f"  ✗ Errore in {name}: {e}")
            results.append((name, False))
            plt.close('all')  # Chiude tutte le figure aperte
    
    print("\n" + "=" * 60)
    print("RIEPILOGO:")
    for name, success in results:
        status = "✓" if success else "✗"
        print(f"  {status} {name}")
    print("=" * 60)

# Placeholder per le altre figure (aggiungerle dal codice originale)
def generate_figure_3_1():
    """Genera Figura 3.1 - da implementare"""
    plt.figure(figsize=(12, 5))
    plt.subplot(121)
    plt.plot([1, 2, 3], [1, 4, 2])
    plt.title("Power Availability")
    plt.subplot(122)
    plt.bar([1, 2, 3], [3, 2, 5])
    plt.title("Cost Analysis")
    plt.savefig('figura_3_1_power_availability.pdf')
    plt.savefig('figura_3_1_power_availability.png')
    plt.close()

def generate_figure_3_2():
    """Genera Figura 3.2 - da implementare"""
    plt.figure(figsize=(12, 10))
    plt.subplot(221)
    plt.bar([1, 2, 3], [4.7, 2.3, 1.2])
    plt.title("MTTR")
    plt.savefig('figura_3_2_network_evolution.pdf')
    plt.savefig('figura_3_2_network_evolution.png')
    plt.close()

def generate_figure_3_4():
    """Genera Figura 3.4 - da implementare"""
    plt.figure(figsize=(14, 8))
    plt.barh([1, 2, 3], [6, 12, 18])
    plt.title("Roadmap")
    plt.savefig('figura_3_4_roadmap.pdf')
    plt.savefig('figura_3_4_roadmap.png')
    plt.close()

def generate_figure_3_5():
    """Genera Figura 3.5 - da implementare"""
    plt.figure(figsize=(14, 10))
    plt.subplot(211)
    plt.bar([1, 2, 3], [31.2, 24.1, 18.4])
    plt.title("Zero Trust Impact")
    plt.savefig('figura_3_5_zero_trust.pdf')
    plt.savefig('figura_3_5_zero_trust.png')
    plt.close()

if __name__ == "__main__":
    # Prima testa solo la figura problematica
    test_figura_3_3()
    
    # Se vuoi generare tutte le figure
    # generate_all_figures_safe()python 