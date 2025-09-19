#!/usr/bin/env python3
"""
Generazione delle figure per il Capitolo 5 della tesi
Richiede: matplotlib, numpy
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
import os

# Crea la directory per le figure se non esiste
os.makedirs('thesis_figures/cap5', exist_ok=True)

# Configurazione globale per font large
plt.rcParams.update({
    'font.size': 14,
    'axes.titlesize': 16,
    'axes.labelsize': 14,
    'xtick.labelsize': 12,
    'ytick.labelsize': 12,
    'legend.fontsize': 12,
    'figure.titlesize': 18
})

def create_synergy_diagram():
    """Genera il diagramma degli effetti sinergici tra le componenti GIST"""
    
    fig, ax = plt.subplots(1, 1, figsize=(14, 10))
    
    # Definizione posizioni componenti
    components = {
        'Sicurezza\nFisica': (2, 6),
        'Architettura\nModerna': (6, 6),
        'Sicurezza\nInformatica': (2, 2),
        'Conformità\nNormativa': (6, 2)
    }
    
    # Colori per le componenti (più saturi per migliore visualizzazione)
    colors = {
        'Sicurezza\nFisica': '#1976D2',
        'Architettura\nModerna': '#FF6F00',
        'Sicurezza\nInformatica': '#388E3C',
        'Conformità\nNormativa': '#C2185B'
    }
    
    # Disegna componenti con testo bianco per contrasto
    for name, (x, y) in components.items():
        box = FancyBboxPatch(
            (x-1.2, y-0.5), 2.4, 1,
            boxstyle="round,pad=0.05",
            facecolor=colors[name],
            edgecolor='#333333',
            linewidth=2
        )
        ax.add_patch(box)
        ax.text(x, y, name, ha='center', va='center', 
                fontsize=13, fontweight='bold', color='white')
    
    # Definizione sinergie con valori percentuali
    synergies = [
        (components['Sicurezza\nFisica'], components['Architettura\nModerna'], '+27%'),
        (components['Architettura\nModerna'], components['Sicurezza\nInformatica'], '+34%'),
        (components['Sicurezza\nInformatica'], components['Conformità\nNormativa'], '+41%'),
        (components['Sicurezza\nFisica'], components['Sicurezza\nInformatica'], '+18%'),
        (components['Architettura\nModerna'], components['Conformità\nNormativa'], '+22%'),
        (components['Sicurezza\nFisica'], components['Conformità\nNormativa'], '+15%')
    ]
    
    # Disegna frecce delle sinergie
    for (start, end, label) in synergies:
        if start[1] == end[1]:  # Stessa altezza
            connectionstyle = "arc3,rad=0.3"
        else:
            connectionstyle = "arc3,rad=0.15"
            
        arrow = FancyArrowPatch(
            start, end,
            connectionstyle=connectionstyle,
            arrowstyle='<->',
            mutation_scale=20,
            color='#4CAF50',
            linewidth=2.5,
            alpha=0.8
        )
        ax.add_patch(arrow)
        
        # Posiziona etichetta al centro
        mid_x = (start[0] + end[0]) / 2
        mid_y = (start[1] + end[1]) / 2
        
        if start[1] == end[1]:
            mid_y += 0.4 if start[1] > 4 else -0.4
            
        ax.text(mid_x, mid_y, label, ha='center', va='center',
                bbox=dict(boxstyle="round,pad=0.3", 
                         facecolor='white', 
                         edgecolor='#4CAF50',
                         linewidth=2),
                fontsize=12, color='#2E7D32', fontweight='bold')
    
    # Box centrale con effetto totale
    center_box = FancyBboxPatch(
        (3, 3.7), 2, 1,
        boxstyle="round,pad=0.05",
        facecolor='#FFD700',
        edgecolor='#F57C00',
        linewidth=3
    )
    ax.add_patch(center_box)
    ax.text(4, 4.2, 'Effetto Sistema\nTotale: +52%', 
            ha='center', va='center',
            fontsize=14, fontweight='bold')
    
    # Impostazioni grafico
    ax.set_xlim(0, 8)
    ax.set_ylim(0, 8)
    ax.axis('off')
    ax.set_title('Effetti Sinergici tra le Componenti del Modello GIST', 
                 fontsize=16, fontweight='bold', pad=20)
    
    plt.tight_layout()
    plt.savefig('thesis_figures/cap5/synergy_diagram.pdf', dpi=300, bbox_inches='tight')
    plt.savefig('thesis_figures/cap5/synergy_diagram.png', dpi=300, bbox_inches='tight')
    print("✓ Creato: synergy_diagram.pdf/png")
    return fig

def create_roi_analysis():
    """Genera il grafico dell'analisi ROI"""
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    # Dati per il primo grafico - ROI cumulativo
    years = np.array([0, 1, 2, 3, 4, 5])
    investment = np.array([100, 120, 130, 135, 140, 145])  # Investimento cumulativo
    returns = np.array([0, 45, 110, 195, 310, 455])  # Ritorno cumulativo
    net_benefit = returns - investment
    
    ax1.plot(years, investment, 'r-', linewidth=2.5, label='Investimento Cumulativo', 
             marker='o', markersize=8)
    ax1.plot(years, returns, 'g-', linewidth=2.5, label='Benefici Cumulativi', 
             marker='s', markersize=8)
    ax1.plot(years, net_benefit, 'b--', linewidth=2.5, label='Beneficio Netto', 
             marker='^', markersize=8)
    
    # Punto di pareggio
    ax1.axhline(y=0, color='gray', linestyle=':', linewidth=1)
    ax1.axvline(x=1.8, color='orange', linestyle='--', linewidth=2, 
                label='Punto di Pareggio (1.8 anni)')
    
    ax1.set_xlabel('Anni dall\'Implementazione', fontsize=14)
    ax1.set_ylabel('Valore (Indice Base = 100)', fontsize=14)
    ax1.set_title('Analisi del Ritorno sull\'Investimento (ROI)', 
                  fontsize=15, fontweight='bold')
    ax1.legend(loc='upper left', fontsize=12)
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(0, 5)
    ax1.set_ylim(-150, 500)
    
    # Secondo grafico - Distribuzione dei benefici
    categories = ['Riduzione\nCosti IT', 'Minori\nIncidenti', 'Efficienza\nOperativa', 
                  'Nuovi\nRicavi', 'Conformità']
    values = [38, 25, 22, 10, 5]
    colors_bar = ['#2E7D32', '#1976D2', '#FF6F00', '#7B1FA2', '#C62828']
    
    bars = ax2.bar(categories, values, color=colors_bar, edgecolor='black', linewidth=1.5)
    
    # Aggiungi valori sopra le barre
    for bar, value in zip(bars, values):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height + 1,
                f'{value}%', ha='center', va='bottom', fontweight='bold', fontsize=12)
    
    ax2.set_ylabel('Contributo al ROI (%)', fontsize=14)
    ax2.set_title('Distribuzione dei Benefici per Categoria', fontsize=15, fontweight='bold')
    ax2.set_ylim(0, 45)
    ax2.grid(True, axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('thesis_figures/cap5/roi_analysis.pdf', dpi=300, bbox_inches='tight')
    plt.savefig('thesis_figures/cap5/roi_analysis.png', dpi=300, bbox_inches='tight')
    print("✓ Creato: roi_analysis.pdf/png")
    return fig

def create_maturity_evolution():
    """Genera il grafico dell'evoluzione della maturità digitale"""
    
    fig, ax = plt.subplots(figsize=(14, 8))
    
    # Dati temporali
    months = np.arange(0, 37, 1)
    
    # Tre scenari di evoluzione
    scenario_ottimale = 40 + 35 * (1 - np.exp(-0.08 * months))  # Crescita esponenziale
    scenario_medio = 40 + 25 * (1 - np.exp(-0.06 * months))
    scenario_minimo = 40 + 15 * (1 - np.exp(-0.04 * months))
    
    # Plot delle curve
    ax.plot(months, scenario_ottimale, 'g-', linewidth=3, label='Scenario Ottimale', 
            marker='o', markevery=6)
    ax.plot(months, scenario_medio, 'b-', linewidth=2.5, label='Scenario Medio', 
            marker='s', markevery=6)
    ax.plot(months, scenario_minimo, 'r--', linewidth=2, label='Scenario Base', 
            marker='^', markevery=6)
    
    # Zone di maturità
    ax.axhspan(0, 40, alpha=0.2, color='red', label='Livello Critico')
    ax.axhspan(40, 60, alpha=0.2, color='orange')
    ax.axhspan(60, 75, alpha=0.2, color='yellow')
    ax.axhspan(75, 100, alpha=0.2, color='green')
    
    # Annotazioni per le zone
    ax.text(35, 20, 'CRITICO', fontsize=12, fontweight='bold', color='darkred')
    ax.text(35, 50, 'BASE', fontsize=12, fontweight='bold', color='darkorange')
    ax.text(35, 67, 'BUONO', fontsize=12, fontweight='bold', color='goldenrod')
    ax.text(35, 80, 'ECCELLENTE', fontsize=12, fontweight='bold', color='darkgreen')
    
    # Milestone importanti
    milestones = [(6, 'Valutazione\nCompletata'), 
                  (12, 'Fondamenta\nConsolidate'), 
                  (24, 'Architettura\nModernizzata'), 
                  (36, 'Eccellenza\nOperativa')]
    
    for month, label in milestones:
        ax.axvline(x=month, color='gray', linestyle=':', alpha=0.5)
        ax.text(month, 85, label, ha='center', fontsize=11, 
                bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.8))
    
    ax.set_xlabel('Mesi dall\'Inizio della Trasformazione', fontsize=14)
    ax.set_ylabel('Punteggio GIST', fontsize=14)
    ax.set_title('Evoluzione della Maturità Digitale - Scenari di Trasformazione', 
                 fontsize=16, fontweight='bold')
    ax.legend(loc='lower right', fontsize=12)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 36)
    ax.set_ylim(0, 90)
    
    plt.tight_layout()
    plt.savefig('thesis_figures/cap5/maturity_evolution.pdf', dpi=300, bbox_inches='tight')
    plt.savefig('thesis_figures/cap5/maturity_evolution.png', dpi=300, bbox_inches='tight')
    print("✓ Creato: maturity_evolution.pdf/png")
    return fig

def create_transformation_phases():
    """Genera un diagramma delle fasi di trasformazione"""
    
    fig, ax = plt.subplots(figsize=(14, 8))
    
    # Definizione delle fasi
    phases = [
        ('Valutazione e\nPianificazione', 0, 6, '#E3F2FD', '#1976D2'),
        ('Consolidamento\nFondamenta', 6, 12, '#FFF3E0', '#F57C00'),
        ('Modernizzazione\nArchitetturale', 12, 18, '#E8F5E9', '#388E3C'),
        ('Ottimizzazione\nContinua', 18, 24, '#FCE4EC', '#C2185B')
    ]
    
    y_base = 2
    height = 3
    
    for i, (name, start, end, color, edge_color) in enumerate(phases):
        # Rettangolo della fase
        rect = patches.Rectangle((start, y_base), end-start, height,
                                linewidth=2, edgecolor=edge_color, 
                                facecolor=color, alpha=0.7)
        ax.add_patch(rect)
        
        # Testo della fase
        ax.text((start+end)/2, y_base + height/2, name,
               ha='center', va='center', fontsize=13, fontweight='bold')
        
        # Durata sotto
        ax.text((start+end)/2, y_base - 0.5, f'{end-start} mesi',
               ha='center', va='center', fontsize=11, style='italic')
    
    # Freccia di continuità
    arrow = FancyArrowPatch((24, y_base + height/2), (28, y_base + height/2),
                           connectionstyle="arc3", arrowstyle='->',
                           mutation_scale=30, color='#666666', linewidth=2)
    ax.add_patch(arrow)
    ax.text(26, y_base + height/2 + 0.7, 'Miglioramento\nContinuo', 
           ha='center', fontsize=11, style='italic')
    
    # Milestone chiave sopra le fasi
    milestones = [
        (3, 'Assessment\nGIST', 6),
        (9, 'Security\nBaseline', 6),
        (15, 'Cloud\nMigration', 6),
        (21, 'AI/ML\nIntegration', 6)
    ]
    
    for x, label, y in milestones:
        ax.plot(x, y, 'ro', markersize=10)
        ax.text(x, y + 0.5, label, ha='center', fontsize=10,
               bbox=dict(boxstyle="round,pad=0.3", facecolor='white', 
                        edgecolor='red', alpha=0.8))
    
    ax.set_xlim(-1, 30)
    ax.set_ylim(0, 8)
    ax.set_xlabel('Mesi dall\'Inizio del Progetto', fontsize=14)
    ax.set_title('Roadmap della Trasformazione Digitale Sicura', 
                fontsize=16, fontweight='bold')
    ax.set_yticks([])
    ax.grid(True, axis='x', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('thesis_figures/cap5/transformation_phases.pdf', dpi=300, bbox_inches='tight')
    plt.savefig('thesis_figures/cap5/transformation_phases.png', dpi=300, bbox_inches='tight')
    print("✓ Creato: transformation_phases.pdf/png")
    return fig

def main():
    """Funzione principale per generare tutte le figure"""
    
    print("\n=== Generazione Figure Capitolo 5 ===\n")
    
    # Genera tutte le figure
    fig1 = create_synergy_diagram()
    plt.close(fig1)
    
    fig2 = create_roi_analysis()
    plt.close(fig2)
    
    fig3 = create_maturity_evolution()
    plt.close(fig3)
    
    fig4 = create_transformation_phases()
    plt.close(fig4)
    
    print("\n✅ Tutte le figure sono state generate con successo!")
    print("📁 Posizione: thesis_figures/cap5/")
    
    # Mostra un riepilogo
    print("\nFigure generate:")
    print("1. synergy_diagram.pdf/png - Effetti sinergici del modello GIST")
    print("2. roi_analysis.pdf/png - Analisi del ritorno sull'investimento")
    print("3. maturity_evolution.pdf/png - Evoluzione della maturità digitale")
    print("4. transformation_phases.pdf/png - Roadmap della trasformazione")

if __name__ == "__main__":
    main()
