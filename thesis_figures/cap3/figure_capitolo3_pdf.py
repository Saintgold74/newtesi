#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Figure PDF Accademiche per Capitolo 3 - Tesi di Laurea
Versione con font large e layout spazioso per massima leggibilità
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle, FancyArrow
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np

# Configurazione globale per font MOLTO GRANDI e stile accademico
plt.rcParams['font.size'] = 18
plt.rcParams['font.family'] = 'serif'  # Font accademico
plt.rcParams['axes.titlesize'] = 24
plt.rcParams['axes.labelsize'] = 20
plt.rcParams['xtick.labelsize'] = 18
plt.rcParams['ytick.labelsize'] = 18
plt.rcParams['legend.fontsize'] = 18
plt.rcParams['figure.titlesize'] = 26
plt.rcParams['figure.dpi'] = 100
plt.rcParams['lines.linewidth'] = 2.5
plt.rcParams['patch.linewidth'] = 2.5

# Palette colori sobria e accademica
colors = {
    'primary': '#1f4788',      # Blu scuro professionale
    'secondary': '#4472C4',    # Blu medio
    'success': '#548235',      # Verde scuro
    'warning': '#ED7D31',      # Arancione sobrio  
    'danger': '#C5504B',       # Rosso mattone
    'info': '#70AD47',         # Verde chiaro
    'light': '#F2F2F2',        # Grigio molto chiaro
    'dark': '#2E3440'          # Grigio scuro
}

# ========================================================================
# FIGURA 1: Architettura Alimentazione Ridondante (SEMPLIFICATA)
# ========================================================================

def create_power_architecture_pdf():
    """Architettura alimentazione con layout spazioso e font grandi"""
    
    fig = plt.figure(figsize=(14, 10))
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Titolo principale
    fig.text(0.5, 0.95, 'Architettura Ridondante 2N - Sistemi di Alimentazione Critica', 
             fontsize=26, fontweight='bold', ha='center')
    
    # Rete Elettrica
    grid = FancyBboxPatch((1, 7.5), 3, 1.5,
                          boxstyle="round,pad=0.1",
                          facecolor=colors['dark'],
                          edgecolor='black', linewidth=3)
    ax.add_patch(grid)
    ax.text(2.5, 8.25, 'RETE ELETTRICA', ha='center', va='center',
            color='white', fontsize=20, fontweight='bold')
    
    # Sistema UPS A
    ups_a = FancyBboxPatch((0.5, 4.5), 3, 2,
                          boxstyle="round,pad=0.1",
                          facecolor=colors['primary'],
                          edgecolor='black', linewidth=3)
    ax.add_patch(ups_a)
    ax.text(2, 5.5, 'UPS SISTEMA A\n500 kW', ha='center', va='center',
            color='white', fontsize=20, fontweight='bold')
    
    # Sistema UPS B  
    ups_b = FancyBboxPatch((4.5, 4.5), 3, 2,
                          boxstyle="round,pad=0.1",
                          facecolor=colors['success'],
                          edgecolor='black', linewidth=3)
    ax.add_patch(ups_b)
    ax.text(6, 5.5, 'UPS SISTEMA B\n500 kW', ha='center', va='center',
            color='white', fontsize=20, fontweight='bold')
    
    # Carichi Critici
    load = FancyBboxPatch((2.5, 1.5), 3, 1.8,
                         boxstyle="round,pad=0.1",
                         facecolor=colors['danger'],
                         edgecolor='black', linewidth=3)
    ax.add_patch(load)
    ax.text(4, 2.4, 'CARICHI CRITICI', ha='center', va='center',
            color='white', fontsize=20, fontweight='bold')
    
    # Frecce di collegamento (più spesse e visibili)
    # Dalla rete agli UPS
    ax.arrow(2.5, 7.3, -0.3, -0.6, head_width=0.25, head_length=0.15,
             fc='black', ec='black', linewidth=3)
    ax.arrow(2.5, 7.3, 3.3, -0.6, head_width=0.25, head_length=0.15,
             fc='black', ec='black', linewidth=3)
    
    # Dagli UPS ai carichi
    ax.arrow(2, 4.3, 1.5, -0.6, head_width=0.25, head_length=0.15,
             fc=colors['primary'], ec='black', linewidth=3)
    ax.arrow(6, 4.3, -1.5, -0.6, head_width=0.25, head_length=0.15,
             fc=colors['success'], ec='black', linewidth=3)
    
    # Box KPI (solo metriche essenziali)
    kpi_box = FancyBboxPatch((8.5, 4), 4.5, 4,
                             boxstyle="round,pad=0.1",
                             facecolor='white',
                             edgecolor=colors['dark'], linewidth=3)
    ax.add_patch(kpi_box)
    
    ax.text(10.75, 7.5, 'METRICHE CHIAVE', ha='center', fontsize=22, fontweight='bold')
    
    metrics = [
        'Disponibilità: 99,94%',
        'MTBF: 87.600 ore',
        'Autonomia: 15 minuti',
        'ROI: 24 mesi'
    ]
    
    for i, metric in enumerate(metrics):
        ax.text(10.75, 6.8 - i*0.7, metric, ha='center', fontsize=20)
    
    # Etichetta configurazione
    ax.text(4, 0.5, 'Configurazione 2N: Ridondanza Completa', 
            ha='center', fontsize=18, style='italic')
    
    plt.tight_layout()
    return fig

# ========================================================================
# FIGURA 2: Confronto Reti MPLS vs SD-WAN (SEMPLIFICATO)
# ========================================================================

def create_network_evolution_pdf():
    """Confronto reti con layout chiaro e senza sovrapposizioni"""
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 10))
    fig.suptitle('Evoluzione Architetture di Rete: MPLS vs SD-WAN', 
                 fontsize=26, fontweight='bold', y=0.98)
    
    # --- MPLS Tradizionale ---
    ax1.set_title('Architettura MPLS', fontsize=22, fontweight='bold', pad=20)
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)
    ax1.axis('off')
    
    # Data Center
    dc = Circle((5, 8), 1, facecolor=colors['dark'], 
                edgecolor='black', linewidth=3)
    ax1.add_patch(dc)
    ax1.text(5, 8, 'DC', ha='center', va='center',
             color='white', fontsize=20, fontweight='bold')
    
    # Router MPLS (solo 2 per semplicità)
    for i, x in enumerate([2.5, 7.5]):
        router = FancyBboxPatch((x-0.8, 5), 1.6, 1,
                               boxstyle="round,pad=0.05",
                               facecolor=colors['danger'],
                               edgecolor='black', linewidth=2.5)
        ax1.add_patch(router)
        ax1.text(x, 5.5, f'MPLS\n{i+1}', ha='center', va='center',
                color='white', fontsize=16, fontweight='bold')
        # Connessione al DC
        ax1.plot([x, 5], [6.1, 7], 'k-', linewidth=3)
    
    # Punti vendita (solo 3 per chiarezza)
    for i, x in enumerate([2, 5, 8]):
        pv = Rectangle((x-0.5, 2), 1, 0.8,
                      facecolor=colors['secondary'],
                      edgecolor='black', linewidth=2.5)
        ax1.add_patch(pv)
        ax1.text(x, 2.4, f'PV{i+1}', ha='center', va='center',
                color='white', fontsize=16, fontweight='bold')
        # Connessione dedicata
        target_router = 2.5 if x <= 5 else 7.5
        ax1.plot([x, target_router], [2.8, 5], 'r-', linewidth=2.5)
    
    # Problemi principali
    ax1.text(5, 0.5, 'Costo: 450€/Mbps\nAttivazione: 45 giorni', 
            ha='center', fontsize=18, color=colors['danger'], fontweight='bold')
    
    # --- SD-WAN ---
    ax2.set_title('Architettura SD-WAN', fontsize=22, fontweight='bold', pad=20)
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    ax2.axis('off')
    
    # Cloud Orchestrator
    cloud = patches.Ellipse((5, 8), 3, 1.5,
                           facecolor=colors['info'],
                           edgecolor='black', linewidth=3)
    ax2.add_patch(cloud)
    ax2.text(5, 8, 'SD-WAN\nController', ha='center', va='center',
            color='white', fontsize=18, fontweight='bold')
    
    # Edge Gateway (solo 2 per semplicità)
    for i, x in enumerate([2.5, 7.5]):
        edge = FancyBboxPatch((x-0.8, 5), 1.6, 1,
                             boxstyle="round,pad=0.05",
                             facecolor=colors['primary'],
                             edgecolor='black', linewidth=2.5)
        ax2.add_patch(edge)
        ax2.text(x, 5.5, f'Edge\n{i+1}', ha='center', va='center',
                color='white', fontsize=16, fontweight='bold')
        # Connessione al controller
        ax2.plot([x, 5], [6.1, 7.2], 'g--', linewidth=2.5, alpha=0.7)
    
    # Punti vendita
    for i, x in enumerate([2, 5, 8]):
        pv = Rectangle((x-0.5, 2), 1, 0.8,
                      facecolor=colors['success'],
                      edgecolor='black', linewidth=2.5)
        ax2.add_patch(pv)
        ax2.text(x, 2.4, f'PV{i+1}', ha='center', va='center',
                color='white', fontsize=16, fontweight='bold')
        # Multi-path (Internet + LTE)
        target_edge = 2.5 if x <= 5 else 7.5
        ax2.plot([x, target_edge], [2.8, 5], 'b-', linewidth=2, label='Internet' if i==0 else '')
        ax2.plot([x+0.1, target_edge+0.1], [2.8, 5], 'orange', linewidth=2, linestyle=':', label='LTE' if i==0 else '')
    
    # Vantaggi principali
    ax2.text(5, 0.5, 'Costo: -70%\nAttivazione: 7 giorni', 
            ha='center', fontsize=18, color=colors['success'], fontweight='bold')
    
    ax2.legend(loc='upper right', fontsize=16)
    
    plt.tight_layout()
    return fig

# ========================================================================
# FIGURA 3: Architettura Cloud Ibrida (SEMPLIFICATA)
# ========================================================================

def create_cloud_architecture_pdf():
    """Architettura cloud con componenti essenziali ben distanziati"""
    
    fig = plt.figure(figsize=(16, 10))
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    fig.text(0.5, 0.95, 'Architettura Cloud Ibrida per la GDO', 
             fontsize=26, fontweight='bold', ha='center')
    
    # On-Premise (30%)
    on_prem = FancyBboxPatch((0.5, 3), 4, 3,
                             boxstyle="round,pad=0.1",
                             facecolor='#FFE5CC',
                             edgecolor=colors['dark'], linewidth=3)
    ax.add_patch(on_prem)
    ax.text(2.5, 5.3, 'ON-PREMISE', fontsize=20, fontweight='bold', ha='center')
    ax.text(2.5, 4.7, '30% Workload', fontsize=18, ha='center', style='italic')
    ax.text(2.5, 3.8, 'Sistemi POS\nStorage Locale', fontsize=16, ha='center')
    
    # Private Cloud (35%)
    private = FancyBboxPatch((6, 3), 4, 3,
                            boxstyle="round,pad=0.1",
                            facecolor='#E6F3FF',
                            edgecolor=colors['primary'], linewidth=3)
    ax.add_patch(private)
    ax.text(8, 5.3, 'PRIVATE CLOUD', fontsize=20, fontweight='bold', ha='center')
    ax.text(8, 4.7, '35% Workload', fontsize=18, ha='center', style='italic')
    ax.text(8, 3.8, 'ERP - HR\nFinanza', fontsize=16, ha='center')
    
    # Public Cloud (35%)
    public = FancyBboxPatch((11.5, 3), 4, 3,
                           boxstyle="round,pad=0.1",
                           facecolor='#E6FFE6',
                           edgecolor=colors['success'], linewidth=3)
    ax.add_patch(public)
    ax.text(13.5, 5.3, 'PUBLIC CLOUD', fontsize=20, fontweight='bold', ha='center')
    ax.text(13.5, 4.7, '35% Workload', fontsize=18, ha='center', style='italic')
    ax.text(13.5, 3.8, 'Web - Analytics\nBackup', fontsize=16, ha='center')
    
    # Orchestrazione Kubernetes
    orch = FancyBboxPatch((3, 7.5), 10, 1.2,
                         boxstyle="round,pad=0.05",
                         facecolor=colors['info'], alpha=0.7,
                         edgecolor='black', linewidth=2.5)
    ax.add_patch(orch)
    ax.text(8, 8.1, 'ORCHESTRAZIONE KUBERNETES', 
           ha='center', fontsize=20, color='white', fontweight='bold')
    
    # Frecce di connessione
    for x in [2.5, 8, 13.5]:
        ax.arrow(x, 6.1, 0, 1.2, head_width=0.3, head_length=0.15,
                fc=colors['dark'], ec=colors['dark'], linewidth=2, alpha=0.5)
    
    # KPI Box
    kpi_text = 'TCO: -31%  |  Disponibilità: 99.95%  |  ROI: 24 mesi'
    ax.text(8, 1, kpi_text, ha='center', fontsize=18, 
           bbox=dict(boxstyle="round,pad=0.5", facecolor=colors['light'], 
                     edgecolor=colors['dark'], linewidth=2))
    
    plt.tight_layout()
    return fig

# ========================================================================
# FIGURA 4: Edge Computing (SEMPLIFICATA)
# ========================================================================

def create_edge_architecture_pdf():
    """Architettura Edge con elementi essenziali"""
    
    fig = plt.figure(figsize=(16, 10))
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    fig.text(0.5, 0.95, 'Architettura Edge Computing Distribuita', 
             fontsize=26, fontweight='bold', ha='center')
    
    # Cloud Centrale
    cloud = patches.Ellipse((7, 8), 3.5, 1.5,
                           facecolor=colors['primary'],
                           edgecolor='black', linewidth=3)
    ax.add_patch(cloud)
    ax.text(7, 8, 'CLOUD CENTRALE', ha='center', va='center',
            fontsize=20, color='white', fontweight='bold')
    
    # Edge Nodes (solo 3 per chiarezza)
    regions = [
        (2, 5, 'MILANO', colors['success']),
        (7, 5, 'ROMA', colors['warning']),
        (12, 5, 'NAPOLI', colors['info'])
    ]
    
    for x, y, city, color in regions:
        # Edge node
        edge = FancyBboxPatch((x-1.2, y-0.6), 2.4, 1.2,
                             boxstyle="round,pad=0.05",
                             facecolor=color,
                             edgecolor='black', linewidth=2.5)
        ax.add_patch(edge)
        ax.text(x, y, f'EDGE\n{city}', ha='center', va='center',
                fontsize=18, color='white', fontweight='bold')
        
        # Connessione al cloud
        ax.plot([x, 7], [y+0.7, 6.8], 'k--', linewidth=2, alpha=0.5)
        
        # Punti vendita (2 per edge)
        for i in [-0.8, 0.8]:
            pv_x = x + i
            pv = Rectangle((pv_x-0.3, 1.5), 0.6, 0.8,
                          facecolor=color, alpha=0.6,
                          edgecolor='black', linewidth=2)
            ax.add_patch(pv)
            ax.text(pv_x, 1.9, 'PV', ha='center', va='center',
                   fontsize=14, fontweight='bold')
            # Connessione all'edge
            ax.plot([pv_x, x], [2.3, 4.3], color=color, linewidth=1.5, alpha=0.7)
    
    # Metriche chiave
    metrics_box = FancyBboxPatch((0.5, 8), 4, 1.5,
                                boxstyle="round,pad=0.05",
                                facecolor=colors['light'],
                                edgecolor=colors['dark'], linewidth=2.5)
    ax.add_patch(metrics_box)
    ax.text(2.5, 8.75, 'Latenza: <50ms | Traffico: -73%', 
           ha='center', fontsize=18, fontweight='bold')
    
    plt.tight_layout()
    return fig

# ========================================================================
# FIGURA 5: Framework GIST - Roadmap (SEMPLIFICATA)
# ========================================================================

def create_gist_framework_pdf():
    """Framework GIST con timeline chiara"""
    
    fig = plt.figure(figsize=(16, 11))
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 11)
    ax.axis('off')
    
    fig.text(0.5, 0.95, 'Framework GIST - Roadmap Implementativa', 
             fontsize=26, fontweight='bold', ha='center')
    
    # Definizione fasi
    phases = [
        (2, 'FASE 1\nConsolidamento\n0-6 mesi', colors['danger'], '350k€'),
        (4.2, 'FASE 2\nModernizzazione\n6-18 mesi', colors['warning'], '850k€'),
        (6.4, 'FASE 3\nOttimizzazione\n18-36 mesi', colors['success'], '1.2M€')
    ]
    
    # Disegna le fasi come blocchi progressivi
    for i, (y_pos, label, color, cost) in enumerate(phases):
        width = 10 - i*2
        x_start = 3 + i
        
        # Blocco fase
        phase = FancyBboxPatch((x_start, y_pos), width, 1.8,
                              boxstyle="round,pad=0.05",
                              facecolor=color, alpha=0.7,
                              edgecolor='black', linewidth=3)
        ax.add_patch(phase)
        
        # Testo fase
        ax.text(x_start + width/2, y_pos + 0.9, label,
               ha='center', va='center', fontsize=20, 
               fontweight='bold', color='white')
        
        # Costo
        ax.text(x_start - 1.5, y_pos + 0.9, cost,
               ha='center', va='center', fontsize=18,
               fontweight='bold')
        
        # Freccia alla fase successiva
        if i < len(phases) - 1:
            ax.arrow(x_start + width/2, y_pos + 1.9, 0, 0.8,
                    head_width=0.4, head_length=0.15,
                    fc='gray', ec='gray', linewidth=2)
    
    # Timeline in basso
    timeline_y = 0.5
    ax.arrow(2, timeline_y, 12, 0, head_width=0.2, head_length=0.3,
            fc='black', ec='black', linewidth=3)
    
    # Milestone
    milestones = [(2, '0'), (6, '6'), (10, '18'), (14, '36')]
    for x, months in milestones:
        ax.plot([x, x], [timeline_y-0.15, timeline_y+0.15], 'k-', linewidth=3)
        ax.text(x, timeline_y-0.5, f'{months} mesi', 
               ha='center', fontsize=18, fontweight='bold')
    
    # Box risultati finali
    results_box = FancyBboxPatch((10.5, 8), 5, 2.5,
                                boxstyle="round,pad=0.1",
                                facecolor='white',
                                edgecolor=colors['dark'], linewidth=3)
    ax.add_patch(results_box)
    
    ax.text(13, 9.8, 'RISULTATI ATTESI', ha='center', 
           fontsize=20, fontweight='bold')
    
    results = [
        'Disponibilità: 99.95%',
        'TCO: -35%',
        'ROI: 180% (36 mesi)'
    ]
    
    for i, result in enumerate(results):
        ax.text(13, 9.2 - i*0.5, result, ha='center', fontsize=18)
    
    plt.tight_layout()
    return fig

# ========================================================================
# GENERAZIONE PDF
# ========================================================================

def generate_all_pdfs():
    """Genera tutti i PDF delle figure"""
    
    print("Generazione Figure PDF per Capitolo 3")
    print("=" * 50)
    
    # Lista delle figure da generare
    figures = [
        ("Architettura Alimentazione", create_power_architecture_pdf, "fig1_power_architecture.pdf"),
        ("Evoluzione Reti", create_network_evolution_pdf, "fig2_network_evolution.pdf"),
        ("Architettura Cloud", create_cloud_architecture_pdf, "fig3_cloud_architecture.pdf"),
        ("Edge Computing", create_edge_architecture_pdf, "fig4_edge_architecture.pdf"),
        ("Framework GIST", create_gist_framework_pdf, "fig5_gist_framework.pdf")
    ]
    
    # Genera ogni figura
    for i, (name, func, filename) in enumerate(figures, 1):
        print(f"\n{i}. Generazione {name}...")
        
        # Crea la figura
        fig = func()
        
        # Salva come PDF
        fig.savefig(filename, format='pdf', dpi=300, 
                   bbox_inches='tight', facecolor='white')
        plt.close(fig)
        
        print(f"   ✓ Salvata come: {filename}")
    
    # Crea anche un PDF unificato con tutte le figure
    print("\n6. Creazione PDF unificato...")
    with PdfPages('capitolo3_tutte_figure.pdf') as pdf:
        for name, func, _ in figures:
            fig = func()
            pdf.savefig(fig, bbox_inches='tight', facecolor='white')
            plt.close(fig)
    
    print("   ✓ Salvato come: capitolo3_tutte_figure.pdf")
    
    print("\n" + "=" * 50)
    print("GENERAZIONE COMPLETATA!")
    print("\nFile PDF generati:")
    print("- fig1_power_architecture.pdf")
    print("- fig2_network_evolution.pdf")
    print("- fig3_cloud_architecture.pdf")
    print("- fig4_edge_architecture.pdf")
    print("- fig5_gist_framework.pdf")
    print("- capitolo3_tutte_figure.pdf (tutte le figure)")
    
    print("\n📌 POSIZIONAMENTO NEL CAPITOLO:")
    print("- Figura 1: dopo Sezione 3.3.1")
    print("- Figura 2: dopo Sezione 3.4.1")
    print("- Figura 3: dopo Sezione 3.5.2")
    print("- Figura 4: dopo Sezione 3.6.2")
    print("- Figura 5: dopo Sezione 3.8.2")

if __name__ == "__main__":
    generate_all_pdfs()
