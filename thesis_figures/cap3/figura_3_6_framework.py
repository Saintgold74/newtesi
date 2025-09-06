#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Figura 3.6 - Framework Integrato GIST
Diagramma di sintesi che collega i risultati del Capitolo 3 con il Capitolo 4
"""

import matplotlib
matplotlib.rcParams['text.usetex'] = False

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch, Rectangle
import matplotlib.lines as mlines
import warnings
warnings.filterwarnings('ignore')

# Configurazione stile
plt.rcParams.update({
    'text.usetex': False,
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'DejaVu Sans'],
    'font.size': 10,
    'figure.dpi': 100,
    'savefig.dpi': 300,
    'axes.unicode_minus': False
})

def generate_framework_integrato():
    """
    Genera il Framework Integrato GIST che collega infrastruttura e compliance
    """
    print("Generando Figura 3.6 - Framework Integrato GIST...")
    
    # Crea figura grande per il framework
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Colori per i diversi layer
    colors = {
        'physical': '#90CAF9',      # Blu chiaro
        'network': '#81C784',        # Verde chiaro
        'cloud': '#FFB74D',          # Arancione chiaro
        'security': '#F48FB1',       # Rosa chiaro
        'compliance': '#CE93D8',     # Viola chiaro
        'metrics': '#FFF176',        # Giallo chiaro
        'arrows': '#455A64'          # Grigio scuro
    }
    
    # ========== LAYER 1: FONDAMENTA FISICHE ==========
    layer1 = FancyBboxPatch((0.5, 1), 5, 1.2,
                            boxstyle="round,pad=0.05",
                            facecolor=colors['physical'],
                            edgecolor='black', linewidth=2)
    ax.add_patch(layer1)
    ax.text(3, 1.6, 'FONDAMENTA FISICHE', fontsize=12, fontweight='bold', ha='center')
    
    # Componenti
    components_l1 = ['Power\n2N Config', 'Cooling\nPUE 1.22', 'Connectivity\nRedundant']
    for i, comp in enumerate(components_l1):
        x = 1.5 + i * 1.5
        rect = FancyBboxPatch((x-0.4, 1.15), 0.8, 0.5,
                              boxstyle="round,pad=0.02",
                              facecolor='white', alpha=0.8,
                              edgecolor='darkblue', linewidth=1)
        ax.add_patch(rect)
        ax.text(x, 1.4, comp, fontsize=8, ha='center', va='center')
    
    # ========== LAYER 2: EVOLUZIONE RETE ==========
    layer2 = FancyBboxPatch((0.5, 2.5), 5, 1.2,
                            boxstyle="round,pad=0.05",
                            facecolor=colors['network'],
                            edgecolor='black', linewidth=2)
    ax.add_patch(layer2)
    ax.text(3, 3.1, 'EVOLUZIONE RETE', fontsize=12, fontweight='bold', ha='center')
    
    # Componenti
    components_l2 = ['SD-WAN\nMTTR 1.2h', 'Edge\nComputing', 'Full Mesh\nTopology']
    for i, comp in enumerate(components_l2):
        x = 1.5 + i * 1.5
        rect = FancyBboxPatch((x-0.4, 2.65), 0.8, 0.5,
                              boxstyle="round,pad=0.02",
                              facecolor='white', alpha=0.8,
                              edgecolor='darkgreen', linewidth=1)
        ax.add_patch(rect)
        ax.text(x, 2.9, comp, fontsize=8, ha='center', va='center')
    
    # ========== LAYER 3: TRASFORMAZIONE CLOUD ==========
    layer3 = FancyBboxPatch((0.5, 4), 5, 1.2,
                            boxstyle="round,pad=0.05",
                            facecolor=colors['cloud'],
                            edgecolor='black', linewidth=2)
    ax.add_patch(layer3)
    ax.text(3, 4.6, 'TRASFORMAZIONE CLOUD', fontsize=12, fontweight='bold', ha='center')
    
    # Componenti
    components_l3 = ['Hybrid\nCloud', 'Multi-Cloud\nStrategy', 'Cloud\nNative']
    for i, comp in enumerate(components_l3):
        x = 1.5 + i * 1.5
        rect = FancyBboxPatch((x-0.4, 4.15), 0.8, 0.5,
                              boxstyle="round,pad=0.02",
                              facecolor='white', alpha=0.8,
                              edgecolor='darkorange', linewidth=1)
        ax.add_patch(rect)
        ax.text(x, 4.4, comp, fontsize=8, ha='center', va='center')
    
    # ========== LAYER 4: ARCHITETTURA SICUREZZA ==========
    layer4 = FancyBboxPatch((0.5, 5.5), 5, 1.2,
                            boxstyle="round,pad=0.05",
                            facecolor=colors['security'],
                            edgecolor='black', linewidth=2)
    ax.add_patch(layer4)
    ax.text(3, 6.1, 'ARCHITETTURA SICUREZZA', fontsize=12, fontweight='bold', ha='center')
    
    # Componenti
    components_l4 = ['Zero Trust\n-42.7% ASSA', 'Micro-\nsegmentation', 'SASE/SSE\nIntegration']
    for i, comp in enumerate(components_l4):
        x = 1.5 + i * 1.5
        rect = FancyBboxPatch((x-0.4, 5.65), 0.8, 0.5,
                              boxstyle="round,pad=0.02",
                              facecolor='white', alpha=0.8,
                              edgecolor='darkred', linewidth=1)
        ax.add_patch(rect)
        ax.text(x, 5.9, comp, fontsize=8, ha='center', va='center')
    
    # ========== LAYER 5: COMPLIANCE INTEGRATA (Preview Cap. 4) ==========
    layer5 = FancyBboxPatch((0.5, 7), 5, 1.2,
                            boxstyle="round,pad=0.05",
                            facecolor=colors['compliance'],
                            edgecolor='black', linewidth=2, linestyle='--')
    ax.add_patch(layer5)
    ax.text(3, 7.6, 'COMPLIANCE INTEGRATA', fontsize=12, fontweight='bold', ha='center')
    ax.text(3, 7.3, '(→ Capitolo 4)', fontsize=9, ha='center', style='italic')
    
    # Componenti
    components_l5 = ['PCI-DSS\n4.0', 'GDPR\nCompliance', 'NIS2\nReadiness']
    for i, comp in enumerate(components_l5):
        x = 1.5 + i * 1.5
        rect = FancyBboxPatch((x-0.4, 7.15), 0.8, 0.5,
                              boxstyle="round,pad=0.02",
                              facecolor='white', alpha=0.8,
                              edgecolor='purple', linewidth=1, linestyle='--')
        ax.add_patch(rect)
        ax.text(x, 7.4, comp, fontsize=8, ha='center', va='center')
    
    # ========== METRICHE CHIAVE (LATO DESTRO) ==========
    
    # Box per Availability
    metric1 = FancyBboxPatch((7, 2), 2.5, 0.8,
                             boxstyle="round,pad=0.05",
                             facecolor=colors['metrics'],
                             edgecolor='black', linewidth=1.5)
    ax.add_patch(metric1)
    ax.text(8.25, 2.55, 'AVAILABILITY', fontsize=10, fontweight='bold', ha='center')
    ax.text(8.25, 2.25, '99.96%', fontsize=14, fontweight='bold', ha='center', color='green')
    
    # Box per TCO
    metric2 = FancyBboxPatch((7, 3.5), 2.5, 0.8,
                             boxstyle="round,pad=0.05",
                             facecolor=colors['metrics'],
                             edgecolor='black', linewidth=1.5)
    ax.add_patch(metric2)
    ax.text(8.25, 4.05, 'TCO REDUCTION', fontsize=10, fontweight='bold', ha='center')
    ax.text(8.25, 3.75, '-38.2%', fontsize=14, fontweight='bold', ha='center', color='green')
    
    # Box per ASSA
    metric3 = FancyBboxPatch((7, 5), 2.5, 0.8,
                             boxstyle="round,pad=0.05",
                             facecolor=colors['metrics'],
                             edgecolor='black', linewidth=1.5)
    ax.add_patch(metric3)
    ax.text(8.25, 5.55, 'ASSA REDUCTION', fontsize=10, fontweight='bold', ha='center')
    ax.text(8.25, 5.25, '-42.7%', fontsize=14, fontweight='bold', ha='center', color='green')
    
    # Box per Compliance (preview)
    metric4 = FancyBboxPatch((7, 6.5), 2.5, 0.8,
                             boxstyle="round,pad=0.05",
                             facecolor=colors['metrics'],
                             edgecolor='black', linewidth=1.5, linestyle='--')
    ax.add_patch(metric4)
    ax.text(8.25, 7.05, 'COMPLIANCE COST', fontsize=10, fontweight='bold', ha='center')
    ax.text(8.25, 6.75, '-37.8%', fontsize=14, fontweight='bold', ha='center', color='orange')
    ax.text(8.25, 6.55, '(Target Cap.4)', fontsize=8, ha='center', style='italic')
    
    # ========== FRECCE DI CONNESSIONE ==========
    
    # Frecce verticali tra layer
    for y in [2.2, 3.7, 5.2, 6.7]:
        arrow = FancyArrowPatch((3, y), (3, y+0.3),
                               connectionstyle="arc3", 
                               arrowstyle='->', mutation_scale=20,
                               color=colors['arrows'], linewidth=2)
        ax.add_patch(arrow)
    
    # Frecce dalle metriche ai layer
    # Availability <- Physical + Network
    arrow1 = FancyArrowPatch((6.5, 2.4), (7, 2.4),
                            connectionstyle="arc3,rad=0.3", 
                            arrowstyle='->', mutation_scale=15,
                            color='gray', linewidth=1.5, alpha=0.7)
    ax.add_patch(arrow1)
    
    # TCO <- Cloud
    arrow2 = FancyArrowPatch((6.5, 3.9), (7, 3.9),
                            connectionstyle="arc3,rad=0.3", 
                            arrowstyle='->', mutation_scale=15,
                            color='gray', linewidth=1.5, alpha=0.7)
    ax.add_patch(arrow2)
    
    # ASSA <- Security
    arrow3 = FancyArrowPatch((6.5, 5.4), (7, 5.4),
                            connectionstyle="arc3,rad=0.3", 
                            arrowstyle='->', mutation_scale=15,
                            color='gray', linewidth=1.5, alpha=0.7)
    ax.add_patch(arrow3)
    
    # ========== TIMELINE E INVESTIMENTO (LATO SINISTRO) ==========
    
    # Timeline
    timeline_x = 10.5
    ax.plot([timeline_x, timeline_x], [1, 7.5], 'k-', linewidth=2)
    
    # Milestone sulla timeline
    milestones = [
        (1.5, '0 mesi\nBaseline'),
        (3, '6 mesi\nQuick Wins'),
        (4.5, '18 mesi\nCore Transform'),
        (6, '30 mesi\nOptimization'),
        (7.5, '36 mesi\nMaturity')
    ]
    
    for y, text in milestones:
        ax.plot(timeline_x, y, 'ko', markersize=8)
        ax.text(timeline_x + 0.2, y, text, fontsize=8, va='center')
    
    ax.text(timeline_x, 0.5, 'TIMELINE', fontsize=10, fontweight='bold', ha='center')
    
    # Investment Box
    inv_box = FancyBboxPatch((11.5, 3), 2, 2,
                             boxstyle="round,pad=0.05",
                             facecolor='lightcyan',
                             edgecolor='black', linewidth=1.5)
    ax.add_patch(inv_box)
    ax.text(12.5, 4.6, 'INVESTMENT', fontsize=10, fontweight='bold', ha='center')
    ax.text(12.5, 4.2, 'Total: €8.95M', fontsize=9, ha='center')
    ax.text(12.5, 3.9, 'Phase 1: €1.05M', fontsize=8, ha='center')
    ax.text(12.5, 3.6, 'Phase 2: €5.7M', fontsize=8, ha='center')
    ax.text(12.5, 3.3, 'Phase 3: €2.2M', fontsize=8, ha='center')
    
    # ROI Box
    roi_box = FancyBboxPatch((11.5, 5.5), 2, 1.2,
                             boxstyle="round,pad=0.05",
                             facecolor='lightgreen',
                             edgecolor='black', linewidth=1.5)
    ax.add_patch(roi_box)
    ax.text(12.5, 6.4, 'ROI', fontsize=10, fontweight='bold', ha='center')
    ax.text(12.5, 6, '237%', fontsize=14, fontweight='bold', ha='center', color='darkgreen')
    ax.text(12.5, 5.7, '@ 36 mesi', fontsize=8, ha='center')
    
    # ========== TITOLO E SOTTOTITOLO ==========
    ax.text(7, 9.2, 'FRAMEWORK GIST', fontsize=16, fontweight='bold', ha='center')
    ax.text(7, 8.8, 'GDO Infrastructure Security Transformation', fontsize=12, ha='center', style='italic')
    ax.text(7, 8.5, 'Integrazione dei Risultati del Capitolo 3 → Bridge verso Capitolo 4 (Compliance)', 
           fontsize=10, ha='center', color='gray')
    
    # ========== LEGENDA ==========
    legend_elements = [
        mlines.Line2D([], [], color='white', marker='s', markersize=10, 
                     markerfacecolor=colors['physical'], label='Infrastruttura Fisica'),
        mlines.Line2D([], [], color='white', marker='s', markersize=10, 
                     markerfacecolor=colors['network'], label='Rete Evoluta'),
        mlines.Line2D([], [], color='white', marker='s', markersize=10, 
                     markerfacecolor=colors['cloud'], label='Cloud Transformation'),
        mlines.Line2D([], [], color='white', marker='s', markersize=10, 
                     markerfacecolor=colors['security'], label='Sicurezza Zero Trust'),
        mlines.Line2D([], [], color='white', marker='s', markersize=10, 
                     markerfacecolor=colors['compliance'], label='Compliance (Cap. 4)'),
    ]
    
    ax.legend(handles=legend_elements, loc='lower center', ncol=5, 
             frameon=True, fancybox=True, shadow=True, fontsize=9)
    
    # Salva figura
    plt.tight_layout()
    plt.savefig('figura_3_6_framework_integrato.pdf', bbox_inches='tight', dpi=300)
    plt.savefig('figura_3_6_framework_integrato.png', bbox_inches='tight', dpi=300)
    print("  ✓ Figura 3.6 Framework Integrato salvata con successo!")
    
    plt.show()

if __name__ == "__main__":
    print("=" * 60)
    print("GENERAZIONE FIGURA 3.6 - FRAMEWORK INTEGRATO GIST")
    print("=" * 60)
    generate_framework_integrato()
    print("=" * 60)
    print("Framework che collega i risultati del Capitolo 3")
    print("con le tematiche del Capitolo 4 (Compliance)")
    print("\nFile generati:")
    print("  - figura_3_6_framework_integrato.pdf")
    print("  - figura_3_6_framework_integrato.png")
    print("=" * 60)