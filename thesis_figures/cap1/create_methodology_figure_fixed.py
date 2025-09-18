#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Figura 1.3 - Schema Metodologico della Ricerca
Versione CORRETTA senza emoji per compatibilità Windows/Times New Roman
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import matplotlib.lines as mlines
import numpy as np

# Configurazione stile accademico
plt.style.use('seaborn-v0_8-paper')

# Colori professionali
COLORS = {
    'primary': '#2E4057',      # Blu scuro professionale
    'secondary': '#048A81',    # Verde acqua
    'accent': '#F18F01',       # Arancione accento
    'danger': '#C73E1D',       # Rosso per minacce
    'success': '#6A994E',      # Verde successo
    'info': '#277DA1',         # Blu informativo
    'light': '#F7F7F7',        # Grigio chiaro
    'dark': '#212529'          # Grigio scuro
}

# Font settings
FONT_SETTINGS = {
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif'],
    'font.size': 10,
    'axes.titlesize': 12,
    'axes.labelsize': 10
}
plt.rcParams.update(FONT_SETTINGS)

def create_methodology_figure():
    """
    Crea la Figura 1.3: Schema metodologico della ricerca (senza emoji)
    """
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # FASE 1: ANALISI E RACCOLTA DATI
    phase1_x, phase1_y = 2.5, 7
    phase1_box = FancyBboxPatch((phase1_x-2, phase1_y-1.5), 4, 3,
                                boxstyle="round,pad=0.1",
                                facecolor=COLORS['info'],
                                edgecolor=COLORS['dark'],
                                linewidth=2, alpha=0.9)
    ax.add_patch(phase1_box)
    
    ax.text(phase1_x, phase1_y+1, 'FASE 1', ha='center', va='center',
            fontweight='bold', fontsize=12, color='white')
    ax.text(phase1_x, phase1_y+0.5, 'ANALISI E RACCOLTA DATI', 
            ha='center', va='center', fontweight='bold', fontsize=10, color='white')
    
    # Componenti Fase 1
    fase1_items = [
        '• Revisione sistematica\n  487 pubblicazioni (2019-2024)',
        '• Dataset pubblici GDO\n  ISTAT, Federdistribuzione',
        '• Report di settore\n  Gartner, ENISA, Osservatorio'
    ]
    for i, item in enumerate(fase1_items):
        ax.text(phase1_x, phase1_y-0.3-i*0.4, item, ha='center', va='center',
                fontsize=8, color='white')
    
    # FASE 2: RICERCA SUL CAMPO
    phase2_x, phase2_y = 7, 7
    phase2_box = FancyBboxPatch((phase2_x-2, phase2_y-1.5), 4, 3,
                                boxstyle="round,pad=0.1",
                                facecolor=COLORS['secondary'],
                                edgecolor=COLORS['dark'],
                                linewidth=2, alpha=0.9)
    ax.add_patch(phase2_box)
    
    ax.text(phase2_x, phase2_y+1, 'FASE 2', ha='center', va='center',
            fontweight='bold', fontsize=12, color='white')
    ax.text(phase2_x, phase2_y+0.5, 'RICERCA SUL CAMPO', 
            ha='center', va='center', fontweight='bold', fontsize=10, color='white')
    
    # Componenti Fase 2
    fase2_items = [
        '• Interviste semi-strutturate\n  23 dirigenti IT',
        '• Casi studio internazionali\n  5 aziende leader',
        '• Osservazione partecipante\n  3 implementazioni pilota'
    ]
    for i, item in enumerate(fase2_items):
        ax.text(phase2_x, phase2_y-0.3-i*0.4, item, ha='center', va='center',
                fontsize=8, color='white')
    
    # FASE 3: MODELLAZIONE E VALIDAZIONE
    phase3_x, phase3_y = 11.5, 7
    phase3_box = FancyBboxPatch((phase3_x-2, phase3_y-1.5), 4, 3,
                                boxstyle="round,pad=0.1",
                                facecolor=COLORS['accent'],
                                edgecolor=COLORS['dark'],
                                linewidth=2, alpha=0.9)
    ax.add_patch(phase3_box)
    
    ax.text(phase3_x, phase3_y+1, 'FASE 3', ha='center', va='center',
            fontweight='bold', fontsize=12, color='white')
    ax.text(phase3_x, phase3_y+0.5, 'MODELLAZIONE E VALIDAZIONE', 
            ha='center', va='center', fontweight='bold', fontsize=10, color='white')
    
    # Componenti Fase 3
    fase3_items = [
        '• Simulazione Monte Carlo\n  10.000 iterazioni/scenario',
        '• Machine Learning XGBoost\n  50.000 esempi training',
        '• Digital Twin validation\n  24 mesi dati sintetici'
    ]
    for i, item in enumerate(fase3_items):
        ax.text(phase3_x, phase3_y-0.3-i*0.4, item, ha='center', va='center',
                fontsize=8, color='white')
    
    # Frecce di connessione tra fasi
    arrow1 = FancyArrowPatch((phase1_x+2, phase1_y), (phase2_x-2, phase2_y),
                            connectionstyle="arc3,rad=0",
                            arrowstyle='->', mutation_scale=25,
                            linewidth=2.5, color=COLORS['dark'], alpha=0.7)
    ax.add_patch(arrow1)
    
    arrow2 = FancyArrowPatch((phase2_x+2, phase2_y), (phase3_x-2, phase3_y),
                            connectionstyle="arc3,rad=0",
                            arrowstyle='->', mutation_scale=25,
                            linewidth=2.5, color=COLORS['dark'], alpha=0.7)
    ax.add_patch(arrow2)
    
    # APPROCCIO METODOLOGICO (sopra)
    approach_box = FancyBboxPatch((1, 9.2), 12, 0.6,
                                  boxstyle="round,pad=0.05",
                                  facecolor=COLORS['primary'],
                                  edgecolor=COLORS['dark'],
                                  linewidth=1.5)
    ax.add_patch(approach_box)
    ax.text(7, 9.5, 'APPROCCIO MIXED-METHODS: CONVERGENT PARALLEL DESIGN',
            ha='center', va='center', fontweight='bold', fontsize=11, color='white')
    
    # Sotto-approcci
    # Quantitativo
    quant_box = FancyBboxPatch((1.5, 4.5), 5, 0.8,
                               boxstyle="round,pad=0.05",
                               facecolor=COLORS['light'],
                               edgecolor=COLORS['info'],
                               linewidth=1.5)
    ax.add_patch(quant_box)
    ax.text(4, 4.9, 'APPROCCIO QUANTITATIVO', ha='center', va='center',
            fontweight='bold', fontsize=9, color=COLORS['info'])
    
    quant_methods = ['Analisi statistica', 'Simulazione', 'Machine Learning', 'Serie temporali']
    for i, method in enumerate(quant_methods):
        ax.text(1.8 + i*1.2, 4.6, method, ha='center', va='center',
                fontsize=7, color=COLORS['dark'])
    
    # Qualitativo
    qual_box = FancyBboxPatch((7.5, 4.5), 5, 0.8,
                              boxstyle="round,pad=0.05",
                              facecolor=COLORS['light'],
                              edgecolor=COLORS['secondary'],
                              linewidth=1.5)
    ax.add_patch(qual_box)
    ax.text(10, 4.9, 'APPROCCIO QUALITATIVO', ha='center', va='center',
            fontweight='bold', fontsize=9, color=COLORS['secondary'])
    
    qual_methods = ['Interviste', 'Casi studio', 'Osservazione', 'Analisi tematica']
    for i, method in enumerate(qual_methods):
        ax.text(8 + i*1.2, 4.6, method, ha='center', va='center',
                fontsize=7, color=COLORS['dark'])
    
    # OUTPUT PRINCIPALI (in basso)
    output_box = FancyBboxPatch((1, 0.5), 12, 2.5,
                               boxstyle="round,pad=0.1",
                               facecolor='#FFE66D',  # Giallo chiaro
                               edgecolor=COLORS['dark'],
                               linewidth=2)
    ax.add_patch(output_box)
    
    ax.text(7, 2.7, 'OUTPUT DELLA RICERCA', ha='center', va='center',
            fontweight='bold', fontsize=11, color=COLORS['dark'])
    
    # 5 Output principali - uso numeri semplici per massima compatibilità
    outputs = [
        {'x': 2.5, 'num': '1', 'title': 'Framework GIST', 
         'desc': 'Modello integrato\n4 dimensioni'},
        {'x': 4.5, 'num': '2', 'title': 'ASSA-GDO', 
         'desc': 'Algoritmo scoring\nr=0.82'},
        {'x': 6.5, 'num': '3', 'title': 'Digital Twin', 
         'desc': 'Simulatore\nvalidato'},
        {'x': 8.5, 'num': '4', 'title': 'ML Predictor', 
         'desc': 'Sistema predittivo\nAUC=0.89'},
        {'x': 10.5, 'num': '5', 'title': 'GDO-Bench', 
         'desc': 'Dataset riferimento\n2 anni dati'}
    ]
    
    for output in outputs:
        # Cerchio per l'output
        circle = Circle((output['x'], 1.7), 0.35, 
                       facecolor='white', edgecolor=COLORS['primary'], linewidth=2)
        ax.add_patch(circle)
        # Numero semplice invece di simboli speciali
        ax.text(output['x'], 1.7, output['num'], ha='center', va='center',
                fontsize=20, fontweight='bold', color=COLORS['primary'])
        # Titolo
        ax.text(output['x'], 2.2, output['title'], ha='center', va='center',
                fontweight='bold', fontsize=8, color=COLORS['dark'])
        # Descrizione
        ax.text(output['x'], 1.2, output['desc'], ha='center', va='center',
                fontsize=7, color=COLORS['dark'])
    
    # Frecce da fasi a output
    for phase_x in [phase1_x, phase2_x, phase3_x]:
        arrow_to_output = FancyArrowPatch((phase_x, phase1_y-1.5), 
                                         (phase_x, 3),
                                         connectionstyle="arc3,rad=0",
                                         arrowstyle='->', mutation_scale=15,
                                         linewidth=1.5, color=COLORS['dark'], 
                                         alpha=0.3, linestyle='dashed')
        ax.add_patch(arrow_to_output)
    
    # Timeline laterale
    timeline_x = 0.3
    ax.plot([timeline_x, timeline_x], [9, 1], 'k-', linewidth=2, alpha=0.5)
    
    timeline_points = [
        {'y': 8.5, 'label': 'Mesi 1-3', 'desc': 'Raccolta dati'},
        {'y': 7, 'label': 'Mesi 4-9', 'desc': 'Analisi campo'},
        {'y': 5.5, 'label': 'Mesi 10-15', 'desc': 'Modellazione'},
        {'y': 4, 'label': 'Mesi 16-18', 'desc': 'Validazione'},
        {'y': 2.5, 'label': 'Mesi 19-24', 'desc': 'Scrittura'}
    ]
    
    for point in timeline_points:
        ax.plot(timeline_x, point['y'], 'ko', markersize=8)
        ax.text(timeline_x-0.15, point['y'], point['label'], 
                ha='right', va='center', fontsize=7, fontweight='bold')
        ax.text(timeline_x+0.15, point['y'], point['desc'], 
                ha='left', va='center', fontsize=7, style='italic')
    
    # Legenda metodologica
    legend_elements = [
        mlines.Line2D([], [], color=COLORS['info'], marker='s', linestyle='None',
                     markersize=10, label='Analisi quantitativa'),
        mlines.Line2D([], [], color=COLORS['secondary'], marker='s', linestyle='None',
                     markersize=10, label='Analisi qualitativa'),
        mlines.Line2D([], [], color=COLORS['accent'], marker='s', linestyle='None',
                     markersize=10, label='Sintesi e validazione')
    ]
    ax.legend(handles=legend_elements, loc='upper right', 
             bbox_to_anchor=(0.98, 0.15), fontsize=8)
    
    # Validazione statistica (box informativo)
    val_box = FancyBboxPatch((10.5, 0.8), 2.5, 0.6,
                             boxstyle="round,pad=0.05",
                             facecolor='white',
                             edgecolor=COLORS['success'],
                             linewidth=1.5)
    ax.add_patch(val_box)
    ax.text(11.75, 1.1, 'Validazione: p<0.001\nConfidenza: 95%\nPotenza: 0.80',
            ha='center', va='center', fontsize=7, color=COLORS['success'])
    
    plt.title('Schema metodologico della ricerca con le tre fasi principali e relativi output',
              fontsize=12, fontweight='bold', pad=20)
    plt.tight_layout()
    return fig

def create_simple_methodology():
    """
    Versione alternativa più semplice e lineare (senza emoji)
    """
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis('off')
    
    # Titolo
    ax.text(6, 7.5, 'METODOLOGIA DELLA RICERCA', ha='center', va='center',
            fontsize=14, fontweight='bold', color=COLORS['primary'])
    
    # Fasi principali come flowchart
    phases = [
        {'x': 2, 'y': 5.5, 'title': 'FASE 1\nFondamenti', 
         'color': COLORS['info'], 'width': 2.5, 'height': 1.2},
        {'x': 6, 'y': 5.5, 'title': 'FASE 2\nSviluppo', 
         'color': COLORS['secondary'], 'width': 2.5, 'height': 1.2},
        {'x': 10, 'y': 5.5, 'title': 'FASE 3\nValidazione', 
         'color': COLORS['accent'], 'width': 2.5, 'height': 1.2}
    ]
    
    # Disegna le fasi
    for i, phase in enumerate(phases):
        # Box principale
        rect = FancyBboxPatch((phase['x']-phase['width']/2, phase['y']-phase['height']/2),
                              phase['width'], phase['height'],
                              boxstyle="round,pad=0.05",
                              facecolor=phase['color'],
                              edgecolor=COLORS['dark'],
                              linewidth=2, alpha=0.9)
        ax.add_patch(rect)
        
        # Titolo fase
        ax.text(phase['x'], phase['y'], phase['title'],
                ha='center', va='center', fontweight='bold',
                fontsize=11, color='white')
        
        # Freccia alla fase successiva
        if i < len(phases) - 1:
            arrow = FancyArrowPatch((phase['x']+phase['width']/2, phase['y']),
                                  (phases[i+1]['x']-phases[i+1]['width']/2, phases[i+1]['y']),
                                  arrowstyle='->', mutation_scale=20,
                                  linewidth=2, color=COLORS['dark'])
            ax.add_patch(arrow)
    
    # Dettagli per ogni fase
    details = [
        # Fase 1
        {'x': 2, 'y': 3.8, 'items': [
            '• Revisione letteratura (487 paper)',
            '• Analisi documenti settore',
            '• Definizione framework teorico'
        ]},
        # Fase 2
        {'x': 6, 'y': 3.8, 'items': [
            '• 23 interviste dirigenti IT',
            '• 5 casi studio internazionali',
            '• Sviluppo algoritmi (ASSA-GDO)'
        ]},
        # Fase 3
        {'x': 10, 'y': 3.8, 'items': [
            '• Simulazione Monte Carlo (10k iter)',
            '• Machine Learning (XGBoost)',
            '• Digital Twin (24 mesi dati)'
        ]}
    ]
    
    for detail in details:
        for i, item in enumerate(detail['items']):
            ax.text(detail['x'], detail['y']-i*0.25, item,
                    ha='center', va='top', fontsize=8)
    
    # Metodi utilizzati (in basso)
    methods_box = FancyBboxPatch((0.5, 1.5), 11, 1.5,
                                boxstyle="round,pad=0.05",
                                facecolor=COLORS['light'],
                                edgecolor=COLORS['dark'],
                                linewidth=1)
    ax.add_patch(methods_box)
    
    ax.text(6, 2.6, 'METODI E STRUMENTI', ha='center', va='center',
            fontweight='bold', fontsize=10)
    
    # Colonne di metodi
    methods_cols = [
        {'x': 2, 'title': 'Quantitativi', 
         'items': ['Statistica descrittiva', 'Analisi correlazione', 'Test ipotesi']},
        {'x': 6, 'title': 'Qualitativi',
         'items': ['Codifica tematica', 'Analisi contenuto', 'Triangolazione']},
        {'x': 10, 'title': 'Computazionali',
         'items': ['Python/R', 'Simulazione', 'Machine Learning']}
    ]
    
    for col in methods_cols:
        ax.text(col['x'], 2.2, col['title'], ha='center', va='center',
                fontweight='bold', fontsize=9)
        for i, item in enumerate(col['items']):
            ax.text(col['x'], 1.9-i*0.2, f'• {item}', ha='center', va='center',
                    fontsize=7)
    
    # Output finale
    output_box = FancyBboxPatch((3.5, 0.2), 5, 0.6,
                               boxstyle="round,pad=0.05",
                               facecolor=COLORS['success'],
                               edgecolor=COLORS['dark'],
                               linewidth=2, alpha=0.9)
    ax.add_patch(output_box)
    ax.text(6, 0.5, 'OUTPUT: Framework GIST + 5 Strumenti Computazionali',
            ha='center', va='center', fontweight='bold',
            fontsize=9, color='white')
    
    plt.tight_layout()
    return fig

# Genera entrambe le versioni
if __name__ == "__main__":
    import os
    
    # Adatta il percorso per Windows se necessario
    output_dir = './thesis_figures/cap1/'
    if not os.path.exists(output_dir):
        output_dir = './'
    
    # Versione dettagliata
    fig1 = create_methodology_figure()
    fig1.savefig(os.path.join(output_dir, 'fig_1_3_methodology.pdf'),
                dpi=300, bbox_inches='tight', format='pdf')
    fig1.savefig(os.path.join(output_dir, 'fig_1_3_methodology.png'),
                dpi=150, bbox_inches='tight', format='png')
    print("✓ Salvato: fig_1_3_methodology.pdf e .png")
    plt.close(fig1)
    
    # Versione semplice alternativa
    fig2 = create_simple_methodology()
    fig2.savefig(os.path.join(output_dir, 'fig_1_3_methodology_simple.pdf'),
                dpi=300, bbox_inches='tight', format='pdf')
    fig2.savefig(os.path.join(output_dir, 'fig_1_3_methodology_simple.png'),
                dpi=150, bbox_inches='tight', format='png')
    print("✓ Salvato: fig_1_3_methodology_simple.pdf e .png (versione alternativa)")
    plt.close(fig2)
    
    print("✓ Figure della metodologia generate con successo!")
    print(f"✓ Salvate in: {os.path.abspath(output_dir)}")
