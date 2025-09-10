#!/usr/bin/env python3
"""
Script per generare le figure del Capitolo 1 della tesi GDO
Include solo le figure effettivamente citate nel capitolo:
- Figura 1.1: Framework GIST
- Figura 1.4: Struttura della Tesi
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle, ConnectionPatch
import numpy as np
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

# ========== FIGURA 1.1: FRAMEWORK GIST ==========
def create_fig_1_1_gist_framework():
    """
    Il Framework GIST: Integrazione delle quattro dimensioni fondamentali
    per la trasformazione sicura della GDO
    """
    fig, ax = plt.subplots(figsize=(12, 9))
    ax.set_xlim(-7, 7)
    ax.set_ylim(-7, 7)
    ax.axis('off')
    
    # Definizione componenti del framework
    components = {
        'Governance': {
            'pos': (-3.5, 3.5),
            'color': COLOR_PRIMARY,
            'items': ['• Politiche', '• Processi', '• Risk Management', '• KPI e Metriche'],
            'connections': ['Direttive', 'Standards', 'Compliance']
        },
        'Infrastructure': {
            'pos': (3.5, 3.5),
            'color': COLOR_SUCCESS,
            'items': ['• Fondamenta Fisiche', '• Reti SD-WAN', '• Cloud Ibrido', '• Edge Computing'],
            'connections': ['Requisiti', 'Standards', 'Resilienza']
        },
        'Security': {
            'pos': (-3.5, -3.5),
            'color': COLOR_DANGER,
            'items': ['• Zero Trust', '• Threat Detection', '• Incident Response', '• Data Protection'],
            'connections': ['Controlli', 'Compliance', 'Sicurezza']
        },
        'Transformation': {
            'pos': (3.5, -3.5),
            'color': COLOR_WARNING,
            'items': ['• Change Management', '• Migration Path', '• Training', '• Innovation'],
            'connections': ['Evoluzione', 'Resilienza', 'Sicurezza']
        }
    }
    
    # Nodo centrale GIST
    center = Circle((0, 0), 1.8, color=COLOR_SECONDARY, alpha=0.9, zorder=10)
    ax.add_patch(center)
    ax.text(0, 0.3, 'GIST', ha='center', va='center', 
            fontsize=20, fontweight='bold', color='white', zorder=11)
    ax.text(0, -0.3, 'Framework\nIntegrato', ha='center', va='center', 
            fontsize=12, color='white', zorder=11)
    
    # Disegna i quattro componenti
    for name, props in components.items():
        x, y = props['pos']
        
        # Box del componente con ombra
        shadow = FancyBboxPatch((x-2.2, y-1.4), 4.4, 2.8,
                               boxstyle="round,pad=0.1",
                               facecolor='gray',
                               alpha=0.3,
                               zorder=1)
        ax.add_patch(shadow)
        
        # Box principale
        box = FancyBboxPatch((x-2, y-1.2), 4, 2.4,
                            boxstyle="round,pad=0.1",
                            facecolor=props['color'],
                            edgecolor='darkgray',
                            alpha=0.85,
                            linewidth=2,
                            zorder=2)
        ax.add_patch(box)
        
        # Nome del componente
        ax.text(x, y+0.8, name.upper(), ha='center', va='center',
                fontsize=14, fontweight='bold', color='white')
        
        # Elementi del componente
        for i, item in enumerate(props['items']):
            ax.text(x, y+0.3-i*0.35, item, ha='center', va='center',
                    fontsize=9, color='white')
        
        # Frecce bidirezionali con il centro
        angle = np.arctan2(y, x)
        start_x = x - 1.8 * np.cos(angle)
        start_y = y - 1.8 * np.sin(angle)
        end_x = 1.8 * np.cos(angle)
        end_y = 1.8 * np.sin(angle)
        
        ax.annotate('', xy=(end_x, end_y), xytext=(start_x, start_y),
                   arrowprops=dict(arrowstyle='<->', color='gray', 
                                 lw=2.5, alpha=0.7))
    
    # Labels delle connessioni con il centro
    ax.text(-1.8, 1.8, 'Direttive', ha='center', va='center',
            fontsize=9, bbox=dict(boxstyle="round,pad=0.3", 
                                facecolor='white', alpha=0.8))
    ax.text(1.8, 1.8, 'Requisiti', ha='center', va='center',
            fontsize=9, bbox=dict(boxstyle="round,pad=0.3", 
                                facecolor='white', alpha=0.8))
    ax.text(-1.8, -1.8, 'Controlli', ha='center', va='center',
            fontsize=9, bbox=dict(boxstyle="round,pad=0.3", 
                                facecolor='white', alpha=0.8))
    ax.text(1.8, -1.8, 'Evoluzione', ha='center', va='center',
            fontsize=9, bbox=dict(boxstyle="round,pad=0.3", 
                                facecolor='white', alpha=0.8))
    
    # Connessioni tra componenti (linee tratteggiate)
    connections = [
        ((-3.5, 3.5), (3.5, 3.5), 'Standards'),
        ((3.5, 3.5), (3.5, -3.5), 'Resilienza'),
        ((3.5, -3.5), (-3.5, -3.5), 'Sicurezza'),
        ((-3.5, -3.5), (-3.5, 3.5), 'Compliance')
    ]
    
    for start, end, label in connections:
        mid_x = (start[0] + end[0]) / 2
        mid_y = (start[1] + end[1]) / 2
        ax.plot([start[0], end[0]], [start[1], end[1]], 
                'k--', alpha=0.4, linewidth=1.5)
        ax.text(mid_x, mid_y, label, fontsize=9, ha='center',
                bbox=dict(boxstyle="round,pad=0.3", 
                         facecolor='white', edgecolor='gray', alpha=0.9))
    
    # Box metriche chiave in basso
    metrics_box = FancyBboxPatch((-6, -6.5), 12, 1,
                                boxstyle="round,pad=0.1",
                                facecolor='lightgray',
                                edgecolor='darkgray',
                                alpha=0.8,
                                linewidth=2)
    ax.add_patch(metrics_box)
    
    metrics_text = 'METRICHE CHIAVE: Availability ≥99.95% | TCO -38% | ASSA -42% | ROI 287%'
    ax.text(0, -6, metrics_text, ha='center', va='center',
            fontsize=12, fontweight='bold')
    
    # Titolo
    plt.title('Framework GIST: GDO Integrated Security Transformation',
              fontsize=16, fontweight='bold', pad=20)
    
    return fig

# ========== FIGURA 1.4: STRUTTURA DELLA TESI ==========
def create_fig_1_4_thesis_structure():
    """
    Struttura della Tesi e Interdipendenze tra Capitoli
    """
    fig, ax = plt.subplots(figsize=(12, 10))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 12)
    ax.axis('off')
    
    # Definizione capitoli con posizioni e contenuti
    chapters = {
        'Cap. 1': {
            'title': 'Introduzione',
            'pos': (5, 10.5),
            'width': 8,
            'height': 1,
            'color': COLOR_NEUTRAL,
            'content': 'Contesto • Problema • Framework GIST • Metodologia'
        },
        'Cap. 2': {
            'title': 'Threat Landscape',
            'pos': (2.5, 8),
            'width': 3.5,
            'height': 1.5,
            'color': COLOR_DANGER,
            'content': 'Analisi minacce\nZero Trust\nValidazione H2',
            'pages': '18-20 pp'
        },
        'Cap. 3': {
            'title': 'Evoluzione\nInfrastrutturale',
            'pos': (7.5, 8),
            'width': 3.5,
            'height': 1.5,
            'color': COLOR_SUCCESS,
            'content': 'Da fisico a cloud\nArchitetture ibride\nValidazione H1',
            'pages': '20-22 pp'
        },
        'Cap. 4': {
            'title': 'Compliance\nIntegrata',
            'pos': (5, 5.5),
            'width': 3.5,
            'height': 1.5,
            'color': COLOR_PRIMARY,
            'content': 'Multi-standard\nSinergie normative\nValidazione H3',
            'pages': '20-22 pp'
        },
        'Cap. 5': {
            'title': 'Sintesi e Direzioni',
            'pos': (5, 3),
            'width': 6,
            'height': 1.2,
            'color': COLOR_SECONDARY,
            'content': 'Framework validato • Roadmap • Future research',
            'pages': '8-10 pp'
        }
    }
    
    # Appendici
    appendices = {
        'pos': (5, 1),
        'width': 8,
        'height': 0.8,
        'color': 'lightgray',
        'content': 'A: Metodologia | B: Metriche | C: Algoritmi | D: Risultati'
    }
    
    # Disegna capitoli
    for cap, props in chapters.items():
        x, y = props['pos']
        w, h = props['width'], props['height']
        
        # Box principale
        box = FancyBboxPatch((x-w/2, y-h/2), w, h,
                            boxstyle="round,pad=0.05",
                            facecolor=props['color'],
                            edgecolor='darkgray',
                            alpha=0.8,
                            linewidth=2)
        ax.add_patch(box)
        
        # Titolo capitolo
        ax.text(x, y+h/4, f"{cap}: {props['title']}", 
                ha='center', va='center',
                fontsize=11, fontweight='bold', color='white')
        
        # Contenuto
        ax.text(x, y-h/4, props['content'], 
                ha='center', va='center',
                fontsize=8, color='white')
        
        # Pagine (se specificato)
        if 'pages' in props:
            ax.text(x+w/2-0.2, y+h/2-0.2, props['pages'], 
                    ha='right', va='top',
                    fontsize=7, color='white', style='italic')
    
    # Disegna appendici
    x, y = appendices['pos']
    w, h = appendices['width'], appendices['height']
    box = FancyBboxPatch((x-w/2, y-h/2), w, h,
                        boxstyle="round,pad=0.05",
                        facecolor=appendices['color'],
                        edgecolor='darkgray',
                        alpha=0.6,
                        linewidth=2)
    ax.add_patch(box)
    ax.text(x, y, f"APPENDICI: {appendices['content']}", 
            ha='center', va='center',
            fontsize=9, fontweight='bold')
    
    # Frecce di flusso principale
    main_flow = [
        ((5, 9.5), (2.5, 9)),      # Cap1 → Cap2
        ((5, 9.5), (7.5, 9)),      # Cap1 → Cap3
        ((2.5, 6.5), (5, 6.5)),    # Cap2 → Cap4
        ((7.5, 6.5), (5, 6.5)),    # Cap3 → Cap4
        ((5, 4), (5, 3.6))         # Cap4 → Cap5
    ]
    
    for start, end in main_flow:
        ax.annotate('', xy=end, xytext=start,
                   arrowprops=dict(arrowstyle='->', color='black', 
                                 lw=2, alpha=0.7))
    
    # Connessioni secondarie (interdipendenze)
    interdeps = [
        ((2.5, 7.25), (7.5, 7.25), 'Threat-Infrastructure\ninteraction'),
        ((3.5, 5.5), (6.5, 5.5), 'Security-Compliance\nintegration')
    ]
    
    for start, end, label in interdeps:
        ax.plot([start[0], end[0]], [start[1], end[1]], 
                'k:', alpha=0.5, linewidth=1.5)
        mid_x = (start[0] + end[0]) / 2
        ax.text(mid_x, start[1]-0.2, label, ha='center', va='top',
                fontsize=7, style='italic', alpha=0.7)
    
    # Ipotesi di ricerca
    hypotheses = [
        'H1: Cloud-Ibrido → SLA ≥99.95% + TCO -30%',
        'H2: Zero Trust → ASSA -35% + Latenza <50ms',
        'H3: Compliance Integrata → Costi -30-40%'
    ]
    
    y_start = 11.5
    for i, hyp in enumerate(hypotheses):
        ax.text(0.5, y_start-i*0.3, hyp, ha='left', va='center',
                fontsize=8, bbox=dict(boxstyle="round,pad=0.3", 
                                    facecolor='lightyellow', alpha=0.8))
    
    # Legenda metodologica
    ax.text(9.5, 11.5, 'Metodologia:\n• Simulazione Monte Carlo\n• Dati pilota (15 org)\n• Validazione empirica',
            ha='right', va='top', fontsize=8,
            bbox=dict(boxstyle="round,pad=0.3", 
                     facecolor='lightblue', alpha=0.8))
    
    # Titolo
    plt.title('Struttura della Tesi e Interdipendenze tra Capitoli',
              fontsize=16, fontweight='bold', pad=20)
    
    return fig

# ========== MAIN: Genera le figure del Capitolo 1 ==========
def main():
    """Funzione principale per generare le figure del Capitolo 1"""
    print("=" * 60)
    print("GENERAZIONE FIGURE CAPITOLO 1 - TESI GDO")
    print("=" * 60)
    
    # Crea directory output
    output_dir = create_output_directory()
    
    # Figure da generare
    figures = {
        'fig_1_1_gist_framework': ('Framework GIST', create_fig_1_1_gist_framework),
        'fig_1_4_thesis_structure': ('Struttura della Tesi', create_fig_1_4_thesis_structure)
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
    print(f"Le figure sono state salvate in: {output_dir}/")
    print("\nPer includere in LaTeX:")
    print("\\begin{figure}[htbp]")
    print("    \\centering")
    print("    \\includegraphics[width=0.9\\textwidth]{thesis_figures/fig_1_1_gist_framework.pdf}")
    print("    \\caption{Il Framework GIST: Integrazione delle quattro dimensioni fondamentali...}")
    print("    \\label{fig:gist_framework}")
    print("\\end{figure}")
    print("=" * 60)

if __name__ == "__main__":
    main()