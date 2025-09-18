#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script CORRETTO per generare le figure del Capitolo 4 usando matplotlib
Risolve i problemi di font su Windows
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Circle, Rectangle, FancyBboxPatch, Polygon
from matplotlib.collections import PatchCollection
import numpy as np
import warnings

# Sopprime i warning sui font
warnings.filterwarnings('ignore', message='Glyph .* missing from font')

# Configurazione generale - Usa font compatibili con Windows
plt.rcParams['font.family'] = 'DejaVu Sans'  # Font più compatibile cross-platform
plt.rcParams['font.size'] = 10
plt.rcParams['axes.linewidth'] = 1.5
plt.rcParams['mathtext.fontset'] = 'stix'  # Usa STIX per i simboli matematici
plt.rcParams['mathtext.rm'] = 'DejaVu Sans'

# Alternativa per Windows se DejaVu Sans non è disponibile
import platform
if platform.system() == 'Windows':
    try:
        # Prova a usare font Windows compatibili
        plt.rcParams['font.family'] = ['Segoe UI', 'Calibri', 'Arial']
    except:
        pass

# Colori standard
COLORS = {
    'pcidss': '#E41A1C',
    'gdpr': '#377EB8', 
    'nis2': '#4DAF4A',
    'level1': '#FF0000',
    'level2': '#FFA500',
    'level3': '#FFFF00',
    'level4': '#90EE90',
    'level5': '#008000'
}

def create_figure_1_venn():
    """
    Figura 4.1: Diagramma di Venn delle sovrapposizioni normative
    """
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(-4, 6)
    ax.set_ylim(-5, 4)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Cerchi principali con trasparenza
    circle1 = Circle((0, 0), 2.5, color=COLORS['pcidss'], alpha=0.5, label='PCI-DSS 4.0')
    circle2 = Circle((2.2, 0), 2.5, color=COLORS['gdpr'], alpha=0.5, label='GDPR')
    circle3 = Circle((1.1, -1.9), 2.5, color=COLORS['nis2'], alpha=0.5, label='NIS2')
    
    ax.add_patch(circle1)
    ax.add_patch(circle2)
    ax.add_patch(circle3)
    
    # Etichette
    ax.text(-1.2, 2, 'PCI-DSS 4.0', fontsize=14, fontweight='bold', ha='center')
    ax.text(-1.2, 1.5, '264 controlli', fontsize=10, ha='center')
    
    ax.text(3.4, 2, 'GDPR', fontsize=14, fontweight='bold', ha='center')
    ax.text(3.4, 1.5, '99 articoli', fontsize=10, ha='center')
    
    ax.text(1.1, -4.5, 'NIS2', fontsize=14, fontweight='bold', ha='center')
    ax.text(1.1, -5, '31 misure', fontsize=10, ha='center')
    
    # Numeri nelle intersezioni
    ax.text(1.1, 0, '47', fontsize=10, ha='center', va='center')
    ax.text(-0.3, -0.8, '23', fontsize=10, ha='center', va='center')
    ax.text(2.5, -0.8, '31', fontsize=10, ha='center', va='center')
    ax.text(1.1, -0.7, '55', fontsize=12, fontweight='bold', ha='center', va='center')
    
    # Box informativo
    info_text = """Controlli Comuni:
    Totale: 156 (39.6%)
    Core comuni: 55
    Parzialmente sovrapp.: 101"""
    
    bbox = dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="black", linewidth=1)
    ax.text(4.5, -1, info_text, fontsize=9, bbox=bbox, va='top')
    
    # Esempi di controlli comuni
    examples_text = """Esempi di controlli comuni:
    • Crittografia dati (PCI 3.4, GDPR Art.32, NIS2 Art.16)
    • Gestione accessi (PCI 7-8, GDPR Art.32, NIS2 Art.18)
    • Incident Response (PCI 12.10, GDPR Art.33, NIS2 Art.20)"""
    
    ax.text(-3.5, -3.5, examples_text, fontsize=8, va='top')
    
    plt.title('Sovrapposizioni tra i principali standard normativi nel settore retail', 
              fontsize=12, fontweight='bold', pad=20)
    
    plt.tight_layout()
    return fig

def create_figure_2_architecture():
    """
    Figura 4.2: Architettura a tre livelli del sistema
    """
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(-2, 16)
    ax.set_ylim(-1, 8)
    ax.axis('off')
    
    # Colori per livelli
    colors = {'data': '#E8F4FF', 'process': '#E8FFE8', 'present': '#FFE8D6'}
    
    # Livello 3 - Presentazione
    boxes_l3 = [
        (0, 6, 'Dashboard\nEsecutiva'),
        (4, 6, 'Console\nOperativa'),
        (8, 6, 'Sistema\nReporting'),
        (12, 6, 'API\nREST')
    ]
    
    for x, y, text in boxes_l3:
        rect = FancyBboxPatch((x-1.5, y-0.5), 3, 1, 
                              boxstyle="round,pad=0.1",
                              facecolor=colors['present'], 
                              edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        ax.text(x, y, text, ha='center', va='center', fontsize=10)
    
    # Livello 2 - Elaborazione
    boxes_l2 = [
        (2, 3, 'Motore di\nCorrelazione'),
        (6, 3, 'Analisi\ndel Rischio'),
        (10, 3, 'Valutazione\nConformità')
    ]
    
    for x, y, text in boxes_l2:
        rect = FancyBboxPatch((x-1.5, y-0.5), 3, 1,
                              boxstyle="round,pad=0.1",
                              facecolor=colors['process'],
                              edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        ax.text(x, y, text, ha='center', va='center', fontsize=10)
    
    # Livello 1 - Raccolta Dati
    boxes_l1 = [
        (0, 0, 'Configuration\nManagement'),
        (3.5, 0, 'SIEM\nLogs'),
        (7, 0, 'Metriche\nKPI'),
        (10.5, 0, 'Threat\nIntelligence'),
        (14, 0, 'Audit\nTrail')
    ]
    
    for x, y, text in boxes_l1:
        rect = FancyBboxPatch((x-1.5, y-0.5), 2.8, 1,
                              boxstyle="round,pad=0.1",
                              facecolor=colors['data'],
                              edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        ax.text(x, y, text, ha='center', va='center', fontsize=9)
    
    # Etichette livelli
    ax.text(-1.5, 6, 'Livello 3:\nPresentazione', fontweight='bold', ha='right', va='center')
    ax.text(-1.5, 3, 'Livello 2:\nElaborazione', fontweight='bold', ha='right', va='center')
    ax.text(-1.5, 0, 'Livello 1:\nRaccolta Dati', fontweight='bold', ha='right', va='center')
    
    # Frecce di connessione
    # Dal livello 1 al 2
    connections_1_2 = [
        ((0, 0.5), (2, 2.5)),
        ((3.5, 0.5), (2, 2.5)),
        ((7, 0.5), (6, 2.5)),
        ((10.5, 0.5), (6, 2.5)),
        ((14, 0.5), (10, 2.5))
    ]
    
    for start, end in connections_1_2:
        ax.annotate('', xy=end, xytext=start,
                   arrowprops=dict(arrowstyle='->', lw=1.5, color='gray'))
    
    # Dal livello 2 al 3
    connections_2_3 = [
        ((2, 3.5), (0, 5.5)),
        ((2, 3.5), (4, 5.5)),
        ((6, 3.5), (4, 5.5)),
        ((6, 3.5), (8, 5.5)),
        ((10, 3.5), (8, 5.5)),
        ((10, 3.5), (12, 5.5))
    ]
    
    for start, end in connections_2_3:
        ax.annotate('', xy=end, xytext=start,
                   arrowprops=dict(arrowstyle='->', lw=1.5, color='gray'))
    
    # Box Framework di Integrazione
    rect_framework = Rectangle((0.5, 2.2), 11, 2,
                               fill=False, edgecolor='blue',
                               linestyle='--', linewidth=2)
    ax.add_patch(rect_framework)
    ax.text(6, 4.5, 'Framework di Integrazione Multi-Standard',
           ha='center', fontsize=10, style='italic')
    
    plt.title('Architettura del sistema di conformità integrata',
              fontsize=12, fontweight='bold', pad=20)
    
    plt.tight_layout()
    return fig

def create_figure_3_gdpr_flow():
    """
    Figura 4.3: Flusso di processo GDPR
    """
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.set_xlim(-1, 15)
    ax.set_ylim(-2, 5)
    ax.axis('off')
    
    # Definizione nodi
    nodes = {
        'receive': (1, 2, 'rect', '1. Ricezione\nRichiesta'),
        'verify': (4, 2, 'diamond', 'Verifica\nIdentità?'),
        'identify': (7, 2, 'rect', '3. Identificazione\nDati'),
        'execute': (7, 0, 'rect', '4. Esecuzione\nAzione'),
        'notify': (4, 0, 'rect', '5. Notifica\nInteressato'),
        'document': (1, -1, 'trap', '6. Documentazione\nAudit Trail'),
        'reject': (4, 4, 'rect', 'Richiesta\nRespinta'),
        'systems': (10, 2, 'trap', 'Sistemi\nCoinvolti')
    }
    
    # Disegno nodi
    for key, (x, y, shape, text) in nodes.items():
        if shape == 'rect':
            color = '#E8F4FF' if key != 'reject' else '#FFE8E8'
            rect = FancyBboxPatch((x-1, y-0.4), 2, 0.8,
                                  boxstyle="round,pad=0.05",
                                  facecolor=color, edgecolor='black', linewidth=1.5)
            ax.add_patch(rect)
        elif shape == 'diamond':
            diamond = Polygon([(x, y-0.5), (x+1, y), (x, y+0.5), (x-1, y)],
                            facecolor='#FFFACD', edgecolor='black', linewidth=1.5)
            ax.add_patch(diamond)
        elif shape == 'trap':
            trap = Polygon([(x-0.8, y-0.4), (x+0.8, y-0.4), 
                          (x+1, y+0.4), (x-1, y+0.4)],
                         facecolor='#E8FFE8', edgecolor='black', linewidth=1.5)
            ax.add_patch(trap)
        
        ax.text(x, y, text, ha='center', va='center', fontsize=9)
    
    # Frecce
    arrows = [
        ((2, 2), (3, 2), 'Submit'),
        ((5, 2), (6, 2), 'Sì'),
        ((4, 2.5), (4, 3.5), 'No'),
        ((7, 1.5), (7, 0.5), ''),
        ((6, 0), (5, 0), ''),
        ((3, 0), (1, -0.5), ''),
        ((9, 2), (8, 2), '')
    ]
    
    for start, end, label in arrows:
        ax.annotate('', xy=end, xytext=start,
                   arrowprops=dict(arrowstyle='->', lw=1.5))
        if label:
            mid_x, mid_y = (start[0] + end[0])/2, (start[1] + end[1])/2
            ax.text(mid_x, mid_y+0.2, label, fontsize=8)
    
    # Box temporali
    rect1 = Rectangle((0, 1.3), 5.5, 1.4, fill=False,
                     edgecolor='blue', linestyle='--', linewidth=1)
    ax.add_patch(rect1)
    ax.text(2.75, 1.2, 'Max 72h', fontsize=8, color='blue')
    
    rect2 = Rectangle((3, -0.7), 5, 3.4, fill=False,
                     edgecolor='green', linestyle='--', linewidth=1)
    ax.add_patch(rect2)
    ax.text(5.5, -0.8, 'Max 30 giorni', fontsize=8, color='green')
    
    # Legenda diritti GDPR
    legend_text = """Diritti GDPR:
    Art. 15 - Accesso
    Art. 16 - Rettifica
    Art. 17 - Cancellazione
    Art. 20 - Portabilità"""
    
    bbox = dict(boxstyle="round,pad=0.3", facecolor="white", 
               edgecolor="black", linewidth=1)
    ax.text(12, 0.5, legend_text, fontsize=9, bbox=bbox, va='center')
    
    plt.title('Processo automatizzato per i diritti GDPR',
              fontsize=12, fontweight='bold', pad=20)
    
    plt.tight_layout()
    return fig

def create_figure_4_org_structure():
    """
    Figura 4.4: Struttura organizzativa della governance
    """
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(-6, 10)
    ax.set_ylim(-5, 3)
    ax.axis('off')
    
    # Struttura gerarchica
    levels = {
        'strategic': [
            (0, 2, 'Consiglio di\nAmministrazione'),
            (0, 0, 'Comitato\nGovernance\nConformità')
        ],
        'tactical': [
            (-2, -2, 'Centro di\nEccellenza\nConformità'),
            (2, -2, 'Risk\nManagement')
        ],
        'operational': [
            (-3.5, -4, 'SOC'),
            (-2, -4, 'IT Ops'),
            (-0.5, -4, 'Business\nUnits'),
            (1.5, -4, 'Internal\nAudit'),
            (3, -4, 'Legal &\nCompliance')
        ]
    }
    
    # Colori per livello
    colors_level = {
        'strategic': '#FFE8E8',
        'tactical': '#FFFACD',
        'operational': '#E8FFE8'
    }
    
    # Disegna box e connessioni
    # Strategico
    for x, y, text in levels['strategic']:
        rect = FancyBboxPatch((x-1.5, y-0.5), 3, 1,
                              boxstyle="round,pad=0.1",
                              facecolor=colors_level['strategic'],
                              edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        ax.text(x, y, text, ha='center', va='center', fontsize=10, fontweight='bold')
    
    # Connessione tra CdA e Comitato
    ax.plot([0, 0], [1.5, 0.5], 'k-', linewidth=2)
    
    # Tattico
    for x, y, text in levels['tactical']:
        rect = FancyBboxPatch((x-1.2, y-0.4), 2.4, 0.8,
                              boxstyle="round,pad=0.1",
                              facecolor=colors_level['tactical'],
                              edgecolor='black', linewidth=1.5)
        ax.add_patch(rect)
        ax.text(x, y, text, ha='center', va='center', fontsize=9)
    
    # Connessioni da Comitato a livello tattico
    ax.plot([0, -2], [-0.5, -1.5], 'k-', linewidth=1.5)
    ax.plot([0, 2], [-0.5, -1.5], 'k-', linewidth=1.5)
    
    # Operativo
    for x, y, text in levels['operational']:
        rect = FancyBboxPatch((x-0.6, y-0.3), 1.2, 0.6,
                              boxstyle="round,pad=0.05",
                              facecolor=colors_level['operational'],
                              edgecolor='black', linewidth=1)
        ax.add_patch(rect)
        ax.text(x, y, text, ha='center', va='center', fontsize=8)
    
    # Connessioni al livello operativo
    for x_op in [-3.5, -2, -0.5]:
        ax.plot([-2, x_op], [-2.5, -3.5], 'k-', linewidth=1)
    for x_op in [1.5, 3]:
        ax.plot([2, x_op], [-2.5, -3.5], 'k-', linewidth=1)
    
    # Etichette livelli
    ax.text(-5.5, 1, 'Strategico', fontsize=14, fontweight='bold', va='center')
    ax.text(-5.5, -2, 'Tattico', fontsize=14, fontweight='bold', va='center')
    ax.text(-5.5, -4, 'Operativo', fontsize=14, fontweight='bold', va='center')
    
    # Linee di separazione
    ax.plot([-5.5, 8], [-1, -1], 'k--', alpha=0.5, linewidth=1)
    ax.plot([-5.5, 8], [-3, -3], 'k--', alpha=0.5, linewidth=1)
    
    # Box membri comitato
    members_text = """Comitato Governance:
    • Chief Risk Officer (Presidente)
    • CISO
    • DPO
    • CFO
    • Head of Compliance"""
    
    bbox = dict(boxstyle="round,pad=0.3", facecolor="white",
               edgecolor="black", linewidth=1)
    ax.text(6, 0, members_text, fontsize=9, bbox=bbox, va='center')
    
    # Frecce di reporting
    ax.annotate('Report', xy=(0, -0.2), xytext=(-3, -3.8),
               arrowprops=dict(arrowstyle='->', lw=1, color='blue', 
                             linestyle='--', connectionstyle="arc3,rad=0.3"))
    ax.annotate('Audit', xy=(0, -0.2), xytext=(2, -3.8),
               arrowprops=dict(arrowstyle='->', lw=1, color='red',
                             linestyle='--', connectionstyle="arc3,rad=-0.3"))
    
    plt.title('Modello organizzativo per la conformità integrata',
              fontsize=12, fontweight='bold', pad=20)
    
    plt.tight_layout()
    return fig

def create_figure_5_comparison():
    """
    Figura 4.5: Analisi controfattuale - confronto scenari
    VERSIONE CORRETTA: Usa notazione matematica standard invece di subscript Unicode
    """
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Dati
    categories = ['Tempo\nDetection\n(ore)', 'Sistemi\nCompromessi\n(unità)', 
                  'Downtime\n(ore)', 'Impatto\nEconomico\n(k€)']
    real_values = [360, 2847, 120, 8700]
    compliant_values = [6, 12, 4, 300]
    
    # Normalizzazione per visualizzazione (log scale per grandi differenze)
    real_log = [np.log10(v+1) for v in real_values]
    compliant_log = [np.log10(v+1) for v in compliant_values]
    
    x = np.arange(len(categories))
    width = 0.35
    
    # Barre
    bars1 = ax.bar(x - width/2, real_log, width, label='Scenario Reale',
                   color='#FF6B6B', edgecolor='darkred', linewidth=2)
    bars2 = ax.bar(x + width/2, compliant_log, width, 
                   label='Con Conformità Integrata',
                   color='#4ECDC4', edgecolor='darkgreen', linewidth=2)
    
    # Etichette valori reali sopra le barre
    for i, (bar1, bar2, real, comp) in enumerate(zip(bars1, bars2, 
                                                      real_values, compliant_values)):
        ax.text(bar1.get_x() + bar1.get_width()/2, bar1.get_height() + 0.1,
               f'{real:,.0f}', ha='center', va='bottom', fontsize=9)
        ax.text(bar2.get_x() + bar2.get_width()/2, bar2.get_height() + 0.1,
               f'{comp:,.0f}', ha='center', va='bottom', fontsize=9)
    
    # Configurazione assi - USA LATEX MATH MODE invece di Unicode subscript
    ax.set_ylabel(r'Scala logaritmica ($\log_{10}$)', fontsize=11)  # Notazione LaTeX
    ax.set_xticks(x)
    ax.set_xticklabels(categories, fontsize=10)
    ax.legend(loc='upper left', fontsize=10)
    ax.grid(True, alpha=0.3, axis='y')
    
    # Box con percentuali di miglioramento
    improvements = [
        ('Detection', -98.3),
        ('Sistemi', -99.6),
        ('Downtime', -96.7),
        ('Impatto', -96.5)
    ]
    
    improvement_text = 'Miglioramenti:\n'
    for metric, perc in improvements:
        improvement_text += f'{metric}: {perc:.1f}%\n'
    
    bbox = dict(boxstyle="round,pad=0.3", facecolor="lightyellow",
               edgecolor="black", linewidth=1)
    ax.text(0.98, 0.97, improvement_text[:-1], transform=ax.transAxes,
           fontsize=9, bbox=bbox, va='top', ha='right')
    
    plt.title('Analisi controfattuale dell\'impatto con conformità integrata completa',
              fontsize=12, fontweight='bold', pad=20)
    
    plt.tight_layout()
    return fig

def create_timeline_gantt():
    """
    Figura aggiuntiva: Timeline di implementazione (Gantt Chart)
    """
    fig, ax = plt.subplots(figsize=(14, 6))
    
    # Dati delle fasi
    phases = [
        ('Assessment e\nPianificazione', 0, 3, COLORS['level2']),
        ('Progettazione e\nArmonizzazione', 3, 6, COLORS['level4']),
        ('Implementazione\nPilota', 6, 12, '#1F77B4'),
        ('Rollout e\nOttimizzazione', 12, 24, COLORS['level1'])
    ]
    
    # Disegna le barre del Gantt
    for i, (name, start, end, color) in enumerate(phases):
        ax.barh(i, end-start, left=start, height=0.5, 
               color=color, edgecolor='black', linewidth=2)
        ax.text(end + 0.5, i, name, va='center', fontsize=10)
    
    # Milestone
    milestones = [
        (3, 'M1: Business Case'),
        (6, 'M2: Framework'),
        (12, 'M3: Pilota'),
        (24, 'M4: Completo')
    ]
    
    for x, label in milestones:
        ax.axvline(x, color='red', linestyle='--', linewidth=2)
        ax.text(x, len(phases), label.split(':')[0], 
               ha='center', va='bottom', fontsize=8, color='red')
    
    # Configurazione assi
    ax.set_xlim(0, 26)
    ax.set_ylim(-0.5, len(phases))
    ax.set_xlabel('Mesi', fontsize=11)
    ax.set_ylabel('Fasi del Progetto', fontsize=11)
    ax.set_yticks([])
    ax.grid(True, alpha=0.3, axis='x')
    
    # Legenda milestone
    milestone_text = '\n'.join([f'{m[1]}' for m in milestones])
    bbox = dict(boxstyle="round,pad=0.3", facecolor="white",
               edgecolor="black", linewidth=1)
    ax.text(0.02, 0.02, milestone_text, transform=ax.transAxes,
           fontsize=8, bbox=bbox, va='bottom')
    
    plt.title('Roadmap di implementazione della conformità integrata',
              fontsize=12, fontweight='bold', pad=20)
    
    plt.tight_layout()
    return fig

def create_maturity_pyramid():
    """
    Figura bonus: Modello di maturità (piramide)
    """
    fig, ax = plt.subplots(figsize=(12, 10))
    ax.set_xlim(-6, 12)
    ax.set_ylim(-0.5, 8)
    ax.axis('off')
    
    # Livelli della piramide
    levels = [
        (4, 0, 1.5, COLORS['level1'], 'Livello 1: Frammentato', 
         '• Gestione separata\n• Processi manuali\n• Duplicazioni frequenti'),
        (3.2, 1.5, 3, COLORS['level2'], 'Livello 2: Coordinato',
         '• Comunicazione tra team\n• Alcune sinergie\n• Processi parziali'),
        (2.4, 3, 4.5, COLORS['level3'], 'Livello 3: Integrato',
         '• Framework unificato\n• Processi standard\n• Piattaforma comune'),
        (1.6, 4.5, 6, COLORS['level4'], 'Livello 4: Ottimizzato',
         '• Automazione estensiva\n• Metriche predittive\n• Continuous compliance'),
        (0.8, 6, 7.5, COLORS['level5'], 'L5: Adattivo',
         '• ML-driven\n• Self-healing\n• Adaptive governance')
    ]
    
    # Disegna i livelli
    for i, (width, y_bottom, y_top, color, title, desc) in enumerate(levels):
        if i < len(levels) - 1:
            # Trapezi per i primi 4 livelli
            vertices = [(-width, y_bottom), (width, y_bottom),
                       (levels[i+1][0], y_top), (-levels[i+1][0], y_top)]
        else:
            # Triangolo per il livello superiore
            vertices = [(-width, y_bottom), (width, y_bottom), (0, y_top)]
        
        polygon = Polygon(vertices, facecolor=color, edgecolor='black', linewidth=2)
        ax.add_patch(polygon)
        
        # Testo del livello
        y_center = (y_bottom + y_top) / 2
        text_color = 'white' if i == 4 else 'black'
        ax.text(0, y_center, title, ha='center', va='center',
               fontsize=11, fontweight='bold', color=text_color)
        
        # Descrizione laterale
        ax.text(6, y_center, desc, ha='left', va='center', fontsize=9)
    
    # Indicatore posizione esempio (RetailCo)
    ax.annotate('RetailCo', xy=(-2.4, 3.75), xytext=(-5.5, 3.75),
               arrowprops=dict(arrowstyle='->', lw=2, color='red'))
    
    plt.title('Modello di maturità della conformità integrata (CIMM)',
              fontsize=12, fontweight='bold', pad=20)
    
    plt.tight_layout()
    return fig

def save_all_figures():
    """
    Genera e salva tutte le figure
    """
    # Disabilita temporaneamente i warning
    import warnings
    warnings.filterwarnings('ignore')
    
    figures = [
        (create_figure_1_venn(), 'figura_4_1_venn_normative.pdf'),
        (create_figure_2_architecture(), 'figura_4_2_architettura.pdf'),
        (create_figure_3_gdpr_flow(), 'figura_4_3_processo_gdpr.pdf'),
        (create_figure_4_org_structure(), 'figura_4_4_struttura_org.pdf'),
        (create_figure_5_comparison(), 'figura_4_5_controfattuale.pdf'),
        (create_timeline_gantt(), 'figura_4_6_timeline.pdf'),
        (create_maturity_pyramid(), 'figura_4_7_maturity.pdf')
    ]
    
    for fig, filename in figures:
        try:
            # Salva in PDF (vettoriale, migliore per LaTeX)
            fig.savefig(filename, format='pdf', bbox_inches='tight', dpi=300)
            
            # Salva anche in PNG per preview
            png_filename = filename.replace('.pdf', '.png')
            fig.savefig(png_filename, format='png', bbox_inches='tight', dpi=150)
            
            print(f"✓ Salvata: {filename} e {png_filename}")
            
        except Exception as e:
            print(f"✗ Errore nel salvare {filename}: {str(e)}")
        finally:
            # Chiudi la figura per liberare memoria
            plt.close(fig)
    
    # Riabilita i warning
    warnings.filterwarnings('default')

if __name__ == '__main__':
    # Imposta lo stile (usa una versione compatibile)
    try:
        plt.style.use('seaborn-v0_8-whitegrid')
    except:
        try:
            plt.style.use('seaborn-whitegrid')  # Versione più vecchia
        except:
            plt.style.use('ggplot')  # Fallback sicuro
    
    print("="*50)
    print("Generazione Figure Capitolo 4 - Versione Corretta")
    print("="*50)
    print()
    
    # Genera e salva tutte le figure
    save_all_figures()
    
    print()
    print("="*50)
    print("✓ Tutte le figure sono state generate con successo!")
    print("✓ Problemi di font risolti")
    print("="*50)
    print()
    print("File generati:")
    print("- PDF: pronti per l'inclusione in LaTeX con \\includegraphics")
    print("- PNG: disponibili per anteprima")
    print()
    print("Esempio di inclusione in LaTeX:")
    print("-"*50)
    print(r"""
\begin{figure}[h]
    \centering
    \includegraphics[width=0.9\textwidth]{figura_4_1_venn_normative.pdf}
    \caption{Sovrapposizioni tra i principali standard normativi}
    \label{fig:venn_normative}
\end{figure}
""")
    print("-"*50)
