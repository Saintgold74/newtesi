#!/usr/bin/env python3
"""
Script per generare le figure dei Capitoli 2-5 della tesi GDO
Queste figure erano state erroneamente associate al Capitolo 1
"""

import matplotlib.pyplot as plt
import numpy as np
import os

# Configurazione matplotlib
plt.rcParams['font.size'] = 10
plt.rcParams['figure.dpi'] = 150
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['savefig.bbox'] = 'tight'

# Colori tema
COLOR_PRIMARY = '#2E86AB'
COLOR_SECONDARY = '#A23B72'
COLOR_SUCCESS = '#73AB84'
COLOR_WARNING = '#F18F01'
COLOR_DANGER = '#C73E1D'
COLOR_NEUTRAL = '#7A7A7A'

def create_output_directory(chapter):
    """Crea directory per il capitolo specificato"""
    output_dir = f"thesis_figures/cap{chapter}"
    os.makedirs(output_dir, exist_ok=True)
    return output_dir

# ========== CAPITOLO 2: THREAT LANDSCAPE ==========

def create_fig_2_1_cyber_evolution():
    """Fig 2.1: Evoluzione attacchi cyber (per Capitolo 2)"""
    fig, ax1 = plt.subplots(figsize=(10, 6))
    
    years = np.array([2020, 2021, 2022, 2023, 2024, 2025])
    incidents = np.array([142, 187, 312, 584, 721, 847])
    impact = np.array([23, 34, 67, 124, 189, 234])
    
    # Grafico incidenti
    ax1.set_xlabel('Anno')
    ax1.set_ylabel('Numero di Incidenti', color=COLOR_DANGER)
    ax1.plot(years, incidents, color=COLOR_DANGER, marker='o', linewidth=2.5)
    ax1.fill_between(years, 0, incidents, alpha=0.2, color=COLOR_DANGER)
    ax1.tick_params(axis='y', labelcolor=COLOR_DANGER)
    ax1.grid(True, alpha=0.3)
    
    # Asse secondario per impatto
    ax2 = ax1.twinx()
    ax2.set_ylabel('Impatto Economico (M€)', color=COLOR_PRIMARY)
    ax2.plot(years, impact, color=COLOR_PRIMARY, marker='s', linewidth=2.5)
    ax2.tick_params(axis='y', labelcolor=COLOR_PRIMARY)
    
    # Annotazione +312%
    ax1.annotate('+312%\n(2021-2023)', xy=(2023, 584), xytext=(2022.3, 700),
                arrowprops=dict(arrowstyle='->', color=COLOR_DANGER, lw=2),
                fontsize=12, fontweight='bold', color=COLOR_DANGER,
                bbox=dict(boxstyle="round,pad=0.3", facecolor='white',
                         edgecolor=COLOR_DANGER, linewidth=2))
    
    plt.title('Evoluzione degli Attacchi Cyber al Settore Retail (2020-2025)',
              fontsize=13, fontweight='bold')
    plt.tight_layout()
    
    return fig, 'fig_2_1_cyber_evolution'

def create_fig_2_2_attack_types():
    """Fig 2.2: Distribuzione tipologie attacco (per Capitolo 2)"""
    fig, ax = plt.subplots(figsize=(8, 8))
    
    types = ['Ransomware\n31%', 'Data Breach\n24%', 'Supply Chain\n18%', 
             'POS Malware\n12%', 'Cyber-Physical\n8%', 'Altri\n7%']
    sizes = [31, 24, 18, 12, 8, 7]
    colors = [COLOR_DANGER, COLOR_PRIMARY, COLOR_WARNING,
              COLOR_SUCCESS, COLOR_SECONDARY, COLOR_NEUTRAL]
    
    wedges, texts = ax.pie(sizes, labels=types, colors=colors,
                           startangle=90, wedgeprops=dict(width=0.5))
    
    # Centro del donut
    ax.text(0, 0, '1.847\nIncidenti\nAnalizzati', ha='center', va='center',
            fontsize=14, fontweight='bold')
    
    plt.title('Distribuzione Tipologie di Attacco nel Settore GDO',
              fontsize=13, fontweight='bold')
    
    return fig, 'fig_2_2_attack_types'

def create_fig_2_5_assa_reduction():
    """Fig 2.5: Riduzione ASSA con Zero Trust (per Capitolo 2)"""
    fig = plt.figure(figsize=(12, 6))
    
    categories = ['Network\nExposure', 'Endpoint\nVuln.', 'Identity\nMgmt',
                 'Data\nProtection', 'Application\nSecurity', 'Physical\nSecurity']
    
    traditional = [85, 72, 68, 75, 70, 65]
    zero_trust = [45, 38, 42, 48, 40, 52]
    
    # Radar chart
    ax1 = plt.subplot(121, projection='polar')
    angles = np.linspace(0, 2*np.pi, len(categories), endpoint=False).tolist()
    traditional_plot = traditional + [traditional[0]]
    zero_trust_plot = zero_trust + [zero_trust[0]]
    angles += angles[:1]
    
    ax1.plot(angles, traditional_plot, 'o-', linewidth=2, 
             color=COLOR_DANGER, label='Tradizionale')
    ax1.fill(angles, traditional_plot, alpha=0.25, color=COLOR_DANGER)
    ax1.plot(angles, zero_trust_plot, 'o-', linewidth=2,
             color=COLOR_PRIMARY, label='Zero Trust')
    ax1.fill(angles, zero_trust_plot, alpha=0.25, color=COLOR_PRIMARY)
    
    ax1.set_xticks(angles[:-1])
    ax1.set_xticklabels(categories, size=9)
    ax1.set_ylim(0, 100)
    ax1.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1))
    ax1.set_title('Confronto Superficie di Attacco', fontsize=11)
    
    # Bar chart riduzione
    ax2 = plt.subplot(122)
    reduction = [(traditional[i]-zero_trust[i])/traditional[i]*100 
                 for i in range(len(traditional))]
    
    y_pos = np.arange(len(categories))
    bars = ax2.barh(y_pos, reduction, color=COLOR_SUCCESS, alpha=0.8)
    ax2.set_yticks(y_pos)
    ax2.set_yticklabels(categories)
    ax2.set_xlabel('Riduzione (%)')
    ax2.set_title('Riduzione % ASSA', fontsize=11)
    
    for bar, val in zip(bars, reduction):
        ax2.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2,
                f'{val:.1f}%', va='center', fontsize=9)
    
    avg = np.mean(reduction)
    ax2.axvline(x=avg, color=COLOR_DANGER, linestyle='--', linewidth=2)
    ax2.text(avg, -0.7, f'Media: {avg:.1f}%', ha='center', fontsize=10,
             fontweight='bold', color=COLOR_DANGER)
    
    plt.suptitle('Riduzione della Superficie di Attacco (ASSA) con Zero Trust',
                 fontsize=14, fontweight='bold')
    plt.tight_layout()
    
    return fig, 'fig_2_5_assa_reduction'

def create_fig_2_5_framework_security():
    """Fig 2.5 (finale): Framework Integrato di Sicurezza GDO"""
    fig, ax = plt.subplots(figsize=(12, 10))
    ax.set_xlim(-8, 8)
    ax.set_ylim(-8, 8)
    ax.axis('off')
    
    # Definizione dei layer del framework
    # Layer esterno: Threat Landscape
    threat_circle = plt.Circle((0, 0), 7, fill=False, edgecolor=COLOR_DANGER, 
                              linewidth=3, linestyle='--', alpha=0.7)
    ax.add_patch(threat_circle)
    
    # Minacce esterne
    threats = [
        {'name': 'Ransomware\n31%', 'pos': (0, 7.5), 'color': COLOR_DANGER},
        {'name': 'Data Breach\n24%', 'pos': (5.3, 5.3), 'color': COLOR_DANGER},
        {'name': 'Supply Chain\n18%', 'pos': (7.5, 0), 'color': COLOR_WARNING},
        {'name': 'POS Malware\n12%', 'pos': (5.3, -5.3), 'color': COLOR_WARNING},
        {'name': 'Cyber-Physical\n8%', 'pos': (0, -7.5), 'color': COLOR_SECONDARY},
        {'name': 'Altri\n7%', 'pos': (-5.3, -5.3), 'color': COLOR_NEUTRAL},
    ]
    
    for threat in threats:
        threat_box = FancyBboxPatch((threat['pos'][0]-1.2, threat['pos'][1]-0.5), 
                                   2.4, 1,
                                   boxstyle="round,pad=0.1",
                                   facecolor=threat['color'],
                                   edgecolor='darkgray',
                                   alpha=0.7)
        ax.add_patch(threat_box)
        ax.text(threat['pos'][0], threat['pos'][1], threat['name'], 
                ha='center', va='center', fontsize=9, fontweight='bold', color='white')
    
    # Layer intermedio: Zero Trust Principles
    zt_circle = plt.Circle((0, 0), 5, fill=False, edgecolor=COLOR_PRIMARY, 
                          linewidth=4, alpha=0.8)
    ax.add_patch(zt_circle)
    
    # Principi Zero Trust
    zt_principles = [
        {'name': 'Never Trust\nAlways Verify', 'pos': (0, 5.5)},
        {'name': 'Micro-\nsegmentation', 'pos': (3.9, 3.9)},
        {'name': 'Least\nPrivilege', 'pos': (5.5, 0)},
        {'name': 'Continuous\nVerification', 'pos': (3.9, -3.9)},
        {'name': 'Assume\nBreach', 'pos': (0, -5.5)},
        {'name': 'Encryption\nEverywhere', 'pos': (-3.9, -3.9)},
        {'name': 'Identity\nCentric', 'pos': (-5.5, 0)},
        {'name': 'Context\nAware', 'pos': (-3.9, 3.9)}
    ]
    
    for i, principle in enumerate(zt_principles):
        angle = i * 2 * np.pi / len(zt_principles)
        principle_circle = Circle(principle['pos'], 0.8, 
                                 facecolor=COLOR_PRIMARY, alpha=0.8)
        ax.add_patch(principle_circle)
        ax.text(principle['pos'][0], principle['pos'][1], principle['name'], 
                ha='center', va='center', fontsize=8, fontweight='bold', 
                color='white')
    
    # Core: Architettura GDO
    core_components = {
        'Infrastructure': {'pos': (-1.5, 1.5), 'color': COLOR_SUCCESS},
        'Governance': {'pos': (1.5, 1.5), 'color': COLOR_PRIMARY},
        'Security': {'pos': (-1.5, -1.5), 'color': COLOR_DANGER},
        'Transformation': {'pos': (1.5, -1.5), 'color': COLOR_WARNING}
    }
    
    # Core centrale
    core_circle = Circle((0, 0), 2.5, facecolor='white', 
                        edgecolor='black', linewidth=3)
    ax.add_patch(core_circle)
    
    for name, props in core_components.items():
        comp_box = FancyBboxPatch((props['pos'][0]-0.7, props['pos'][1]-0.4), 
                                 1.4, 0.8,
                                 boxstyle="round,pad=0.05",
                                 facecolor=props['color'],
                                 alpha=0.9)
        ax.add_patch(comp_box)
        ax.text(props['pos'][0], props['pos'][1], name, 
                ha='center', va='center', fontsize=9, fontweight='bold', 
                color='white')
    
    # Centro del core
    ax.text(0, 0, 'GDO\nArchitecture', ha='center', va='center', 
            fontsize=11, fontweight='bold')
    
    # Flussi di informazione (frecce curve)
    # Dal threat landscape ai principi Zero Trust
    for i in range(0, 360, 45):
        angle = np.radians(i)
        start_r, end_r = 6.5, 5.5
        start_x, start_y = start_r * np.cos(angle), start_r * np.sin(angle)
        end_x, end_y = end_r * np.cos(angle), end_r * np.sin(angle)
        ax.annotate('', xy=(end_x, end_y), xytext=(start_x, start_y),
                   arrowprops=dict(arrowstyle='->', color='gray', 
                                 lw=1.5, alpha=0.6))
    
    # Dai principi Zero Trust al core
    for principle in zt_principles:
        direction = np.array(principle['pos']) / np.linalg.norm(principle['pos'])
        start = principle['pos'] - direction * 0.8
        end = direction * 2.5
        ax.annotate('', xy=end, xytext=start,
                   arrowprops=dict(arrowstyle='->', color=COLOR_PRIMARY, 
                                 lw=2, alpha=0.7))
    
    # Labels dei layer
    ax.text(0, 7.8, 'THREAT LANDSCAPE', ha='center', va='bottom', 
            fontsize=12, fontweight='bold', color=COLOR_DANGER)
    ax.text(0, 5.8, 'ZERO TRUST PRINCIPLES', ha='center', va='bottom', 
            fontsize=11, fontweight='bold', color=COLOR_PRIMARY)
    ax.text(0, -2.8, 'ARCHITECTURAL CORE', ha='center', va='top', 
            fontsize=10, fontweight='bold')
    
    # Metriche chiave
    metrics_text = 'Key Metrics: ASSA -42.7% | MTTD -81.1% | ROI +287%'
    ax.text(0, -7.5, metrics_text, ha='center', va='center',
            fontsize=11, fontweight='bold',
            bbox=dict(boxstyle="round,pad=0.5", 
                     facecolor='lightgray', alpha=0.8))
    
    # Feedback loops (frecce curve)
    feedback_angles = [45, 135, 225, 315]
    for angle in feedback_angles:
        theta = np.radians(angle)
        r1, r2 = 3, 4.5
        ax.annotate('', 
                   xy=(r2*np.cos(theta), r2*np.sin(theta)),
                   xytext=(r1*np.cos(theta), r1*np.sin(theta)),
                   arrowprops=dict(arrowstyle='<->', connectionstyle="arc3,rad=.3",
                                 color='gray', lw=1, alpha=0.5, linestyle='--'))
    
    plt.title('Framework Integrato di Sicurezza GDO\nDal Threat Landscape all\'Architettura',
              fontsize=16, fontweight='bold', pad=20)
    
    return fig, 'fig_2_5_framework_security'

# ========== CAPITOLO 3: EVOLUZIONE INFRASTRUTTURALE ==========

def create_fig_3_2_cloud_adoption():
    """Fig 3.2: Trend adozione cloud (per Capitolo 3)"""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    years = ['2021', '2022', '2023', '2024']
    on_premise = np.array([77, 64, 50, 33])
    hybrid = np.array([15, 24, 32, 44])
    full_cloud = np.array([8, 12, 18, 23])
    
    x = np.arange(len(years))
    width = 0.6
    
    # Stacked bars
    ax.bar(x, on_premise, width, label='On-Premise', color=COLOR_DANGER, alpha=0.8)
    ax.bar(x, hybrid, width, bottom=on_premise, label='Hybrid Cloud', 
           color=COLOR_PRIMARY, alpha=0.8)
    ax.bar(x, full_cloud, width, bottom=on_premise+hybrid,
           label='Full Cloud', color=COLOR_SUCCESS, alpha=0.8)
    
    # Trend line
    cloud_total = hybrid + full_cloud
    ax2 = ax.twinx()
    ax2.plot(x, cloud_total, 'k--', linewidth=2.5, marker='o', markersize=8)
    ax2.set_ylabel('Adozione Cloud Totale (%)')
    ax2.set_ylim(0, 100)
    
    ax.set_ylabel('Distribuzione (%)')
    ax.set_xlabel('Anno')
    ax.set_title('Evoluzione dell\'Adozione Cloud nella GDO Europea',
                 fontsize=13, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(years)
    ax.legend(loc='upper left')
    ax.grid(True, axis='y', alpha=0.3)
    
    plt.tight_layout()
    return fig, 'fig_3_2_cloud_adoption'

def create_fig_3_4_tco_comparison():
    """Fig 3.4: Confronto TCO (per Capitolo 3)"""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    years = np.arange(0, 6)
    tco_trad = np.array([100, 180, 265, 355, 450, 550])
    tco_cloud = np.array([120, 170, 220, 275, 330, 390])
    
    # Area risparmio
    ax.fill_between(years[2:], tco_trad[2:], tco_cloud[2:],
                    alpha=0.3, color=COLOR_SUCCESS, label='Risparmio')
    
    # Linee TCO
    ax.plot(years, tco_trad, 'r--', linewidth=2.5, label='TCO On-Premise', 
            marker='v', markersize=8)
    ax.plot(years, tco_cloud, 'b-', linewidth=2.5, label='TCO Cloud-Ibrido',
            marker='o', markersize=8)
    
    # Break-even
    ax.plot(1.31, 198, 'r*', markersize=15, zorder=5)
    ax.annotate('Break-even\n15.7 mesi', xy=(1.31, 198), xytext=(0.8, 250),
                arrowprops=dict(arrowstyle='->', color=COLOR_WARNING, lw=2),
                fontsize=10, fontweight='bold',
                bbox=dict(boxstyle="round,pad=0.3", facecolor='white',
                         edgecolor=COLOR_WARNING, linewidth=2))
    
    ax.set_xlabel('Anni dall\'Implementazione')
    ax.set_ylabel('TCO Cumulativo (Indice base=100)')
    ax.set_title('Confronto Total Cost of Ownership - Cloud vs On-Premise',
                 fontsize=13, fontweight='bold')
    ax.legend(loc='upper left')
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    return fig, 'fig_3_4_tco_comparison'

# ========== CAPITOLO 5: SINTESI ==========

def create_fig_5_2_roi_progression():
    """Fig 5.2: Progressione ROI (per Capitolo 5)"""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    quarters = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8']
    roi = [-15, 8, 34, 67, 112, 178, 234, 287]
    
    colors = [COLOR_DANGER if v < 0 else COLOR_SUCCESS for v in roi]
    bars = ax.bar(quarters, roi, color=colors, edgecolor='black',
                  linewidth=1.5, alpha=0.8)
    
    # Linea zero
    ax.axhline(y=0, color='black', linewidth=1.5)
    
    # Valori sulle barre
    for bar, val in zip(bars, roi):
        height = bar.get_height()
        y_pos = height + (10 if height > 0 else -20)
        ax.text(bar.get_x() + bar.get_width()/2, y_pos,
               f'{val}%', ha='center', va='bottom' if height > 0 else 'top',
               fontweight='bold')
    
    # Target
    ax.axhline(y=287, color=COLOR_WARNING, linestyle='--', linewidth=2)
    ax.text(7.5, 295, 'Target: 287%', fontsize=10, fontweight='bold',
             color=COLOR_WARNING)
    
    ax.set_ylabel('ROI Cumulativo (%)')
    ax.set_title('Progressione del Return on Investment (24 mesi)',
                 fontsize=13, fontweight='bold')
    ax.grid(True, alpha=0.3, axis='y')
    ax.set_ylim(-50, 320)
    
    plt.tight_layout()
    return fig, 'fig_5_2_roi_progression'

# ========== MAIN ==========
def main():
    """Genera figure per i capitoli 2-5"""
    print("=" * 60)
    print("GENERAZIONE FIGURE CAPITOLI 2-5 - TESI GDO")
    print("=" * 60)
    
    # Mapping figure -> capitolo
    figures_map = {
        2: [create_fig_2_1_cyber_evolution, create_fig_2_2_attack_types, 
            create_fig_2_5_assa_reduction],
        3: [create_fig_3_2_cloud_adoption, create_fig_3_4_tco_comparison],
        5: [create_fig_5_2_roi_progression]
    }
    
    for chapter, figure_funcs in figures_map.items():
        print(f"\n--- Capitolo {chapter} ---")
        output_dir = create_output_directory(chapter)
        
        for func in figure_funcs:
            fig, filename = func()
            filepath = os.path.join(output_dir, filename)
            fig.savefig(f"{filepath}.pdf", format='pdf', bbox_inches='tight')
            fig.savefig(f"{filepath}.png", format='png', dpi=300, bbox_inches='tight')
            plt.close(fig)
            print(f"✓ Salvato: {filename}")
    
    print("\n" + "=" * 60)
    print("COMPLETATO! Figure salvate in thesis_figures/cap[N]/")
    print("=" * 60)

if __name__ == "__main__":
    main()