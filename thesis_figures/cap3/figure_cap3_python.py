#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script per la generazione delle figure del Capitolo 3
Tesi di Laurea in Ingegneria Informatica
Università Niccolò Cusano

Autore: [Nome Studente]
Data: 2024
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import seaborn as sns
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle, FancyArrowPatch
from matplotlib.patches import ConnectionPatch
import matplotlib.lines as mlines

# Configurazione globale per font large e stile accademico
plt.rcParams.update({
    'font.size': 14,
    'axes.titlesize': 16,
    'axes.labelsize': 14,
    'xtick.labelsize': 12,
    'ytick.labelsize': 12,
    'legend.fontsize': 12,
    'figure.titlesize': 18,
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'DejaVu Sans'],
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.format': 'pdf'
})

# Palette colori professionale
colors = {
    'primary': '#1e88e5',
    'secondary': '#43a047',
    'warning': '#fb8c00',
    'danger': '#e53935',
    'info': '#00acc1',
    'dark': '#37474f',
    'light': '#eceff1',
    'success': '#00897b'
}

def create_power_architecture():
    """
    Figura 3.1: Architettura ridondante 2N per sistemi di alimentazione
    """
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')
    
    # Titolo
    fig.suptitle('Architettura Ridondante 2N per Sistemi di Alimentazione Critica', 
                 fontsize=18, fontweight='bold', y=0.98)
    
    # Rete elettrica
    grid = FancyBboxPatch((0.5, 6), 1.5, 1, 
                          boxstyle="round,pad=0.1",
                          facecolor='#ffeb3b', edgecolor='black', linewidth=2)
    ax.add_patch(grid)
    ax.text(1.25, 6.5, 'RETE\nELETTRICA', ha='center', va='center', 
            fontsize=12, fontweight='bold')
    
    # UPS Sistema A (Primario)
    ups_a = FancyBboxPatch((2.5, 4.5), 1.8, 2,
                           boxstyle="round,pad=0.05",
                           facecolor=colors['primary'], edgecolor='black', 
                           linewidth=2, alpha=0.8)
    ax.add_patch(ups_a)
    ax.text(3.4, 5.8, 'UPS SISTEMA A', ha='center', fontweight='bold', 
            fontsize=12, color='white')
    ax.text(3.4, 5.4, 'PRIMARIO', ha='center', fontsize=11, color='white')
    ax.text(3.4, 5.0, '300 kW', ha='center', fontsize=11, color='white')
    ax.text(3.4, 4.7, 'Config: N+1', ha='center', fontsize=10, color='white')
    
    # UPS Sistema B (Secondario)
    ups_b = FancyBboxPatch((5.5, 4.5), 1.8, 2,
                           boxstyle="round,pad=0.05",
                           facecolor=colors['secondary'], edgecolor='black', 
                           linewidth=2, alpha=0.8)
    ax.add_patch(ups_b)
    ax.text(6.4, 5.8, 'UPS SISTEMA B', ha='center', fontweight='bold', 
            fontsize=12, color='white')
    ax.text(6.4, 5.4, 'SECONDARIO', ha='center', fontsize=11, color='white')
    ax.text(6.4, 5.0, '300 kW', ha='center', fontsize=11, color='white')
    ax.text(6.4, 4.7, 'Config: N+1', ha='center', fontsize=10, color='white')
    
    # Quadri di distribuzione
    quad_a = Rectangle((2.7, 2.5), 1.4, 0.8, 
                       facecolor=colors['light'], edgecolor='black', linewidth=2)
    ax.add_patch(quad_a)
    ax.text(3.4, 2.9, 'QUADRO A', ha='center', fontweight='bold', fontsize=11)
    
    quad_b = Rectangle((5.7, 2.5), 1.4, 0.8,
                       facecolor=colors['light'], edgecolor='black', linewidth=2)
    ax.add_patch(quad_b)
    ax.text(6.4, 2.9, 'QUADRO B', ha='center', fontweight='bold', fontsize=11)
    
    # Carichi critici
    load = FancyBboxPatch((3.8, 0.5), 2.8, 1.2,
                          boxstyle="round,pad=0.1",
                          facecolor=colors['warning'], edgecolor='black', 
                          linewidth=2, alpha=0.8)
    ax.add_patch(load)
    ax.text(5.2, 1.1, 'CARICHI CRITICI', ha='center', fontweight='bold', 
            fontsize=12, color='white')
    ax.text(5.2, 0.7, 'Server, Storage, Network', ha='center', 
            fontsize=10, color='white')
    
    # Frecce di connessione
    # Dalla rete agli UPS
    ax.arrow(1.5, 6.3, 0.9, -1.5, head_width=0.15, head_length=0.1, 
             fc='black', ec='black', linewidth=2)
    ax.arrow(1.5, 6.3, 3.9, -1.5, head_width=0.15, head_length=0.1, 
             fc='black', ec='black', linewidth=2)
    
    # Dagli UPS ai quadri
    ax.arrow(3.4, 4.5, 0, -1.1, head_width=0.15, head_length=0.1, 
             fc=colors['primary'], ec=colors['primary'], linewidth=2)
    ax.arrow(6.4, 4.5, 0, -1.1, head_width=0.15, head_length=0.1, 
             fc=colors['secondary'], ec=colors['secondary'], linewidth=2)
    
    # Dai quadri ai carichi
    ax.arrow(3.4, 2.5, 0.8, -1.2, head_width=0.15, head_length=0.1, 
             fc=colors['primary'], ec=colors['primary'], linewidth=2)
    ax.arrow(6.4, 2.5, -0.8, -1.2, head_width=0.15, head_length=0.1, 
             fc=colors['secondary'], ec=colors['secondary'], linewidth=2)
    
    # Box metriche
    metrics_box = FancyBboxPatch((7.8, 2), 2, 3.5,
                                 boxstyle="round,pad=0.1",
                                 facecolor='white', edgecolor=colors['dark'], 
                                 linewidth=2)
    ax.add_patch(metrics_box)
    
    ax.text(8.8, 5.2, 'METRICHE CHIAVE', fontweight='bold', fontsize=12, 
            ha='center', color=colors['dark'])
    
    metrics_text = [
        'Disponibilità: 99,94%',
        'MTBF: 87.600 ore',
        'MTTR: 1,8 ore',
        'Autonomia: 15 min',
        'PUE: 1,4',
        'ROI: 24 mesi'
    ]
    
    for i, text in enumerate(metrics_text):
        ax.text(8.8, 4.7 - i*0.4, text, fontsize=11, ha='center')
    
    # Legenda
    ax.text(0.5, 0.3, 'Alimentazione Primaria', fontsize=11, 
            color=colors['primary'], fontweight='bold')
    ax.text(3, 0.3, 'Alimentazione Secondaria', fontsize=11, 
            color=colors['secondary'], fontweight='bold')
    ax.text(5.5, 0.3, 'Ridondanza Completa 2N', fontsize=11, 
            color=colors['danger'], fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('figura_3_1_architettura_alimentazione.pdf', 
                format='pdf', bbox_inches='tight')
    plt.show()
    return fig

def create_network_evolution():
    """
    Figura 3.2: Evoluzione delle architetture di rete - da tradizionale a SD-WAN
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
    fig.suptitle('Evoluzione delle Architetture di Rete: da Tradizionale a SD-WAN', 
                 fontsize=18, fontweight='bold')
    
    # Rete Tradizionale (sinistra)
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)
    ax1.axis('off')
    ax1.set_title('Architettura Tradizionale MPLS', fontsize=14, fontweight='bold')
    
    # Datacenter
    dc_trad = Circle((5, 8), 0.8, facecolor=colors['dark'], edgecolor='black', linewidth=2)
    ax1.add_patch(dc_trad)
    ax1.text(5, 8, 'DC', color='white', ha='center', fontweight='bold', fontsize=12)
    
    # Router MPLS
    mpls_positions = [(2, 5), (5, 5), (8, 5)]
    for i, pos in enumerate(mpls_positions):
        mpls = Rectangle((pos[0]-0.5, pos[1]-0.3), 1, 0.6,
                        facecolor=colors['warning'], edgecolor='black', linewidth=2)
        ax1.add_patch(mpls)
        ax1.text(pos[0], pos[1], f'MPLS-{i+1}', ha='center', fontsize=10, fontweight='bold')
    
    # Punti vendita
    stores_trad = [(1.5, 2), (3, 2), (5, 2), (7, 2), (8.5, 2)]
    for i, pos in enumerate(stores_trad):
        store = Rectangle((pos[0]-0.3, pos[1]-0.3), 0.6, 0.6,
                         facecolor=colors['info'], edgecolor='black', linewidth=1)
        ax1.add_patch(store)
        ax1.text(pos[0], pos[1], f'PV{i+1}', ha='center', fontsize=9, color='white')
    
    # Connessioni rigide
    for mpls_pos in mpls_positions:
        ax1.plot([5, mpls_pos[0]], [7.2, mpls_pos[1]+0.3], 'k-', linewidth=2)
    
    for i, store_pos in enumerate(stores_trad):
        mpls_idx = i // 2
        ax1.plot([store_pos[0], mpls_positions[mpls_idx][0]], 
                [store_pos[1]+0.3, mpls_positions[mpls_idx][1]-0.3], 
                'r-', linewidth=1.5)
    
    # Problematiche
    ax1.text(5, 0.5, 'CRITICITÀ:', fontweight='bold', fontsize=11, ha='center', color=colors['danger'])
    ax1.text(5, 0.1, '• Costi elevati (450€/Mbps/mese) • Tempi attivazione: 30-45 giorni', 
            fontsize=10, ha='center')
    
    # SD-WAN (destra)
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    ax2.axis('off')
    ax2.set_title('Architettura SD-WAN', fontsize=14, fontweight='bold')
    
    # Cloud/Datacenter
    cloud = Circle((5, 8), 1, facecolor=colors['primary'], edgecolor='black', 
                  linewidth=2, alpha=0.8)
    ax2.add_patch(cloud)
    ax2.text(5, 8, 'CLOUD\nSD-WAN', color='white', ha='center', 
            fontweight='bold', fontsize=11)
    
    # Internet/MPLS hybrid
    internet_box = FancyBboxPatch((1, 4.5), 8, 1.5,
                                 boxstyle="round,pad=0.1",
                                 facecolor=colors['light'], edgecolor='black', 
                                 linewidth=2, alpha=0.5)
    ax2.add_patch(internet_box)
    ax2.text(5, 5.2, 'INTERNET + MPLS IBRIDO', ha='center', 
            fontweight='bold', fontsize=12)
    
    # Punti vendita con edge
    stores_sdwan = [(1.5, 2), (3, 2), (5, 2), (7, 2), (8.5, 2)]
    for i, pos in enumerate(stores_sdwan):
        # Edge device
        edge = Circle((pos[0], pos[1]+0.7), 0.2, facecolor=colors['secondary'], 
                     edgecolor='black', linewidth=1)
        ax2.add_patch(edge)
        # Store
        store = Rectangle((pos[0]-0.3, pos[1]-0.3), 0.6, 0.6,
                         facecolor=colors['info'], edgecolor='black', linewidth=1)
        ax2.add_patch(store)
        ax2.text(pos[0], pos[1], f'PV{i+1}', ha='center', fontsize=9, color='white')
        
        # Connessioni dinamiche
        ax2.plot([pos[0], 5], [pos[1]+0.9, 4.5], 'g--', linewidth=1, alpha=0.6)
        ax2.plot([pos[0], 5], [pos[1]+0.9, 7], 'b--', linewidth=1, alpha=0.6)
    
    # Vantaggi
    ax2.text(5, 0.5, 'VANTAGGI:', fontweight='bold', fontsize=11, 
            ha='center', color=colors['success'])
    ax2.text(5, 0.1, '• Costi -70% • Attivazione: 5-7 giorni • MTTR: 1,8h • Sicurezza centralizzata', 
            fontsize=10, ha='center')
    
    plt.tight_layout()
    plt.savefig('figura_3_2_evoluzione_rete.pdf', format='pdf', bbox_inches='tight')
    plt.show()
    return fig

def create_maturity_levels():
    """
    Figura 3.3: Livelli di maturità infrastrutturale con KPI
    """
    fig, ax = plt.subplots(figsize=(14, 10))
    
    # Dati per il grafico
    levels = ['Tradizionale', 'Consolidato', 'Automatizzato', 'Ottimizzato', 'Adattivo']
    availability = [96, 98, 99, 99.7, 99.95]
    costs = [100, 87, 72, 58, 47]
    automation = [5, 20, 45, 70, 85]
    
    x = np.arange(len(levels))
    width = 0.25
    
    # Creazione delle barre
    bars1 = ax.bar(x - width, availability, width, label='Disponibilità (%)', 
                   color=colors['primary'], alpha=0.8)
    bars2 = ax.bar(x, costs, width, label='Costi Operativi (% baseline)', 
                   color=colors['warning'], alpha=0.8)
    bars3 = ax.bar(x + width, automation, width, label='Automazione (%)', 
                   color=colors['secondary'], alpha=0.8)
    
    # Personalizzazione
    ax.set_xlabel('Livelli di Maturità', fontsize=14, fontweight='bold')
    ax.set_ylabel('Percentuale (%)', fontsize=14, fontweight='bold')
    ax.set_title('Framework di Maturità Infrastrutturale GDO', 
                fontsize=16, fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(levels, fontsize=12)
    ax.legend(loc='upper left', fontsize=12)
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    
    # Aggiunta valori sulle barre
    for bar in bars1:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                f'{height:.1f}%', ha='center', fontsize=10, fontweight='bold')
    
    for bar in bars2:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                f'{height:.0f}%', ha='center', fontsize=10, fontweight='bold')
    
    for bar in bars3:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                f'{height:.0f}%', ha='center', fontsize=10, fontweight='bold')
    
    # Box con timeline
    timeline_text = """
    Timeline di Implementazione:
    • Livello 1→2: 12-14 mesi, investimento 15% budget IT
    • Livello 2→3: 14-16 mesi, investimento 20% budget IT
    • Livello 3→4: 16-18 mesi, investimento 22% budget IT
    • Livello 4→5: 18-24 mesi, investimento 25% budget IT
    """
    
    ax.text(0.02, 0.98, timeline_text, transform=ax.transAxes,
            fontsize=11, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
    
    plt.tight_layout()
    plt.savefig('figura_3_3_maturity_levels.pdf', format='pdf', bbox_inches='tight')
    plt.show()
    return fig

def create_edge_architecture():
    """
    Figura 3.4: Architettura Edge Computing distribuita per la GDO
    """
    fig, ax = plt.subplots(figsize=(16, 10))
    ax.set_xlim(-1, 11)
    ax.set_ylim(-1, 8)
    ax.axis('off')
    
    fig.suptitle('Architettura Edge Computing Distribuita per la GDO', 
                fontsize=18, fontweight='bold')
    
    # Cloud centrale
    cloud_center = patches.Ellipse((5, 6.5), 2.5, 1.2, 
                                  facecolor=colors['primary'], 
                                  edgecolor='black', linewidth=2, alpha=0.7)
    ax.add_patch(cloud_center)
    ax.text(5, 6.5, 'CLOUD CENTRALE\nAnalytics & ML', 
           ha='center', va='center', fontsize=12, 
           fontweight='bold', color='white')
    
    # Regional Edge Nodes
    regions = [
        {'name': 'MILANO\nNord', 'pos': (1, 3.5), 'stores': 45},
        {'name': 'ROMA\nCentro', 'pos': (3, 3.5), 'stores': 38},
        {'name': 'NAPOLI\nSud', 'pos': (5, 3.5), 'stores': 32},
        {'name': 'PALERMO\nIsole', 'pos': (7, 3.5), 'stores': 28},
        {'name': 'BOLOGNA\nEmilia', 'pos': (9, 3.5), 'stores': 35}
    ]
    
    for region in regions:
        # Edge node box
        edge_box = FancyBboxPatch((region['pos'][0]-0.6, region['pos'][1]-0.4), 
                                  1.2, 0.8,
                                  boxstyle="round,pad=0.05",
                                  facecolor=colors['secondary'], 
                                  edgecolor='black', linewidth=2, alpha=0.8)
        ax.add_patch(edge_box)
        ax.text(region['pos'][0], region['pos'][1], region['name'], 
               ha='center', va='center', fontsize=10, 
               fontweight='bold', color='white')
        
        # Connection to cloud
        ax.plot([region['pos'][0], 5], 
               [region['pos'][1]+0.4, 5.9], 
               'b--', linewidth=1.5, alpha=0.6)
        
        # Store count
        ax.text(region['pos'][0], region['pos'][1]-0.7, 
               f'{region["stores"]} PV', 
               ha='center', fontsize=9, fontweight='bold')
        
        # Mini stores below
        for i in range(3):
            store_y = 1.5 - i*0.3
            store_rect = Rectangle((region['pos'][0]-0.15, store_y), 0.3, 0.2,
                                  facecolor=colors['info'], 
                                  edgecolor='black', linewidth=0.5)
            ax.add_patch(store_rect)
    
    # Servizi Edge box
    services_box = FancyBboxPatch((0, 5), 2.5, 2,
                                 boxstyle="round,pad=0.1",
                                 facecolor='white', 
                                 edgecolor=colors['dark'], linewidth=2)
    ax.add_patch(services_box)
    ax.text(1.25, 6.7, 'SERVIZI EDGE', fontweight='bold', 
           fontsize=11, ha='center')
    
    services = [
        '• Cache dati locali',
        '• Analytics real-time',
        '• Video processing',
        '• Security locale',
        '• IoT gateway',
        '• Backup automatico'
    ]
    
    for i, service in enumerate(services):
        ax.text(0.1, 6.3 - i*0.25, service, fontsize=10)
    
    # Metriche box
    metrics_box = FancyBboxPatch((7.5, 5), 2.5, 2,
                                boxstyle="round,pad=0.1",
                                facecolor='white', 
                                edgecolor=colors['dark'], linewidth=2)
    ax.add_patch(metrics_box)
    ax.text(8.75, 6.7, 'METRICHE', fontweight='bold', 
           fontsize=11, ha='center')
    
    metrics = [
        'Latenza: <50ms',
        'Traffico WAN: -73%',
        'Uptime: 99.97%',
        'Response time: -85%',
        'Bandwidth saving: 68%',
        'ROI: 14 mesi'
    ]
    
    for i, metric in enumerate(metrics):
        ax.text(7.6, 6.3 - i*0.25, metric, fontsize=10)
    
    # Flussi di dati
    ax.text(5, 0.5, 'Elaborazione Locale: 73% dei dati processati all\'edge', 
           ha='center', fontsize=11, fontweight='bold', 
           color=colors['success'])
    ax.text(5, 0.1, 'Solo aggregati e anomalie verso il cloud centrale', 
           ha='center', fontsize=10, style='italic')
    
    plt.tight_layout()
    plt.savefig('figura_3_4_edge_architecture.pdf', 
                format='pdf', bbox_inches='tight')
    plt.show()
    return fig

def create_gist_framework():
    """
    Figura 3.5: Framework GIST - GDO Integrated Security Transformation
    """
    fig, ax = plt.subplots(figsize=(16, 12))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    fig.suptitle('Framework GIST - GDO Integrated Security Transformation', 
                fontsize=18, fontweight='bold')
    
    # Definizione livelli (piramide)
    levels = [
        {'name': 'LIVELLO 5\nIntelligence & AI', 'y': 8, 'width': 2, 
         'color': colors['primary'], 'kpi': '99.95%'},
        {'name': 'LIVELLO 4\nSicurezza Zero Trust', 'y': 6.5, 'width': 3, 
         'color': colors['secondary'], 'kpi': '99.7%'},
        {'name': 'LIVELLO 3\nCloud & Automazione', 'y': 5, 'width': 4, 
         'color': colors['info'], 'kpi': '99.5%'},
        {'name': 'LIVELLO 2\nRete SD-WAN', 'y': 3.5, 'width': 5, 
         'color': colors['warning'], 'kpi': '98.5%'},
        {'name': 'LIVELLO 1\nInfrastruttura Fisica', 'y': 2, 'width': 6, 
         'color': colors['danger'], 'kpi': '97%'}
    ]
    
    for level in levels:
        x_center = 5
        x_left = x_center - level['width']/2
        
        level_box = FancyBboxPatch((x_left, level['y']-0.4), level['width'], 0.8,
                                   boxstyle="round,pad=0.05",
                                   facecolor=level['color'], 
                                   edgecolor='black', linewidth=2, alpha=0.7)
        ax.add_patch(level_box)
        ax.text(x_center, level['y'], level['name'], 
               ha='center', va='center', fontsize=11, 
               fontweight='bold', color='white')
        ax.text(x_left + level['width'] + 0.2, level['y'], 
               f"SLA: {level['kpi']}", 
               fontsize=10, fontweight='bold')
    
    # Timeline
    timeline_y = 0.8
    ax.plot([1, 9], [timeline_y, timeline_y], 'k-', linewidth=2)
    
    milestones = [
        {'x': 2, 'label': '0-6 mesi\nQuick Wins'},
        {'x': 4, 'label': '6-18 mesi\nTrasformazione'},
        {'x': 6, 'label': '18-24 mesi\nOttimizzazione'},
        {'x': 8, 'label': '24-36 mesi\nMaturità'}
    ]
    
    for milestone in milestones:
        ax.plot(milestone['x'], timeline_y, 'ko', markersize=8)
        ax.text(milestone['x'], timeline_y-0.3, milestone['label'], 
               ha='center', fontsize=9)
    
    # Investment box
    inv_box = FancyBboxPatch((0.5, 4), 1.8, 2,
                             boxstyle="round,pad=0.1",
                             facecolor='lightyellow', 
                             edgecolor='black', linewidth=2)
    ax.add_patch(inv_box)
    ax.text(1.4, 5.7, 'INVESTIMENTI', fontweight='bold', 
           fontsize=11, ha='center')
    ax.text(1.4, 5.3, 'Totale: €2.4M', fontsize=10, ha='center')
    ax.text(1.4, 4.9, 'Fase 1: €350k', fontsize=9, ha='center')
    ax.text(1.4, 4.6, 'Fase 2: €850k', fontsize=9, ha='center')
    ax.text(1.4, 4.3, 'Fase 3: €1.2M', fontsize=9, ha='center')
    
    # ROI box
    roi_box = FancyBboxPatch((8.2, 4), 1.5, 2,
                            boxstyle="round,pad=0.1",
                            facecolor='lightgreen', 
                            edgecolor='black', linewidth=2)
    ax.add_patch(roi_box)
    ax.text(8.95, 5.7, 'RISULTATI', fontweight='bold', 
           fontsize=11, ha='center')
    ax.text(8.95, 5.3, 'TCO: -35%', fontsize=10, ha='center')
    ax.text(8.95, 4.9, 'MTTR: -85%', fontsize=9, ha='center')
    ax.text(8.95, 4.6, 'Security: +67%', fontsize=9, ha='center')
    ax.text(8.95, 4.3, 'ROI: 24 mesi', fontsize=9, ha='center', 
           fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('figura_3_5_gist_framework.pdf', 
                format='pdf', bbox_inches='tight')
    plt.show()
    return fig

def create_all_figures():
    """
    Genera tutte le figure del Capitolo 3
    """
    print("Generazione Figure Capitolo 3 - Tesi di Laurea")
    print("=" * 50)
    
    figures = []
    
    print("\n1. Creazione Figura 3.1 - Architettura Alimentazione...")
    fig1 = create_power_architecture()
    figures.append(fig1)
    print("   ✓ Completata")
    
    print("\n2. Creazione Figura 3.2 - Evoluzione Rete...")
    fig2 = create_network_evolution()
    figures.append(fig2)
    print("   ✓ Completata")
    
    print("\n3. Creazione Figura 3.3 - Livelli di Maturità...")
    fig3 = create_maturity_levels()
    figures.append(fig3)
    print("   ✓ Completata")
    
    print("\n4. Creazione Figura 3.4 - Architettura Edge...")
    fig4 = create_edge_architecture()
    figures.append(fig4)
    print("   ✓ Completata")
    
    print("\n5. Creazione Figura 3.5 - Framework GIST...")
    fig5 = create_gist_framework()
    figures.append(fig5)
    print("   ✓ Completata")
    
    print("\n" + "=" * 50)
    print("TUTTE LE FIGURE SONO STATE GENERATE CON SUCCESSO!")
    print("File salvati in formato PDF ad alta risoluzione")
    print("Font size: Large (14-18pt) per ottima leggibilità")
    
    return figures

if __name__ == "__main__":
    # Genera tutte le figure
    all_figures = create_all_figures()
    
    # Mostra riepilogo
    print("\n" + "=" * 50)
    print("RIEPILOGO FIGURE GENERATE:")
    print("- figura_3_1_architettura_alimentazione.pdf")
    print("- figura_3_2_evoluzione_rete.pdf") 
    print("- figura_3_3_maturity_levels.pdf")
    print("- figura_3_4_edge_architecture.pdf")
    print("- figura_3_5_gist_framework.pdf")
    print("\nTutte le figure sono pronte per l'inserimento nella tesi!")
