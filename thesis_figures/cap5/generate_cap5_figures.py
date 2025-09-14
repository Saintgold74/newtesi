#!/usr/bin/env python3
"""
Generazione grafici per Capitolo 5 - Framework GIST
Grafici professionali per la sintesi finale della tesi
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Rectangle
import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib.sankey import Sankey

# Configurazione professionale
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.labelsize'] = 11
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['xtick.labelsize'] = 9
plt.rcParams['ytick.labelsize'] = 9
plt.rcParams['legend.fontsize'] = 9
plt.rcParams['figure.dpi'] = 150

# Palette colori coerente con la tesi
COLORS = {
    'primary': '#1e3a8a',      # Blu scuro
    'secondary': '#3b82f6',    # Blu medio
    'accent': '#10b981',       # Verde
    'warning': '#f59e0b',      # Arancione
    'danger': '#ef4444',       # Rosso
    'neutral': '#6b7280',      # Grigio
    'light': '#f3f4f6',        # Grigio chiaro
    'dark': '#1f2937',         # Grigio scuro
    # Colori per le 4 dimensioni GIST
    'fisica': '#E8F4FD',       # Azzurro chiaro
    'architetturale': '#FFF4E6', # Giallo chiaro
    'sicurezza': '#E8F5E9',    # Verde chiaro
    'conformita': '#FCE4EC',   # Rosa chiaro
    'sinergia': '#FFE082'      # Oro per effetto totale
}

def create_synergy_effects_diagram():
    """
    Figura 5.1: Diagramma degli effetti sinergici del framework GIST
    Mostra le 4 componenti e le loro interazioni con percentuali di amplificazione
    """
    fig, ax = plt.subplots(1, 1, figsize=(14, 10))
    
    # Posizioni ottimizzate per le 4 componenti (quadrato)
    components = {
        'Fisica\n(18%)': (2, 7),
        'Architetturale\n(32%)': (7, 7),
        'Sicurezza\n(28%)': (2, 2),
        'Conformità\n(22%)': (7, 2)
    }
    
    # Colori specifici per componente
    comp_colors = {
        'Fisica\n(18%)': COLORS['fisica'],
        'Architetturale\n(32%)': COLORS['architetturale'],
        'Sicurezza\n(28%)': COLORS['sicurezza'],
        'Conformità\n(22%)': COLORS['conformita']
    }
    
    # Disegna le componenti come box arrotondati
    boxes = {}
    for name, (x, y) in components.items():
        # Box principale
        box = FancyBboxPatch(
            (x-1.2, y-0.5), 2.4, 1,
            boxstyle="round,pad=0.08",
            facecolor=comp_colors[name],
            edgecolor='#333333',
            linewidth=2.5,
            zorder=2
        )
        ax.add_patch(box)
        boxes[name] = box
        
        # Testo del componente
        component_name = name.split('\n')[0]
        weight = name.split('\n')[1]
        
        ax.text(x, y+0.15, component_name, ha='center', va='center', 
                fontsize=12, fontweight='bold', zorder=3)
        ax.text(x, y-0.2, weight, ha='center', va='center', 
                fontsize=10, style='italic', color='#555', zorder=3)
    
    # Definizione delle sinergie con valori dal testo originale
    synergies = [
        (components['Fisica\n(18%)'], components['Architetturale\n(32%)'], '+27%', 'above'),
        (components['Architetturale\n(32%)'], components['Sicurezza\n(28%)'], '+34%', 'right'),
        (components['Sicurezza\n(28%)'], components['Conformità\n(22%)'], '+41%', 'below'),
        (components['Fisica\n(18%)'], components['Sicurezza\n(28%)'], '+18%', 'left'),
        (components['Architetturale\n(32%)'], components['Conformità\n(22%)'], '+22%', 'right'),
        (components['Fisica\n(18%)'], components['Conformità\n(22%)'], '+15%', 'diagonal')
    ]
    
    # Disegna frecce per le sinergie
    for (start, end, label, position) in synergies:
        # Calcola il tipo di connessione basato sulla posizione
        if start[1] == end[1]:  # Stessa altezza (orizzontale)
            connectionstyle = "arc3,rad=0.2"
            mid_y_offset = 0.4 if start[1] > 4 else -0.4
        else:
            if start[0] == end[0]:  # Stessa x (verticale)
                connectionstyle = "arc3,rad=0.2"
                mid_y_offset = 0
            else:  # Diagonale
                connectionstyle = "arc3,rad=0.15"
                mid_y_offset = 0
        
        # Crea freccia bidirezionale
        arrow = FancyArrowPatch(
            start, end,
            connectionstyle=connectionstyle,
            arrowstyle='<->',
            mutation_scale=20,
            color='#4CAF50',
            linewidth=2,
            alpha=0.8,
            zorder=1
        )
        ax.add_patch(arrow)
        
        # Posiziona etichetta della sinergia
        mid_x = (start[0] + end[0]) / 2
        mid_y = (start[1] + end[1]) / 2 + mid_y_offset
        
        # Aggiusta posizione per diagonali
        if position == 'diagonal':
            if start[0] < end[0]:  # Da sinistra a destra
                mid_x -= 0.5
            else:
                mid_x += 0.5
        
        # Box per la percentuale
        bbox_props = dict(
            boxstyle="round,pad=0.3",
            facecolor='white',
            edgecolor='#4CAF50',
            linewidth=1.5,
            alpha=0.95
        )
        
        ax.text(mid_x, mid_y, label, ha='center', va='center',
                bbox=bbox_props, fontsize=10, color='#2E7D32', 
                fontweight='bold', zorder=4)
    
    # Box centrale per l'effetto sistema totale
    center_x, center_y = 4.5, 4.5
    
    # Cerchio decorativo dietro il box centrale
    circle = Circle((center_x, center_y), 1.2, 
                   facecolor=COLORS['sinergia'], 
                   edgecolor=COLORS['warning'],
                   linewidth=2, alpha=0.3, zorder=1)
    ax.add_patch(circle)
    
    # Box centrale
    center_box = FancyBboxPatch(
        (center_x-1, center_y-0.5), 2, 1,
        boxstyle="round,pad=0.08",
        facecolor=COLORS['sinergia'],
        edgecolor='#F57C00',
        linewidth=3,
        zorder=2
    )
    ax.add_patch(center_box)
    
    # Testo effetto totale
    ax.text(center_x, center_y+0.15, 'Effetto Sistema', 
            ha='center', va='center', fontsize=11, fontweight='bold', zorder=3)
    ax.text(center_x, center_y-0.2, 'Totale: +52%', 
            ha='center', va='center', fontsize=12, fontweight='bold',
            color='#E65100', zorder=3)
    
    # Aggiungi formula GIST nell'angolo
    formula_text = r'$GIST = \sum_{k=1}^{4} w_k \times S_k^{0.95}$'
    ax.text(0.5, 8.5, formula_text, fontsize=11, 
           bbox=dict(boxstyle='round', facecolor='white', 
                    edgecolor=COLORS['primary'], alpha=0.9))
    
    # Impostazioni grafico
    ax.set_xlim(0, 9)
    ax.set_ylim(0, 9)
    ax.axis('off')
    
    # Titolo
    ax.set_title('Effetti Sinergici del Framework GIST: Amplificazione del Valore attraverso Integrazione Sistemica', 
                 fontsize=14, fontweight='bold', pad=20)
    
    # Legenda
    legend_elements = [
        patches.Patch(facecolor=COLORS['fisica'], edgecolor='#333', 
                     label='Dimensione Fisica (18%)'),
        patches.Patch(facecolor=COLORS['architetturale'], edgecolor='#333', 
                     label='Dimensione Architetturale (32%)'),
        patches.Patch(facecolor=COLORS['sicurezza'], edgecolor='#333', 
                     label='Dimensione Sicurezza (28%)'),
        patches.Patch(facecolor=COLORS['conformita'], edgecolor='#333', 
                     label='Dimensione Conformità (22%)'),
        patches.Patch(facecolor=COLORS['sinergia'], edgecolor='#F57C00', 
                     label='Effetto Sinergico (+52%)')
    ]
    ax.legend(handles=legend_elements, loc='upper left', 
             frameon=True, fancybox=True, shadow=True, fontsize=9)
    
    plt.tight_layout()
    plt.savefig('synergy_effects.pdf', dpi=300, bbox_inches='tight')
    plt.savefig('synergy_effects.png', dpi=300, bbox_inches='tight')
    print("✓ Generato: synergy_effects.pdf/png")
    plt.show()

def create_validation_dashboard():
    """
    Figura 5.2: Dashboard di validazione delle tre ipotesi H1, H2, H3
    """
    fig = plt.figure(figsize=(15, 10))
    
    # Crea una griglia 2x3 per i subplot
    gs = fig.add_gridspec(2, 3, hspace=0.3, wspace=0.3)
    
    # Dati per le validazioni
    hypotheses_data = {
        'H1': {
            'name': 'Cloud-Ibrido',
            'metrics': ['Disponibilità', 'Riduzione TCO'],
            'targets': [99.9, 30],
            'results': [99.96, 38.2],
            'units': ['%', '%']
        },
        'H2': {
            'name': 'Zero Trust',
            'metrics': ['Riduzione Attack Surface'],
            'targets': [30],
            'results': [42.7],
            'units': ['%']
        },
        'H3': {
            'name': 'Conformità Integrata',
            'metrics': ['Riduzione Costi'],
            'targets': [25],
            'results': [39.1],
            'units': ['%']
        }
    }
    
    # Subplot 1: H1 Disponibilità
    ax1 = fig.add_subplot(gs[0, 0])
    categories = ['Target', 'Risultato']
    values_h1_disp = [99.9, 99.96]
    bars1 = ax1.bar(categories, values_h1_disp, color=[COLORS['neutral'], COLORS['accent']])
    ax1.set_ylim(99.8, 100)
    ax1.set_ylabel('Disponibilità (%)')
    ax1.set_title('H1: Disponibilità Cloud-Ibrido', fontweight='bold')
    
    # Aggiungi valori sulle barre
    for bar, val in zip(bars1, values_h1_disp):
        ax1.text(bar.get_x() + bar.get_width()/2, val + 0.01,
                f'{val}%', ha='center', va='bottom', fontweight='bold')
    
    # Aggiungi linea target
    ax1.axhline(y=99.9, color=COLORS['danger'], linestyle='--', 
               linewidth=1, label='Target')
    ax1.legend()
    
    # Subplot 2: H1 TCO
    ax2 = fig.add_subplot(gs[0, 1])
    values_h1_tco = [30, 38.2]
    bars2 = ax2.bar(categories, values_h1_tco, color=[COLORS['neutral'], COLORS['accent']])
    ax2.set_ylabel('Riduzione TCO (%)')
    ax2.set_title('H1: Riduzione TCO', fontweight='bold')
    
    for bar, val in zip(bars2, values_h1_tco):
        ax2.text(bar.get_x() + bar.get_width()/2, val + 1,
                f'{val}%', ha='center', va='bottom', fontweight='bold')
    
    ax2.axhline(y=30, color=COLORS['danger'], linestyle='--', 
               linewidth=1, label='Target')
    
    # Subplot 3: H2 Attack Surface
    ax3 = fig.add_subplot(gs[0, 2])
    values_h2 = [30, 42.7]
    bars3 = ax3.bar(categories, values_h2, color=[COLORS['neutral'], COLORS['accent']])
    ax3.set_ylabel('Riduzione Attack Surface (%)')
    ax3.set_title('H2: Zero Trust Architecture', fontweight='bold')
    
    for bar, val in zip(bars3, values_h2):
        ax3.text(bar.get_x() + bar.get_width()/2, val + 1,
                f'{val}%', ha='center', va='bottom', fontweight='bold')
    
    ax3.axhline(y=30, color=COLORS['danger'], linestyle='--', 
               linewidth=1, label='Target')
    
    # Subplot 4: H3 Conformità
    ax4 = fig.add_subplot(gs[1, 0])
    values_h3 = [25, 39.1]
    bars4 = ax4.bar(categories, values_h3, color=[COLORS['neutral'], COLORS['accent']])
    ax4.set_ylabel('Riduzione Costi Conformità (%)')
    ax4.set_title('H3: Conformità Integrata', fontweight='bold')
    
    for bar, val in zip(bars4, values_h3):
        ax4.text(bar.get_x() + bar.get_width()/2, val + 1,
                f'{val}%', ha='center', va='bottom', fontweight='bold')
    
    ax4.axhline(y=25, color=COLORS['danger'], linestyle='--', 
               linewidth=1, label='Target')
    
    # Subplot 5: Matrice di correlazione effetti sinergici
    ax5 = fig.add_subplot(gs[1, 1:])
    
    # Dati di correlazione tra componenti
    components_list = ['Fisica', 'Architetturale', 'Sicurezza', 'Conformità']
    correlation_matrix = np.array([
        [1.00, 0.27, 0.18, 0.15],
        [0.27, 1.00, 0.34, 0.22],
        [0.18, 0.34, 1.00, 0.41],
        [0.15, 0.22, 0.41, 1.00]
    ])
    
    # Heatmap
    im = ax5.imshow(correlation_matrix, cmap='YlOrRd', aspect='auto', vmin=0, vmax=1)
    
    # Etichette
    ax5.set_xticks(np.arange(len(components_list)))
    ax5.set_yticks(np.arange(len(components_list)))
    ax5.set_xticklabels(components_list, rotation=45, ha='right')
    ax5.set_yticklabels(components_list)
    
    # Aggiungi valori nelle celle
    for i in range(len(components_list)):
        for j in range(len(components_list)):
            if i != j:
                text = ax5.text(j, i, f'+{int(correlation_matrix[i, j]*100)}%',
                              ha='center', va='center', color='black', fontsize=9)
    
    ax5.set_title('Matrice Effetti Sinergici', fontweight='bold')
    
    # Colorbar
    cbar = plt.colorbar(im, ax=ax5, fraction=0.046, pad=0.04)
    cbar.set_label('Intensità Sinergia', rotation=270, labelpad=20)
    
    # Titolo generale
    fig.suptitle('Dashboard Validazione Ipotesi - Framework GIST', 
                fontsize=16, fontweight='bold', y=1.02)
    
    # Box con statistiche aggregate
    stats_text = (
        "Validazione Complessiva:\n"
        "• Tutti i target superati (p < 0.001)\n"
        "• Miglioramento medio: +35.2%\n"
        "• Effetto sinergico: +52%\n"
        "• ROI complessivo: 262%"
    )
    fig.text(0.02, 0.5, stats_text, fontsize=10, 
            bbox=dict(boxstyle='round', facecolor='white', 
                     edgecolor=COLORS['primary'], linewidth=2),
            va='center')
    
    plt.tight_layout()
    plt.savefig('validation_dashboard.pdf', dpi=300, bbox_inches='tight')
    plt.savefig('validation_dashboard.png', dpi=300, bbox_inches='tight')
    print("✓ Generato: validation_dashboard.pdf/png")
    plt.show()

def create_gist_evolution_timeline():
    """
    Figura 5.3: Timeline evoluzione GIST Score nei tre scenari
    """
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), 
                                   gridspec_kw={'height_ratios': [2, 1]})
    
    # Timeline in mesi
    months = np.arange(0, 37)
    
    # Traiettorie GIST Score per i tre scenari
    # Baseline: crescita lenta
    baseline = 40.9 + months * 0.3 + np.random.normal(0, 0.5, len(months))
    baseline = np.clip(baseline, 40, 50)
    
    # Transizione: crescita moderata
    transition = np.zeros(len(months))
    transition[0:6] = np.linspace(40.9, 48, 6)
    transition[6:12] = np.linspace(48, 56, 6)
    transition[12:18] = np.linspace(56, 62.46, 6)
    transition[18:] = 62.46 + (months[18:] - 18) * 0.5
    transition = np.clip(transition, 40, 75)
    
    # Ottimizzato: crescita rapida secondo roadmap
    optimized = np.zeros(len(months))
    optimized[0:6] = np.linspace(40.9, 48.9, 6)   # Fase 1: +8
    optimized[6:12] = np.linspace(48.9, 62.9, 6)  # Fase 2: +14
    optimized[12:18] = np.linspace(62.9, 74.9, 6) # Fase 3: +12
    optimized[18:36] = np.linspace(74.9, 81.05, 18) # Fase 4: +6
    
    # Plot principale - GIST Score evolution
    ax1.plot(months, baseline, linewidth=2, color=COLORS['danger'], 
            label='Scenario Baseline', linestyle='--')
    ax1.plot(months, transition, linewidth=2.5, color=COLORS['warning'], 
            label='Scenario Transizione')
    ax1.plot(months, optimized, linewidth=3, color=COLORS['accent'], 
            label='Scenario Ottimizzato (GIST)')
    
    # Aree colorate per livelli di maturità
    ax1.axhspan(0, 25, alpha=0.1, color='red', label='Iniziale')
    ax1.axhspan(25, 50, alpha=0.1, color='orange', label='In Sviluppo')
    ax1.axhspan(50, 75, alpha=0.1, color='yellow', label='Avanzato')
    ax1.axhspan(75, 100, alpha=0.1, color='green', label='Ottimizzato')
    
    # Linee verticali per le fasi
    phases = [
        (6, 'Fine Fase 1'),
        (12, 'Fine Fase 2'),
        (18, 'Fine Fase 3'),
        (36, 'Fine Fase 4')
    ]
    
    for month, label in phases:
        ax1.axvline(x=month, color='gray', linestyle=':', alpha=0.5)
        ax1.text(month, 85, label, rotation=90, va='bottom', fontsize=8)
    
    ax1.set_ylabel('GIST Score', fontsize=12)
    ax1.set_title('Evoluzione del GIST Score: Confronto Scenari di Trasformazione', 
                 fontsize=14, fontweight='bold')
    ax1.set_xlim(0, 36)
    ax1.set_ylim(35, 90)
    ax1.legend(loc='lower right', fontsize=10)
    ax1.grid(True, alpha=0.3)
    
    # Subplot 2 - Investimenti cumulativi
    investment_baseline = months * 0.05  # Manutenzione minima
    investment_transition = np.zeros(len(months))
    investment_optimized = np.zeros(len(months))
    
    # Transizione: investimenti moderati
    investment_transition[0:6] = np.linspace(0, 0.6, 6)
    investment_transition[6:12] = np.linspace(0.6, 2.0, 6)
    investment_transition[12:18] = np.linspace(2.0, 3.2, 6)
    investment_transition[18:] = 3.2 + (months[18:] - 18) * 0.05
    
    # Ottimizzato: secondo roadmap
    investment_optimized[0:6] = np.linspace(0, 1.0, 6)    # Fase 1: 1M€
    investment_optimized[6:12] = np.linspace(1.0, 3.7, 6)  # Fase 2: 2.7M€
    investment_optimized[12:18] = np.linspace(3.7, 5.8, 6) # Fase 3: 2.1M€
    investment_optimized[18:36] = np.linspace(5.8, 7.2, 18) # Fase 4: 1.4M€
    
    ax2.fill_between(months, 0, investment_baseline, alpha=0.3, 
                    color=COLORS['danger'], label='Baseline')
    ax2.fill_between(months, 0, investment_transition, alpha=0.3, 
                    color=COLORS['warning'], label='Transizione')
    ax2.fill_between(months, 0, investment_optimized, alpha=0.3, 
                    color=COLORS['accent'], label='Ottimizzato')
    
    ax2.set_xlabel('Tempo (mesi)', fontsize=12)
    ax2.set_ylabel('Investimento Cumulativo (M€)', fontsize=12)
    ax2.set_title('Profilo di Investimento per Scenario', fontsize=12, fontweight='bold')
    ax2.set_xlim(0, 36)
    ax2.legend(loc='upper left', fontsize=10)
    ax2.grid(True, alpha=0.3)
    
    # Annotazioni ROI
    ax2.text(30, investment_optimized[30] + 0.3, 
            f'ROI: 262%\n@ 36 mesi', fontsize=9, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='white', 
                     edgecolor=COLORS['accent']))
    
    plt.tight_layout()
    plt.savefig('gist_evolution_timeline.pdf', dpi=300, bbox_inches='tight')
    plt.savefig('gist_evolution_timeline.png', dpi=300, bbox_inches='tight')
    print("✓ Generato: gist_evolution_timeline.pdf/png")
    plt.show()

def create_roadmap_gantt():
    """
    Figura 5.4: Gantt chart della roadmap implementativa GIST
    """
    fig, ax = plt.subplots(figsize=(14, 8))
    
    # Definizione delle fasi con colori e dettagli
    phases = [
        {
            'name': 'Fase 1: Fondamenta',
            'start': 0, 'duration': 6,
            'color': COLORS['primary'],
            'tasks': ['Assessment', 'Infrastruttura', 'Segmentazione', 'Governance'],
            'investment': '0.9-1.2M€',
            'roi': '140%'
        },
        {
            'name': 'Fase 2: Modernizzazione',
            'start': 6, 'duration': 6,
            'color': COLORS['secondary'],
            'tasks': ['SD-WAN', 'Cloud Migration', 'Zero Trust Base', 'Automazione'],
            'investment': '2.3-3.1M€',
            'roi': '220%'
        },
        {
            'name': 'Fase 3: Integrazione',
            'start': 12, 'duration': 6,
            'color': COLORS['accent'],
            'tasks': ['Multi-cloud', 'Compliance Auto', 'Edge Computing', 'API Gateway'],
            'investment': '1.8-2.4M€',
            'roi': '310%'
        },
        {
            'name': 'Fase 4: Ottimizzazione',
            'start': 18, 'duration': 18,
            'color': COLORS['warning'],
            'tasks': ['AI/ML Integration', 'Zero Trust Maturo', 'Analytics', 'E2E Automation'],
            'investment': '1.2-1.6M€',
            'roi': '380%'
        }
    ]
    
    # Plot delle fasi principali
    y_positions = []
    for i, phase in enumerate(phases):
        y_pos = len(phases) - i - 1
        y_positions.append(y_pos)
        
        # Barra principale della fase
        ax.barh(y_pos, phase['duration'], left=phase['start'],
               height=0.5, color=phase['color'], alpha=0.7,
               edgecolor='white', linewidth=2)
        
        # Nome della fase
        ax.text(phase['start'] + phase['duration']/2, y_pos,
               phase['name'], ha='center', va='center',
               fontsize=11, fontweight='bold', color='white')
        
        # Dettagli sotto la barra
        detail_text = f"Invest: {phase['investment']} | ROI: {phase['roi']}"
        ax.text(phase['start'] + phase['duration']/2, y_pos - 0.35,
               detail_text, ha='center', va='center',
               fontsize=8, style='italic')
    
    # Milestones critici
    milestones = [
        (3, 'Assessment\nCompletato', 3.7),
        (6, 'Infrastruttura\nModernizzata', 2.7),
        (9, 'Cloud\nMigration 50%', 2.7),
        (12, 'Zero Trust\nOperativo', 1.7),
        (15, 'Multi-cloud\nAttivo', 1.7),
        (18, 'Compliance\nAutomatizzata', 0.7),
        (24, 'AI/ML\nIntegrato', 0.7),
        (36, 'Trasformazione\nCompleta', 0.7)
    ]
    
    for month, label, y in milestones:
        ax.scatter(month, y, s=150, color=COLORS['danger'], 
                  marker='D', zorder=5, edgecolors='white', linewidth=1)
        ax.text(month, y + 0.15, label, ha='center', fontsize=7,
               fontweight='bold')
    
    # Quick wins (stelle)
    quick_wins = [
        (2, 'MFA\nUniversale', 3.3),
        (4, 'SIEM\nCentralizzato', 3.3),
        (8, 'API Gateway\nUnificato', 2.3),
        (14, 'Patch\nAutomatiche', 1.3)
    ]
    
    for month, label, y in quick_wins:
        ax.scatter(month, y, s=100, color='gold', marker='*',
                  zorder=5, edgecolors='orange', linewidth=1)
        ax.text(month, y - 0.15, label, ha='center', fontsize=7,
               color='darkorange')
    
    # Griglia temporale
    for month in range(0, 37, 3):
        ax.axvline(x=month, color='gray', linestyle=':', alpha=0.3)
        ax.text(month, -0.5, f'M{month}', ha='center', fontsize=8)
    
    # Configurazione assi
    ax.set_xlim(-1, 37)
    ax.set_ylim(-0.7, 4.2)
    ax.set_xlabel('Timeline (mesi)', fontsize=12, fontweight='bold')
    ax.set_yticks(y_positions)
    ax.set_yticklabels([f'Fase {i+1}' for i in range(len(phases))])
    ax.set_title('Roadmap Implementativa Framework GIST - Timeline e Milestones', 
                fontsize=14, fontweight='bold')
    
    # Legenda
    from matplotlib.lines import Line2D
    legend_elements = [
        Line2D([0], [0], marker='D', color='w', markerfacecolor=COLORS['danger'],
              markersize=10, label='Milestone'),
        Line2D([0], [0], marker='*', color='w', markerfacecolor='gold',
              markersize=12, label='Quick Win'),
        patches.Patch(facecolor=COLORS['primary'], alpha=0.7, label='Fondamenta'),
        patches.Patch(facecolor=COLORS['secondary'], alpha=0.7, label='Modernizzazione'),
        patches.Patch(facecolor=COLORS['accent'], alpha=0.7, label='Integrazione'),
        patches.Patch(facecolor=COLORS['warning'], alpha=0.7, label='Ottimizzazione')
    ]
    ax.legend(handles=legend_elements, loc='upper right', 
             ncol=2, fontsize=9, frameon=True)
    
    # Box con metriche totali
    summary_text = (
        "Riepilogo Programma:\n"
        "• Durata: 36 mesi\n"
        "• Investimento: 6.2-8.3M€\n"
        "• ROI Complessivo: 262%\n"
        "• GIST Score: +40 punti"
    )
    ax.text(31, 3.5, summary_text, fontsize=9,
           bbox=dict(boxstyle='round', facecolor='white',
                    edgecolor=COLORS['primary'], linewidth=2))
    
    ax.grid(True, alpha=0.2, axis='x')
    plt.tight_layout()
    plt.savefig('roadmap_gantt.pdf', dpi=300, bbox_inches='tight')
    plt.savefig('roadmap_gantt.png', dpi=300, bbox_inches='tight')
    print("✓ Generato: roadmap_gantt.pdf/png")
    plt.show()

def generate_all_figures():
    """
    Genera tutte le figure del Capitolo 5
    """
    print("=" * 60)
    print("GENERAZIONE FIGURE CAPITOLO 5 - FRAMEWORK GIST")
    print("=" * 60)
    
    print("\n1. Generazione Diagramma Effetti Sinergici...")
    create_synergy_effects_diagram()
    
    print("\n2. Generazione Dashboard Validazione Ipotesi...")
    create_validation_dashboard()
    
    print("\n3. Generazione Timeline Evoluzione GIST Score...")
    create_gist_evolution_timeline()
    
    print("\n4. Generazione Gantt Roadmap Implementativa...")
    create_roadmap_gantt()
    
    print("\n" + "=" * 60)
    print("✅ TUTTE LE FIGURE GENERATE CON SUCCESSO!")
    print("=" * 60)
    
    print("\nFile generati:")
    print("  📊 synergy_effects.pdf/png - Figura 5.1")
    print("  📊 validation_dashboard.pdf/png - Figura 5.2")
    print("  📊 gist_evolution_timeline.pdf/png - Figura 5.3")
    print("  📊 roadmap_gantt.pdf/png - Figura 5.4")
    
    print("\nDimensioni consigliate per inclusione in LaTeX:")
    print("  - Figure principali: width=\\textwidth")
    print("  - Dashboard: width=1.1\\textwidth")

if __name__ == "__main__":
    # Imposta stile Seaborn per grafici professionali
    sns.set_style("whitegrid")
    sns.set_context("paper")
    
    # Genera tutte le figure
    generate_all_figures()
