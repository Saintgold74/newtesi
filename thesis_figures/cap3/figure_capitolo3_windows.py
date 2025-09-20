#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Figure professionali per il Capitolo 3 della tesi
Tema: Evoluzione dell'Infrastruttura Tecnologica nella GDO
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle, FancyArrow
from matplotlib.patches import ConnectionPatch
import seaborn as sns

# Configurazione globale per font grandi e stile professionale
plt.rcParams['font.size'] = 14
plt.rcParams['font.family'] = 'Arial'
plt.rcParams['axes.titlesize'] = 18
plt.rcParams['axes.labelsize'] = 16
plt.rcParams['xtick.labelsize'] = 14
plt.rcParams['ytick.labelsize'] = 14
plt.rcParams['legend.fontsize'] = 14
plt.rcParams['figure.titlesize'] = 20
plt.rcParams['figure.dpi'] = 150

# Palette colori professionale
colors = {
    'primary': '#2E5090',      # Blu scuro
    'secondary': '#3498db',    # Blu medio
    'success': '#27ae60',      # Verde
    'warning': '#f39c12',      # Arancione
    'danger': '#e74c3c',       # Rosso
    'info': '#9b59b6',         # Viola
    'light': '#ecf0f1',        # Grigio chiaro
    'dark': '#34495e'          # Grigio scuro
}

# ========================================================================
# FIGURA 1: Architettura Ridondante 2N per Sistemi di Alimentazione
# Da inserire dopo il paragrafo sulla configurazione 2N (Sezione 3.3.1)
# ========================================================================

def create_power_architecture():
    """Crea il diagramma dell'architettura di alimentazione ridondante 2N"""
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))
    fig.suptitle('Architettura Sistemi di Alimentazione Critica nella GDO', 
                 fontsize=20, fontweight='bold', y=1.02)
    
    # --- Sottografico 1: Schema architetturale ---
    ax1.set_title('Configurazione Ridondante 2N', fontsize=18, fontweight='bold', pad=20)
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)
    ax1.axis('off')
    
    # Rete elettrica principale
    grid_box = FancyBboxPatch((0.5, 8), 2, 1.5, 
                              boxstyle="round,pad=0.05",
                              facecolor=colors['dark'], 
                              edgecolor='black', linewidth=2)
    ax1.add_patch(grid_box)
    ax1.text(1.5, 8.75, 'RETE\nELETTRICA', ha='center', va='center',
             color='white', fontsize=14, fontweight='bold')
    
    # UPS Sistema A
    ups_a = FancyBboxPatch((0.5, 5), 2, 2,
                           boxstyle="round,pad=0.05",
                           facecolor=colors['primary'],
                           edgecolor='black', linewidth=2)
    ax1.add_patch(ups_a)
    ax1.text(1.5, 6.5, 'UPS', ha='center', va='center',
             color='white', fontsize=16, fontweight='bold')
    ax1.text(1.5, 6, 'Sistema A', ha='center', va='center',
             color='white', fontsize=14)
    ax1.text(1.5, 5.5, '500 kW', ha='center', va='center',
             color='white', fontsize=13, style='italic')
    
    # UPS Sistema B
    ups_b = FancyBboxPatch((3, 5), 2, 2,
                           boxstyle="round,pad=0.05",
                           facecolor=colors['success'],
                           edgecolor='black', linewidth=2)
    ax1.add_patch(ups_b)
    ax1.text(4, 6.5, 'UPS', ha='center', va='center',
             color='white', fontsize=16, fontweight='bold')
    ax1.text(4, 6, 'Sistema B', ha='center', va='center',
             color='white', fontsize=14)
    ax1.text(4, 5.5, '500 kW', ha='center', va='center',
             color='white', fontsize=13, style='italic')
    
    # STS (Static Transfer Switch)
    sts_box = FancyBboxPatch((5.5, 5.5), 2, 1,
                             boxstyle="round,pad=0.05",
                             facecolor=colors['warning'],
                             edgecolor='black', linewidth=2)
    ax1.add_patch(sts_box)
    ax1.text(6.5, 6, 'STS', ha='center', va='center',
             color='white', fontsize=14, fontweight='bold')
    
    # PDU (Power Distribution Units)
    for i, (x, label) in enumerate([(1, 'PDU-A'), (4, 'PDU-B')]):
        pdu = Rectangle((x-0.5, 2.5), 1, 1.5,
                       facecolor=colors['info'],
                       edgecolor='black', linewidth=2)
        ax1.add_patch(pdu)
        ax1.text(x, 3.25, label, ha='center', va='center',
                color='white', fontsize=13, fontweight='bold')
    
    # Carichi critici
    loads_box = FancyBboxPatch((7.5, 1), 2, 2,
                               boxstyle="round,pad=0.05",
                               facecolor=colors['danger'],
                               edgecolor='black', linewidth=2)
    ax1.add_patch(loads_box)
    ax1.text(8.5, 2.5, 'CARICHI', ha='center', va='center',
             color='white', fontsize=14, fontweight='bold')
    ax1.text(8.5, 2, 'CRITICI', ha='center', va='center',
             color='white', fontsize=14, fontweight='bold')
    ax1.text(8.5, 1.5, 'Server, Storage\nRete Core', ha='center', va='center',
             color='white', fontsize=11)
    
    # Frecce di connessione con spessore maggiore
    # Dalla rete agli UPS
    ax1.arrow(1.5, 7.8, 0, -0.6, head_width=0.15, head_length=0.1,
             fc='black', ec='black', linewidth=2)
    ax1.arrow(2, 8.5, 1.8, -1.3, head_width=0.15, head_length=0.1,
             fc='black', ec='black', linewidth=2)
    
    # Dagli UPS ai PDU
    ax1.arrow(1.5, 4.8, 0, -0.6, head_width=0.15, head_length=0.1,
             fc=colors['primary'], ec='black', linewidth=2)
    ax1.arrow(4, 4.8, 0, -0.6, head_width=0.15, head_length=0.1,
             fc=colors['success'], ec='black', linewidth=2)
    
    # Dal STS ai carichi
    ax1.arrow(7.3, 6, 1, -2.5, head_width=0.15, head_length=0.1,
             fc=colors['warning'], ec='black', linewidth=2)
    
    # Bypass di manutenzione (linea tratteggiata)
    ax1.plot([2.5, 7.5], [8.5, 3], 'r--', linewidth=2, alpha=0.5)
    ax1.text(5, 7, 'Bypass\nManutenzione', ha='center', va='center',
             color='red', fontsize=12, style='italic', alpha=0.7)
    
    # --- Sottografico 2: Metriche e KPI ---
    ax2.set_title('Metriche di Affidabilità e ROI', fontsize=18, fontweight='bold', pad=20)
    ax2.axis('off')
    
    # Dati per il grafico a barre
    metrics = ['Disponibilità\nSistema', 'Riduzione\nMTTR', 'Efficienza\nEnergetica', 'ROI\nAnnuale']
    values = [99.94, 73, 96, 180]
    colors_bars = [colors['success'], colors['info'], colors['primary'], colors['warning']]
    
    # Crea mini subplot per le barre
    ax2_bars = plt.axes([0.55, 0.45, 0.35, 0.25])
    bars = ax2_bars.bar(range(len(metrics)), values, color=colors_bars, edgecolor='black', linewidth=2)
    ax2_bars.set_xticks(range(len(metrics)))
    ax2_bars.set_xticklabels(metrics, fontsize=11, rotation=0, ha='center')
    ax2_bars.set_ylabel('Percentuale (%)', fontsize=12, fontweight='bold')
    ax2_bars.set_ylim(0, 200)
    ax2_bars.grid(axis='y', alpha=0.3, linestyle='--')
    
    # Aggiungi valori sopra le barre
    for bar, val in zip(bars, values):
        height = bar.get_height()
        ax2_bars.text(bar.get_x() + bar.get_width()/2., height + 3,
                     f'{val}%', ha='center', va='bottom', fontsize=12, fontweight='bold')
    
    # Box informativo con parametri tecnici
    info_box = FancyBboxPatch((0.52, 0.05), 0.4, 0.3,
                              boxstyle="round,pad=0.02",
                              facecolor=colors['light'],
                              edgecolor=colors['dark'], linewidth=2)
    ax2.add_patch(info_box)
    
    technical_info = [
        "PARAMETRI TECNICI",
        "----------------",
        "• Autonomia batterie: 15 min",
        "• Tempo commutazione: <4ms",
        "• THD output: <3%",
        "• Fattore potenza: >0.99",
        "• MTBF: 87,600 ore",
        "• Ridondanza: 2N completa"
    ]
    
    for i, text in enumerate(technical_info):
        weight = 'bold' if i == 0 else 'normal'
        size = 13 if i == 0 else 11
        ax2.text(0.72, 0.28 - i*0.035, text, ha='center', va='center',
                fontsize=size, fontweight=weight)
    
    plt.tight_layout()
    plt.savefig('fig1_power_architecture.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.show()
    return fig

# ========================================================================
# FIGURA 2: Evoluzione delle Architetture di Rete - SD-WAN
# Da inserire dopo il paragrafo su SD-WAN (Sezione 3.4.1)
# ========================================================================

def create_network_evolution():
    """Crea il diagramma comparativo tra rete tradizionale e SD-WAN"""
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 9))
    fig.suptitle('Evoluzione Architetture di Rete: da MPLS a SD-WAN', 
                 fontsize=20, fontweight='bold', y=1.02)
    
    # --- Rete Tradizionale MPLS ---
    ax1.set_title('Architettura Tradizionale MPLS', fontsize=16, fontweight='bold')
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)
    ax1.axis('off')
    
    # Data center centrale
    dc_trad = Circle((5, 8), 0.8, facecolor=colors['dark'], edgecolor='black', linewidth=2)
    ax1.add_patch(dc_trad)
    ax1.text(5, 8, 'DATA\nCENTER', ha='center', va='center',
             color='white', fontsize=12, fontweight='bold')
    
    # Router MPLS centrali
    mpls_positions = [(3, 5.5), (7, 5.5)]
    for i, (x, y) in enumerate(mpls_positions):
        router = FancyBboxPatch((x-0.6, y-0.4), 1.2, 0.8,
                                boxstyle="round,pad=0.02",
                                facecolor=colors['danger'],
                                edgecolor='black', linewidth=2)
        ax1.add_patch(router)
        ax1.text(x, y, f'MPLS\nRouter {i+1}', ha='center', va='center',
                color='white', fontsize=10, fontweight='bold')
        # Connessioni al DC
        ax1.plot([x, 5], [y+0.4, 7.2], 'k-', linewidth=3)
    
    # Punti vendita
    pv_positions = [(1, 2), (3, 2), (5, 2), (7, 2), (9, 2)]
    for i, (x, y) in enumerate(pv_positions):
        pv = Rectangle((x-0.4, y-0.3), 0.8, 0.6,
                      facecolor=colors['secondary'],
                      edgecolor='black', linewidth=1.5)
        ax1.add_patch(pv)
        ax1.text(x, y, f'PV{i+1}', ha='center', va='center',
                color='white', fontsize=10, fontweight='bold')
        # Connessioni MPLS dedicate
        if x <= 5:
            ax1.plot([x, 3], [y+0.3, 5.1], 'r-', linewidth=2)
        else:
            ax1.plot([x, 7], [y+0.3, 5.1], 'r-', linewidth=2)
    
    # Problemi della rete tradizionale
    problems = [
        "❌ Costi elevati: 450€/Mbps/mese",
        "❌ Attivazione lenta: 30-45 giorni",
        "❌ Scalabilità limitata",
        "❌ Gestione complessa"
    ]
    
    for i, problem in enumerate(problems):
        ax1.text(0.5, 9 - i*0.5, problem, fontsize=11,
                color=colors['danger'], fontweight='bold')
    
    # --- Architettura SD-WAN ---
    ax2.set_title('Architettura SD-WAN Moderna', fontsize=16, fontweight='bold')
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    ax2.axis('off')
    
    # Cloud orchestrator
    cloud = patches.Ellipse((5, 8.5), 2.5, 1.2, 
                           facecolor=colors['info'], 
                           edgecolor='black', linewidth=2)
    ax2.add_patch(cloud)
    ax2.text(5, 8.5, 'SD-WAN\nORCHESTRATOR', ha='center', va='center',
             color='white', fontsize=13, fontweight='bold')
    
    # Multi-cloud connectivity
    cloud_providers = [(2.5, 6.5, 'AWS'), (5, 6.5, 'AZURE'), (7.5, 6.5, 'GCP')]
    for x, y, name in cloud_providers:
        provider = Circle((x, y), 0.5, facecolor=colors['success'], 
                         edgecolor='black', linewidth=2)
        ax2.add_patch(provider)
        ax2.text(x, y, name, ha='center', va='center',
                color='white', fontsize=10, fontweight='bold')
        # Connessioni all'orchestrator
        ax2.plot([x, 5], [y+0.4, 7.8], 'g--', linewidth=2, alpha=0.7)
    
    # Edge routers SD-WAN
    edge_positions = [(2, 4), (5, 4), (8, 4)]
    for i, (x, y) in enumerate(edge_positions):
        edge = FancyBboxPatch((x-0.5, y-0.3), 1, 0.6,
                              boxstyle="round,pad=0.02",
                              facecolor=colors['primary'],
                              edgecolor='black', linewidth=2)
        ax2.add_patch(edge)
        ax2.text(x, y, f'Edge {i+1}', ha='center', va='center',
                color='white', fontsize=10, fontweight='bold')
    
    # Punti vendita con connettività ibrida
    for i, (x, y) in enumerate(pv_positions):
        pv = Rectangle((x-0.4, y-0.3), 0.8, 0.6,
                      facecolor=colors['success'],
                      edgecolor='black', linewidth=1.5)
        ax2.add_patch(pv)
        ax2.text(x, y, f'PV{i+1}', ha='center', va='center',
                color='white', fontsize=10, fontweight='bold')
        
        # Connessioni multiple (Internet + 4G/5G)
        nearest_edge = edge_positions[min(i//2, 2)]
        # Linea Internet
        ax2.plot([x, nearest_edge[0]], [y+0.3, nearest_edge[1]-0.3], 
                'b-', linewidth=1.5, label='Internet' if i==0 else '')
        # Linea 4G/5G backup
        ax2.plot([x-0.1, nearest_edge[0]-0.1], [y+0.3, nearest_edge[1]-0.3], 
                'orange', linewidth=1, linestyle=':', alpha=0.8,
                label='4G/5G Backup' if i==0 else '')
    
    # Vantaggi SD-WAN
    benefits = [
        "✓ Riduzione costi: -70%",
        "✓ Attivazione rapida: 5-7 giorni",
        "✓ Scalabilità illimitata",
        "✓ Gestione centralizzata",
        "✓ Failover automatico",
        "✓ QoS dinamico"
    ]
    
    for i, benefit in enumerate(benefits):
        ax2.text(0.5, 9.2 - i*0.4, benefit, fontsize=11,
                color=colors['success'], fontweight='bold')
    
    # Legenda
    ax2.legend(loc='lower right', fontsize=10, framealpha=0.9)
    
    plt.tight_layout()
    plt.savefig('fig2_network_evolution.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.show()
    return fig

# ========================================================================
# FIGURA 3: Architettura Cloud Ibrida e Multi-Cloud
# Da inserire dopo la sezione su Cloud e Architetture Ibride (Sezione 3.5.2)
# ========================================================================

def create_cloud_architecture():
    """Crea il diagramma dell'architettura cloud ibrida per la GDO"""
    
    fig = plt.figure(figsize=(16, 10))
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    fig.suptitle('Architettura Cloud Ibrida per la Grande Distribuzione Organizzata', 
                 fontsize=20, fontweight='bold')
    
    # On-Premise Infrastructure
    on_prem = FancyBboxPatch((0.5, 1), 3.5, 3,
                             boxstyle="round,pad=0.05",
                             facecolor='#FFE5CC', 
                             edgecolor=colors['dark'], linewidth=2)
    ax.add_patch(on_prem)
    ax.text(2.25, 3.5, 'ON-PREMISE', fontsize=14, fontweight='bold', ha='center')
    ax.text(2.25, 3, '(30% Workload)', fontsize=11, ha='center', style='italic')
    
    # Componenti on-premise
    components_onprem = [
        (1.2, 2.2, 'POS\nSystems'),
        (2.2, 2.2, 'Local\nStorage'),
        (3.2, 2.2, 'Edge\nCompute')
    ]
    for x, y, label in components_onprem:
        comp = Rectangle((x-0.35, y-0.35), 0.7, 0.7,
                        facecolor=colors['warning'],
                        edgecolor='black', linewidth=1)
        ax.add_patch(comp)
        ax.text(x, y, label, ha='center', va='center',
               fontsize=10, color='white', fontweight='bold')
    
    # Private Cloud
    private_cloud = FancyBboxPatch((5, 1), 3.5, 3,
                                   boxstyle="round,pad=0.05",
                                   facecolor='#E6F3FF',
                                   edgecolor=colors['primary'], linewidth=2)
    ax.add_patch(private_cloud)
    ax.text(6.75, 3.5, 'PRIVATE CLOUD', fontsize=14, fontweight='bold', ha='center')
    ax.text(6.75, 3, '(35% Workload)', fontsize=11, ha='center', style='italic')
    
    # Componenti private cloud
    components_private = [
        (5.7, 2.2, 'Core\nERP'),
        (6.7, 2.2, 'Financial\nSystems'),
        (7.7, 2.2, 'HR\nData')
    ]
    for x, y, label in components_private:
        comp = Rectangle((x-0.35, y-0.35), 0.7, 0.7,
                        facecolor=colors['primary'],
                        edgecolor='black', linewidth=1)
        ax.add_patch(comp)
        ax.text(x, y, label, ha='center', va='center',
               fontsize=10, color='white', fontweight='bold')
    
    # Public Cloud Providers
    public_clouds = [
        (10.5, 2.5, 'AWS', colors['warning']),
        (12.5, 2.5, 'Azure', colors['info']),
        (14.5, 2.5, 'GCP', colors['success'])
    ]
    
    for x, y, name, color in public_clouds:
        cloud = patches.Ellipse((x, y), 1.5, 1.2,
                               facecolor=color, alpha=0.8,
                               edgecolor='black', linewidth=2)
        ax.add_patch(cloud)
        ax.text(x, y, name, ha='center', va='center',
               fontsize=13, color='white', fontweight='bold')
    
    ax.text(12.5, 3.8, 'PUBLIC CLOUD', fontsize=14, fontweight='bold', ha='center')
    ax.text(12.5, 3.4, '(35% Workload)', fontsize=11, ha='center', style='italic')
    
    # Orchestration Layer
    orch_layer = FancyBboxPatch((2, 6), 12, 1.5,
                                boxstyle="round,pad=0.03",
                                facecolor=colors['info'], alpha=0.9,
                                edgecolor='black', linewidth=2)
    ax.add_patch(orch_layer)
    ax.text(8, 6.75, 'KUBERNETES ORCHESTRATION LAYER', 
           ha='center', va='center', fontsize=15, 
           color='white', fontweight='bold')
    
    # Security & Compliance Layer
    sec_layer = FancyBboxPatch((2, 8), 12, 1.2,
                               boxstyle="round,pad=0.03",
                               facecolor=colors['danger'], alpha=0.8,
                               edgecolor='black', linewidth=2)
    ax.add_patch(sec_layer)
    ax.text(8, 8.6, 'ZERO TRUST SECURITY & COMPLIANCE', 
           ha='center', va='center', fontsize=15, 
           color='white', fontweight='bold')
    
    # Connessioni
    # On-prem to Private
    ax.arrow(3.8, 2.5, 0.9, 0, head_width=0.15, head_length=0.1,
            fc='gray', ec='gray', linewidth=2)
    ax.text(4.4, 2.8, 'VPN', fontsize=10, ha='center')
    
    # Private to Public
    ax.arrow(8.3, 2.5, 1.4, 0, head_width=0.15, head_length=0.1,
            fc='gray', ec='gray', linewidth=2)
    ax.text(9.4, 2.8, 'Direct\nConnect', fontsize=10, ha='center')
    
    # Vertical connections to orchestration
    for x in [2.25, 6.75, 12.5]:
        ax.arrow(x, 4.2, 0, 1.5, head_width=0.2, head_length=0.1,
                fc='blue', ec='blue', linewidth=1.5, alpha=0.6)
    
    # KPI Box
    kpi_box = FancyBboxPatch((0.5, 5), 3, 2.5,
                             boxstyle="round,pad=0.02",
                             facecolor='white',
                             edgecolor='black', linewidth=2)
    ax.add_patch(kpi_box)
    
    kpis = [
        "📊 RISULTATI MISURATI",
        "----------------",
        "TCO: -31% in 3 anni",
        "Time-to-Market: -65%",
        "Energia: -45%",
        "Disponibilità: 99.95%"
    ]
    
    for i, kpi in enumerate(kpis):
        weight = 'bold' if i == 0 else 'normal'
        size = 12 if i == 0 else 11
        ax.text(2, 7.2 - i*0.35, kpi, ha='center', va='center',
               fontsize=size, fontweight=weight)
    
    # Cost breakdown pie chart (mini)
    ax_pie = plt.axes([0.75, 0.15, 0.15, 0.15])
    sizes = [30, 35, 35]
    colors_pie = ['#FFE5CC', '#E6F3FF', '#90EE90']
    labels = ['On-Prem', 'Private', 'Public']
    ax_pie.pie(sizes, labels=labels, colors=colors_pie, autopct='%1.0f%%',
              startangle=90, textprops={'fontsize': 9})
    ax_pie.set_title('Distribuzione Workload', fontsize=10, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('fig3_cloud_architecture.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.show()
    return fig

# ========================================================================
# FIGURA 4: Edge Computing Architecture
# Da inserire nella sezione Edge Computing (Sezione 3.6.1)
# ========================================================================

def create_edge_architecture():
    """Crea il diagramma dell'architettura Edge Computing per la GDO"""
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(16, 12), gridspec_kw={'height_ratios': [3, 1]})
    fig.suptitle('Architettura Edge Computing Distribuita per la GDO', 
                 fontsize=20, fontweight='bold', y=1.02)
    
    # --- Parte superiore: Architettura ---
    ax1.set_xlim(0, 12)
    ax1.set_ylim(0, 8)
    ax1.axis('off')
    
    # Cloud Centrale
    cloud_central = patches.Ellipse((6, 7), 3, 1.2,
                                   facecolor=colors['primary'],
                                   edgecolor='black', linewidth=2)
    ax1.add_patch(cloud_central)
    ax1.text(6, 7, 'CLOUD CENTRALE\nAnalytics & ML', ha='center', va='center',
            fontsize=13, color='white', fontweight='bold')
    
    # Regional Edge Nodes
    regions = [
        (2, 4.5, 'EDGE\nMILANO', colors['success']),
        (4.5, 4.5, 'EDGE\nROMA', colors['info']),
        (7, 4.5, 'EDGE\nNAPOLI', colors['warning']),
        (9.5, 4.5, 'EDGE\nPALERMO', colors['danger'])
    ]
    
    for x, y, label, color in regions:
        # Edge node box
        edge = FancyBboxPatch((x-0.7, y-0.4), 1.4, 0.8,
                              boxstyle="round,pad=0.02",
                              facecolor=color,
                              edgecolor='black', linewidth=2)
        ax1.add_patch(edge)
        ax1.text(x, y, label, ha='center', va='center',
                fontsize=11, color='white', fontweight='bold')
        
        # Connection to cloud
        ax1.plot([x, 6], [y+0.4, 6.4], 'k--', linewidth=1.5, alpha=0.5)
        
        # Edge capabilities
        capabilities = ['Cache', 'AI/ML', 'Security']
        for i, cap in enumerate(capabilities):
            cap_y = y - 0.8 - i*0.25
            ax1.text(x, cap_y, f'• {cap}', ha='center', va='center',
                    fontsize=9, style='italic')
    
    # Store clusters
    store_y = 1.5
    for i, (edge_x, _, _, edge_color) in enumerate(regions):
        # Draw 3 stores per edge
        for j in range(3):
            store_x = edge_x - 0.6 + j*0.6
            store = Rectangle((store_x-0.2, store_y-0.2), 0.4, 0.4,
                            facecolor=edge_color, alpha=0.6,
                            edgecolor='black', linewidth=1)
            ax1.add_patch(store)
            ax1.text(store_x, store_y, 'PV', ha='center', va='center',
                    fontsize=9, fontweight='bold')
            
            # Connection to edge
            ax1.plot([store_x, edge_x], [store_y+0.2, 4.1],
                    color=edge_color, linewidth=1, alpha=0.7)
    
    ax1.text(6, 0.8, 'PUNTI VENDITA (200+ locations)', 
            ha='center', fontsize=12, fontweight='bold')
    
    # IoT devices indicators
    iot_y = 0.3
    iot_devices = ['🌡️ Sensori', '📹 Telecamere', '📊 Smart Meter', '🏷️ RFID']
    for i, device in enumerate(iot_devices):
        ax1.text(2 + i*2, iot_y, device, ha='center', fontsize=11)
    
    # Latency and bandwidth indicators
    # Cloud to Edge
    ax1.annotate('', xy=(4, 5.5), xytext=(5, 6.2),
                arrowprops=dict(arrowstyle='<->', color='red', lw=2))
    ax1.text(4.5, 5.9, 'Latenza: 20-30ms\nBanda: 1 Gbps', 
            ha='center', fontsize=10, bbox=dict(boxstyle="round,pad=0.3", 
                                               facecolor='yellow', alpha=0.7))
    
    # Edge to Store
    ax1.annotate('', xy=(2.5, 2), xytext=(2.5, 3.8),
                arrowprops=dict(arrowstyle='<->', color='green', lw=2))
    ax1.text(1.2, 2.9, 'Latenza: <5ms\nBanda: 100 Mbps', 
            ha='center', fontsize=10, bbox=dict(boxstyle="round,pad=0.3", 
                                               facecolor='lightgreen', alpha=0.7))
    
    # Benefits box
    benefits_box = FancyBboxPatch((9.5, 1.5), 2.3, 2,
                                  boxstyle="round,pad=0.02",
                                  facecolor=colors['light'],
                                  edgecolor='black', linewidth=2)
    ax1.add_patch(benefits_box)
    
    benefits = [
        "VANTAGGI EDGE",
        "-------------",
        "✓ Latenza <50ms",
        "✓ Traffico -73%",
        "✓ Uptime 99.97%",
        "✓ Resilienza locale"
    ]
    
    for i, benefit in enumerate(benefits):
        weight = 'bold' if i == 0 else 'normal'
        size = 11 if i == 0 else 10
        ax1.text(10.65, 3.2 - i*0.25, benefit, ha='center', va='center',
                fontsize=size, fontweight=weight)
    
    # --- Parte inferiore: Grafico delle prestazioni ---
    ax2.set_xlabel('Tempo (ore del giorno)', fontsize=14, fontweight='bold')
    ax2.set_ylabel('Latenza (ms)', fontsize=14, fontweight='bold')
    ax2.set_title('Confronto Prestazioni: Edge vs Cloud Tradizionale', 
                  fontsize=14, fontweight='bold', pad=10)
    ax2.grid(True, alpha=0.3, linestyle='--')
    
    # Dati simulati per 24 ore
    hours = np.arange(0, 24)
    latency_traditional = 80 + 40*np.sin((hours-14)*np.pi/12) + np.random.normal(0, 5, 24)
    latency_edge = 25 + 10*np.sin((hours-14)*np.pi/12) + np.random.normal(0, 2, 24)
    
    ax2.plot(hours, latency_traditional, 'r-', linewidth=2.5, label='Cloud Tradizionale', marker='o', markersize=5)
    ax2.plot(hours, latency_edge, 'g-', linewidth=2.5, label='Edge Computing', marker='s', markersize=5)
    
    # Evidenzia ore di picco
    peak_hours = [12, 13, 18, 19, 20]
    for hour in peak_hours:
        ax2.axvspan(hour-0.5, hour+0.5, alpha=0.1, color='red')
    
    ax2.axhline(y=50, color='orange', linestyle='--', linewidth=1.5, alpha=0.7)
    ax2.text(1, 52, 'Soglia critica (50ms)', fontsize=10, color='orange')
    
    ax2.set_xlim(-0.5, 23.5)
    ax2.set_ylim(0, 140)
    ax2.legend(loc='upper left', fontsize=12, framealpha=0.95)
    ax2.set_xticks([0, 4, 8, 12, 16, 20, 24])
    
    # Aggiungi annotazione per il risparmio
    ax2.annotate('Riduzione media:\n-68% latenza',
                xy=(16, 35), xytext=(19, 60),
                arrowprops=dict(arrowstyle='->', color='green', lw=2),
                fontsize=11, ha='center',
                bbox=dict(boxstyle="round,pad=0.5", facecolor='lightgreen', alpha=0.8))
    
    plt.tight_layout()
    plt.savefig('fig4_edge_architecture.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.show()
    return fig

# ========================================================================
# FIGURA 5: Framework GIST - Roadmap Implementativa
# Da inserire nella sezione Framework di Implementazione (Sezione 3.8)
# ========================================================================

def create_gist_framework():
    """Crea il diagramma del Framework GIST con timeline e KPI"""
    
    fig = plt.figure(figsize=(18, 10))
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    fig.suptitle('Framework GIST: GDO Integrated Security Transformation', 
                 fontsize=22, fontweight='bold', y=0.98)
    
    # Definizione livelli con colori gradient
    levels = [
        (1, colors['danger'], 'LIVELLO 1\nInfrastruttura\nFisica', '0-6 mesi\n350k€'),
        (2.8, colors['warning'], 'LIVELLO 2\nReti e\nConnettività', '6-12 mesi\n500k€'),
        (4.6, colors['info'], 'LIVELLO 3\nCloud e\nVirtualizzazione', '12-18 mesi\n850k€'),
        (6.4, colors['success'], 'LIVELLO 4\nSicurezza e\nAutomazione', '18-24 mesi\n750k€'),
        (8.2, colors['primary'], 'LIVELLO 5\nIntelligenza\nArtificiale', '24-36 mesi\n450k€')
    ]
    
    # Disegna la piramide evolutiva
    for i, (y, color, label, timing) in enumerate(levels):
        width = 10 - i*1.5
        x_start = 2 + i*0.75
        
        # Livello principale
        level_box = FancyBboxPatch((x_start, y-0.7), width, 1.4,
                                   boxstyle="round,pad=0.02",
                                   facecolor=color, alpha=0.7,
                                   edgecolor='black', linewidth=2)
        ax.add_patch(level_box)
        
        # Testo del livello
        ax.text(x_start + width/2, y, label, ha='center', va='center',
               fontsize=13, fontweight='bold', color='white')
        
        # Timing e costo
        ax.text(x_start - 1.5, y, timing, ha='center', va='center',
               fontsize=10, style='italic')
        
        # Freccia di progressione
        if i < len(levels) - 1:
            ax.arrow(x_start + width/2, y+0.8, 0, 0.9,
                    head_width=0.3, head_length=0.1,
                    fc='gray', ec='gray', linewidth=1, alpha=0.5)
    
    # KPI per ogni livello (sulla destra)
    kpi_data = [
        ('Disponibilità: 97%→99%', 'MTBF: +45%'),
        ('MTTR: 4h→2h', 'Banda: +200%'),
        ('TCO: -25%', 'Scalabilità: 10x'),
        ('Incidenti: -67%', 'Compliance: 95%'),
        ('Automazione: 82%', 'Predittività: 94%')
    ]
    
    for i, (y, _, _, _) in enumerate(levels):
        kpi_box = FancyBboxPatch((11, y-0.5), 2.5, 1,
                                 boxstyle="round,pad=0.02",
                                 facecolor='white',
                                 edgecolor=levels[i][1], linewidth=2)
        ax.add_patch(kpi_box)
        
        kpi1, kpi2 = kpi_data[i]
        ax.text(12.25, y+0.15, kpi1, ha='center', va='center',
               fontsize=9, fontweight='bold')
        ax.text(12.25, y-0.15, kpi2, ha='center', va='center',
               fontsize=9)
    
    # Timeline in basso
    timeline_y = 0.5
    ax.arrow(2, timeline_y, 9, 0, head_width=0.15, head_length=0.2,
            fc='black', ec='black', linewidth=2)
    
    milestones = [(2, '0'), (4, '6'), (6, '12'), (8, '18'), (10, '24'), (11, '36')]
    for x, month in milestones:
        ax.plot([x, x], [timeline_y-0.1, timeline_y+0.1], 'k-', linewidth=2)
        ax.text(x, timeline_y-0.3, f'{month} mesi', ha='center', fontsize=10)
    
    ax.text(6.5, 0, 'TIMELINE IMPLEMENTAZIONE', ha='center', 
           fontsize=12, fontweight='bold')
    
    # ROI Curve (in alto a destra)
    ax_roi = plt.axes([0.72, 0.65, 0.22, 0.2])
    months_roi = np.arange(0, 37)
    investment = np.array([350, 350, 350, 350, 350, 350,  # Fase 1
                          850, 850, 850, 850, 850, 850,  # Fase 2  
                          1700, 1700, 1700, 1700, 1700, 1700,  # Fase 3
                          2450, 2450, 2450, 2450, 2450, 2450,  # Fase 4
                          2900, 2900, 2900, 2900, 2900, 2900,  # Fase 5
                          2900, 2900, 2900, 2900, 2900, 2900, 2900])
    
    savings = np.array([0] + [i*120 for i in range(1, 37)])
    roi = (savings - investment[:37]) / investment[:37] * 100
    
    ax_roi.plot(months_roi, roi, 'g-', linewidth=2.5, label='ROI')
    ax_roi.axhline(y=0, color='black', linestyle='-', linewidth=1)
    ax_roi.axhline(y=100, color='red', linestyle='--', linewidth=1, alpha=0.5)
    ax_roi.fill_between(months_roi, 0, roi, where=(roi > 0), 
                        color='green', alpha=0.3)
    ax_roi.set_xlabel('Mesi', fontsize=10)
    ax_roi.set_ylabel('ROI (%)', fontsize=10)
    ax_roi.set_title('Curva ROI', fontsize=11, fontweight='bold')
    ax_roi.grid(True, alpha=0.3, linestyle='--')
    ax_roi.set_xlim(0, 36)
    
    # Break-even point
    break_even = np.where(roi > 0)[0][0] if any(roi > 0) else None
    if break_even:
        ax_roi.plot(break_even, 0, 'ro', markersize=8)
        ax_roi.annotate(f'Break-even:\n{break_even} mesi',
                       xy=(break_even, 0), xytext=(break_even+5, 20),
                       arrowprops=dict(arrowstyle='->', color='red'),
                       fontsize=9)
    
    # Summary box (in basso a destra)
    summary_box = FancyBboxPatch((10.5, 1.5), 3, 2.5,
                                 boxstyle="round,pad=0.02",
                                 facecolor=colors['light'],
                                 edgecolor='black', linewidth=2)
    ax.add_patch(summary_box)
    
    summary_text = [
        "RISULTATI FINALI",
        "----------------",
        "✓ SLA: 99.95%",
        "✓ TCO: -35%",
        "✓ Security Score: 94/100",
        "✓ Compliance: 98%",
        "✓ ROI: 180% a 36 mesi",
        "----------------",
        "Investimento: €2.9M",
        "Risparmio annuo: €1.4M"
    ]
    
    for i, text in enumerate(summary_text):
        weight = 'bold' if i in [0, 8, 9] else 'normal'
        size = 11 if i == 0 else 10
        ax.text(12, 3.7 - i*0.22, text, ha='center', va='center',
               fontsize=size, fontweight=weight)
    
    plt.tight_layout()
    plt.savefig('fig5_gist_framework.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.show()
    return fig

# ========================================================================
# Esecuzione principale
# ========================================================================

if __name__ == "__main__":
    print("Generazione Figure Capitolo 3 - Evoluzione Infrastrutturale")
    print("=" * 60)
    
    # Genera tutte le figure
    print("\n1. Generazione Figura 1: Architettura Alimentazione...")
    fig1 = create_power_architecture()
    print("   ✓ Salvata come: fig1_power_architecture.png")
    
    print("\n2. Generazione Figura 2: Evoluzione Reti...")
    fig2 = create_network_evolution()
    print("   ✓ Salvata come: fig2_network_evolution.png")
    
    print("\n3. Generazione Figura 3: Architettura Cloud...")
    fig3 = create_cloud_architecture()
    print("   ✓ Salvata come: fig3_cloud_architecture.png")
    
    print("\n4. Generazione Figura 4: Edge Computing...")
    fig4 = create_edge_architecture()
    print("   ✓ Salvata come: fig4_edge_architecture.png")
    
    print("\n5. Generazione Figura 5: Framework GIST...")
    fig5 = create_gist_framework()
    print("   ✓ Salvata come: fig5_gist_framework.png")
    
    print("\n" + "=" * 60)
    print("GENERAZIONE COMPLETATA!")
    print("\nTutte le figure sono state salvate nella directory corrente")
    print("\nPosizionamento nel capitolo:")
    print("- Figura 1: dopo Sezione 3.3.1 (Architettura UPS)")
    print("- Figura 2: dopo Sezione 3.4.1 (SD-WAN)")  
    print("- Figura 3: dopo Sezione 3.5.2 (Multi-Cloud)")
    print("- Figura 4: dopo Sezione 3.6.1 (Edge Computing)")
    print("- Figura 5: dopo Sezione 3.8 (Framework GIST)")
