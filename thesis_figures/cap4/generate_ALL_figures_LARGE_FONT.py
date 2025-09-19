#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TUTTE LE FIGURE CAPITOLO 4 - VERSIONE ALTA LEGGIBILITÀ
Font grandi, design pulito, massima visibilità
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Circle, FancyBboxPatch, Polygon, Rectangle, FancyArrowPatch, Wedge
import matplotlib.patheffects as path_effects
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# =============================================================================
# CONFIGURAZIONE GLOBALE - FONT GRANDI
# =============================================================================

# Impostazioni per massima leggibilità
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'Helvetica', 'DejaVu Sans'],
    'font.size': 16,  # Font base molto più grande
    'axes.labelsize': 18,
    'axes.titlesize': 22,
    'xtick.labelsize': 16,
    'ytick.labelsize': 16,
    'legend.fontsize': 16,
    'figure.titlesize': 24,
    'axes.linewidth': 2.5,
    'lines.linewidth': 3,
    'patch.linewidth': 2,
    'figure.facecolor': 'white',
    'axes.facecolor': 'white',
})

# Palette colori ad alto contrasto
COLORS = {
    'primary': '#1E3A5F',      # Blu scuro (alta leggibilità)
    'secondary': '#D32F2F',     # Rosso forte
    'success': '#2E7D32',       # Verde scuro
    'warning': '#F57C00',       # Arancione
    'info': '#0288D1',          # Blu medio
    'accent': '#7B1FA2',        # Viola
    'light': '#F5F5F5',         # Grigio chiaro
    'dark': '#212121',          # Nero quasi puro
    'white': '#FFFFFF',
}

# =============================================================================
# FIGURA 1: DIAGRAMMA DI VENN - FONT GRANDI
# =============================================================================

def create_figure_1_venn_large():
    """
    Diagramma di Venn con font molto grandi
    """
    fig = plt.figure(figsize=(18, 14), facecolor='white')
    ax = fig.add_subplot(111)
    ax.set_xlim(-5, 8)
    ax.set_ylim(-6, 5)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Cerchi principali
    circles_data = [
        (0, 0, 2.8, COLORS['primary'], 'PCI-DSS 4.0', '264 controlli'),
        (2.4, 0, 2.8, COLORS['secondary'], 'GDPR', '99 articoli'),
        (1.2, -2.1, 2.8, COLORS['success'], 'NIS2', '31 misure')
    ]
    
    for x, y, r, color, title, subtitle in circles_data:
        circle = Circle((x, y), r, color=color, alpha=0.3, 
                       edgecolor=color, linewidth=4)
        ax.add_patch(circle)
    
    # ETICHETTE PRINCIPALI - FONT MOLTO GRANDI
    labels_main = [
        (-1.5, 2.5, 'PCI-DSS 4.0', COLORS['primary'], 28, 'bold'),
        (-1.5, 1.8, '264 controlli', COLORS['dark'], 20, 'normal'),
        (3.9, 2.5, 'GDPR', COLORS['secondary'], 28, 'bold'),
        (3.9, 1.8, '99 articoli', COLORS['dark'], 20, 'normal'),
        (1.2, -5.0, 'NIS2', COLORS['success'], 28, 'bold'),
        (1.2, -5.7, '31 misure', COLORS['dark'], 20, 'normal')
    ]
    
    for x, y, text, color, size, weight in labels_main:
        ax.text(x, y, text, fontsize=size, fontweight=weight,
               color=color, ha='center', va='center')
    
    # NUMERI INTERSEZIONI - FONT EXTRA LARGE
    intersections = [
        (1.2, 0, '47', 32),
        (-0.3, -0.9, '23', 26),
        (2.7, -0.9, '31', 26),
        (1.2, -0.8, '55', 36)
    ]
    
    for x, y, value, size in intersections:
        # Cerchio di sfondo
        bg = Circle((x, y), 0.5, color='white', 
                   edgecolor=COLORS['info'], linewidth=3)
        ax.add_patch(bg)
        # Numero
        ax.text(x, y, value, fontsize=size, fontweight='bold',
               color=COLORS['info'], ha='center', va='center')
    
    # BOX INFORMATIVO - FONT GRANDE
    info_box = FancyBboxPatch((4.8, -3), 3, 2.5,
                              boxstyle="round,pad=0.15",
                              facecolor='white',
                              edgecolor=COLORS['primary'],
                              linewidth=3)
    ax.add_patch(info_box)
    
    ax.text(6.3, -1.5, 'CONTROLLI COMUNI', fontsize=20, fontweight='bold',
           ha='center', va='center', color=COLORS['primary'])
    ax.text(6.3, -2.2, '156 totali (39.6%)', fontsize=18,
           ha='center', va='center', color=COLORS['dark'])
    ax.text(6.3, -2.8, '55 core - 101 parziali', fontsize=16,
           ha='center', va='center', color=COLORS['dark'])
    
    # TITOLO PRINCIPALE
    ax.text(1.5, 4.2, 'Sovrapposizioni Standard Normativi', 
           fontsize=28, fontweight='bold',
           color=COLORS['dark'], ha='center')
    
    plt.tight_layout()
    return fig

# =============================================================================
# FIGURA 2: ARCHITETTURA A TRE LIVELLI - FONT GRANDI
# =============================================================================

def create_figure_2_architecture_large():
    """
    Architettura del sistema con font molto grandi
    """
    fig = plt.figure(figsize=(20, 14), facecolor='white')
    ax = fig.add_subplot(111)
    ax.set_xlim(-3, 18)
    ax.set_ylim(-2, 10)
    ax.axis('off')
    
    # Dimensioni box aumentate per font grandi
    box_width = 4.5
    box_height = 1.5
    
    # LIVELLO 3 - PRESENTAZIONE
    level3_y = 7
    boxes_l3 = [
        (2, 'Dashboard\nEsecutiva'),
        (7, 'Console\nOperativa'),
        (12, 'Sistema\nReporting')
    ]
    
    for x, text in boxes_l3:
        box = FancyBboxPatch((x-box_width/2, level3_y-box_height/2), 
                             box_width, box_height,
                             boxstyle="round,pad=0.1",
                             facecolor=COLORS['warning'],
                             edgecolor=COLORS['dark'],
                             linewidth=3, alpha=0.9)
        ax.add_patch(box)
        ax.text(x, level3_y, text, fontsize=18, fontweight='bold',
               ha='center', va='center', color='white')
    
    # LIVELLO 2 - ELABORAZIONE
    level2_y = 4
    boxes_l2 = [
        (3.5, 'Motore\nCorrelazione'),
        (7, 'Analisi\nRischio'),
        (10.5, 'Valutazione\nConformità')
    ]
    
    for x, text in boxes_l2:
        box = FancyBboxPatch((x-box_width/2, level2_y-box_height/2), 
                             box_width, box_height,
                             boxstyle="round,pad=0.1",
                             facecolor=COLORS['info'],
                             edgecolor=COLORS['dark'],
                             linewidth=3, alpha=0.9)
        ax.add_patch(box)
        ax.text(x, level2_y, text, fontsize=18, fontweight='bold',
               ha='center', va='center', color='white')
    
    # LIVELLO 1 - RACCOLTA DATI
    level1_y = 1
    boxes_l1 = [
        (1, 'Config\nMgmt'),
        (4.5, 'SIEM\nLogs'),
        (8, 'Metriche\nKPI'),
        (11.5, 'Threat\nIntel'),
        (15, 'Audit\nTrail')
    ]
    
    for x, text in boxes_l1:
        box = FancyBboxPatch((x-box_width/2+0.3, level1_y-box_height/2), 
                             box_width-0.6, box_height,
                             boxstyle="round,pad=0.1",
                             facecolor=COLORS['success'],
                             edgecolor=COLORS['dark'],
                             linewidth=3, alpha=0.9)
        ax.add_patch(box)
        ax.text(x, level1_y, text, fontsize=16, fontweight='bold',
               ha='center', va='center', color='white')
    
    # ETICHETTE LIVELLI - EXTRA LARGE
    ax.text(-2, level3_y, 'LIVELLO 3:\nPRESENTAZIONE', fontsize=18, 
           fontweight='bold', ha='center', va='center', color=COLORS['warning'])
    ax.text(-2, level2_y, 'LIVELLO 2:\nELABORAZIONE', fontsize=18,
           fontweight='bold', ha='center', va='center', color=COLORS['info'])
    ax.text(-2, level1_y, 'LIVELLO 1:\nRACCOLTA', fontsize=18,
           fontweight='bold', ha='center', va='center', color=COLORS['success'])
    
    # Frecce di connessione più spesse
    arrow_style = dict(arrowstyle='->', lw=3, color=COLORS['dark'], alpha=0.6)
    
    # Connessioni tra livelli
    connections = [
        (3.5, 1.8, 3.5, 3.2),
        (7, 1.8, 7, 3.2),
        (10.5, 1.8, 10.5, 3.2),
        (3.5, 4.8, 2, 6.2),
        (7, 4.8, 7, 6.2),
        (10.5, 4.8, 12, 6.2)
    ]
    
    for x1, y1, x2, y2 in connections:
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1), arrowprops=arrow_style)
    
    # TITOLO
    ax.text(7, 9, 'Architettura del Sistema di Conformità', 
           fontsize=28, fontweight='bold',
           color=COLORS['dark'], ha='center')
    
    plt.tight_layout()
    return fig

# =============================================================================
# FIGURA 3: PROCESSO GDPR - FONT GRANDI
# =============================================================================

def create_figure_3_gdpr_large():
    """
    Flowchart processo GDPR con font molto grandi
    """
    fig = plt.figure(figsize=(20, 12), facecolor='white')
    ax = fig.add_subplot(111)
    ax.set_xlim(-2, 18)
    ax.set_ylim(-2, 6)
    ax.axis('off')
    
    # Nodi del processo - dimensioni aumentate
    node_size = 1.8
    nodes = [
        (2, 3, 'process', '1. RICEZIONE\nRICHIESTA', COLORS['info']),
        (5, 3, 'decision', 'VERIFICA\nIDENTITÀ', COLORS['warning']),
        (8, 3, 'process', '3. IDENTIFICA\nDATI', COLORS['info']),
        (11, 3, 'process', '4. ESECUZIONE', COLORS['success']),
        (14, 3, 'process', '5. NOTIFICA', COLORS['primary']),
        (5, 5, 'process', 'RESPINTA', COLORS['secondary']),
        (14, 1, 'data', 'AUDIT TRAIL', COLORS['accent'])
    ]
    
    for x, y, node_type, text, color in nodes:
        if node_type == 'process':
            box = FancyBboxPatch((x-node_size/2, y-0.6), node_size, 1.2,
                                 boxstyle="round,pad=0.05",
                                 facecolor=color, edgecolor=COLORS['dark'],
                                 linewidth=3, alpha=0.9)
            ax.add_patch(box)
        elif node_type == 'decision':
            diamond = Polygon([(x, y-0.8), (x+1, y), (x, y+0.8), (x-1, y)],
                            facecolor=color, edgecolor=COLORS['dark'],
                            linewidth=3, alpha=0.9)
            ax.add_patch(diamond)
        elif node_type == 'data':
            trap = Polygon([(x-1, y-0.5), (x+1, y-0.5), 
                          (x+1.2, y+0.5), (x-1.2, y+0.5)],
                         facecolor=color, edgecolor=COLORS['dark'],
                         linewidth=3, alpha=0.9)
            ax.add_patch(trap)
        
        # Testo del nodo - FONT GRANDE
        ax.text(x, y, text, fontsize=16, fontweight='bold',
               ha='center', va='center', color='white')
    
    # Frecce di flusso più spesse
    arrows = [
        (3, 3, 4, 3, ''),
        (6, 3, 7, 3, 'SÌ'),
        (5, 3.8, 5, 4.2, 'NO'),
        (9, 3, 10, 3, ''),
        (12, 3, 13, 3, ''),
        (14, 2.4, 14, 1.6, '')
    ]
    
    for x1, y1, x2, y2, label in arrows:
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                   arrowprops=dict(arrowstyle='->', lw=3, color=COLORS['dark']))
        if label:
            mid_x, mid_y = (x1+x2)/2, (y1+y2)/2
            ax.text(mid_x, mid_y+0.3, label, fontsize=18, fontweight='bold',
                   ha='center', color=COLORS['dark'])
    
    # Timer zones - FONT GRANDI
    timer_box1 = Rectangle((1, 2.2), 7, 1.6, fill=False,
                          edgecolor=COLORS['warning'], linewidth=3, 
                          linestyle='--', alpha=0.7)
    ax.add_patch(timer_box1)
    ax.text(4.5, 2, 'MAX 72 ORE', fontsize=20, fontweight='bold',
           color=COLORS['warning'], ha='center')
    
    timer_box2 = Rectangle((7.5, 2.2), 7, 1.6, fill=False,
                          edgecolor=COLORS['info'], linewidth=3,
                          linestyle='--', alpha=0.7)
    ax.add_patch(timer_box2)
    ax.text(11, 2, 'MAX 30 GIORNI', fontsize=20, fontweight='bold',
           color=COLORS['info'], ha='center')
    
    # TITOLO
    ax.text(8, 5.5, 'Processo Automatizzato Diritti GDPR', 
           fontsize=28, fontweight='bold',
           color=COLORS['dark'], ha='center')
    
    # Legenda diritti - FONT GRANDE
    legend_box = FancyBboxPatch((15.5, 2.5), 2.5, 2,
                               boxstyle="round,pad=0.1",
                               facecolor='white',
                               edgecolor=COLORS['primary'],
                               linewidth=3)
    ax.add_patch(legend_box)
    
    ax.text(16.75, 4.2, 'DIRITTI GDPR', fontsize=18, fontweight='bold',
           ha='center', color=COLORS['primary'])
    rights = ['Art. 15 - Accesso', 'Art. 16 - Rettifica', 
              'Art. 17 - Cancella', 'Art. 20 - Portabilità']
    for i, right in enumerate(rights):
        ax.text(16.75, 3.7-i*0.3, right, fontsize=14,
               ha='center', color=COLORS['dark'])
    
    plt.tight_layout()
    return fig

# =============================================================================
# FIGURA 4: STRUTTURA ORGANIZZATIVA - FONT GRANDI
# =============================================================================

def create_figure_4_org_structure_large():
    """
    Organigramma con font molto grandi
    """
    fig = plt.figure(figsize=(20, 16), facecolor='white')
    ax = fig.add_subplot(111)
    ax.set_xlim(-10, 10)
    ax.set_ylim(-3, 12)
    ax.axis('off')
    
    # Dimensioni box aumentate
    box_width = 5
    box_height = 1.8
    
    # LIVELLO STRATEGICO
    # Consiglio di Amministrazione
    cda_box = FancyBboxPatch((-box_width/2, 10), box_width, box_height,
                            boxstyle="round,pad=0.1",
                            facecolor=COLORS['primary'],
                            edgecolor=COLORS['dark'], linewidth=4)
    ax.add_patch(cda_box)
    ax.text(0, 10.9, 'CONSIGLIO DI', fontsize=20, fontweight='bold',
           color='white', ha='center', va='center')
    ax.text(0, 10.3, 'AMMINISTRAZIONE', fontsize=20, fontweight='bold',
           color='white', ha='center', va='center')
    
    # Comitato Governance
    com_box = FancyBboxPatch((-box_width/2, 7), box_width, box_height,
                            boxstyle="round,pad=0.1",
                            facecolor=COLORS['primary'],
                            edgecolor=COLORS['dark'], linewidth=4, alpha=0.9)
    ax.add_patch(com_box)
    ax.text(0, 7.9, 'COMITATO', fontsize=20, fontweight='bold',
           color='white', ha='center', va='center')
    ax.text(0, 7.3, 'GOVERNANCE', fontsize=20, fontweight='bold',
           color='white', ha='center', va='center')
    
    # LIVELLO TATTICO
    # Centro Eccellenza
    cec_box = FancyBboxPatch((-6, 4), box_width-0.5, box_height-0.2,
                            boxstyle="round,pad=0.1",
                            facecolor=COLORS['info'],
                            edgecolor=COLORS['dark'], linewidth=3)
    ax.add_patch(cec_box)
    ax.text(-3.5, 4.9, 'CENTRO ECCELLENZA', fontsize=18, fontweight='bold',
           color='white', ha='center', va='center')
    ax.text(-3.5, 4.3, 'CONFORMITÀ', fontsize=18, fontweight='bold',
           color='white', ha='center', va='center')
    
    # Risk Management
    risk_box = FancyBboxPatch((1.5, 4), box_width-0.5, box_height-0.2,
                             boxstyle="round,pad=0.1",
                             facecolor=COLORS['info'],
                             edgecolor=COLORS['dark'], linewidth=3)
    ax.add_patch(risk_box)
    ax.text(4, 4.9, 'RISK', fontsize=18, fontweight='bold',
           color='white', ha='center', va='center')
    ax.text(4, 4.3, 'MANAGEMENT', fontsize=18, fontweight='bold',
           color='white', ha='center', va='center')
    
    # LIVELLO OPERATIVO
    ops_boxes = [
        (-7.5, 1, 'SOC'),
        (-4.5, 1, 'IT OPS'),
        (-1.5, 1, 'BUSINESS\nUNITS'),
        (2, 1, 'INTERNAL\nAUDIT'),
        (5.5, 1, 'LEGAL &\nCOMPLIANCE')
    ]
    
    for x, y, text in ops_boxes:
        color = COLORS['secondary'] if 'AUDIT' in text else COLORS['success']
        box = FancyBboxPatch((x-1.3, y-0.6), 2.6, 1.4,
                            boxstyle="round,pad=0.05",
                            facecolor=color,
                            edgecolor=COLORS['dark'], linewidth=3, alpha=0.9)
        ax.add_patch(box)
        ax.text(x, y, text, fontsize=14, fontweight='bold',
               color='white', ha='center', va='center')
    
    # Connessioni - linee più spesse
    connections = [
        (0, 10, 0, 8.8),  # CdA -> Comitato
        (0, 7, -3.5, 5.8),  # Comitato -> CEC
        (0, 7, 4, 5.8),  # Comitato -> Risk
        (-3.5, 4, -7.5, 2.4),  # CEC -> SOC
        (-3.5, 4, -4.5, 2.4),  # CEC -> IT
        (-3.5, 4, -1.5, 2.4),  # CEC -> BU
        (4, 4, 2, 2.4),  # Risk -> Audit
        (4, 4, 5.5, 2.4)  # Risk -> Legal
    ]
    
    for x1, y1, x2, y2 in connections:
        ax.plot([x1, x2], [y1, y2], color=COLORS['dark'], 
               linewidth=3, alpha=0.7)
    
    # ETICHETTE LIVELLI - EXTRA LARGE
    ax.text(-8.5, 8.5, 'LIVELLO\nSTRATEGICO', fontsize=20, fontweight='bold',
           color=COLORS['primary'], ha='center', va='center', rotation=90)
    ax.text(-8.5, 4.5, 'LIVELLO\nTATTICO', fontsize=20, fontweight='bold',
           color=COLORS['info'], ha='center', va='center', rotation=90)
    ax.text(-8.5, 1, 'LIVELLO\nOPERATIVO', fontsize=20, fontweight='bold',
           color=COLORS['success'], ha='center', va='center', rotation=90)
    
    # Box membri comitato - FONT GRANDE
    members_box = FancyBboxPatch((5.5, 6.5), 4, 3.5,
                                boxstyle="round,pad=0.1",
                                facecolor='white',
                                edgecolor=COLORS['primary'], linewidth=3)
    ax.add_patch(members_box)
    
    ax.text(7.5, 9.5, 'MEMBRI COMITATO', fontsize=18, fontweight='bold',
           ha='center', color=COLORS['primary'])
    
    members = [
        '• Chief Risk Officer (Pres.)',
        '• CISO',
        '• DPO',
        '• CFO',
        '• Head of Compliance'
    ]
    
    for i, member in enumerate(members):
        ax.text(7.5, 8.8-i*0.5, member, fontsize=14,
               ha='center', color=COLORS['dark'])
    
    # TITOLO
    ax.text(0, 11.5, 'Modello Organizzativo Conformità Integrata', 
           fontsize=28, fontweight='bold',
           color=COLORS['dark'], ha='center')
    
    plt.tight_layout()
    return fig

# =============================================================================
# FIGURA 5: CONFRONTO SCENARI - FONT GRANDI
# =============================================================================

def create_figure_5_comparison_large():
    """
    Grafico confronto con font molto grandi
    """
    fig = plt.figure(figsize=(18, 12), facecolor='white')
    ax = fig.add_subplot(111)
    
    # Dati
    categories = ['Detection\n(ore)', 'Sistemi\n(unità)', 
                  'Downtime\n(ore)', 'Impatto\n(k€)']
    real_values = [360, 2847, 120, 8700]
    compliant_values = [6, 12, 4, 300]
    
    x = np.arange(len(categories))
    width = 0.35
    
    # Barre con dimensioni maggiori
    bars1 = ax.bar(x - width/2, real_values, width, 
                   label='Scenario Reale',
                   color=COLORS['secondary'], edgecolor=COLORS['dark'],
                   linewidth=3, alpha=0.9)
    bars2 = ax.bar(x + width/2, compliant_values, width,
                   label='Con Conformità',
                   color=COLORS['success'], edgecolor=COLORS['dark'],
                   linewidth=3, alpha=0.9)
    
    # Valori sopra le barre - FONT MOLTO GRANDI
    for bar in bars1:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height*1.02,
               f'{int(height):,}', ha='center', va='bottom',
               fontsize=18, fontweight='bold', color=COLORS['secondary'])
    
    for bar in bars2:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height*1.02,
               f'{int(height):,}', ha='center', va='bottom',
               fontsize=18, fontweight='bold', color=COLORS['success'])
    
    # Percentuali di miglioramento - FONT GRANDI
    improvements = [98.3, 99.6, 96.7, 96.5]
    for i, imp in enumerate(improvements):
        ax.text(i, max(real_values[i], compliant_values[i])*1.15,
               f'-{imp}%', ha='center', va='bottom',
               fontsize=20, fontweight='bold', color=COLORS['info'],
               bbox=dict(boxstyle="round,pad=0.3", 
                        facecolor='white', edgecolor=COLORS['info'], linewidth=2))
    
    # Configurazione assi - FONT GRANDI
    ax.set_ylabel('Valori (scala log)', fontsize=20, fontweight='bold')
    ax.set_yscale('log')
    ax.set_xticks(x)
    ax.set_xticklabels(categories, fontsize=18, fontweight='bold')
    
    # Legenda - FONT GRANDE
    ax.legend(fontsize=18, loc='upper left', frameon=True, 
             fancybox=True, shadow=True)
    
    # Griglia
    ax.grid(True, which='both', alpha=0.3, linewidth=1)
    ax.set_axisbelow(True)
    
    # Rimuovi spine superiore e destra
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    # TITOLO
    ax.set_title('Analisi Controfattuale: Impatto Conformità', 
                fontsize=26, fontweight='bold', pad=20)
    
    plt.tight_layout()
    return fig

# =============================================================================
# FIGURA 6: TIMELINE IMPLEMENTAZIONE - FONT GRANDI
# =============================================================================

def create_figure_6_timeline_large():
    """
    Timeline Gantt con font molto grandi
    """
    fig = plt.figure(figsize=(20, 10), facecolor='white')
    ax = fig.add_subplot(111)
    
    # Fasi del progetto
    phases = [
        ('Assessment e\nPianificazione', 0, 3, COLORS['info']),
        ('Progettazione e\nArmonizzazione', 3, 6, COLORS['success']),
        ('Implementazione\nPilota', 6, 12, COLORS['warning']),
        ('Rollout e\nOttimizzazione', 12, 24, COLORS['primary'])
    ]
    
    # Disegna le barre Gantt
    for i, (name, start, end, color) in enumerate(phases):
        ax.barh(i, end-start, left=start, height=0.6,
               color=color, edgecolor=COLORS['dark'],
               linewidth=3, alpha=0.9)
        # Testo fase - FONT GRANDE
        ax.text(start + (end-start)/2, i, name, 
               fontsize=16, fontweight='bold',
               ha='center', va='center', color='white')
    
    # Milestone - FONT GRANDI
    milestones = [
        (3, 'M1:\nBusiness\nCase'),
        (6, 'M2:\nFramework'),
        (12, 'M3:\nPilota\nCompletato'),
        (24, 'M4:\nRollout\nCompleto')
    ]
    
    for x, label in milestones:
        ax.axvline(x, color=COLORS['secondary'], linewidth=3,
                  linestyle='--', alpha=0.7)
        ax.text(x, len(phases), label, fontsize=14, fontweight='bold',
               ha='center', va='bottom', color=COLORS['secondary'])
    
    # Configurazione assi - FONT GRANDI
    ax.set_xlim(0, 26)
    ax.set_ylim(-0.5, len(phases)+1)
    ax.set_xlabel('MESI', fontsize=20, fontweight='bold')
    ax.set_yticks(range(len(phases)))
    ax.set_yticklabels([f'FASE {i+1}' for i in range(len(phases))],
                       fontsize=16, fontweight='bold')
    
    # Scala temporale - FONT GRANDE
    ax.set_xticks(range(0, 25, 3))
    ax.set_xticklabels(range(0, 25, 3), fontsize=16)
    
    ax.grid(True, axis='x', alpha=0.3, linewidth=1)
    ax.set_axisbelow(True)
    
    # TITOLO
    ax.set_title('Roadmap Implementazione Conformità Integrata',
                fontsize=26, fontweight='bold', pad=20)
    
    plt.tight_layout()
    return fig

# =============================================================================
# FIGURA 7: MODELLO DI MATURITÀ - FONT GRANDI
# =============================================================================

def create_figure_7_maturity_large():
    """
    Modello di maturità con font molto grandi
    """
    fig = plt.figure(figsize=(18, 14), facecolor='white')
    ax = fig.add_subplot(111)
    ax.set_xlim(-7, 7)
    ax.set_ylim(-1, 9)
    ax.axis('off')
    
    # Livelli della piramide
    levels = [
        (5, 0, 1.5, COLORS['secondary'], 'LIVELLO 1:\nFRAMMENTATO'),
        (4, 1.5, 3, COLORS['warning'], 'LIVELLO 2:\nCOORDINATO'),
        (3, 3, 4.5, COLORS['info'], 'LIVELLO 3:\nINTEGRATO'),
        (2, 4.5, 6, COLORS['success'], 'LIVELLO 4:\nOTTIMIZZATO'),
        (1, 6, 7.5, COLORS['primary'], 'LIVELLO 5:\nADATTIVO')
    ]
    
    # Disegna i livelli
    for i, (width, y_bottom, y_top, color, title) in enumerate(levels):
        if i < len(levels) - 1:
            vertices = [(-width, y_bottom), (width, y_bottom),
                       (levels[i+1][0], y_top), (-levels[i+1][0], y_top)]
        else:
            vertices = [(-width, y_bottom), (width, y_bottom), (0, y_top)]
        
        polygon = Polygon(vertices, facecolor=color, 
                         edgecolor=COLORS['dark'], linewidth=3, alpha=0.9)
        ax.add_patch(polygon)
        
        # Testo livello - FONT MOLTO GRANDE
        y_center = (y_bottom + y_top) / 2
        text_color = 'white'
        ax.text(0, y_center, title, ha='center', va='center',
               fontsize=20, fontweight='bold', color=text_color)
    
    # Indicatore posizione attuale
    ax.annotate('', xy=(-3, 3.75), xytext=(-6, 3.75),
               arrowprops=dict(arrowstyle='->', lw=4, 
                             color=COLORS['accent']))
    ax.text(-6.5, 3.75, 'POSIZIONE\nATTUALE', fontsize=18, fontweight='bold',
           color=COLORS['accent'], ha='right', va='center')
    
    # TITOLO
    ax.text(0, 8.5, 'Modello di Maturità della Conformità',
           fontsize=26, fontweight='bold',
           color=COLORS['dark'], ha='center')
    
    plt.tight_layout()
    return fig

# =============================================================================
# FUNZIONE PRINCIPALE PER SALVARE TUTTE LE FIGURE
# =============================================================================

def save_all_figures_large_font():
    """
    Genera e salva tutte le figure con font grandi
    """
    print("\n" + "="*80)
    print("📊 GENERAZIONE DI TUTTE LE FIGURE - VERSIONE ALTA LEGGIBILITÀ")
    print("="*80 + "\n")
    
    figures = [
        (create_figure_1_venn_large, 'figura_4_1_venn_LARGE'),
        (create_figure_2_architecture_large, 'figura_4_2_architettura_LARGE'),
        (create_figure_3_gdpr_large, 'figura_4_3_processo_LARGE'),
        (create_figure_4_org_structure_large, 'figura_4_4_organigramma_LARGE'),
        (create_figure_5_comparison_large, 'figura_4_5_confronto_LARGE'),
        (create_figure_6_timeline_large, 'figura_4_6_timeline_LARGE'),
        (create_figure_7_maturity_large, 'figura_4_7_maturity_LARGE')
    ]
    
    for i, (func, filename) in enumerate(figures, 1):
        try:
            print(f"[{i}/7] Generazione {filename}...")
            fig = func()
            
            # Salva in tutti i formati
            fig.savefig(f'{filename}.pdf', format='pdf', 
                       bbox_inches='tight', dpi=300)
            fig.savefig(f'{filename}.png', format='png', 
                       bbox_inches='tight', dpi=200)
            fig.savefig(f'{filename}.svg', format='svg', 
                       bbox_inches='tight')
            
            print(f"    ✅ Salvata in PDF, PNG e SVG")
            plt.close(fig)
            
        except Exception as e:
            print(f"    ❌ Errore: {e}")
    
    print("\n" + "="*80)
    print("✨ GENERAZIONE COMPLETATA!")
    print("="*80)
    print("\n📁 FILE GENERATI:")
    print("   • 7 figure in formato PDF (per LaTeX)")
    print("   • 7 figure in formato PNG (per presentazioni)")
    print("   • 7 figure in formato SVG (per editing)")
    print("\n🎯 CARATTERISTICHE:")
    print("   • Font molto grandi per massima leggibilità")
    print("   • Colori ad alto contrasto")
    print("   • Dimensioni ottimizzate per stampa A4")
    print("   • Design pulito e professionale")
    print("\n📝 USO IN LATEX:")
    print("   \\includegraphics[width=\\textwidth]{figura_4_X_nome_LARGE.pdf}")
    print("\n" + "="*80)

if __name__ == '__main__':
    save_all_figures_large_font()
