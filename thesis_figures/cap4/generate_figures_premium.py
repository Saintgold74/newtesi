#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Figure Professionali per Capitolo 4 - Versione Premium
Design moderno e accattivante per pubblicazione accademica
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Circle, FancyBboxPatch, Polygon, Wedge, FancyArrow
from matplotlib.collections import PatchCollection
import matplotlib.patheffects as path_effects
import numpy as np
import seaborn as sns
from matplotlib import cm
from matplotlib.colors import LinearSegmentedColormap
import warnings
warnings.filterwarnings('ignore')

# =============================================================================
# CONFIGURAZIONE STILE PREMIUM
# =============================================================================

# Stile professionale personalizzato
plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Helvetica', 'Arial', 'DejaVu Sans'],
    'font.size': 11,
    'axes.labelsize': 12,
    'axes.titlesize': 14,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.titlesize': 16,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.grid': True,
    'grid.alpha': 0.3,
    'axes.facecolor': '#f8f9fa',
    'figure.facecolor': 'white',
    'axes.edgecolor': '#dee2e6',
    'axes.linewidth': 2,
    'xtick.major.size': 0,
    'ytick.major.size': 0,
})

# Palette di colori professionali
COLORS_MODERN = {
    'primary': '#2E86AB',      # Blu professionale
    'secondary': '#A23B72',     # Viola elegante
    'accent': '#F18F01',        # Arancione accento
    'success': '#73AB84',       # Verde successo
    'danger': '#C73E1D',        # Rosso pericolo
    'warning': '#FFB700',       # Giallo warning
    'info': '#6C9BD1',          # Blu info
    'dark': '#2D3436',          # Grigio scuro
    'light': '#F5F7FA',         # Grigio chiaro
}

# Gradient personalizzati
def create_gradient(color1, color2, n=256):
    """Crea un gradiente tra due colori"""
    return LinearSegmentedColormap.from_list('custom', [color1, color2], N=n)

# =============================================================================
# FIGURA 1: DIAGRAMMA DI VENN AVANZATO
# =============================================================================

def create_figure_1_venn_premium():
    """
    Diagramma di Venn con design moderno e effetti visivi
    """
    fig = plt.figure(figsize=(14, 10), facecolor='white')
    ax = fig.add_subplot(111)
    ax.set_xlim(-5, 7)
    ax.set_ylim(-6, 5)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Sfondo con gradiente sottile
    gradient = ax.imshow([[0, 0], [1, 1]], extent=[-5, 7, -6, 5], 
                        aspect='auto', cmap='RdBu_r', alpha=0.02, zorder=0)
    
    # Definizione posizioni e colori
    circles_data = [
        (0, 0, 2.8, COLORS_MODERN['primary'], 'PCI-DSS 4.0', '264 controlli'),
        (2.4, 0, 2.8, COLORS_MODERN['secondary'], 'GDPR', '99 articoli'),
        (1.2, -2.1, 2.8, COLORS_MODERN['success'], 'NIS2', '31 misure')
    ]
    
    # Disegna cerchi con effetto glow
    for x, y, r, color, title, subtitle in circles_data:
        # Effetto glow esterno
        for i in range(5):
            glow = Circle((x, y), r + 0.1*i, color=color, 
                         alpha=0.05, zorder=1)
            ax.add_patch(glow)
        
        # Cerchio principale
        circle = Circle((x, y), r, color=color, alpha=0.3, 
                       edgecolor=color, linewidth=3, zorder=2)
        ax.add_patch(circle)
    
    # Etichette con design moderno
    labels = [
        (-1.5, 2.2, 'PCI-DSS 4.0', 'bold', 16, COLORS_MODERN['primary']),
        (-1.5, 1.7, '264 controlli', 'normal', 11, COLORS_MODERN['dark']),
        (3.8, 2.2, 'GDPR', 'bold', 16, COLORS_MODERN['secondary']),
        (3.8, 1.7, '99 articoli', 'normal', 11, COLORS_MODERN['dark']),
        (1.2, -5.2, 'NIS2', 'bold', 16, COLORS_MODERN['success']),
        (1.2, -5.7, '31 misure', 'normal', 11, COLORS_MODERN['dark'])
    ]
    
    for x, y, text, weight, size, color in labels:
        txt = ax.text(x, y, text, fontweight=weight, fontsize=size, 
                     color=color, ha='center', va='center')
        # Effetto ombra per maggiore leggibilità
        txt.set_path_effects([path_effects.withStroke(linewidth=3, 
                                                      foreground='white')])
    
    # Numeri intersezioni con cerchi di sfondo
    intersections = [
        (1.2, 0, '47', COLORS_MODERN['info']),
        (-0.3, -0.9, '23', COLORS_MODERN['info']),
        (2.7, -0.9, '31', COLORS_MODERN['info']),
        (1.2, -0.8, '55', COLORS_MODERN['danger'])
    ]
    
    for x, y, value, color in intersections:
        # Cerchio di sfondo per il numero
        bg = Circle((x, y), 0.35, color='white', 
                   edgecolor=color, linewidth=2, zorder=3)
        ax.add_patch(bg)
        # Numero
        ax.text(x, y, value, fontsize=14, fontweight='bold', 
               color=color, ha='center', va='center', zorder=4)
    
    # Box informativo con stile card
    info_box = FancyBboxPatch((4.5, -2.5), 2.3, 2, 
                              boxstyle="round,pad=0.15",
                              facecolor='white',
                              edgecolor=COLORS_MODERN['primary'],
                              linewidth=2,
                              zorder=5)
    ax.add_patch(info_box)
    
    info_text = "CONTROLLI COMUNI\n\n156 totali (39.6%)\n55 core comuni\n101 parziali"
    ax.text(5.65, -1.5, info_text, fontsize=10, 
           ha='center', va='center', zorder=6,
           color=COLORS_MODERN['dark'], linespacing=1.5)
    
    # Esempi con icone stilizzate
    examples = [
        "🔐 Crittografia dati",
        "👤 Gestione accessi", 
        "🚨 Incident Response"
    ]
    
    for i, ex in enumerate(examples):
        ax.text(-3.5, -3.5-i*0.5, ex, fontsize=10, 
               color=COLORS_MODERN['dark'], ha='left')
    
    # Titolo con stile
    title = ax.text(1.2, 4.2, 'Sovrapposizioni Standard Normativi', 
                   fontsize=18, fontweight='bold',
                   color=COLORS_MODERN['dark'], ha='center')
    title.set_path_effects([path_effects.SimplePatchShadow(offset=(1, -1)),
                          path_effects.Normal()])
    
    ax.text(1.2, 3.6, 'Analisi del settore Grande Distribuzione', 
           fontsize=12, style='italic',
           color=COLORS_MODERN['dark'], ha='center', alpha=0.8)
    
    plt.tight_layout()
    return fig

# =============================================================================
# FIGURA 2: ARCHITETTURA A LAYER MODERNA
# =============================================================================

def create_figure_2_architecture_premium():
    """
    Architettura con design isometrico e moderno
    """
    fig = plt.figure(figsize=(16, 10), facecolor='white')
    ax = fig.add_subplot(111)
    ax.set_xlim(-3, 17)
    ax.set_ylim(-2, 9)
    ax.axis('off')
    
    # Gradiente di sfondo
    for i in range(10):
        rect = plt.Rectangle((-3, -2+i*1.1), 20, 1.1, 
                            facecolor=COLORS_MODERN['light'], 
                            alpha=0.1-i*0.01, zorder=0)
        ax.add_patch(rect)
    
    # Definizione livelli con effetto 3D
    levels = {
        3: {
            'y': 6.5,
            'color': COLORS_MODERN['warning'],
            'boxes': [
                (2, 'Dashboard\nEsecutiva', '📊'),
                (6, 'Console\nOperativa', '⚙️'),
                (10, 'Sistema\nReporting', '📈'),
                (14, 'API\nREST', '🔌')
            ]
        },
        2: {
            'y': 3.5,
            'color': COLORS_MODERN['info'],
            'boxes': [
                (3, 'Motore\nCorrelazione', '🔄'),
                (7, 'Analisi\nRischio', '⚠️'),
                (11, 'Valutazione\nConformità', '✓')
            ]
        },
        1: {
            'y': 0.5,
            'color': COLORS_MODERN['success'],
            'boxes': [
                (1, 'Config\nMgmt', '⚙️'),
                (4, 'SIEM\nLogs', '📝'),
                (7, 'Metriche\nKPI', '📊'),
                (10, 'Threat\nIntel', '🛡️'),
                (13, 'Audit\nTrail', '📋')
            ]
        }
    }
    
    # Disegna i livelli
    for level_num, level_data in levels.items():
        y = level_data['y']
        color = level_data['color']
        
        # Sfondo del livello con effetto glass
        level_bg = FancyBboxPatch((-1, y-0.8), 17, 1.8,
                                 boxstyle="round,pad=0.1",
                                 facecolor=color, alpha=0.08,
                                 edgecolor=color, linewidth=0,
                                 zorder=1)
        ax.add_patch(level_bg)
        
        # Etichetta livello
        label_box = FancyBboxPatch((-2.5, y-0.4), 1.5, 0.8,
                                  boxstyle="round,pad=0.05",
                                  facecolor=color, alpha=0.9,
                                  edgecolor='none',
                                  zorder=3)
        ax.add_patch(label_box)
        
        ax.text(-1.75, y, f'LIVELLO {level_num}', 
               fontsize=10, fontweight='bold',
               color='white', ha='center', va='center',
               zorder=4)
        
        # Box dei componenti
        for x, text, icon in level_data['boxes']:
            # Ombra
            shadow = FancyBboxPatch((x-1.2, y-0.45), 2.4, 0.9,
                                   boxstyle="round,pad=0.05",
                                   facecolor='gray', alpha=0.2,
                                   edgecolor='none',
                                   transform=ax.transData,
                                   zorder=2)
            ax.add_patch(shadow)
            
            # Box principale con gradiente
            box = FancyBboxPatch((x-1.2, y-0.4), 2.4, 0.9,
                                boxstyle="round,pad=0.05",
                                facecolor='white',
                                edgecolor=color,
                                linewidth=2,
                                zorder=3)
            ax.add_patch(box)
            
            # Icona e testo
            ax.text(x-0.7, y, icon, fontsize=14, ha='center', va='center', zorder=4)
            ax.text(x+0.2, y, text, fontsize=9, ha='center', va='center',
                   color=COLORS_MODERN['dark'], zorder=4)
    
    # Frecce di connessione stilizzate
    connections = [
        # Livello 1 a 2
        (1, 0.9, 3, 3.1), (4, 0.9, 3, 3.1),
        (7, 0.9, 7, 3.1), (10, 0.9, 11, 3.1),
        # Livello 2 a 3
        (3, 3.9, 2, 6.1), (3, 3.9, 6, 6.1),
        (7, 3.9, 6, 6.1), (7, 3.9, 10, 6.1),
        (11, 3.9, 10, 6.1), (11, 3.9, 14, 6.1)
    ]
    
    for x1, y1, x2, y2 in connections:
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                   arrowprops=dict(arrowstyle='->', 
                                 connectionstyle="arc3,rad=0.3",
                                 color=COLORS_MODERN['dark'],
                                 alpha=0.4,
                                 linewidth=2))
    
    # Framework di integrazione
    integration_box = FancyBboxPatch((1.5, 2.7), 11, 1.9,
                                    boxstyle="round,pad=0.1",
                                    facecolor='none',
                                    edgecolor=COLORS_MODERN['accent'],
                                    linewidth=3,
                                    linestyle='--',
                                    alpha=0.7,
                                    zorder=2)
    ax.add_patch(integration_box)
    
    ax.text(7, 5.0, '🔗 Framework di Integrazione Multi-Standard', 
           fontsize=11, fontweight='bold',
           color=COLORS_MODERN['accent'], ha='center',
           style='italic', alpha=0.9)
    
    # Titolo elegante
    title = ax.text(7, 8.2, 'Architettura Sistema di Conformità Integrata', 
                   fontsize=18, fontweight='bold',
                   color=COLORS_MODERN['dark'], ha='center')
    title.set_path_effects([path_effects.SimplePatchShadow(offset=(1, -1)),
                          path_effects.Normal()])
    
    # Database centrale
    db_x, db_y = 15.5, 3.5
    # Cilindro stilizzato per database
    ellipse_top = patches.Ellipse((db_x, db_y+0.3), 1.2, 0.3,
                                 facecolor=COLORS_MODERN['warning'],
                                 edgecolor=COLORS_MODERN['dark'],
                                 linewidth=2, zorder=5)
    ax.add_patch(ellipse_top)
    
    rect_body = patches.Rectangle((db_x-0.6, db_y-0.7), 1.2, 1,
                                 facecolor=COLORS_MODERN['warning'],
                                 edgecolor=COLORS_MODERN['dark'],
                                 linewidth=2, zorder=4)
    ax.add_patch(rect_body)
    
    ellipse_bottom = patches.Ellipse((db_x, db_y-0.7), 1.2, 0.3,
                                    facecolor=COLORS_MODERN['warning'],
                                    edgecolor=COLORS_MODERN['dark'],
                                    linewidth=2, zorder=5)
    ax.add_patch(ellipse_bottom)
    
    ax.text(db_x, db_y-0.2, '💾\nData\nLake', fontsize=9,
           ha='center', va='center', color='white',
           fontweight='bold', zorder=6)
    
    plt.tight_layout()
    return fig

# =============================================================================
# FIGURA 3: PROCESSO GDPR FLOWCHART MODERNO
# =============================================================================

def create_figure_3_gdpr_flow_premium():
    """
    Flowchart GDPR con design moderno e pulito
    """
    fig = plt.figure(figsize=(16, 10), facecolor='white')
    ax = fig.add_subplot(111)
    ax.set_xlim(-2, 16)
    ax.set_ylim(-3, 6)
    ax.axis('off')
    
    # Timeline di sfondo
    timeline_y = 2
    ax.plot([-1, 15], [timeline_y, timeline_y], 
           color=COLORS_MODERN['light'], linewidth=40, 
           alpha=0.5, zorder=0, solid_capstyle='round')
    
    # Definizione nodi del processo
    process_nodes = [
        # (x, y, tipo, testo, colore, icona)
        (1, 2, 'process', '1. Ricezione\nRichiesta', COLORS_MODERN['info'], '📥'),
        (4, 2, 'decision', 'Verifica\nIdentità', COLORS_MODERN['warning'], '🔍'),
        (7, 2, 'process', '3. Identificazione\nDati', COLORS_MODERN['info'], '🔎'),
        (10, 0, 'process', '4. Esecuzione\nAzione', COLORS_MODERN['success'], '⚡'),
        (7, 0, 'process', '5. Notifica\nInteressato', COLORS_MODERN['primary'], '📧'),
        (4, -1, 'data', '6. Documentazione\nAudit Trail', COLORS_MODERN['secondary'], '📝'),
        (4, 4, 'process', 'Richiesta\nRespinta', COLORS_MODERN['danger'], '❌'),
        (13, 2, 'data', 'Sistemi\nCoinvolti', COLORS_MODERN['accent'], '💻')
    ]
    
    # Disegna i nodi
    for x, y, node_type, text, color, icon in process_nodes:
        if node_type == 'process':
            # Nodo processo rettangolare con bordi arrotondati
            box = FancyBboxPatch((x-1.2, y-0.5), 2.4, 1,
                                boxstyle="round,pad=0.05",
                                facecolor='white',
                                edgecolor=color,
                                linewidth=3,
                                zorder=3)
            ax.add_patch(box)
            
        elif node_type == 'decision':
            # Nodo decisionale a diamante
            diamond = Polygon([(x, y-0.8), (x+1.2, y), (x, y+0.8), (x-1.2, y)],
                            facecolor='white',
                            edgecolor=color,
                            linewidth=3,
                            zorder=3)
            ax.add_patch(diamond)
            
        elif node_type == 'data':
            # Nodo dati con forma trapezoidale
            trap = Polygon([(x-1, y-0.5), (x+1, y-0.5), 
                          (x+1.2, y+0.5), (x-1.2, y+0.5)],
                         facecolor='white',
                         edgecolor=color,
                         linewidth=3,
                         zorder=3)
            ax.add_patch(trap)
        
        # Icona e testo
        ax.text(x, y+0.15, icon, fontsize=16, ha='center', va='center', zorder=4)
        ax.text(x, y-0.25, text, fontsize=9, ha='center', va='center',
               color=COLORS_MODERN['dark'], fontweight='bold', zorder=4)
    
    # Frecce di flusso con stile
    flows = [
        (2.2, 2, 2.8, 2, 'Submit', False),
        (5.2, 2, 5.8, 2, 'Sì', False),
        (4, 2.8, 4, 3.2, 'No', False),
        (8.2, 2, 8.8, 1, '', True),
        (8.8, 0.3, 8.2, 0, '', False),
        (5.8, 0, 5.2, -0.5, '', True),
        (11.8, 2, 11.2, 2, '', False)
    ]
    
    for x1, y1, x2, y2, label, curved in flows:
        style = "arc3,rad=0.3" if curved else "arc3,rad=0"
        arrow = patches.FancyArrowPatch((x1, y1), (x2, y2),
                                      connectionstyle=style,
                                      arrowstyle='-|>',
                                      mutation_scale=20,
                                      linewidth=2,
                                      color=COLORS_MODERN['dark'],
                                      alpha=0.7,
                                      zorder=2)
        ax.add_patch(arrow)
        
        if label:
            mid_x, mid_y = (x1+x2)/2, (y1+y2)/2
            label_bg = FancyBboxPatch((mid_x-0.3, mid_y-0.15), 0.6, 0.3,
                                     boxstyle="round,pad=0.02",
                                     facecolor='white',
                                     edgecolor='none',
                                     zorder=3)
            ax.add_patch(label_bg)
            ax.text(mid_x, mid_y, label, fontsize=9,
                   ha='center', va='center',
                   color=COLORS_MODERN['dark'],
                   fontweight='bold', zorder=4)
    
    # Timer badges
    timer_data = [
        (2.5, 2.8, '⏱️ Max 72h', COLORS_MODERN['danger']),
        (8.5, 0.8, '📅 Max 30 giorni', COLORS_MODERN['warning'])
    ]
    
    for x, y, text, color in timer_data:
        badge = FancyBboxPatch((x-0.7, y-0.2), 1.4, 0.4,
                              boxstyle="round,pad=0.05",
                              facecolor=color, alpha=0.2,
                              edgecolor=color, linewidth=2,
                              zorder=3)
        ax.add_patch(badge)
        ax.text(x, y, text, fontsize=9, ha='center', va='center',
               color=color, fontweight='bold', zorder=4)
    
    # Legenda GDPR Articles
    legend_x, legend_y = 13, -1
    legend_box = FancyBboxPatch((legend_x-1.5, legend_y-1), 3, 2,
                               boxstyle="round,pad=0.1",
                               facecolor='white',
                               edgecolor=COLORS_MODERN['primary'],
                               linewidth=2,
                               zorder=3)
    ax.add_patch(legend_box)
    
    legend_items = [
        ('Art. 15', 'Accesso', '👁️'),
        ('Art. 16', 'Rettifica', '✏️'),
        ('Art. 17', 'Cancellazione', '🗑️'),
        ('Art. 20', 'Portabilità', '📦')
    ]
    
    ax.text(legend_x, legend_y+0.7, 'Diritti GDPR', 
           fontsize=10, fontweight='bold',
           ha='center', color=COLORS_MODERN['primary'])
    
    for i, (art, desc, icon) in enumerate(legend_items):
        y_pos = legend_y + 0.3 - i*0.3
        ax.text(legend_x-1.2, y_pos, icon, fontsize=10, ha='left')
        ax.text(legend_x-0.9, y_pos, f'{art}', fontsize=8, 
               ha='left', color=COLORS_MODERN['dark'], fontweight='bold')
        ax.text(legend_x-0.2, y_pos, desc, fontsize=8,
               ha='left', color=COLORS_MODERN['dark'])
    
    # Titolo
    title = ax.text(7, 5.2, 'Processo Automatizzato Diritti GDPR', 
                   fontsize=18, fontweight='bold',
                   color=COLORS_MODERN['dark'], ha='center')
    title.set_path_effects([path_effects.SimplePatchShadow(offset=(1, -1)),
                          path_effects.Normal()])
    
    plt.tight_layout()
    return fig

# =============================================================================
# FIGURA 5: GRAFICO COMPARATIVO AVANZATO
# =============================================================================

def create_figure_5_comparison_premium():
    """
    Grafico a barre comparativo con design moderno
    """
    fig = plt.figure(figsize=(14, 8), facecolor='white')
    ax = fig.add_subplot(111)
    
    # Sfondo con gradiente
    ax.set_facecolor('#f8f9fa')
    
    # Dati
    metrics = ['Tempo Detection', 'Sistemi Compromessi', 'Downtime', 'Impatto Economico']
    real_values = [360, 2847, 120, 8700]
    compliant_values = [6, 12, 4, 300]
    improvements = [98.3, 99.6, 96.7, 96.5]
    
    x = np.arange(len(metrics))
    width = 0.35
    
    # Crea le barre con gradiente simulato
    bars1 = ax.bar(x - width/2, real_values, width, 
                   label='Scenario Reale',
                   color=COLORS_MODERN['danger'],
                   edgecolor='darkred', linewidth=2,
                   alpha=0.8)
    
    bars2 = ax.bar(x + width/2, compliant_values, width, 
                   label='Con Conformità',
                   color=COLORS_MODERN['success'],
                   edgecolor='darkgreen', linewidth=2,
                   alpha=0.8)
    
    # Aggiungi pattern alle barre per distinguerle meglio
    for bar in bars1:
        bar.set_hatch('//')
    for bar in bars2:
        bar.set_hatch('\\\\')
    
    # Valori sopra le barre con design elegante
    for i, (bar1, bar2, v1, v2, imp) in enumerate(zip(bars1, bars2, 
                                                       real_values, compliant_values,
                                                       improvements)):
        # Valore scenario reale
        height1 = bar1.get_height()
        value_box1 = FancyBboxPatch((bar1.get_x()-0.05, height1+100), 
                                   bar1.get_width()+0.1, 300,
                                   boxstyle="round,pad=0.02",
                                   facecolor=COLORS_MODERN['danger'],
                                   alpha=0.2,
                                   edgecolor='none',
                                   zorder=3)
        ax.add_patch(value_box1)
        ax.text(bar1.get_x() + bar1.get_width()/2, height1 + 200,
               f'{v1:,}', ha='center', va='bottom',
               fontweight='bold', fontsize=10,
               color=COLORS_MODERN['danger'])
        
        # Valore scenario conforme
        height2 = bar2.get_height()
        ax.text(bar2.get_x() + bar2.get_width()/2, height2 + 200,
               f'{v2:,}', ha='center', va='bottom',
               fontweight='bold', fontsize=10,
               color=COLORS_MODERN['success'])
        
        # Badge miglioramento
        improve_y = max(height1, height2) + 600
        badge = FancyBboxPatch((x[i]-0.3, improve_y), 0.6, 250,
                              boxstyle="round,pad=0.02",
                              facecolor=COLORS_MODERN['info'],
                              edgecolor='none',
                              alpha=0.3,
                              zorder=3)
        ax.add_patch(badge)
        ax.text(x[i], improve_y+125, f'-{imp}%', 
               ha='center', va='center',
               fontsize=9, fontweight='bold',
               color=COLORS_MODERN['info'])
    
    # Configurazione assi
    ax.set_ylabel('Valori Assoluti', fontsize=12, fontweight='bold',
                 color=COLORS_MODERN['dark'])
    ax.set_xticks(x)
    ax.set_xticklabels(metrics, fontsize=11, rotation=0)
    ax.set_yscale('log')  # Scala logaritmica per gestire grandi differenze
    
    # Griglia stilizzata
    ax.grid(True, which='both', alpha=0.2, linestyle='--', linewidth=0.5)
    ax.set_axisbelow(True)
    
    # Legenda personalizzata
    legend = ax.legend(loc='upper right', frameon=True, 
                      fancybox=True, shadow=True,
                      fontsize=11, title='Scenari',
                      title_fontsize=12)
    legend.get_frame().set_facecolor('white')
    legend.get_frame().set_alpha(0.95)
    
    # Box statistiche riassuntive
    stats_text = "IMPATTO COMPLESSIVO\n" + "─"*20 + "\n"
    stats_text += "Riduzione Media: 97.8%\n"
    stats_text += "ROI Stimato: 340%\n"
    stats_text += "Payback: 18 mesi"
    
    stats_box = FancyBboxPatch((0.02, 0.65), 0.18, 0.25,
                              boxstyle="round,pad=0.02",
                              facecolor='white',
                              edgecolor=COLORS_MODERN['primary'],
                              linewidth=2,
                              transform=ax.transAxes,
                              zorder=5)
    ax.add_patch(stats_box)
    
    ax.text(0.11, 0.775, stats_text, transform=ax.transAxes,
           fontsize=9, ha='center', va='center',
           color=COLORS_MODERN['dark'], linespacing=1.5)
    
    # Titolo e sottotitolo
    ax.set_title('Analisi Controfattuale: Impatto della Conformità Integrata',
                fontsize=16, fontweight='bold', color=COLORS_MODERN['dark'],
                pad=20)
    ax.text(0.5, 1.02, 'Confronto tra scenario reale e scenario con conformità completa',
           transform=ax.transAxes, ha='center',
           fontsize=11, style='italic', color=COLORS_MODERN['dark'])
    
    # Rimuovi spine superiore e destra
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    # Unità di misura
    units = ['ore', 'unità', 'ore', 'k€']
    for i, (metric, unit) in enumerate(zip(metrics, units)):
        ax.text(i, -0.05, f'({unit})', transform=ax.get_xaxis_transform(),
               ha='center', fontsize=8, color='gray')
    
    plt.tight_layout()
    return fig

# =============================================================================
# SALVATAGGIO FIGURE
# =============================================================================

def save_all_premium_figures():
    """
    Genera e salva tutte le figure in versione premium
    """
    figures = [
        (create_figure_1_venn_premium(), 'figura_4_1_venn_premium.pdf'),
        (create_figure_2_architecture_premium(), 'figura_4_2_architettura_premium.pdf'),
        (create_figure_3_gdpr_flow_premium(), 'figura_4_3_processo_premium.pdf'),
        (create_figure_5_comparison_premium(), 'figura_4_5_confronto_premium.pdf'),
    ]
    
    print("\n" + "="*60)
    print("GENERAZIONE FIGURE PREMIUM - CAPITOLO 4")
    print("="*60 + "\n")
    
    for fig, filename in figures:
        try:
            # Salva in PDF
            fig.savefig(filename, format='pdf', bbox_inches='tight', 
                       dpi=300, facecolor='white', edgecolor='none')
            
            # Salva in PNG alta risoluzione
            png_filename = filename.replace('.pdf', '.png')
            fig.savefig(png_filename, format='png', bbox_inches='tight', 
                       dpi=200, facecolor='white', edgecolor='none')
            
            # Salva in SVG per editing
            svg_filename = filename.replace('.pdf', '.svg')
            fig.savefig(svg_filename, format='svg', bbox_inches='tight',
                       facecolor='white', edgecolor='none')
            
            print(f"✅ {filename[:-4]}")
            print(f"   ├─ PDF: {filename}")
            print(f"   ├─ PNG: {png_filename}")
            print(f"   └─ SVG: {svg_filename}")
            
        except Exception as e:
            print(f"❌ Errore: {filename} - {str(e)}")
        finally:
            plt.close(fig)
    
    print("\n" + "="*60)
    print("✨ FIGURE PREMIUM GENERATE CON SUCCESSO!")
    print("="*60)
    print("\nCaratteristiche delle figure:")
    print("• Design moderno e professionale")
    print("• Colori coordinati e gradevoli")
    print("• Effetti visivi avanzati")
    print("• Alta risoluzione per pubblicazione")
    print("• Formato vettoriale per qualità ottimale")

if __name__ == '__main__':
    # Genera tutte le figure premium
    save_all_premium_figures()
    
    # Suggerimenti per l'uso
    print("\n📝 SUGGERIMENTI PER L'USO:")
    print("-"*40)
    print("1. Usa i PDF per il documento LaTeX finale")
    print("2. Usa i PNG per presentazioni")
    print("3. Usa gli SVG se vuoi modificare in Inkscape/Illustrator")
    print("\n" + "="*60)
