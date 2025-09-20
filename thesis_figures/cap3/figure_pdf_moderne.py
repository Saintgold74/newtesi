#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Figure PDF Moderne e Accattivanti per Capitolo 3
Design contemporaneo con gradienti, ombre e icone
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle, Ellipse, Polygon, Wedge, Arc
from matplotlib.patches import PathPatch, FancyArrow
from matplotlib.path import Path
import matplotlib.patheffects as path_effects
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
import datetime
import warnings
warnings.filterwarnings('ignore')

# Configurazione globale per font moderni
plt.rcParams['font.size'] = 16
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.titlesize'] = 24
plt.rcParams['axes.labelsize'] = 18
plt.rcParams['xtick.labelsize'] = 16
plt.rcParams['ytick.labelsize'] = 16
plt.rcParams['legend.fontsize'] = 16
plt.rcParams['figure.titlesize'] = 26
plt.rcParams['figure.dpi'] = 100

# Palette colori moderna con gradienti
colors_modern = {
    'blue1': '#0EA5E9',      # Sky blue
    'blue2': '#0284C7',      # Blue  
    'blue3': '#075985',      # Dark blue
    'green1': '#34D399',     # Emerald light
    'green2': '#10B981',     # Emerald
    'green3': '#047857',     # Emerald dark
    'purple1': '#A78BFA',    # Purple light
    'purple2': '#8B5CF6',    # Purple
    'purple3': '#6D28D9',    # Purple dark
    'orange1': '#FCD34D',    # Amber light
    'orange2': '#F59E0B',    # Amber
    'orange3': '#D97706',    # Amber dark
    'red1': '#F87171',       # Red light
    'red2': '#EF4444',       # Red
    'red3': '#DC2626',       # Red dark
    'gray1': '#F3F4F6',      # Gray light
    'gray2': '#9CA3AF',      # Gray
    'gray3': '#374151',      # Gray dark
}

def add_gradient(ax, x, y, width, height, color1, color2, alpha=1.0):
    """Aggiunge un rettangolo con gradiente"""
    n = 100
    for i in range(n):
        color = plt.cm.colors.to_rgb(color1) if i < n/2 else plt.cm.colors.to_rgb(color2)
        rect = Rectangle((x, y + i*height/n), width, height/n,
                        facecolor=color, alpha=alpha*(1-i/(2*n)), 
                        edgecolor='none')
        ax.add_patch(rect)

def add_shadow(patch, ax, offset=(0.1, -0.1), alpha=0.3):
    """Aggiunge ombra a un elemento"""
    shadow = patches.Shadow(patch, offset[0], offset[1])
    shadow.set_alpha(alpha)
    shadow.set_facecolor('gray')
    ax.add_patch(shadow)

def draw_modern_box(ax, x, y, width, height, color, label, sublabel=None, icon=None):
    """Disegna un box moderno con gradiente e ombra"""
    # Ombra
    shadow = FancyBboxPatch((x+0.05, y-0.05), width, height,
                            boxstyle="round,pad=0.02",
                            facecolor='gray', alpha=0.2,
                            edgecolor='none', zorder=1)
    ax.add_patch(shadow)
    
    # Box principale con gradiente simulato
    main_box = FancyBboxPatch((x, y), width, height,
                              boxstyle="round,pad=0.02",
                              facecolor=color, alpha=0.9,
                              edgecolor='white', linewidth=3, zorder=2)
    ax.add_patch(main_box)
    
    # Highlight superiore
    highlight = FancyBboxPatch((x+0.05, y+height*0.7), width*0.9, height*0.25,
                               boxstyle="round,pad=0.01",
                               facecolor='white', alpha=0.2,
                               edgecolor='none', zorder=3)
    ax.add_patch(highlight)
    
    # Testo con effetto
    text = ax.text(x + width/2, y + height*0.6, label,
                  ha='center', va='center', fontsize=18,
                  fontweight='bold', color='white', zorder=4)
    text.set_path_effects([path_effects.withStroke(linewidth=3, foreground='black', alpha=0.3)])
    
    if sublabel:
        subtext = ax.text(x + width/2, y + height*0.3, sublabel,
                         ha='center', va='center', fontsize=14,
                         color='white', alpha=0.9, zorder=4)
    
    return main_box

def draw_cloud_shape(ax, x, y, width, height, color, label):
    """Disegna una forma cloud moderna"""
    # Crea forma cloud con cerchi sovrapposti
    circles = [
        Circle((x - width*0.2, y), height*0.35),
        Circle((x + width*0.2, y), height*0.35),
        Circle((x, y + height*0.2), height*0.3),
        Circle((x - width*0.1, y - height*0.15), height*0.25),
        Circle((x + width*0.1, y - height*0.15), height*0.25),
    ]
    
    # Ombra
    for circle in circles:
        shadow = Circle((circle.center[0]+0.05, circle.center[1]-0.05), 
                       circle.radius, facecolor='gray', alpha=0.2, edgecolor='none')
        ax.add_patch(shadow)
    
    # Cloud principale
    for circle in circles:
        c = Circle(circle.center, circle.radius, facecolor=color, 
                  edgecolor='white', linewidth=2, alpha=0.95)
        ax.add_patch(c)
    
    # Testo
    text = ax.text(x, y, label, ha='center', va='center',
                  fontsize=16, fontweight='bold', color='white')
    text.set_path_effects([path_effects.withStroke(linewidth=3, foreground='black', alpha=0.3)])

def draw_server_rack(ax, x, y, scale=1.0, color='blue'):
    """Disegna un server rack stilizzato"""
    # Struttura principale
    rack = FancyBboxPatch((x-0.3*scale, y-0.5*scale), 0.6*scale, 1*scale,
                          boxstyle="round,pad=0.02",
                          facecolor=colors_modern[f'{color}3'],
                          edgecolor='white', linewidth=2)
    ax.add_patch(rack)
    
    # Server slots
    for i in range(4):
        slot_y = y - 0.4*scale + i*0.2*scale
        slot = Rectangle((x-0.25*scale, slot_y), 0.5*scale, 0.15*scale,
                        facecolor=colors_modern[f'{color}2'], 
                        edgecolor='white', linewidth=1)
        ax.add_patch(slot)
        
        # LED indicators
        for j in range(3):
            led = Circle((x-0.2*scale + j*0.08*scale, slot_y + 0.075*scale), 
                        0.02*scale, facecolor='#10FF10', edgecolor='none')
            ax.add_patch(led)

def draw_network_icon(ax, x, y, scale=1.0):
    """Disegna icona di rete moderna"""
    # Centro
    center = Circle((x, y), 0.1*scale, facecolor=colors_modern['blue2'], 
                   edgecolor='white', linewidth=2)
    ax.add_patch(center)
    
    # Nodi
    angles = np.linspace(0, 2*np.pi, 6, endpoint=False)
    for angle in angles:
        node_x = x + 0.3*scale * np.cos(angle)
        node_y = y + 0.3*scale * np.sin(angle)
        
        # Connessione
        ax.plot([x, node_x], [y, node_y], color=colors_modern['blue1'], 
               linewidth=2, alpha=0.6, zorder=1)
        
        # Nodo
        node = Circle((node_x, node_y), 0.05*scale, 
                     facecolor=colors_modern['blue3'], 
                     edgecolor='white', linewidth=1, zorder=2)
        ax.add_patch(node)

def draw_shield_icon(ax, x, y, scale=1.0, color='green'):
    """Disegna icona scudo per sicurezza"""
    # Forma scudo
    verts = [
        (x - 0.2*scale, y + 0.3*scale),
        (x - 0.2*scale, y),
        (x, y - 0.3*scale),
        (x + 0.2*scale, y),
        (x + 0.2*scale, y + 0.3*scale),
    ]
    
    shield = Polygon(verts, facecolor=colors_modern[f'{color}2'], 
                    edgecolor='white', linewidth=2)
    ax.add_patch(shield)
    
    # Check mark
    check_verts = [
        (x - 0.1*scale, y + 0.05*scale),
        (x - 0.02*scale, y - 0.05*scale),
        (x + 0.15*scale, y + 0.2*scale)
    ]
    ax.plot([v[0] for v in check_verts], [v[1] for v in check_verts], 
           color='white', linewidth=3)

# ========================================================================
# FIGURA 1: Architettura Alimentazione - Design Moderno
# ========================================================================
def create_power_architecture_modern():
    """Architettura alimentazione con design moderno"""
    
    fig = plt.figure(figsize=(16, 10), facecolor='#F8F9FA')
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Sfondo con gradiente
    gradient = Rectangle((0, 0), 16, 10, facecolor=colors_modern['gray1'], alpha=0.3)
    ax.add_patch(gradient)
    
    # Titolo con effetto
    title = ax.text(8, 9.3, 'ARCHITETTURA ALIMENTAZIONE 2N', 
                   fontsize=26, fontweight='bold', ha='center',
                   color=colors_modern['blue3'])
    title.set_path_effects([path_effects.withStroke(linewidth=4, foreground='white')])
    
    subtitle = ax.text(8, 8.8, 'Ridondanza Completa per Massima Affidabilità', 
                      fontsize=16, ha='center', color=colors_modern['gray3'], style='italic')
    
    # Rete Elettrica (con icona fulmine)
    draw_cloud_shape(ax, 8, 7, 3, 1.2, colors_modern['gray3'], 'RETE ELETTRICA')
    
    # Fulmine decorativo
    lightning = ax.text(8, 7, '⚡', fontsize=40, ha='center', va='center', 
                       color='yellow', zorder=10)
    
    # UPS Sistema A
    ups_a = draw_modern_box(ax, 2, 3.5, 3.5, 2.5, colors_modern['blue2'], 
                           'UPS SISTEMA A', '500 kW N+1')
    draw_server_rack(ax, 3.5, 4.5, scale=0.8, color='blue')
    
    # UPS Sistema B  
    ups_b = draw_modern_box(ax, 10.5, 3.5, 3.5, 2.5, colors_modern['green2'],
                           'UPS SISTEMA B', '500 kW N+1')
    draw_server_rack(ax, 12, 4.5, scale=0.8, color='green')
    
    # Data Center
    dc = draw_modern_box(ax, 6, 0.5, 4, 2, colors_modern['purple2'],
                        'DATA CENTER', 'Carichi Critici')
    
    # Connessioni animate con curve
    # Dalla rete agli UPS
    arrow1 = patches.FancyArrowPatch((8, 6.5), (3.8, 6),
                                     connectionstyle="arc3,rad=-.3",
                                     arrowstyle='->,head_width=0.3,head_length=0.2',
                                     linewidth=3, color=colors_modern['blue3'], alpha=0.8)
    ax.add_patch(arrow1)
    
    arrow2 = patches.FancyArrowPatch((8, 6.5), (12.2, 6),
                                     connectionstyle="arc3,rad=.3",
                                     arrowstyle='->,head_width=0.3,head_length=0.2',
                                     linewidth=3, color=colors_modern['green3'], alpha=0.8)
    ax.add_patch(arrow2)
    
    # Dagli UPS al DC
    arrow3 = patches.FancyArrowPatch((3.8, 3.5), (7, 2.5),
                                     connectionstyle="arc3,rad=-.2",
                                     arrowstyle='->,head_width=0.3,head_length=0.2',
                                     linewidth=3, color=colors_modern['blue2'], alpha=0.8)
    ax.add_patch(arrow3)
    
    arrow4 = patches.FancyArrowPatch((12.2, 3.5), (9, 2.5),
                                     connectionstyle="arc3,rad=.2",
                                     arrowstyle='->,head_width=0.3,head_length=0.2',
                                     linewidth=3, color=colors_modern['green2'], alpha=0.8)
    ax.add_patch(arrow4)
    
    # Dashboard KPI moderno
    dashboard = FancyBboxPatch((0.5, 0.5), 4.5, 2.5,
                               boxstyle="round,pad=0.05",
                               facecolor='white', alpha=0.95,
                               edgecolor=colors_modern['blue2'], linewidth=2)
    ax.add_patch(dashboard)
    
    ax.text(2.75, 2.7, '📊 DASHBOARD KPI', fontsize=16, fontweight='bold',
           ha='center', color=colors_modern['blue3'])
    
    # KPI con icone
    kpis = [
        ('⚡ Disponibilità:', '99.94%', colors_modern['green2']),
        ('⏱️ MTBF:', '87,600h', colors_modern['blue2']),
        ('🔋 Autonomia:', '15 min', colors_modern['orange2']),
        ('💰 ROI:', '12 mesi', colors_modern['purple2'])
    ]
    
    for i, (label, value, color) in enumerate(kpis):
        y_pos = 2.2 - i * 0.4
        ax.text(1.2, y_pos, label, fontsize=13, ha='left')
        ax.text(4.3, y_pos, value, fontsize=14, fontweight='bold', 
               ha='right', color=color)
    
    # Badge di certificazione
    cert = Circle((14.5, 1.5), 0.8, facecolor=colors_modern['orange1'],
                 edgecolor=colors_modern['orange3'], linewidth=3)
    ax.add_patch(cert)
    ax.text(14.5, 1.5, 'TIER\nIII+', fontsize=14, fontweight='bold',
           ha='center', va='center', color=colors_modern['orange3'])
    
    plt.tight_layout()
    return fig

# ========================================================================
# FIGURA 2: Network Evolution - Design Moderno
# ========================================================================
def create_network_evolution_modern():
    """Confronto reti con design moderno"""
    
    fig = plt.figure(figsize=(16, 10), facecolor='#F8F9FA')
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Titolo principale
    title = ax.text(8, 9.3, 'EVOLUZIONE DELLE ARCHITETTURE DI RETE',
                   fontsize=26, fontweight='bold', ha='center',
                   color=colors_modern['blue3'])
    title.set_path_effects([path_effects.withStroke(linewidth=4, foreground='white')])
    
    # Divider verticale
    divider = Rectangle((7.9, 0.5), 0.2, 8, facecolor=colors_modern['gray2'], alpha=0.3)
    ax.add_patch(divider)
    
    # --- LATO SINISTRO: MPLS Legacy ---
    ax.text(4, 8.3, 'ARCHITETTURA MPLS', fontsize=20, fontweight='bold',
           ha='center', color=colors_modern['red3'])
    ax.text(4, 7.8, 'Legacy Infrastructure', fontsize=14, ha='center',
           style='italic', color=colors_modern['gray3'])
    
    # Central router MPLS
    mpls_center = Circle((4, 6), 0.8, facecolor=colors_modern['red2'],
                        edgecolor='white', linewidth=3)
    ax.add_patch(mpls_center)
    ax.text(4, 6, 'MPLS\nCORE', fontsize=12, fontweight='bold',
           ha='center', va='center', color='white')
    
    # Punti vendita MPLS
    for i, angle in enumerate(np.linspace(0, 2*np.pi, 6, endpoint=False)):
        x = 4 + 2.5 * np.cos(angle)
        y = 6 + 2.5 * np.sin(angle)
        
        # Linea dedicata costosa
        ax.plot([4, x], [6, y], color=colors_modern['red1'], 
               linewidth=2, linestyle='-', alpha=0.7)
        
        # Store
        store = Circle((x, y), 0.3, facecolor=colors_modern['gray2'],
                      edgecolor=colors_modern['red3'], linewidth=2)
        ax.add_patch(store)
        ax.text(x, y, f'PV', fontsize=10, fontweight='bold',
               ha='center', va='center', color='white')
    
    # Problems box
    problems = FancyBboxPatch((1, 1.5), 6, 1.5,
                              boxstyle="round,pad=0.05",
                              facecolor=colors_modern['red1'], alpha=0.2,
                              edgecolor=colors_modern['red3'], linewidth=2)
    ax.add_patch(problems)
    
    ax.text(4, 2.5, '⚠️ LIMITI MPLS', fontsize=14, fontweight='bold',
           ha='center', color=colors_modern['red3'])
    
    issues = ['❌ Costi: €450/Mbps', '❌ Setup: 45 giorni', '❌ Rigidità']
    for i, issue in enumerate(issues):
        ax.text(4, 2 - i*0.3, issue, fontsize=11, ha='center',
               color=colors_modern['red3'])
    
    # --- LATO DESTRO: SD-WAN Modern ---
    ax.text(12, 8.3, 'ARCHITETTURA SD-WAN', fontsize=20, fontweight='bold',
           ha='center', color=colors_modern['green3'])
    ax.text(12, 7.8, 'Cloud-Native Network', fontsize=14, ha='center',
           style='italic', color=colors_modern['gray3'])
    
    # Cloud controller
    draw_cloud_shape(ax, 12, 6.5, 2.5, 1, colors_modern['blue2'], 'SD-WAN')
    
    # Edge nodes con mesh
    edge_positions = [(10, 5), (12, 4.5), (14, 5)]
    for i, (x, y) in enumerate(edge_positions):
        # Edge node
        edge = FancyBboxPatch((x-0.4, y-0.3), 0.8, 0.6,
                              boxstyle="round,pad=0.02",
                              facecolor=colors_modern['green2'],
                              edgecolor='white', linewidth=2)
        ax.add_patch(edge)
        ax.text(x, y, f'E{i+1}', fontsize=11, fontweight='bold',
               ha='center', va='center', color='white')
        
        # Cloud connection
        ax.plot([x, 12], [y+0.3, 5.8], '--', color=colors_modern['blue1'],
               linewidth=2, alpha=0.6)
        
        # Mesh connections
        for x2, y2 in edge_positions[i+1:]:
            ax.plot([x, x2], [y, y2], ':', color=colors_modern['green1'],
                   linewidth=1.5, alpha=0.4)
    
    # Stores SD-WAN
    for i in range(4):
        x = 9.5 + i * 1.5
        y = 2.5
        
        # Multi-path connections
        for ex, ey in edge_positions:
            ax.plot([x, ex], [y, ey-0.3], color=colors_modern['green1'],
                   linewidth=1, alpha=0.3)
        
        store = FancyBboxPatch((x-0.25, y-0.25), 0.5, 0.5,
                              boxstyle="round,pad=0.02",
                              facecolor=colors_modern['green2'],
                              edgecolor='white', linewidth=2)
        ax.add_patch(store)
        ax.text(x, y, f'PV', fontsize=10, fontweight='bold',
               ha='center', va='center', color='white')
    
    # Benefits box
    benefits = FancyBboxPatch((9, 0.5), 6, 1.5,
                              boxstyle="round,pad=0.05",
                              facecolor=colors_modern['green1'], alpha=0.2,
                              edgecolor=colors_modern['green3'], linewidth=2)
    ax.add_patch(benefits)
    
    ax.text(12, 1.5, '✅ VANTAGGI SD-WAN', fontsize=14, fontweight='bold',
           ha='center', color=colors_modern['green3'])
    
    advantages = ['✓ Costi: -70%', '✓ Setup: 5 giorni', '✓ Agilità']
    for i, adv in enumerate(advantages):
        ax.text(12, 1 - i*0.3, adv, fontsize=11, ha='center',
               color=colors_modern['green3'])
    
    plt.tight_layout()
    return fig

# ========================================================================
# FIGURA 3: Cloud Architecture - Design Moderno
# ========================================================================
def create_cloud_architecture_modern():
    """Cloud ibrido con design moderno"""
    
    fig = plt.figure(figsize=(16, 10), facecolor='#F8F9FA')
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Titolo
    title = ax.text(8, 9.3, 'ARCHITETTURA MULTI-CLOUD IBRIDA',
                   fontsize=26, fontweight='bold', ha='center',
                   color=colors_modern['purple3'])
    title.set_path_effects([path_effects.withStroke(linewidth=4, foreground='white')])
    
    # Security Shield al centro top
    draw_shield_icon(ax, 8, 8, scale=1.5, color='red')
    ax.text(8, 7.2, 'ZERO TRUST SECURITY', fontsize=16, fontweight='bold',
           ha='center', color=colors_modern['red3'])
    
    # On-Premise (sinistra)
    on_prem_box = FancyBboxPatch((1, 3), 4, 3,
                                 boxstyle="round,pad=0.05",
                                 facecolor=colors_modern['orange1'], alpha=0.3,
                                 edgecolor=colors_modern['orange3'], linewidth=3)
    ax.add_patch(on_prem_box)
    
    server_icon = draw_modern_box(ax, 1.5, 4.8, 3, 1, colors_modern['orange2'],
                                  '🏢 ON-PREMISE', '30%')
    
    # Private Cloud (centro)
    private_box = FancyBboxPatch((6, 3), 4, 3,
                                 boxstyle="round,pad=0.05",
                                 facecolor=colors_modern['blue1'], alpha=0.3,
                                 edgecolor=colors_modern['blue3'], linewidth=3)
    ax.add_patch(private_box)
    
    private_icon = draw_modern_box(ax, 6.5, 4.8, 3, 1, colors_modern['blue2'],
                                   '🔒 PRIVATE CLOUD', '35%')
    
    # Public Cloud (destra)
    public_box = FancyBboxPatch((11, 3), 4, 3,
                                boxstyle="round,pad=0.05",
                                facecolor=colors_modern['green1'], alpha=0.3,
                                edgecolor=colors_modern['green3'], linewidth=3)
    ax.add_patch(public_box)
    
    public_icon = draw_modern_box(ax, 11.5, 4.8, 3, 1, colors_modern['green2'],
                                  '☁️ PUBLIC CLOUD', '35%')
    
    # Workload icons
    workloads = [
        (3, 3.8, 'POS', '💳'),
        (3, 3.3, 'Storage', '💾'),
        (8, 3.8, 'ERP', '📊'),
        (8, 3.3, 'Finance', '💰'),
        (13, 3.8, 'Web', '🌐'),
        (13, 3.3, 'Analytics', '📈')
    ]
    
    for x, y, label, icon in workloads:
        box = FancyBboxPatch((x-0.6, y-0.2), 1.2, 0.4,
                             boxstyle="round,pad=0.02",
                             facecolor='white', alpha=0.8,
                             edgecolor=colors_modern['gray2'], linewidth=1)
        ax.add_patch(box)
        ax.text(x-0.3, y, icon, fontsize=16, ha='center', va='center')
        ax.text(x+0.2, y, label, fontsize=11, ha='center', va='center')
    
    # Kubernetes orchestration layer
    k8s_layer = FancyBboxPatch((2, 2), 12, 0.8,
                               boxstyle="round,pad=0.02",
                               facecolor=colors_modern['purple2'], alpha=0.7,
                               edgecolor='white', linewidth=2)
    ax.add_patch(k8s_layer)
    ax.text(8, 2.4, '⚙️ KUBERNETES ORCHESTRATION', fontsize=14,
           fontweight='bold', ha='center', color='white')
    
    # Connessioni curve
    connections = [
        ((3, 3.5), (8, 2.8)),
        ((8, 3.5), (8, 2.8)),
        ((13, 3.5), (8, 2.8))
    ]
    
    for start, end in connections:
        arrow = patches.FancyArrowPatch(start, end,
                                       connectionstyle="arc3,rad=.3",
                                       arrowstyle='->,head_width=0.2',
                                       linewidth=2, color=colors_modern['purple1'],
                                       alpha=0.6)
        ax.add_patch(arrow)
    
    # Metrics dashboard in basso
    metrics = FancyBboxPatch((4, 0.5), 8, 1.2,
                             boxstyle="round,pad=0.05",
                             facecolor='white', alpha=0.95,
                             edgecolor=colors_modern['purple2'], linewidth=2)
    ax.add_patch(metrics)
    
    metric_values = [
        ('TCO', '-31%', colors_modern['green2']),
        ('Time-to-Market', '-65%', colors_modern['blue2']),
        ('Uptime', '99.95%', colors_modern['orange2'])
    ]
    
    for i, (label, value, color) in enumerate(metric_values):
        x = 5.5 + i * 2.5
        ax.text(x, 1.3, label, fontsize=11, ha='center', color=colors_modern['gray3'])
        ax.text(x, 0.9, value, fontsize=16, fontweight='bold', ha='center', color=color)
    
    plt.tight_layout()
    return fig

# ========================================================================
# FIGURA 4: Edge Computing - Design Moderno
# ========================================================================
def create_edge_architecture_modern():
    """Edge computing con design moderno"""
    
    fig = plt.figure(figsize=(16, 10), facecolor='#F8F9FA')
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Titolo
    title = ax.text(8, 9.3, 'EDGE COMPUTING DISTRIBUITO',
                   fontsize=26, fontweight='bold', ha='center',
                   color=colors_modern['green3'])
    title.set_path_effects([path_effects.withStroke(linewidth=4, foreground='white')])
    
    # Cloud centrale con effetto glow
    for i in range(3, 0, -1):
        glow = Ellipse((8, 7), 3+i*0.3, 1.5+i*0.15,
                      facecolor=colors_modern['blue1'], alpha=0.1*i,
                      edgecolor='none')
        ax.add_patch(glow)
    
    cloud = Ellipse((8, 7), 3, 1.5,
                   facecolor=colors_modern['blue2'],
                   edgecolor='white', linewidth=3)
    ax.add_patch(cloud)
    ax.text(8, 7, '☁️ CLOUD CORE\nAI & Analytics', fontsize=14,
           fontweight='bold', ha='center', va='center', color='white')
    
    # Edge nodes con design moderno
    regions = [
        (3, 4.5, 'NORD', colors_modern['green2'], '🏔️'),
        (7, 4, 'CENTRO', colors_modern['blue2'], '🏛️'),
        (11, 4, 'SUD', colors_modern['orange2'], '🌊'),
        (14, 4.5, 'ISOLE', colors_modern['purple2'], '🏝️')
    ]
    
    for x, y, region, color, icon in regions:
        # Glow effect
        glow = Circle((x, y), 0.7, facecolor=color, alpha=0.2, edgecolor='none')
        ax.add_patch(glow)
        
        # Edge node
        edge = Circle((x, y), 0.5, facecolor=color, edgecolor='white', linewidth=3)
        ax.add_patch(edge)
        ax.text(x, y+0.1, icon, fontsize=20, ha='center', va='center')
        ax.text(x, y-0.2, 'EDGE', fontsize=10, fontweight='bold',
               ha='center', va='center', color='white')
        ax.text(x, y-0.9, region, fontsize=12, fontweight='bold',
               ha='center', color=color)
        
        # Connection to cloud
        connection = patches.FancyArrowPatch((x, y+0.5), (8, 6.2),
                                            connectionstyle="arc3,rad=.2",
                                            arrowstyle='-',
                                            linewidth=2, color=color, alpha=0.4)
        ax.add_patch(connection)
        
        # Edge capabilities
        caps = FancyBboxPatch((x-0.8, y-2), 1.6, 0.5,
                              boxstyle="round,pad=0.02",
                              facecolor='white', alpha=0.8,
                              edgecolor=color, linewidth=1)
        ax.add_patch(caps)
        ax.text(x, y-1.75, 'Cache•AI•5G', fontsize=9, ha='center', color=color)
        
        # PV connections
        for i in range(3):
            pv_angle = -np.pi/3 + i*np.pi/6
            pv_x = x + 1.2 * np.cos(pv_angle)
            pv_y = y-0.5 + 1.2 * np.sin(pv_angle)
            
            # Connection line
            ax.plot([x, pv_x], [y, pv_y], color=color, linewidth=1, 
                   alpha=0.3, linestyle='--')
            
            # PV point
            pv = Circle((pv_x, pv_y), 0.15, facecolor=color, alpha=0.6,
                       edgecolor='white', linewidth=1)
            ax.add_patch(pv)
    
    # Real-time metrics panel
    panel = FancyBboxPatch((0.5, 0.5), 4, 2.5,
                           boxstyle="round,pad=0.05",
                           facecolor='white', alpha=0.95,
                           edgecolor=colors_modern['green2'], linewidth=2)
    ax.add_patch(panel)
    
    ax.text(2.5, 2.7, '📊 REAL-TIME METRICS', fontsize=14, fontweight='bold',
           ha='center', color=colors_modern['green3'])
    
    # Animated metrics style
    metrics = [
        ('Latenza', '<50ms', '🚀'),
        ('Traffico', '-73%', '📉'),
        ('Uptime', '99.97%', '✅')
    ]
    
    for i, (label, value, icon) in enumerate(metrics):
        y_pos = 2.2 - i * 0.5
        
        # Progress bar background
        bar_bg = Rectangle((1.2, y_pos-0.1), 2.5, 0.2,
                          facecolor=colors_modern['gray1'], edgecolor='none')
        ax.add_patch(bar_bg)
        
        # Progress bar fill
        fill_width = [2.3, 1.8, 2.4][i]
        bar_fill = Rectangle((1.2, y_pos-0.1), fill_width, 0.2,
                            facecolor=colors_modern['green2'], edgecolor='none')
        ax.add_patch(bar_fill)
        
        ax.text(1, y_pos, icon, fontsize=14, ha='center', va='center')
        ax.text(2.5, y_pos+0.25, label, fontsize=11, ha='center')
        ax.text(3.9, y_pos, value, fontsize=11, fontweight='bold',
               ha='right', color=colors_modern['green3'])
    
    # Network mesh visualization
    ax.text(12, 1.5, 'NETWORK TOPOLOGY', fontsize=12, fontweight='bold',
           ha='center', color=colors_modern['blue3'])
    draw_network_icon(ax, 12, 0.8, scale=1.5)
    
    plt.tight_layout()
    return fig

# ========================================================================
# FIGURA 5: Framework GIST - Design Moderno
# ========================================================================
def create_gist_framework_modern():
    """Framework GIST con design moderno"""
    
    fig = plt.figure(figsize=(16, 10), facecolor='#F8F9FA')
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Titolo
    title = ax.text(8, 9.3, 'FRAMEWORK GIST - TRANSFORMATION ROADMAP',
                   fontsize=26, fontweight='bold', ha='center',
                   color=colors_modern['purple3'])
    title.set_path_effects([path_effects.withStroke(linewidth=4, foreground='white')])
    
    # Piramide 3D effect
    levels = [
        (1.5, 10, colors_modern['red2'], 'INFRASTRUTTURA', '€350k', '⚙️'),
        (2.5, 8, colors_modern['orange2'], 'NETWORKING', '€500k', '🌐'),
        (3.5, 6, colors_modern['blue2'], 'CLOUD', '€850k', '☁️'),
        (4.5, 4, colors_modern['green2'], 'SECURITY', '€750k', '🔐'),
        (5.5, 2, colors_modern['purple2'], 'AI & ML', '€450k', '🤖')
    ]
    
    for i, (y, width, color, label, cost, icon) in enumerate(levels):
        x_center = 5
        
        # Shadow
        shadow = Polygon([
            (x_center - width/2 + 0.1, y - 0.1),
            (x_center + width/2 + 0.1, y - 0.1),
            (x_center + (width-1)/2 + 0.1, y + 0.9),
            (x_center - (width-1)/2 + 0.1, y + 0.9)
        ], facecolor='gray', alpha=0.2, edgecolor='none')
        ax.add_patch(shadow)
        
        # Main level
        level_poly = Polygon([
            (x_center - width/2, y),
            (x_center + width/2, y),
            (x_center + (width-1)/2, y + 1),
            (x_center - (width-1)/2, y + 1)
        ], facecolor=color, alpha=0.9, edgecolor='white', linewidth=3)
        ax.add_patch(level_poly)
        
        # 3D side effect
        if i < len(levels) - 1:
            side = Polygon([
                (x_center + width/2, y),
                (x_center + width/2 + 0.2, y - 0.1),
                (x_center + (width-1)/2 + 0.2, y + 0.9),
                (x_center + (width-1)/2, y + 1)
            ], facecolor=color, alpha=0.6, edgecolor='none')
            ax.add_patch(side)
        
        # Text
        ax.text(x_center - 0.3, y + 0.5, icon, fontsize=24, ha='center', va='center')
        ax.text(x_center + 0.5, y + 0.5, label, fontsize=14, fontweight='bold',
               ha='center', va='center', color='white')
        
        # Cost badge
        badge = FancyBboxPatch((x_center + width/2 + 0.5, y + 0.2), 1.5, 0.6,
                               boxstyle="round,pad=0.02",
                               facecolor='white', alpha=0.9,
                               edgecolor=color, linewidth=2)
        ax.add_patch(badge)
        ax.text(x_center + width/2 + 1.25, y + 0.5, cost, fontsize=11,
               fontweight='bold', ha='center', va='center', color=color)
    
    # Timeline con design moderno
    timeline_y = 0.8
    
    # Timeline background
    timeline_bg = FancyBboxPatch((9, 0.3), 6.5, 1,
                                 boxstyle="round,pad=0.02",
                                 facecolor=colors_modern['gray1'], alpha=0.8,
                                 edgecolor=colors_modern['gray2'], linewidth=2)
    ax.add_patch(timeline_bg)
    
    milestones = [(9.5, '0'), (11, '6'), (12.5, '12'), (14, '24'), (15, '36')]
    
    # Timeline line
    ax.plot([9.5, 15], [timeline_y, timeline_y], color=colors_modern['gray3'],
           linewidth=3)
    
    for x, month in milestones:
        # Milestone point
        milestone = Circle((x, timeline_y), 0.15, facecolor='white',
                         edgecolor=colors_modern['gray3'], linewidth=2)
        ax.add_patch(milestone)
        ax.text(x, 0.4, f'{month}m', fontsize=11, fontweight='bold',
               ha='center', color=colors_modern['gray3'])
    
    # ROI Dashboard
    roi_panel = FancyBboxPatch((10, 2), 5, 3.5,
                               boxstyle="round,pad=0.05",
                               facecolor='white', alpha=0.95,
                               edgecolor=colors_modern['green2'], linewidth=2)
    ax.add_patch(roi_panel)
    
    ax.text(12.5, 5.2, '💹 ROI ANALYSIS', fontsize=16, fontweight='bold',
           ha='center', color=colors_modern['green3'])
    
    # ROI chart simulation
    x_roi = np.linspace(10.5, 14.5, 100)
    y_roi = 3.5 + 1.5 * np.sin((x_roi - 10.5) * np.pi / 4) * np.exp((x_roi - 10.5) / 4)
    ax.plot(x_roi, y_roi, color=colors_modern['green2'], linewidth=3)
    ax.fill_between(x_roi, 3.5, y_roi, where=(y_roi > 3.5),
                    color=colors_modern['green1'], alpha=0.3)
    
    # Break-even point
    break_even = Circle((12.2, 3.5), 0.1, facecolor=colors_modern['red2'],
                       edgecolor='white', linewidth=2)
    ax.add_patch(break_even)
    ax.text(12.2, 2.9, 'Break-even\n18 months', fontsize=9,
           ha='center', color=colors_modern['red3'])
    
    # Final metrics
    final_metrics = [
        ('SLA', '99.95%', colors_modern['blue2']),
        ('TCO', '-35%', colors_modern['green2']),
        ('Security', '94/100', colors_modern['purple2'])
    ]
    
    for i, (label, value, color) in enumerate(final_metrics):
        x = 11 + i * 1.3
        ax.text(x, 2.5, label, fontsize=10, ha='center', color=colors_modern['gray3'])
        ax.text(x, 2.2, value, fontsize=12, fontweight='bold', ha='center', color=color)
    
    plt.tight_layout()
    return fig

# ========================================================================
# FUNZIONE PRINCIPALE
# ========================================================================
def generate_all_modern_pdfs():
    """Genera tutti i PDF moderni"""
    
    print("=" * 60)
    print("GENERAZIONE FIGURE PDF MODERNE")
    print("Design Contemporaneo e Accattivante")
    print("=" * 60)
    
    figures = [
        ('fig1_power_modern.pdf', create_power_architecture_modern,
         'Architettura Alimentazione Moderna'),
        ('fig2_network_modern.pdf', create_network_evolution_modern,
         'Network Evolution Moderna'),
        ('fig3_cloud_modern.pdf', create_cloud_architecture_modern,
         'Cloud Architecture Moderna'),
        ('fig4_edge_modern.pdf', create_edge_architecture_modern,
         'Edge Computing Moderno'),
        ('fig5_gist_modern.pdf', create_gist_framework_modern,
         'Framework GIST Moderno')
    ]
    
    for i, (filename, func, title) in enumerate(figures, 1):
        print(f"\n{i}. Generazione: {title}...")
        try:
            fig = func()
            fig.savefig(filename, format='pdf', bbox_inches='tight',
                       facecolor='white', edgecolor='none', dpi=300)
            plt.close(fig)
            print(f"   ✓ Salvata: {filename}")
        except Exception as e:
            print(f"   ✗ Errore: {str(e)}")
    
    # PDF unificato
    print("\n6. Generazione PDF unificato moderno...")
    try:
        with PdfPages('capitolo3_moderne_complete.pdf') as pdf:
            for filename, func, title in figures:
                fig = func()
                pdf.savefig(fig, bbox_inches='tight')
                plt.close(fig)
            
            d = pdf.infodict()
            d['Title'] = 'Figure Moderne Capitolo 3'
            d['Author'] = 'Tesi di Laurea'
            d['CreationDate'] = d['ModDate'] = datetime.datetime.now()
        
        print("   ✓ PDF unificato: capitolo3_moderne_complete.pdf")
    except Exception as e:
        print(f"   ✗ Errore: {str(e)}")
    
    print("\n" + "=" * 60)
    print("COMPLETATO! Figure moderne con:")
    print("✓ Design contemporaneo e accattivante")
    print("✓ Gradienti e effetti 3D")
    print("✓ Icone e emoji moderne")
    print("✓ Layout dinamico e pulito")
    print("✓ Colori vivaci ma professionali")
    print("=" * 60)

if __name__ == "__main__":
    generate_all_modern_pdfs()
