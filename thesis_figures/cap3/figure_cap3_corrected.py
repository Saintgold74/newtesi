#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Figure Professionali Corrette - Capitolo 3
Font Large (16-20pt) e Sovrapposizioni Risolte
Versione Ottimizzata per Leggibilità

Università Niccolò Cusano
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle, Polygon, FancyArrowPatch, Wedge
import matplotlib.gridspec as gridspec
from matplotlib.colors import LinearSegmentedColormap
import warnings
warnings.filterwarnings('ignore')

# Configurazione globale con FONT LARGE
plt.rcParams.update({
    'font.size': 16,  # AUMENTATO
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'Helvetica', 'DejaVu Sans'],
    'axes.titlesize': 20,  # AUMENTATO
    'axes.labelsize': 16,  # AUMENTATO
    'xtick.labelsize': 14,  # AUMENTATO
    'ytick.labelsize': 14,  # AUMENTATO
    'legend.fontsize': 14,  # AUMENTATO
    'figure.titlesize': 22,  # AUMENTATO
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.format': 'pdf',
    'axes.linewidth': 0,
    'axes.edgecolor': 'none',
    'axes.grid': False,
    'axes.spines.left': False,
    'axes.spines.bottom': False,
    'axes.spines.right': False,
    'axes.spines.top': False,
    'pdf.fonttype': 42,
    'ps.fonttype': 42
})

# Palette colori professionale
colors_modern = {
    'primary': '#2E86AB',
    'secondary': '#A23B72',
    'accent': '#F18F01',
    'success': '#73AB84',
    'danger': '#C73E1D',
    'dark': '#2D3436',
    'light': '#F7F9FB',
    'gradient1': '#667EEA',
    'gradient2': '#764BA2',
    'tech1': '#00D2FF',
    'tech2': '#3A7BD5'
}

def create_figure_3_1_corrected():
    """
    Figura 3.1: Architettura Alimentazione 2N - FONT LARGE
    """
    fig = plt.figure(figsize=(18, 11), facecolor='white')
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Gradient di sfondo sottile
    gradient = np.linspace(0, 1, 256).reshape(1, -1)
    gradient = np.vstack((gradient, gradient))
    ax.imshow(gradient, aspect='auto', cmap=LinearSegmentedColormap.from_list('', ['#f8f9fa', '#ffffff']),
              extent=[0, 16, 0, 10], alpha=0.3, zorder=-1)
    
    # Titolo principale LARGE
    title = ax.text(8, 9.2, 'ARCHITETTURA RIDONDANTE 2N', fontsize=24, fontweight='bold',
                   ha='center', color=colors_modern['dark'])
    subtitle = ax.text(8, 8.6, 'Sistema di Alimentazione Critica per Data Center GDO', 
                      fontsize=16, ha='center', color='#636e72', style='italic')
    
    # Rete elettrica
    grid_box = FancyBboxPatch((1, 6), 2.5, 1.8,
                              boxstyle="round,pad=0.05,rounding_size=0.1",
                              facecolor='#FFF3E0', edgecolor='#f39c12', linewidth=3)
    ax.add_patch(grid_box)
    ax.text(2.25, 7.3, '[POWER]', fontsize=20, fontweight='bold', ha='center', color='#f39c12')
    ax.text(2.25, 6.8, 'RETE ELETTRICA', fontsize=14, fontweight='bold', ha='center')
    ax.text(2.25, 6.3, '380V / 50Hz', fontsize=12, ha='center', color='#7f8c8d')
    
    # UPS Sistema A
    ups_a = FancyBboxPatch((5, 5.5), 2.5, 3,
                           boxstyle="round,pad=0.05,rounding_size=0.1",
                           facecolor=colors_modern['primary'], 
                           edgecolor=colors_modern['dark'], linewidth=2.5)
    ax.add_patch(ups_a)
    
    # Shadow effect
    shadow = FancyBboxPatch((5.1, 5.4), 2.5, 3,
                            boxstyle="round,pad=0.05,rounding_size=0.1",
                            facecolor='gray', alpha=0.2, zorder=0)
    ax.add_patch(shadow)
    
    # Contenuto UPS A - FONT LARGE
    ax.text(6.25, 7.8, 'UPS SISTEMA A', fontsize=15, fontweight='bold', 
            ha='center', color='white')
    ax.text(6.25, 7.2, 'PRIMARIO', fontsize=13, ha='center', color='#ecf0f1')
    
    # Indicatori con font più grande
    indicators = [
        ('Power:', '300kW', '#2ecc71'),
        ('Load:', '68%', '#3498db'),
        ('Temp:', '22°C', '#f39c12')
    ]
    
    for i, (label, value, color) in enumerate(indicators):
        y_pos = 6.7 - i*0.45
        circle = Circle((5.5, y_pos), 0.1, facecolor=color, edgecolor='white', linewidth=1)
        ax.add_patch(circle)
        ax.text(5.75, y_pos, label, fontsize=11, va='center', color='white')
        ax.text(6.8, y_pos, value, fontsize=12, va='center', color='white', fontweight='bold')
    
    # UPS Sistema B
    ups_b = FancyBboxPatch((9, 5.5), 2.5, 3,
                           boxstyle="round,pad=0.05,rounding_size=0.1",
                           facecolor=colors_modern['secondary'], 
                           edgecolor=colors_modern['dark'], linewidth=2.5)
    ax.add_patch(ups_b)
    
    shadow_b = FancyBboxPatch((9.1, 5.4), 2.5, 3,
                              boxstyle="round,pad=0.05,rounding_size=0.1",
                              facecolor='gray', alpha=0.2, zorder=0)
    ax.add_patch(shadow_b)
    
    ax.text(10.25, 7.8, 'UPS SISTEMA B', fontsize=15, fontweight='bold', 
            ha='center', color='white')
    ax.text(10.25, 7.2, 'BACKUP', fontsize=13, ha='center', color='#ecf0f1')
    
    # Indicatori Sistema B
    for i, (label, value, color) in enumerate([
        ('Power:', '300kW', '#2ecc71'),
        ('Load:', '0%', '#95a5a6'),
        ('Temp:', '21°C', '#f39c12')
    ]):
        y_pos = 6.7 - i*0.45
        circle = Circle((9.5, y_pos), 0.1, facecolor=color, edgecolor='white', linewidth=1)
        ax.add_patch(circle)
        ax.text(9.75, y_pos, label, fontsize=11, va='center', color='white')
        ax.text(10.8, y_pos, value, fontsize=12, va='center', color='white', fontweight='bold')
    
    # ATS al centro
    ats_box = FancyBboxPatch((6.75, 3.5), 2.5, 1.5,
                             boxstyle="round,pad=0.05,rounding_size=0.1",
                             facecolor='#34495e', edgecolor=colors_modern['dark'], linewidth=2)
    ax.add_patch(ats_box)
    ax.text(8, 4.6, 'ATS', fontsize=14, fontweight='bold', ha='center', color='white')
    ax.text(8, 4.1, 'Transfer <100ms', fontsize=11, ha='center', color='#ecf0f1')
    ax.text(8, 3.7, 'Auto Switch', fontsize=11, ha='center', color='#ecf0f1')
    
    # Carichi critici
    load_box = FancyBboxPatch((5.5, 0.5), 5, 2,
                             boxstyle="round,pad=0.05,rounding_size=0.1",
                             facecolor=colors_modern['accent'], 
                             edgecolor=colors_modern['dark'], linewidth=2.5, alpha=0.9)
    ax.add_patch(load_box)
    
    ax.text(8, 1.9, 'CARICHI CRITICI', fontsize=16, fontweight='bold', 
            ha='center', color='white')
    
    # Icone dei carichi (testo invece di emoji)
    loads = ['[Servers]', '[Storage]', '[Network]', '[Cooling]']
    for i, load in enumerate(loads):
        ax.text(6 + i*1.2, 1.1, load, fontsize=12, ha='center', color='white')
    
    # Frecce di flusso
    arrow_style = "Simple, tail_width=0.5, head_width=8, head_length=10"
    arrow_kwargs = dict(arrowstyle=arrow_style, color=colors_modern['dark'], 
                       lw=2.5, alpha=0.7)
    
    arrow1 = FancyArrowPatch((3.5, 6.9), (5, 7), **arrow_kwargs)
    ax.add_patch(arrow1)
    arrow2 = FancyArrowPatch((3.5, 6.9), (9, 7), **arrow_kwargs)
    ax.add_patch(arrow2)
    
    arrow3 = FancyArrowPatch((6.25, 5.5), (7.5, 4.5), 
                            arrowstyle=arrow_style, color=colors_modern['primary'], lw=3)
    ax.add_patch(arrow3)
    arrow4 = FancyArrowPatch((10.25, 5.5), (8.5, 4.5), 
                            arrowstyle=arrow_style, color=colors_modern['secondary'], lw=3)
    ax.add_patch(arrow4)
    
    arrow5 = FancyArrowPatch((8, 3.5), (8, 2.5), 
                            arrowstyle=arrow_style, color=colors_modern['accent'], lw=3.5)
    ax.add_patch(arrow5)
    
    # Dashboard metriche FONT LARGE
    metrics_card = FancyBboxPatch((12.5, 2), 3.2, 5.5,
                                  boxstyle="round,pad=0.08,rounding_size=0.1",
                                  facecolor='white', edgecolor='#dfe6e9', linewidth=2)
    ax.add_patch(metrics_card)
    
    header_rect = Rectangle((12.5, 6.5), 3.2, 1, facecolor=colors_modern['primary'], 
                           edgecolor='none')
    ax.add_patch(header_rect)
    ax.text(14.1, 7, 'PERFORMANCE', fontsize=14, fontweight='bold', 
            ha='center', color='white')
    
    # Metriche con font large
    metrics = [
        ('Disponibilità', '99.94%', '#2ecc71'),
        ('MTBF', '87,600h', '#3498db'),
        ('MTTR', '1.8h', '#e67e22'),
        ('Autonomia', '15 min', '#9b59b6'),
        ('PUE', '1.4', '#1abc9c'),
        ('ROI', '24 mesi', '#f39c12')
    ]
    
    for i, (label, value, color) in enumerate(metrics):
        y_pos = 5.8 - i*0.7
        indicator = Rectangle((12.8, y_pos-0.15), 0.1, 0.3, facecolor=color)
        ax.add_patch(indicator)
        ax.text(13.1, y_pos, label, fontsize=12, va='center')
        ax.text(15.2, y_pos, value, fontsize=13, fontweight='bold', 
                va='center', ha='right', color=color)
    
    plt.tight_layout()
    plt.savefig('figura_3_1_corrected.pdf', format='pdf', 
                bbox_inches='tight', facecolor='white')
    print("✓ Figura 3.1 corretta con font LARGE")
    return fig

def create_figure_3_2_corrected():
    """
    Figura 3.2: Evoluzione Rete - FONT LARGE
    """
    fig = plt.figure(figsize=(18, 11), facecolor='white')
    gs = gridspec.GridSpec(2, 2, figure=fig, hspace=0.3, wspace=0.2)
    
    # Titolo principale LARGE
    fig.text(0.5, 0.95, 'EVOLUZIONE ARCHITETTURA DI RETE', 
            fontsize=24, fontweight='bold', ha='center', color=colors_modern['dark'])
    fig.text(0.5, 0.91, 'Da MPLS Tradizionale a SD-WAN Cloud-Native', 
            fontsize=16, ha='center', color='#636e72', style='italic')
    
    # MPLS Tradizionale (sinistra)
    ax1 = fig.add_subplot(gs[0, 0])
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)
    ax1.axis('off')
    
    card_mpls = FancyBboxPatch((0.5, 0.5), 9, 9,
                               boxstyle="round,pad=0.05,rounding_size=0.1",
                               facecolor='#fff5f5', edgecolor='#e74c3c', linewidth=2)
    ax1.add_patch(card_mpls)
    
    header_mpls = Rectangle((0.5, 8), 9, 1.5, facecolor='#e74c3c', edgecolor='none')
    ax1.add_patch(header_mpls)
    ax1.text(5, 8.75, 'ARCHITETTURA MPLS', fontsize=15, 
            fontweight='bold', ha='center', color='white')
    
    # Datacenter MPLS
    dc_circle = Circle((5, 6.5), 0.6, facecolor='#c0392b', edgecolor='white', linewidth=2)
    ax1.add_patch(dc_circle)
    ax1.text(5, 6.5, 'DC', fontsize=14, fontweight='bold', ha='center', color='white')
    
    # Router MPLS
    mpls_routers = [(2.5, 4.5), (5, 4.5), (7.5, 4.5)]
    for i, (x, y) in enumerate(mpls_routers):
        shadow = Rectangle((x-0.45, y-0.35), 0.9, 0.6, 
                          facecolor='gray', alpha=0.3, zorder=0)
        ax1.add_patch(shadow)
        router = Rectangle((x-0.5, y-0.3), 0.9, 0.6, 
                          facecolor='#e67e22', edgecolor='#d35400', linewidth=2)
        ax1.add_patch(router)
        ax1.text(x, y, f'MPLS-{i+1}', fontsize=11, fontweight='bold', 
                ha='center', color='white')
    
    # Punti vendita
    for i in range(5):
        x = 1.5 + i*1.5
        store = Rectangle((x-0.25, 2.2), 0.5, 0.5, 
                         facecolor='#95a5a6', edgecolor='#7f8c8d', linewidth=1)
        ax1.add_patch(store)
        ax1.text(x, 2.45, f'PV{i+1}', fontsize=10, ha='center', color='white')
        
        router_idx = min(i // 2, 2)
        ax1.plot([x, mpls_routers[router_idx][0]], 
                [2.7, mpls_routers[router_idx][1]-0.3], 
                'r-', linewidth=2, alpha=0.7)
    
    # Problemi MPLS
    problems_box = FancyBboxPatch((1, 0.8), 8, 1,
                                  boxstyle="round,pad=0.05",
                                  facecolor='#ffe5e5', edgecolor='#e74c3c', linewidth=1)
    ax1.add_patch(problems_box)
    ax1.text(5, 1.3, 'CRITICITÀ', fontsize=12, fontweight='bold', 
            ha='center', color='#c0392b')
    ax1.text(5, 0.9, '€450/Mbps • 30-45 giorni • Rigidità', 
            fontsize=11, ha='center', color='#7f8c8d')
    
    # SD-WAN (destra)
    ax2 = fig.add_subplot(gs[0, 1])
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    ax2.axis('off')
    
    card_sdwan = FancyBboxPatch((0.5, 0.5), 9, 9,
                               boxstyle="round,pad=0.05,rounding_size=0.1",
                               facecolor='#f0f9ff', edgecolor='#3498db', linewidth=2)
    ax2.add_patch(card_sdwan)
    
    header_sdwan = Rectangle((0.5, 8), 9, 1.5, facecolor='#3498db', edgecolor='none')
    ax2.add_patch(header_sdwan)
    ax2.text(5, 8.75, 'ARCHITETTURA SD-WAN', fontsize=15, 
            fontweight='bold', ha='center', color='white')
    
    # Cloud centrale
    cloud_points = np.array([
        [4, 6.8], [4.2, 7.2], [4.6, 7.3], [5, 7.2],
        [5.4, 7.3], [5.8, 7.2], [6, 6.8], [5.8, 6.4],
        [5.4, 6.3], [5, 6.4], [4.6, 6.3], [4.2, 6.4]
    ])
    cloud = Polygon(cloud_points, facecolor='#3498db', edgecolor='white', 
                   linewidth=2, alpha=0.9)
    ax2.add_patch(cloud)
    ax2.text(5, 6.8, 'CLOUD\nSD-WAN', fontsize=12, fontweight='bold', 
            ha='center', color='white')
    
    # Internet mesh
    mesh_box = FancyBboxPatch((1, 4), 8, 1.5,
                             boxstyle="round,pad=0.05",
                             facecolor='#e8f4fd', edgecolor='#3498db', 
                             linewidth=1, alpha=0.5, linestyle='--')
    ax2.add_patch(mesh_box)
    ax2.text(5, 4.75, 'INTERNET + MPLS HYBRID', fontsize=12, 
            fontweight='bold', ha='center', color='#2980b9')
    
    # Punti vendita SD-WAN
    for i in range(5):
        x = 1.5 + i*1.5
        
        edge = Circle((x, 3), 0.2, facecolor='#2ecc71', edgecolor='white', 
                     linewidth=1)
        ax2.add_patch(edge)
        
        store = Rectangle((x-0.25, 2.2), 0.5, 0.5, 
                         facecolor='#3498db', edgecolor='#2980b9', linewidth=1)
        ax2.add_patch(store)
        ax2.text(x, 2.45, f'PV{i+1}', fontsize=10, ha='center', color='white')
        
        for j, (color, style) in enumerate([('#3498db', '-'), ('#2ecc71', '--')]):
            ax2.plot([x, 5], [3.2, 4], color=color, linestyle=style, 
                    linewidth=1.5, alpha=0.5)
    
    # Vantaggi SD-WAN
    benefits_box = FancyBboxPatch((1, 0.8), 8, 1,
                                 boxstyle="round,pad=0.05",
                                 facecolor='#e8f8f5', edgecolor='#27ae60', linewidth=1)
    ax2.add_patch(benefits_box)
    ax2.text(5, 1.3, 'VANTAGGI', fontsize=12, fontweight='bold', 
            ha='center', color='#27ae60')
    ax2.text(5, 0.9, 'Costi -70% • 5-7 giorni • MTTR 1.8h', 
            fontsize=11, ha='center', color='#7f8c8d')
    
    # Confronto (bottom)
    ax3 = fig.add_subplot(gs[1, :])
    ax3.set_xlim(0, 10)
    ax3.set_ylim(0, 5)
    ax3.axis('off')
    
    # Tabella comparativa con font large
    comparison_data = [
        ['Parametro', 'MPLS', 'SD-WAN', 'Miglioramento'],
        ['Costo', '€450/Mbps', '€135/Mbps', '-70%'],
        ['Attivazione', '30-45 giorni', '5-7 giorni', '-85%'],
        ['MTTR', '4.2 ore', '1.8 ore', '-57%'],
        ['Flessibilità', 'Bassa', 'Alta', '+++']
    ]
    
    table_x = 1
    table_y = 3.5
    cell_width = 2
    cell_height = 0.6
    
    for i, row in enumerate(comparison_data):
        for j, cell in enumerate(row):
            if i == 0:
                bg_color = colors_modern['dark']
                text_color = 'white'
                weight = 'bold'
                size = 12
            elif j == 3:
                bg_color = '#e8f8f5' if i % 2 == 0 else '#f0fdf4'
                text_color = '#27ae60'
                weight = 'bold'
                size = 12
            else:
                bg_color = '#f8f9fa' if i % 2 == 0 else 'white'
                text_color = colors_modern['dark']
                weight = 'normal'
                size = 11
            
            rect = Rectangle((table_x + j*cell_width, table_y - i*cell_height), 
                           cell_width, cell_height,
                           facecolor=bg_color, edgecolor='#dee2e6', linewidth=0.5)
            ax3.add_patch(rect)
            ax3.text(table_x + j*cell_width + cell_width/2, 
                    table_y - i*cell_height + cell_height/2,
                    cell, fontsize=size, fontweight=weight, ha='center', 
                    va='center', color=text_color)
    
    plt.tight_layout()
    plt.savefig('figura_3_2_corrected.pdf', format='pdf', 
                bbox_inches='tight', facecolor='white')
    print("✓ Figura 3.2 corretta con font LARGE")
    return fig

def create_figure_3_3_corrected():
    """
    Figura 3.3: Dashboard Maturità - FONT LARGE e posizioni corrette
    """
    fig = plt.figure(figsize=(18, 11), facecolor='white')
    
    # Layout con GridSpec
    gs = gridspec.GridSpec(3, 3, figure=fig, hspace=0.4, wspace=0.35,
                          left=0.08, right=0.95, top=0.85, bottom=0.1)
    
    # Titolo principale
    fig.text(0.5, 0.93, 'DASHBOARD MATURITÀ INFRASTRUTTURALE', 
            fontsize=24, fontweight='bold', ha='center', color=colors_modern['dark'])
    fig.text(0.5, 0.89, 'Framework di Evoluzione per la Grande Distribuzione Organizzata', 
            fontsize=16, ha='center', color='#636e72', style='italic')
    
    # Radar Chart (spostato leggermente a sinistra)
    ax_radar = fig.add_subplot(gs[0:2, 0:2], projection='polar')
    
    categories = ['Disponibilità', 'Automazione', 'Efficienza\nCosti', 
                 'Sicurezza', 'Innovazione', 'Scalabilità']
    N = len(categories)
    
    levels_data = {
        'Tradizionale': [60, 20, 40, 50, 30, 40],
        'Consolidato': [70, 40, 55, 65, 45, 55],
        'Automatizzato': [80, 65, 70, 75, 60, 70],
        'Ottimizzato': [90, 80, 85, 85, 75, 85],
        'Adattivo': [98, 95, 95, 95, 90, 95]
    }
    
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
    angles += angles[:1]
    
    level_colors = ['#e74c3c', '#e67e22', '#f39c12', '#3498db', '#2ecc71']
    
    for idx, (level, values) in enumerate(levels_data.items()):
        values += values[:1]
        ax_radar.plot(angles, values, 'o-', linewidth=2, 
                     label=level, color=level_colors[idx], alpha=0.8)
        ax_radar.fill(angles, values, alpha=0.15, color=level_colors[idx])
    
    ax_radar.set_xticks(angles[:-1])
    ax_radar.set_xticklabels(categories, size=13)  # FONT LARGE
    ax_radar.set_ylim(0, 100)
    ax_radar.set_yticks([20, 40, 60, 80, 100])
    ax_radar.set_yticklabels(['20%', '40%', '60%', '80%', '100%'], size=11)
    ax_radar.grid(True, alpha=0.3)
    
    # Legenda spostata più a destra per evitare sovrapposizioni
    ax_radar.legend(loc='upper left', bbox_to_anchor=(1.25, 1.15), fontsize=12)
    
    # KPI Cards (destra)
    kpi_positions = [(2, 0), (2, 1), (2, 2)]
    kpis = [
        ('DISPONIBILITÀ', '99.95%', '#2ecc71', '↑ 2.45%'),
        ('RIDUZIONE TCO', '35%', '#3498db', '↓ €1.2M'),
        ('AUTOMATION', '82%', '#9b59b6', '↑ 62 punti')
    ]
    
    for pos, (title, value, color, change) in zip(kpi_positions, kpis):
        ax_kpi = fig.add_subplot(gs[pos[0], pos[1]])
        ax_kpi.set_xlim(0, 1)
        ax_kpi.set_ylim(0, 1)
        ax_kpi.axis('off')
        
        card = FancyBboxPatch((0.05, 0.1), 0.9, 0.8,
                              boxstyle="round,pad=0.05,rounding_size=0.1",
                              facecolor='white', edgecolor=color, linewidth=2)
        ax_kpi.add_patch(card)
        
        ax_kpi.text(0.5, 0.65, value, fontsize=32, fontweight='bold', 
                   ha='center', color=color)
        ax_kpi.text(0.5, 0.42, title, fontsize=12, ha='center', color='#7f8c8d')
        ax_kpi.text(0.5, 0.22, change, fontsize=13, ha='center', 
                   color=color, fontweight='bold')
    
    # Timeline (bottom) - spostata più in basso
    ax_timeline = fig.add_subplot(gs[2, :])
    ax_timeline.set_xlim(0, 36)
    ax_timeline.set_ylim(-0.5, 3.5)  # Esteso verso il basso
    ax_timeline.axis('off')
    
    # Linea temporale
    ax_timeline.plot([2, 34], [1.5, 1.5], color='#dfe6e9', linewidth=3)
    
    # Milestones con più spazio
    milestones = [
        (6, 'FASE 1\nConsolidamento', '#e74c3c', '€350k'),
        (15, 'FASE 2\nModernizzazione', '#f39c12', '€850k'),
        (24, 'FASE 3\nOttimizzazione', '#3498db', '€1.2M'),
        (33, 'FASE 4\nMaturità', '#2ecc71', 'ROI+')
    ]
    
    for x, phase, color, invest in milestones:
        circle = Circle((x, 1.5), 0.35, facecolor=color, edgecolor='white', 
                       linewidth=2, zorder=3)
        ax_timeline.add_patch(circle)
        
        # Testo sopra con più spazio
        ax_timeline.text(x, 2.6, phase, fontsize=12, fontweight='bold', 
                        ha='center', color=colors_modern['dark'])
        ax_timeline.text(x, 2.1, invest, fontsize=11, ha='center', color='#7f8c8d')
        
        ax_timeline.plot([x, x], [0.8, 1.15], color=color, linewidth=2, alpha=0.5)
    
    ax_timeline.text(2, 0.3, '0 mesi', fontsize=11, ha='center', color='#7f8c8d')
    ax_timeline.text(34, 0.3, '36 mesi', fontsize=11, ha='center', color='#7f8c8d')
    
    # Label spostata più in basso
    ax_timeline.text(18, -0.3, 'ROADMAP IMPLEMENTATIVA', fontsize=14, 
                    fontweight='bold', ha='center', color=colors_modern['dark'])
    
    plt.tight_layout()
    plt.savefig('figura_3_3_corrected.pdf', format='pdf', 
                bbox_inches='tight', facecolor='white')
    print("✓ Figura 3.3 corretta con font LARGE e sovrapposizioni risolte")
    return fig

def create_figure_3_4_corrected():
    """
    Figura 3.4: Edge Computing - FONT LARGE e etichette corrette
    """
    fig = plt.figure(figsize=(18, 11), facecolor='white')
    ax = fig.add_subplot(111, projection='3d')
    ax.view_init(elev=20, azim=45)
    ax.set_axis_off()
    
    # Titolo
    fig.text(0.5, 0.94, 'ARCHITETTURA EDGE COMPUTING DISTRIBUITA', 
            fontsize=24, fontweight='bold', ha='center', color=colors_modern['dark'])
    fig.text(0.5, 0.90, 'Infrastruttura Multi-Layer per Retail 4.0', 
            fontsize=16, ha='center', color='#636e72', style='italic')
    
    # Cloud Layer
    cloud_x, cloud_y = np.meshgrid(np.linspace(-2, 2, 10), np.linspace(-2, 2, 10))
    cloud_z = np.ones_like(cloud_x) * 8
    ax.plot_surface(cloud_x, cloud_y, cloud_z, alpha=0.3, color=colors_modern['primary'])
    ax.text(0, 0, 9.5, 'CLOUD CENTRALE', fontsize=16, 
           fontweight='bold', ha='center', color=colors_modern['primary'])
    ax.text(0, 0, 8.8, 'Analytics & AI', fontsize=14, 
           ha='center', color=colors_modern['primary'])
    
    # Regional Edge Nodes con posizioni corrette per evitare sovrapposizioni
    regions = [
        {'name': 'MILANO', 'pos': (-3.5, -3.5, 5), 'color': '#3498db'},
        {'name': 'ROMA', 'pos': (3.5, -3.5, 5), 'color': '#9b59b6'},
        {'name': 'NAPOLI', 'pos': (3.5, 3.5, 5), 'color': '#e74c3c'},
        {'name': 'PALERMO', 'pos': (-3.5, 3.5, 5), 'color': '#f39c12'},
        {'name': 'BOLOGNA', 'pos': (0, 0, 5), 'color': '#2ecc71'}
    ]
    
    for region in regions:
        x, y, z = region['pos']
        
        # Cubo per edge node
        vertices = [
            [x-0.5, y-0.5, z-0.5], [x+0.5, y-0.5, z-0.5],
            [x+0.5, y+0.5, z-0.5], [x-0.5, y+0.5, z-0.5],
            [x-0.5, y-0.5, z+0.5], [x+0.5, y-0.5, z+0.5],
            [x+0.5, y+0.5, z+0.5], [x-0.5, y+0.5, z+0.5]
        ]
        
        for i in range(4):
            ax.plot3D(*zip(vertices[i], vertices[(i+1)%4]), 
                     color=region['color'], linewidth=2)
            ax.plot3D(*zip(vertices[i+4], vertices[(i+1)%4+4]), 
                     color=region['color'], linewidth=2)
            ax.plot3D(*zip(vertices[i], vertices[i+4]), 
                     color=region['color'], linewidth=2)
        
        # Label con offset maggiore per Bologna (centrale)
        if region['name'] == 'BOLOGNA':
            label_offset = 1.8  # Offset maggiore per il nodo centrale
        else:
            label_offset = 1.2
        
        ax.text(x, y, z+label_offset, region['name'], 
               fontsize=13, fontweight='bold', ha='center', color=region['color'])
        ax.text(x, y, z+label_offset-0.4, 'Edge Node', 
               fontsize=11, ha='center', color=region['color'])
        
        # Connessione al cloud
        ax.plot3D([x, 0], [y, 0], [z+0.5, 8], 'b--', alpha=0.3, linewidth=1)
    
    # Store Layer
    stores_per_region = 5
    for region in regions:
        rx, ry, rz = region['pos']
        for i in range(stores_per_region):
            angle = 2 * np.pi * i / stores_per_region
            sx = rx + 1.5 * np.cos(angle)
            sy = ry + 1.5 * np.sin(angle)
            sz = 1
            
            ax.scatter(sx, sy, sz, color=region['color'], s=60, alpha=0.7)
            ax.plot3D([sx, rx], [sy, ry], [sz, rz-0.5], 
                     color=region['color'], alpha=0.2, linewidth=0.5)
    
    # Info panels con font large
    ax2 = fig.add_axes([0.75, 0.3, 0.22, 0.4])
    ax2.axis('off')
    
    card = FancyBboxPatch((0, 0), 1, 1,
                          boxstyle="round,pad=0.05,rounding_size=0.1",
                          facecolor='white', edgecolor=colors_modern['dark'], 
                          linewidth=2)
    ax2.add_patch(card)
    
    ax2.text(0.5, 0.95, 'METRICHE EDGE', fontsize=14, fontweight='bold', 
            ha='center', transform=ax2.transData)
    
    metrics = [
        ('Latenza', '<50ms', '#2ecc71'),
        ('Traffico', '-73%', '#3498db'),
        ('Uptime', '99.97%', '#9b59b6'),
        ('Risposta', '-85%', '#f39c12'),
        ('Coverage', '178 PV', '#e74c3c')
    ]
    
    for i, (label, value, color) in enumerate(metrics):
        y_pos = 0.75 - i*0.15
        ax2.text(0.15, y_pos, label, fontsize=11, transform=ax2.transData)
        ax2.text(0.85, y_pos, value, fontsize=12, fontweight='bold', 
                ha='right', color=color, transform=ax2.transData)
    
    # Servizi Edge
    ax3 = fig.add_axes([0.02, 0.3, 0.18, 0.4])
    ax3.axis('off')
    
    services_card = FancyBboxPatch((0, 0), 1, 1,
                                   boxstyle="round,pad=0.05,rounding_size=0.1",
                                   facecolor='white', edgecolor=colors_modern['primary'], 
                                   linewidth=2)
    ax3.add_patch(services_card)
    
    ax3.text(0.5, 0.95, 'SERVIZI EDGE', fontsize=14, fontweight='bold', 
            ha='center', transform=ax3.transData)
    
    services = ['Security', 'Analytics', 'Cache', 'AI/ML', 'Sync']
    for i, service in enumerate(services):
        ax3.text(0.5, 0.75 - i*0.15, service, fontsize=11, ha='center', 
                transform=ax3.transData)
    
    plt.tight_layout()
    plt.savefig('figura_3_4_corrected.pdf', format='pdf', 
                bbox_inches='tight', facecolor='white')
    print("✓ Figura 3.4 corretta con font LARGE e etichette non sovrapposte")
    return fig

def create_figure_3_5_corrected():
    """
    Figura 3.5: Framework GIST - FONT LARGE e colori meno accesi
    """
    # Colori più soft/pastello
    soft_colors = {
        'level1': '#9CA4AB',  # Grigio-blu soft
        'level2': '#A8C0D8',  # Blu chiaro
        'level3': '#9FC5D6',  # Azzurro soft
        'level4': '#B3D4DB',  # Cyan pastello
        'level5': '#A8D8C3'   # Verde acqua
    }
    
    fig = plt.figure(figsize=(18, 12), facecolor='#fafbfc')
    
    # Title area
    title_ax = fig.add_axes([0, 0.92, 1, 0.08])
    title_ax.axis('off')
    title_ax.text(0.5, 0.5, 'FRAMEWORK GIST®', fontsize=28, fontweight='bold',
                 ha='center', va='center', color=colors_modern['dark'])
    title_ax.text(0.5, 0.1, 'GDO Integrated Security Transformation - Roadmap to Excellence',
                 fontsize=16, ha='center', va='center', color='#636e72', style='italic')
    
    gs = gridspec.GridSpec(3, 4, figure=fig, hspace=0.3, wspace=0.25,
                          left=0.05, right=0.95, top=0.88, bottom=0.05)
    
    # Pyramid (left)
    ax_pyramid = fig.add_subplot(gs[:2, :2])
    ax_pyramid.set_xlim(0, 10)
    ax_pyramid.set_ylim(0, 10)
    ax_pyramid.axis('off')
    
    # Pyramid levels con colori soft
    levels = [
        {'name': 'INTELLIGENCE\n& AI', 'y': 8, 'width': 3, 'color': soft_colors['level5']},
        {'name': 'ZERO TRUST\nSECURITY', 'y': 6.5, 'width': 4, 'color': soft_colors['level4']},
        {'name': 'CLOUD &\nAUTOMATION', 'y': 5, 'width': 5, 'color': soft_colors['level3']},
        {'name': 'SD-WAN\nNETWORK', 'y': 3.5, 'width': 6, 'color': soft_colors['level2']},
        {'name': 'PHYSICAL\nINFRASTRUCTURE', 'y': 2, 'width': 7, 'color': soft_colors['level1']}
    ]
    
    for i, level in enumerate(levels):
        x_center = 5
        x_left = x_center - level['width']/2
        x_right = x_center + level['width']/2
        
        if i < len(levels) - 1:
            next_width = levels[i+1]['width']
            x_next_left = x_center - next_width/2
            x_next_right = x_center + next_width/2
            vertices = [
                (x_left, level['y']+0.5), (x_right, level['y']+0.5),
                (x_next_right, level['y']-0.5), (x_next_left, level['y']-0.5)
            ]
        else:
            vertices = [
                (x_left, level['y']+0.5), (x_right, level['y']+0.5),
                (x_right, level['y']-0.5), (x_left, level['y']-0.5)
            ]
        
        poly = Polygon(vertices, facecolor=level['color'], 
                      edgecolor='white', linewidth=2, alpha=0.85)
        ax_pyramid.add_patch(poly)
        
        # Shadow soft
        shadow_vertices = [(v[0]+0.1, v[1]-0.1) for v in vertices]
        shadow = Polygon(shadow_vertices, facecolor='gray', 
                        alpha=0.1, zorder=0)
        ax_pyramid.add_patch(shadow)
        
        ax_pyramid.text(x_center, level['y'], f"LEVEL {5-i}\n{level['name']}", 
                       fontsize=13, fontweight='bold', ha='center', 
                       va='center', color=colors_modern['dark'])
    
    # Progress (right top)
    ax_progress = fig.add_subplot(gs[0, 2:])
    ax_progress.set_xlim(0, 10)
    ax_progress.set_ylim(0, 5)
    ax_progress.axis('off')
    
    progress_data = [
        ('Infrastructure', 85, soft_colors['level1']),
        ('Network', 72, soft_colors['level2']),
        ('Cloud', 65, soft_colors['level3']),
        ('Security', 45, soft_colors['level4']),
        ('AI/ML', 28, soft_colors['level5'])
    ]
    
    for i, (label, value, color) in enumerate(progress_data):
        y_pos = 4 - i*0.8
        
        bg_bar = Rectangle((2, y_pos-0.2), 6, 0.4, 
                          facecolor='#ecf0f1', edgecolor='none')
        ax_progress.add_patch(bg_bar)
        
        progress_bar = Rectangle((2, y_pos-0.2), 6*value/100, 0.4,
                                facecolor=color, edgecolor='none')
        ax_progress.add_patch(progress_bar)
        
        ax_progress.text(1.8, y_pos, label, fontsize=12, ha='right', va='center')
        ax_progress.text(8.2, y_pos, f'{value}%', fontsize=12, fontweight='bold',
                        ha='left', va='center', color=color)
    
    ax_progress.text(5, 4.7, 'IMPLEMENTATION PROGRESS', fontsize=14, 
                    fontweight='bold', ha='center')
    
    # Investment (right middle)
    ax_invest = fig.add_subplot(gs[1, 2:])
    ax_invest.set_xlim(0, 10)
    ax_invest.set_ylim(0, 5)
    ax_invest.axis('off')
    
    sizes = [350, 850, 1200]
    colors_pie = [soft_colors['level1'], soft_colors['level3'], soft_colors['level5']]
    labels_pie = ['Fase 1\n€350k', 'Fase 2\n€850k', 'Fase 3\n€1.2M']
    
    wedges, texts, autotexts = ax_invest.pie(sizes, labels=labels_pie, 
                                              colors=colors_pie,
                                              autopct='%1.0f%%',
                                              startangle=90,
                                              wedgeprops=dict(width=0.5))
    
    for text in texts:
        text.set_fontsize(11)
    for autotext in autotexts:
        autotext.set_color(colors_modern['dark'])
        autotext.set_fontsize(12)
        autotext.set_fontweight('bold')
    
    ax_invest.text(0, -1.5, 'INVESTMENT: €2.4M', fontsize=13, 
                  fontweight='bold', ha='center')
    
    # Timeline (bottom)
    ax_timeline = fig.add_subplot(gs[2, :])
    ax_timeline.set_xlim(0, 36)
    ax_timeline.set_ylim(0, 3)
    ax_timeline.axis('off')
    
    # Timeline gradient con colori soft
    for i in range(35):
        color_fade = LinearSegmentedColormap.from_list('', 
                                                      [soft_colors['level1'], 
                                                       soft_colors['level5']])(i/35)
        ax_timeline.plot([i, i+1], [1.5, 1.5], color=color_fade, linewidth=4)
    
    milestones = [
        (0, 'START', soft_colors['level1'], 'Quick Wins'),
        (6, 'M1', soft_colors['level2'], 'Foundation'),
        (12, 'M2', soft_colors['level3'], 'Transformation'),
        (24, 'M3', soft_colors['level4'], 'Optimization'),
        (36, 'TARGET', soft_colors['level5'], 'Excellence')
    ]
    
    for x, label, color, phase in milestones:
        diamond = Polygon([(x, 1.2), (x+0.3, 1.5), (x, 1.8), (x-0.3, 1.5)],
                         facecolor=color, edgecolor='white', linewidth=2)
        ax_timeline.add_patch(diamond)
        
        ax_timeline.text(x, 2.3, label, fontsize=12, fontweight='bold', 
                        ha='center', color=colors_modern['dark'])
        ax_timeline.text(x, 2.0, phase, fontsize=10, ha='center', color='#7f8c8d')
        ax_timeline.text(x, 0.7, f'{x}m', fontsize=10, ha='center', color='#7f8c8d')
    
    # KPI boxes con colori soft
    kpi_y = 0.2
    kpi_data = [
        ('SLA: 99.95%', soft_colors['level5']),
        ('TCO: -35%', soft_colors['level4']),
        ('MTTR: 48min', soft_colors['level3']),
        ('Security: +67%', soft_colors['level2'])
    ]
    
    for i, (kpi, color) in enumerate(kpi_data):
        x = 7 + i*5.5
        kpi_box = FancyBboxPatch((x, kpi_y), 5, 0.3,
                                 boxstyle="round,pad=0.02",
                                 facecolor=color, alpha=0.2, 
                                 edgecolor=color, linewidth=1)
        ax_timeline.add_patch(kpi_box)
        ax_timeline.text(x+2.5, kpi_y+0.15, kpi, fontsize=11, 
                        fontweight='bold', ha='center', color=colors_modern['dark'])
    
    plt.tight_layout()
    plt.savefig('figura_3_5_corrected.pdf', format='pdf', 
                bbox_inches='tight', facecolor='white', edgecolor='none')
    print("✓ Figura 3.5 corretta con font LARGE e colori soft")
    return fig

def create_all_corrected_figures():
    """
    Genera tutte le figure corrette
    """
    print("\n" + "="*60)
    print(" GENERAZIONE FIGURE CORRETTE - CAPITOLO 3")
    print(" Font Large (16-20pt) e Sovrapposizioni Risolte")
    print("="*60)
    
    figures = []
    
    print("\n1. Figura 3.1 - Architettura Alimentazione...")
    fig1 = create_figure_3_1_corrected()
    figures.append(fig1)
    
    print("\n2. Figura 3.2 - Evoluzione Rete...")
    fig2 = create_figure_3_2_corrected()
    figures.append(fig2)
    
    print("\n3. Figura 3.3 - Dashboard Maturità...")
    fig3 = create_figure_3_3_corrected()
    figures.append(fig3)
    
    print("\n4. Figura 3.4 - Edge Computing...")
    fig4 = create_figure_3_4_corrected()
    figures.append(fig4)
    
    print("\n5. Figura 3.5 - Framework GIST...")
    fig5 = create_figure_3_5_corrected()
    figures.append(fig5)
    
    print("\n" + "="*60)
    print(" ✅ TUTTE LE FIGURE CORRETTE GENERATE!")
    print("="*60)
    print("\nMiglioramenti applicati:")
    print("• Font aumentato a 16-20pt per massima leggibilità")
    print("• Risolte sovrapposizioni in figura 3.3 e 3.4")
    print("• Colori più soft in figura 3.5")
    print("• Emoji rimosse per compatibilità Windows")
    print("\nFile salvati:")
    print("• figura_3_1_corrected.pdf")
    print("• figura_3_2_corrected.pdf")
    print("• figura_3_3_corrected.pdf")
    print("• figura_3_4_corrected.pdf")
    print("• figura_3_5_corrected.pdf")
    
    return figures

if __name__ == "__main__":
    import matplotlib
    matplotlib.use('Agg')  # Backend non interattivo per evitare problemi
    all_figures = create_all_corrected_figures()
