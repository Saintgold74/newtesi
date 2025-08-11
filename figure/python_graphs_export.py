#!/usr/bin/env python3
"""
Script per generare tutti i grafici del Capitolo 1 della tesi GDO
Genera file PDF vettoriali pronti per l'inclusione in LaTeX
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle, Wedge
from matplotlib.lines import Line2D
import os

# Configurazione matplotlib per output di qualità
plt.rcParams['font.size'] = 10
plt.rcParams['axes.labelsize'] = 11
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['xtick.labelsize'] = 9
plt.rcParams['ytick.labelsize'] = 9
plt.rcParams['legend.fontsize'] = 9
plt.rcParams['figure.dpi'] = 150
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['savefig.bbox'] = 'tight'

# Palette colori professionale
COLOR_PRIMARY = '#2E86AB'
COLOR_SECONDARY = '#A23B72'
COLOR_SUCCESS = '#73AB84'
COLOR_WARNING = '#F18F01'
COLOR_DANGER = '#C73E1D'
COLOR_NEUTRAL = '#7A7A7A'

def create_output_directory():
    """Crea la directory di output se non esiste"""
    output_dir = "thesis_figures"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"✓ Creata directory: {output_dir}/")
    return output_dir

def save_figure(fig, filename, output_dir):
    """Salva la figura in PDF e PNG"""
    base_path = os.path.join(output_dir, filename)
    fig.savefig(f"{base_path}.pdf", format='pdf', bbox_inches='tight')
    fig.savefig(f"{base_path}.png", format='png', dpi=300, bbox_inches='tight')
    print(f"✓ Salvato: {filename}.pdf e {filename}.png")

# ========== FIGURA 1.1: Framework GIST ==========
def create_fig_1_1_gist_framework():
    """Framework GIST con i 4 componenti principali"""
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_xlim(-6, 6)
    ax.set_ylim(-6, 6)
    ax.axis('off')
    
    # Componenti del framework
    components = {
        'Governance': {
            'pos': (-3, 3),
            'color': COLOR_PRIMARY,
            'items': ['• Politiche', '• Processi', '• Risk Mgmt', '• KPI']
        },
        'Infrastructure': {
            'pos': (3, 3),
            'color': COLOR_SUCCESS,
            'items': ['• Fondamenta', '• SD-WAN', '• Cloud', '• Edge']
        },
        'Security': {
            'pos': (-3, -3),
            'color': COLOR_DANGER,
            'items': ['• Zero Trust', '• Detection', '• Response', '• Protection']
        },
        'Transformation': {
            'pos': (3, -3),
            'color': COLOR_WARNING,
            'items': ['• Change Mgmt', '• Migration', '• Training', '• Innovation']
        }
    }
    
    # Nodo centrale
    center = Circle((0, 0), 1.5, color=COLOR_SECONDARY, alpha=0.9, zorder=10)
    ax.add_patch(center)
    ax.text(0, 0, 'GIST\nFramework', ha='center', va='center', 
            fontsize=16, fontweight='bold', color='white', zorder=11)
    
    # Disegna componenti e connessioni
    for name, props in components.items():
        x, y = props['pos']
        
        # Box del componente
        box = FancyBboxPatch((x-1.8, y-1.2), 3.6, 2.4,
                            boxstyle="round,pad=0.1",
                            facecolor=props['color'],
                            edgecolor='darkgray',
                            alpha=0.8,
                            linewidth=2)
        ax.add_patch(box)
        
        # Nome componente
        ax.text(x, y+0.7, name, ha='center', va='center',
                fontsize=13, fontweight='bold', color='white')
        
        # Elementi del componente
        for i, item in enumerate(props['items']):
            ax.text(x, y+0.2-i*0.3, item, ha='center', va='center',
                    fontsize=9, color='white')
        
        # Freccia bidirezionale con il centro
        ax.annotate('', xy=(x*0.4, y*0.4), xytext=(0, 0),
                   arrowprops=dict(arrowstyle='<->', color='gray', 
                                 lw=2, alpha=0.6))
    
    # Connessioni tra componenti
    connections = [
        ((-3, 3), (3, 3), 'Standards'),
        ((3, 3), (3, -3), 'Resilienza'),
        ((3, -3), (-3, -3), 'Sicurezza'),
        ((-3, -3), (-3, 3), 'Compliance')
    ]
    
    for start, end, label in connections:
        mid_x = (start[0] + end[0]) / 2
        mid_y = (start[1] + end[1]) / 2
        ax.plot([start[0], end[0]], [start[1], end[1]], 
                'k--', alpha=0.3, linewidth=1)
        ax.text(mid_x, mid_y, label, fontsize=9, ha='center',
                bbox=dict(boxstyle="round,pad=0.3", 
                         facecolor='white', edgecolor='gray', alpha=0.8))
    
    # Metriche chiave
    metrics_text = 'Metriche Chiave: Availability ≥99.95% | TCO -38% | ASSA -42% | ROI 287%'
    ax.text(0, -5.5, metrics_text, ha='center', va='center',
            fontsize=11, fontweight='bold',
            bbox=dict(boxstyle="round,pad=0.5", 
                     facecolor='lightgray', alpha=0.8))
    
    plt.title('Framework GIST: Integrazione delle Quattro Dimensioni',
              fontsize=14, fontweight='bold', pad=20)
    
    return fig

# ========== FIGURA 1.2: Evoluzione Attacchi Cyber ==========
def create_fig_1_2_cyber_evolution():
    """Grafico evoluzione attacchi cyber 2020-2025"""
    fig, ax1 = plt.subplots(figsize=(10, 6))
    
    years = np.array([2020, 2021, 2022, 2023, 2024, 2025])
    incidents = np.array([142, 187, 312, 584, 721, 847])
    impact = np.array([23, 34, 67, 124, 189, 234])
    
    # Asse primario - Incidenti
    color1 = COLOR_DANGER
    ax1.set_xlabel('Anno', fontsize=11)
    ax1.set_ylabel('Numero di Incidenti', color=color1, fontsize=11)
    
    # Area sotto la curva
    ax1.fill_between(years, 0, incidents, alpha=0.2, color=color1)
    
    # Linea incidenti
    line1 = ax1.plot(years, incidents, color=color1, marker='o',
                     linewidth=2.5, markersize=8, label='Incidenti')
    
    # Linea tratteggiata per proiezione 2025
    ax1.plot([2024, 2025], [721, 847], 'r--', alpha=0.6, linewidth=2)
    
    ax1.tick_params(axis='y', labelcolor=color1)
    ax1.grid(True, alpha=0.3, linestyle='--')
    
    # Asse secondario - Impatto economico
    ax2 = ax1.twinx()
    color2 = COLOR_PRIMARY
    ax2.set_ylabel('Impatto Economico (M€)', color=color2, fontsize=11)
    
    line2 = ax2.plot(years, impact, color=color2, marker='s',
                     linewidth=2.5, markersize=8, label='Impatto (M€)')
    
    # Linea tratteggiata per proiezione 2025
    ax2.plot([2024, 2025], [189, 234], 'b--', alpha=0.6, linewidth=2)
    
    ax2.tick_params(axis='y', labelcolor=color2)
    
    # Annotazione incremento 312%
    ax1.annotate('+312%\n(2021-2023)',
                xy=(2023, 584), xytext=(2022.3, 700),
                arrowprops=dict(arrowstyle='->', color=color1, lw=2),
                fontsize=12, fontweight='bold', color=color1,
                bbox=dict(boxstyle="round,pad=0.3", facecolor='white',
                         edgecolor=color1, linewidth=2))
    
    # Nota proiezione
    ax1.text(2025, 870, '(Proiezione)', fontsize=9, 
             ha='center', color=color1, style='italic')
    
    # Legenda combinata
    lines = line1 + line2
    labels = [l.get_label() for l in lines]
    ax1.legend(lines, labels, loc='upper left', frameon=True)
    
    ax1.set_xlim(2019.5, 2025.5)
    ax1.set_ylim(0, 950)
    ax2.set_ylim(0, 250)
    
    plt.title('Evoluzione degli Attacchi Cyber al Settore Retail (2020-2025)',
              fontsize=13, fontweight='bold')
    
    return fig

# ========== FIGURA 1.3: Tipologie di Attacco ==========
def create_fig_1_3_attack_types():
    """Distribuzione tipologie di attacco"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Dati
    types = ['Ransomware', 'Data Breach', 'Supply Chain', 
             'POS Malware', 'Cyber-Physical', 'Altri']
    percentages = [31, 24, 18, 12, 8, 7]
    impacts = [3.2, 2.8, 2.1, 1.5, 0.9, 0.7]
    colors = [COLOR_DANGER, COLOR_PRIMARY, COLOR_WARNING,
              COLOR_SUCCESS, COLOR_SECONDARY, COLOR_NEUTRAL]
    
    # Grafico a torta (donut)
    wedges, texts, autotexts = ax1.pie(percentages, labels=types,
                                       colors=colors, autopct='%1.0f%%',
                                       startangle=90, pctdistance=0.85,
                                       wedgeprops=dict(width=0.5))
    
    # Centro del donut
    ax1.text(0, 0, '1.847\nIncidenti', ha='center', va='center',
             fontsize=12, fontweight='bold')
    
    # Formattazione testi
    for text in texts:
        text.set_fontsize(10)
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
    
    ax1.set_title('Distribuzione per Tipologia', fontsize=12, fontweight='bold')
    
    # Grafico a barre orizzontali - Impatto
    y_pos = np.arange(len(types))
    bars = ax2.barh(y_pos, impacts, color=colors, alpha=0.8, height=0.6)
    
    ax2.set_yticks(y_pos)
    ax2.set_yticklabels(types)
    ax2.set_xlabel('Impatto Medio (M€)', fontsize=10)
    ax2.set_title('Impatto Economico Medio', fontsize=12, fontweight='bold')
    
    # Valori sulle barre
    for bar, val in zip(bars, impacts):
        width = bar.get_width()
        ax2.text(width + 0.05, bar.get_y() + bar.get_height()/2,
                f'{val:.1f}M€', va='center', fontsize=9)
    
    ax2.set_xlim(0, max(impacts) * 1.15)
    ax2.grid(True, axis='x', alpha=0.3, linestyle='--')
    
    plt.tight_layout()
    return fig

# ========== FIGURA 1.4: Adozione Cloud ==========
def create_fig_1_4_cloud_adoption():
    """Trend adozione cloud nella GDO"""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    years = ['2021', '2022', '2023', '2024']
    on_premise = np.array([77, 64, 50, 33])
    hybrid = np.array([15, 24, 32, 44])
    full_cloud = np.array([8, 12, 18, 23])
    
    x = np.arange(len(years))
    width = 0.6
    
    # Stacked bars
    p1 = ax.bar(x, on_premise, width, label='On-Premise',
                color=COLOR_DANGER, alpha=0.8)
    p2 = ax.bar(x, hybrid, width, bottom=on_premise,
                label='Hybrid Cloud', color=COLOR_PRIMARY, alpha=0.8)
    p3 = ax.bar(x, full_cloud, width, bottom=on_premise+hybrid,
                label='Full Cloud', color=COLOR_SUCCESS, alpha=0.8)
    
    # Percentuali nelle barre
    for i in range(len(years)):
        # On-premise
        if on_premise[i] > 10:
            ax.text(x[i], on_premise[i]/2, f'{on_premise[i]}%',
                   ha='center', va='center', color='white', fontweight='bold')
        # Hybrid
        if hybrid[i] > 10:
            ax.text(x[i], on_premise[i] + hybrid[i]/2, f'{hybrid[i]}%',
                   ha='center', va='center', color='white', fontweight='bold')
        # Full cloud
        if full_cloud[i] > 10:
            ax.text(x[i], on_premise[i] + hybrid[i] + full_cloud[i]/2, f'{full_cloud[i]}%',
                   ha='center', va='center', color='white', fontweight='bold')
    
    # Trend line cloud totale
    cloud_total = hybrid + full_cloud
    ax2 = ax.twinx()
    ax2.plot(x, cloud_total, 'k--', linewidth=2.5, marker='o', 
             markersize=8, label='Cloud Totale')
    ax2.set_ylabel('Adozione Cloud Totale (%)', fontsize=11)
    ax2.set_ylim(0, 100)
    
    # Annotazione
    ax.annotate(f'{cloud_total[-1]}% Cloud\nAdoption',
               xy=(x[-1], 100), xytext=(x[-2], 85),
               arrowprops=dict(arrowstyle='->', color='black', lw=1.5),
               fontsize=11, fontweight='bold',
               bbox=dict(boxstyle="round,pad=0.3", facecolor='yellow', alpha=0.7))
    
    ax.set_ylabel('Distribuzione (%)', fontsize=11)
    ax.set_xlabel('Anno', fontsize=11)
    ax.set_title('Evoluzione dell\'Adozione Cloud nella GDO Europea',
                 fontsize=13, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(years)
    ax.set_ylim(0, 100)
    ax.legend(loc='upper left')
    ax.grid(True, axis='y', alpha=0.3, linestyle='--')
    
    plt.tight_layout()
    return fig

# ========== FIGURA 1.5: Confronto TCO ==========
def create_fig_1_5_tco_comparison():
    """Confronto TCO architetture"""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    years = np.arange(0, 6)
    tco_trad = np.array([100, 180, 265, 355, 450, 550])
    tco_cloud = np.array([120, 170, 220, 275, 330, 390])
    
    # Area di risparmio
    ax.fill_between(years[2:], tco_trad[2:], tco_cloud[2:],
                    alpha=0.3, color=COLOR_SUCCESS,
                    label='Area di Risparmio')
    
    # Linee TCO
    ax.plot(years, tco_trad, 'r--', linewidth=2.5,
            label='TCO On-Premise', marker='v', markersize=8)
    ax.plot(years, tco_cloud, 'b-', linewidth=2.5,
            label='TCO Cloud-Ibrido', marker='o', markersize=8)
    
    # Break-even point
    break_x, break_y = 1.31, 198
    ax.plot(break_x, break_y, 'r*', markersize=15, zorder=5)
    ax.annotate('Break-even\n15.7 mesi',
                xy=(break_x, break_y), xytext=(break_x-0.5, break_y+50),
                arrowprops=dict(arrowstyle='->', color=COLOR_WARNING, lw=2),
                fontsize=10, fontweight='bold', color=COLOR_WARNING,
                bbox=dict(boxstyle="round,pad=0.3", facecolor='white',
                         edgecolor=COLOR_WARNING, linewidth=2))
    
    # Risparmio finale
    final_saving = (tco_trad[-1] - tco_cloud[-1]) / tco_trad[-1] * 100
    ax.text(4.5, 480, f'Risparmio\n{final_saving:.1f}%',
            fontsize=11, fontweight='bold', color=COLOR_SUCCESS,
            ha='center', bbox=dict(boxstyle="round,pad=0.3",
                                 facecolor='white', edgecolor=COLOR_SUCCESS,
                                 linewidth=2))
    
    # Valori di risparmio annuali
    for i in range(2, 6):
        saving = tco_trad[i] - tco_cloud[i]
        ax.text(i, tco_cloud[i]-20, f'+{saving}', fontsize=9,
                ha='center', color=COLOR_SUCCESS, fontweight='bold')
    
    ax.set_xlabel('Anni dall\'Implementazione', fontsize=11)
    ax.set_ylabel('TCO Cumulativo (Indice base=100)', fontsize=11)
    ax.set_title('Confronto Total Cost of Ownership - Cloud vs On-Premise',
                 fontsize=13, fontweight='bold')
    ax.legend(loc='upper left')
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.set_xlim(-0.2, 5.2)
    ax.set_ylim(0, 600)
    
    return fig

# ========== FIGURA 1.6: Riduzione ASSA ==========
def create_fig_1_6_assa_reduction():
    """Riduzione superficie di attacco con Zero Trust"""
    fig = plt.figure(figsize=(14, 6))
    
    categories = ['Network\nExposure', 'Endpoint\nVuln.', 'Identity\nMgmt',
                 'Data\nProtection', 'Application\nSecurity', 'Physical\nSecurity']
    
    traditional = [85, 72, 68, 75, 70, 65]
    zero_trust = [45, 38, 42, 48, 40, 52]
    reduction = [(traditional[i]-zero_trust[i])/traditional[i]*100 
                 for i in range(len(traditional))]
    
    # Subplot 1: Radar chart
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
    ax1.set_yticks([20, 40, 60, 80, 100])
    ax1.grid(True)
    ax1.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1))
    ax1.set_title('Confronto Superficie di Attacco', fontsize=11, pad=20)
    
    # Subplot 2: Riduzione percentuale
    ax2 = plt.subplot(122)
    
    y_pos = np.arange(len(categories))
    bars = ax2.barh(y_pos, reduction, color=COLOR_SUCCESS, alpha=0.8)
    
    ax2.set_yticks(y_pos)
    ax2.set_yticklabels(categories)
    ax2.set_xlabel('Riduzione (%)', fontsize=10)
    ax2.set_title('Riduzione Percentuale ASSA', fontsize=11)
    
    # Valori sulle barre
    for bar, val in zip(bars, reduction):
        width = bar.get_width()
        ax2.text(width + 1, bar.get_y() + bar.get_height()/2,
                f'{val:.1f}%', va='center', fontsize=9, fontweight='bold')
    
    # Media
    avg = np.mean(reduction)
    ax2.axvline(x=avg, color=COLOR_DANGER, linestyle='--', linewidth=2)
    ax2.text(avg, -0.7, f'Media: {avg:.1f}%', ha='center',
             fontsize=10, fontweight='bold', color=COLOR_DANGER)
    
    ax2.set_xlim(0, max(reduction) * 1.15)
    ax2.grid(True, axis='x', alpha=0.3, linestyle='--')
    
    plt.suptitle('Riduzione della Superficie di Attacco (ASSA) con Zero Trust',
                 fontsize=14, fontweight='bold')
    plt.tight_layout()
    
    return fig

# ========== FIGURA 1.7: Progressione ROI ==========
def create_fig_1_7_roi_progression():
    """Progressione del ROI"""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), 
                                   height_ratios=[3, 1])
    
    quarters = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8']
    roi = [-15, 8, 34, 67, 112, 178, 234, 287]
    investment = [100, 180, 230, 250, 260, 265, 268, 270]
    returns = [85, 188, 264, 317, 372, 443, 502, 557]
    
    # Grafico ROI
    colors = [COLOR_DANGER if v < 0 else COLOR_SUCCESS for v in roi]
    bars = ax1.bar(quarters, roi, color=colors, edgecolor='black',
                   linewidth=1.5, alpha=0.8)
    
    # Linea zero
    ax1.axhline(y=0, color='black', linestyle='-', linewidth=1.5)
    
    # Valori sulle barre
    for bar, val in zip(bars, roi):
        height = bar.get_height()
        y_pos = height + (10 if height > 0 else -20)
        v_align = 'bottom' if height > 0 else 'top'
        ax1.text(bar.get_x() + bar.get_width()/2, y_pos,
                f'{val}%', ha='center', va=v_align,
                fontweight='bold', fontsize=9)
    
    # Target line
    ax1.axhline(y=287, color=COLOR_WARNING, linestyle='--', 
                linewidth=2, alpha=0.7)
    ax1.text(7.5, 295, 'Target: 287%', fontsize=10, 
             fontweight='bold', color=COLOR_WARNING)
    
    # Break-even
    ax1.plot(1.5, 0, 'ro', markersize=12)
    ax1.annotate('Break-even', xy=(1.5, 0), xytext=(1.5, 50),
                arrowprops=dict(arrowstyle='->', color='red', lw=1.5),
                fontsize=10, fontweight='bold', ha='center')
    
    ax1.set_ylabel('ROI Cumulativo (%)', fontsize=11)
    ax1.set_title('Progressione del Return on Investment (24 mesi)',
                  fontsize=13, fontweight='bold')
    ax1.grid(True, alpha=0.3, linestyle='--', axis='y')
    ax1.set_ylim(-50, 320)
    
    # Grafico investimenti vs ritorni
    x = np.arange(len(quarters))
    ax2.plot(x, investment, 'b-', marker='s', linewidth=2,
             markersize=6, label='Investimento')
    ax2.plot(x, returns, 'g-', marker='^', linewidth=2,
             markersize=6, label='Ritorno')
    
    # Area profitto
    ax2.fill_between(x, investment, returns,
                    where=(np.array(returns) > np.array(investment)),
                    color=COLOR_SUCCESS, alpha=0.3, label='Profitto')
    
    ax2.set_xlabel('Trimestri', fontsize=11)
    ax2.set_ylabel('Valore (k€)', fontsize=10)
    ax2.set_xticks(x)
    ax2.set_xticklabels(quarters)
    ax2.legend(loc='upper left')
    ax2.grid(True, alpha=0.3, linestyle='--')
    
    plt.tight_layout()
    return fig

# ========== MAIN: Genera tutti i grafici ==========
def main():
    """Funzione principale per generare tutti i grafici"""
    print("=" * 60)
    print("GENERAZIONE GRAFICI CAPITOLO 1 - TESI GDO")
    print("=" * 60)
    
    # Crea directory output
    output_dir = create_output_directory()
    
    # Dizionario figure
    figures = {
        'fig_1_1_gist_framework': ('Framework GIST', create_fig_1_1_gist_framework),
        'fig_1_2_cyber_evolution': ('Evoluzione Attacchi Cyber', create_fig_1_2_cyber_evolution),
        'fig_1_3_attack_types': ('Tipologie di Attacco', create_fig_1_3_attack_types),
        'fig_1_4_cloud_adoption': ('Adozione Cloud', create_fig_1_4_cloud_adoption),
        'fig_1_5_tco_comparison': ('Confronto TCO', create_fig_1_5_tco_comparison),
        'fig_1_6_assa_reduction': ('Riduzione ASSA', create_fig_1_6_assa_reduction),
        'fig_1_7_roi_progression': ('Progressione ROI', create_fig_1_7_roi_progression)
    }
    
    # Genera e salva ogni figura
    for filename, (title, func) in figures.items():
        print(f"\nGenerando: {title}...")
        try:
            fig = func()
            save_figure(fig, filename, output_dir)
            plt.close(fig)
        except Exception as e:
            print(f"✗ Errore nella generazione di {filename}: {str(e)}")
    
    print("\n" + "=" * 60)
    print("GENERAZIONE COMPLETATA!")
    print(f"I grafici sono stati salvati in: {output_dir}/")
    print("\nPer includere in LaTeX, usa:")
    print("\\includegraphics[width=\\textwidth]{thesis_figures/nome_file.pdf}")
    print("=" * 60)

if __name__ == "__main__":
    main()