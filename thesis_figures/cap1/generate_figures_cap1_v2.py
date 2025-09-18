#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script per generare le figure del Capitolo 1 della tesi
Stile accademico con colori professionali
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch
from matplotlib.patches import ConnectionPatch
import seaborn as sns
import numpy as np
import pandas as pd
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Configurazione stile accademico
plt.style.use('seaborn-v0_8-paper')
sns.set_palette("husl")

# Colori professionali per la tesi
COLORS = {
    'primary': '#2E4057',      # Blu scuro professionale
    'secondary': '#048A81',    # Verde acqua
    'accent': '#F18F01',       # Arancione accento
    'danger': '#C73E1D',       # Rosso per minacce
    'success': '#6A994E',      # Verde successo
    'info': '#277DA1',         # Blu informativo
    'light': '#F7F7F7',        # Grigio chiaro
    'dark': '#212529'          # Grigio scuro
}

# Font settings per aspetto accademico
FONT_SETTINGS = {
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif'],
    'font.size': 10,
    'axes.titlesize': 12,
    'axes.labelsize': 10,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 9,
    'figure.titlesize': 14
}
plt.rcParams.update(FONT_SETTINGS)

def create_attack_evolution_figure():
    """
    Figura 1.1: Evoluzione delle tipologie di attacco alla GDO (2019-2024)
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Dati per il grafico temporale
    years = np.arange(2019, 2025)
    data_theft = [100, 120, 145, 155, 160, 165]  # Crescita moderata
    operational = [20, 35, 60, 150, 280, 450]    # Crescita esponenziale
    phishing = [80, 90, 100, 110, 105, 100]      # Stabile
    ransomware = [40, 60, 90, 180, 250, 320]     # Forte crescita
    
    # Primo subplot: evoluzione temporale
    ax1.plot(years, data_theft, marker='o', label='Furto dati', 
             linewidth=2, color=COLORS['info'])
    ax1.plot(years, operational, marker='s', label='Interruzione operativa', 
             linewidth=2.5, color=COLORS['danger'])
    ax1.plot(years, phishing, marker='^', label='Phishing', 
             linewidth=1.5, color=COLORS['secondary'])
    ax1.plot(years, ransomware, marker='d', label='Ransomware', 
             linewidth=2, color=COLORS['accent'])
    
    ax1.set_xlabel('Anno', fontweight='bold')
    ax1.set_ylabel('Numero di incidenti (indicizzato 2019=100)', fontweight='bold')
    ax1.set_title('Evoluzione temporale degli attacchi', fontweight='bold', pad=10)
    ax1.grid(True, alpha=0.3, linestyle='--')
    ax1.legend(loc='upper left', frameon=True, fancybox=True, shadow=True)
    ax1.set_ylim([0, 500])
    
    # Evidenzia il periodo critico
    ax1.axvspan(2022, 2024, alpha=0.1, color=COLORS['danger'], 
                label='Periodo critico')
    ax1.annotate('Incremento +312%', xy=(2023, 280), xytext=(2021.5, 350),
                arrowprops=dict(arrowstyle='->', color=COLORS['danger'], lw=1.5),
                fontsize=9, color=COLORS['danger'], fontweight='bold')
    
    # Secondo subplot: distribuzione 2024
    categories = ['Interruzione\noperativa', 'Ransomware', 'Furto dati', 
                  'Phishing', 'Altri']
    values = [35, 28, 18, 12, 7]
    colors_pie = [COLORS['danger'], COLORS['accent'], COLORS['info'], 
                  COLORS['secondary'], COLORS['light']]
    
    wedges, texts, autotexts = ax2.pie(values, labels=categories, 
                                        colors=colors_pie, autopct='%1.1f%%',
                                        startangle=90, pctdistance=0.85)
    
    # Migliora l'aspetto del pie chart
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
        autotext.set_fontsize(9)
    
    ax2.set_title('Distribuzione attacchi 2024', fontweight='bold', pad=10)
    
    # Aggiungi un cerchio al centro per effetto donut
    centre_circle = Circle((0, 0), 0.70, fc='white')
    ax2.add_artist(centre_circle)
    ax2.text(0, 0, '2024', ha='center', va='center', fontsize=16, 
             fontweight='bold', color=COLORS['dark'])
    
    plt.suptitle('Figura 1.1: Evoluzione del panorama delle minacce nella GDO italiana',
                 fontsize=12, fontweight='bold', y=1.02)
    plt.tight_layout()
    return fig

def create_threat_landscape_diagram():
    """
    Figura aggiuntiva: Panorama integrato delle minacce alla GDO
    """
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Centro: Sistema GDO
    center = FancyBboxPatch((4, 4.5), 2, 1, 
                            boxstyle="round,pad=0.1",
                            facecolor=COLORS['success'], 
                            edgecolor=COLORS['dark'],
                            linewidth=2)
    ax.add_patch(center)
    ax.text(5, 5, 'SISTEMA GDO\nPunto Vendita', ha='center', va='center',
            fontweight='bold', fontsize=11, color='white')
    
    # Minacce (4 direzioni)
    threats = [
        {'pos': (5, 8), 'label': 'Minacce\nInformatiche', 'examples': 'Ransomware, DDoS'},
        {'pos': (1.5, 5), 'label': 'Minacce\nSupply Chain', 'examples': 'Fornitori\ncompromessi'},
        {'pos': (8.5, 5), 'label': 'Minacce\nInterne', 'examples': 'Errori, Frodi'},
        {'pos': (5, 2), 'label': 'Minacce\nFisiche', 'examples': 'Sabotaggi, Furti'}
    ]
    
    for threat in threats:
        # Box minaccia
        threat_box = FancyBboxPatch((threat['pos'][0]-0.8, threat['pos'][1]-0.4), 
                                    1.6, 0.8,
                                    boxstyle="round,pad=0.05",
                                    facecolor=COLORS['danger'], 
                                    edgecolor=COLORS['dark'],
                                    alpha=0.7, linewidth=1.5)
        ax.add_patch(threat_box)
        ax.text(threat['pos'][0], threat['pos'][1], threat['label'], 
                ha='center', va='center', fontweight='bold', 
                fontsize=10, color='white')
        
        # Frecce verso il centro
        arrow = FancyArrowPatch(threat['pos'], (5, 5),
                               connectionstyle="arc3,rad=0.2",
                               arrowstyle='->', 
                               mutation_scale=20,
                               linewidth=2,
                               color=COLORS['danger'],
                               alpha=0.6)
        ax.add_patch(arrow)
        
        # Esempi
        ax.text(threat['pos'][0], threat['pos'][1]-0.8, threat['examples'],
                ha='center', va='top', fontsize=8, 
                style='italic', color=COLORS['dark'])
    
    # Box impatti
    impact_box = FancyBboxPatch((6.5, 1.5), 3, 2,
                                boxstyle="round,pad=0.1",
                                facecolor=COLORS['accent'],
                                edgecolor=COLORS['dark'],
                                alpha=0.8, linewidth=1.5)
    ax.add_patch(impact_box)
    ax.text(8, 2.5, 'IMPATTI', ha='center', va='center',
            fontweight='bold', fontsize=11, color='white')
    
    impacts = ['• Perdite economiche', '• Danni reputazionali', 
               '• Interruzione servizio', '• Sanzioni normative']
    for i, impact in enumerate(impacts):
        ax.text(8, 2.2-i*0.3, impact, ha='center', va='center',
                fontsize=8, color='white')
    
    # Freccia dagli impatti
    impact_arrow = FancyArrowPatch((5.5, 4.8), (6.5, 2.8),
                                  connectionstyle="arc3,rad=-0.3",
                                  arrowstyle='->', 
                                  mutation_scale=20,
                                  linewidth=2,
                                  color=COLORS['accent'],
                                  alpha=0.6,
                                  linestyle='dashed')
    ax.add_patch(impact_arrow)
    
    # Timeline in basso
    timeline_box = FancyBboxPatch((0.5, 0.2), 9, 0.8,
                                  boxstyle="round,pad=0.05",
                                  facecolor=COLORS['light'],
                                  edgecolor=COLORS['dark'],
                                  linewidth=1)
    ax.add_patch(timeline_box)
    
    ax.text(5, 0.7, 'EVOLUZIONE TEMPORALE', ha='center', va='center',
            fontweight='bold', fontsize=9)
    ax.text(2.5, 0.4, '2019-2021:\nFocus cyber', ha='center', va='center',
            fontsize=7, color=COLORS['info'])
    ax.text(5, 0.4, '2022-2023:\nAttacchi ibridi', ha='center', va='center',
            fontsize=7, color=COLORS['secondary'])
    ax.text(7.5, 0.4, '2024-2025:\nMinacce sistemiche', ha='center', va='center',
            fontsize=7, color=COLORS['danger'])
    
    plt.title('Panorama integrato delle minacce: convergenza fisica-digitale',
              fontsize=12, fontweight='bold', pad=20)
    plt.tight_layout()
    return fig

def create_gist_framework_diagram():
    """
    Figura: Architettura del Framework GIST
    """
    fig, ax = plt.subplots(figsize=(12, 10))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Core centrale GIST
    core_circle = Circle((5, 5), 1.2, facecolor=COLORS['primary'], 
                         edgecolor=COLORS['dark'], linewidth=3)
    ax.add_patch(core_circle)
    ax.text(5, 5, 'Framework\nGIST', ha='center', va='center',
            fontweight='bold', fontsize=14, color='white')
    
    # Quattro componenti principali
    components = [
        {'pos': (2, 7.5), 'title': 'SICUREZZA', 
         'items': ['Algoritmo ASSA', 'Scoring rischio', 'ML predittivo'],
         'color': COLORS['danger']},
        {'pos': (8, 7.5), 'title': 'ARCHITETTURA',
         'items': ['Edge-Cloud', 'Multi-Cloud', 'Compliance-native'],
         'color': COLORS['info']},
        {'pos': (2, 2.5), 'title': 'GOVERNANCE',
         'items': ['Matrice MIN', '156 controlli', 'Audit continuo'],
         'color': COLORS['secondary']},
        {'pos': (8, 2.5), 'title': 'OPERAZIONI',
         'items': ['Digital Twin', 'Simulazione', 'KPI real-time'],
         'color': COLORS['accent']}
    ]
    
    for comp in components:
        # Box componente
        comp_box = FancyBboxPatch((comp['pos'][0]-1.2, comp['pos'][1]-0.8),
                                  2.4, 1.6,
                                  boxstyle="round,pad=0.1",
                                  facecolor=comp['color'],
                                  edgecolor=COLORS['dark'],
                                  alpha=0.8, linewidth=2)
        ax.add_patch(comp_box)
        
        # Titolo componente
        ax.text(comp['pos'][0], comp['pos'][1]+0.5, comp['title'],
                ha='center', va='center', fontweight='bold',
                fontsize=11, color='white')
        
        # Items
        for i, item in enumerate(comp['items']):
            ax.text(comp['pos'][0], comp['pos'][1]-0.1-i*0.25, f'• {item}',
                    ha='center', va='center', fontsize=8, color='white')
        
        # Connessioni bidirezionali con il core
        arrow1 = FancyArrowPatch(comp['pos'], (5, 5),
                                connectionstyle="arc3,rad=0.2",
                                arrowstyle='<->', 
                                mutation_scale=15,
                                linewidth=2,
                                color=COLORS['success'],
                                alpha=0.6)
        ax.add_patch(arrow1)
    
    # Interconnessioni tra componenti (frecce curve tratteggiate)
    interconnections = [
        ((2, 7.5), (8, 7.5), 'Requisiti'),      # Sicurezza -> Architettura
        ((8, 7.5), (8, 2.5), 'Metriche'),       # Architettura -> Operazioni
        ((8, 2.5), (2, 2.5), 'Conformità'),     # Operazioni -> Governance
        ((2, 2.5), (2, 7.5), 'Policy')          # Governance -> Sicurezza
    ]
    
    for start, end, label in interconnections:
        arrow = FancyArrowPatch(start, end,
                               connectionstyle="arc3,rad=0.3",
                               arrowstyle='->', 
                               mutation_scale=12,
                               linewidth=1.5,
                               color=COLORS['accent'],
                               alpha=0.5,
                               linestyle='dashed')
        ax.add_patch(arrow)
        
        # Label sulla freccia
        mid_x, mid_y = (start[0]+end[0])/2, (start[1]+end[1])/2
        if start[1] == end[1]:  # Orizzontale
            offset_y = 0.3 if start[1] > 5 else -0.3
            ax.text(mid_x, mid_y+offset_y, label, ha='center', va='center',
                    fontsize=7, style='italic', color=COLORS['dark'])
        else:  # Verticale
            offset_x = 0.5 if start[0] > 5 else -0.5
            ax.text(mid_x+offset_x, mid_y, label, ha='center', va='center',
                    fontsize=7, style='italic', color=COLORS['dark'])
    
    # Strumenti di supporto (più piccoli)
    tools = [
        {'pos': (1, 5.5), 'name': 'Calcolatore\nGIST'},
        {'pos': (9, 5.5), 'name': 'GDO-Bench\nDataset'},
        {'pos': (1, 4.5), 'name': 'Dashboard\nMonitor'},
        {'pos': (9, 4.5), 'name': 'Risk Scorer\nXGB'}
    ]
    
    for tool in tools:
        tool_box = FancyBboxPatch((tool['pos'][0]-0.5, tool['pos'][1]-0.25),
                                  1, 0.5,
                                  boxstyle="round,pad=0.05",
                                  facecolor=COLORS['light'],
                                  edgecolor=COLORS['dark'],
                                  linewidth=1)
        ax.add_patch(tool_box)
        ax.text(tool['pos'][0], tool['pos'][1], tool['name'],
                ha='center', va='center', fontsize=7)
    
    # Output box in basso
    output_box = FancyBboxPatch((1, 0.2), 8, 1.2,
                               boxstyle="round,pad=0.1",
                               facecolor='#FFE66D',  # Giallo chiaro
                               edgecolor=COLORS['dark'],
                               linewidth=2)
    ax.add_patch(output_box)
    
    ax.text(5, 1.1, 'OUTPUT DEL FRAMEWORK', ha='center', va='center',
            fontweight='bold', fontsize=10)
    
    outputs = [
        'Riduzione superficie attacco: -45%',
        'Disponibilità sistema: 99,96%',
        'Tempo conformità: -60%',
        'ROI: 18-24 mesi'
    ]
    
    for i, output in enumerate(outputs):
        x_pos = 2.5 + (i % 2) * 4.5
        y_pos = 0.7 if i < 2 else 0.4
        ax.text(x_pos, y_pos, f'✓ {output}', ha='left', va='center',
                fontsize=8, color=COLORS['dark'])
    
    plt.title('Architettura Framework GIST: Integrazione componenti e strumenti',
              fontsize=12, fontweight='bold', pad=20)
    plt.tight_layout()
    return fig

def create_comparison_table():
    """
    Tabella: Confronto approccio tradizionale vs GIST
    """
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.axis('off')
    
    # Dati per la tabella
    data = {
        'Dimensione': ['Architettura', 'Sicurezza', 'Conformità', 
                       'Gestione rischi', 'Costi IT', 'Agilità', 
                       'Competenze', 'Scalabilità'],
        'Approccio Tradizionale': [
            'Sistemi monolitici\ncentralizzati',
            'Perimetrale\n(firewall, antivirus)',
            'Gestione separata\nper normativa',
            'Valutazioni\nperiodiche statiche',
            'CAPEX elevato\nROI 5-7 anni',
            'Modifiche\n6-12 mesi',
            'Team IT\ngeneralista',
            'Verticale\ncostosa'
        ],
        'Framework GIST': [
            'Architettura distribuita\nmodulare resiliente',
            'Zero-trust\nmultilivello integrata',
            'Matrice unificata\n156 controlli',
            'Monitoraggio continuo\nML predittivo',
            'Modello OPEX\nROI 18-24 mesi',
            'Deployment continuo\nmodifiche in giorni',
            'Modello ibrido\nspecializzato',
            'Orizzontale elastica\npay-per-use'
        ]
    }
    
    df = pd.DataFrame(data)
    
    # Crea la tabella con colori alternati
    cell_colors = []
    for i in range(len(df)):
        if i % 2 == 0:
            cell_colors.append([COLORS['light'], '#FFE6E6', '#E6FFE6'])
        else:
            cell_colors.append(['white', '#FFD6D6', '#D6FFD6'])
    
    # Header colors
    header_colors = [COLORS['dark'], COLORS['danger'], COLORS['success']]
    
    # Crea la tabella
    table = ax.table(cellText=df.values, 
                     colLabels=df.columns,
                     cellLoc='center',
                     loc='center',
                     cellColours=cell_colors,
                     colColours=header_colors,
                     colWidths=[0.2, 0.4, 0.4])
    
    # Stile della tabella
    table.auto_set_font_size(False)
    table.set_fontsize(9)
    table.scale(1, 2.5)
    
    # Formattazione headers
    for i in range(len(df.columns)):
        cell = table[(0, i)]
        cell.set_text_props(weight='bold', color='white')
        cell.set_facecolor(header_colors[i])
        cell.set_height(0.08)
    
    # Formattazione prima colonna (dimensioni)
    for i in range(1, len(df) + 1):
        cell = table[(i, 0)]
        cell.set_text_props(weight='bold')
        cell.set_facecolor(COLORS['light'])
    
    plt.title('Confronto tra approccio tradizionale e Framework GIST',
              fontsize=14, fontweight='bold', pad=20)
    plt.tight_layout()
    return fig

def create_kpi_dashboard():
    """
    Dashboard KPI attesi dall'implementazione GIST
    """
    fig = plt.figure(figsize=(14, 8))
    
    # Griglia per i subplot
    gs = fig.add_gridspec(2, 3, hspace=0.3, wspace=0.3)
    
    # KPI 1: Riduzione superficie attacco
    ax1 = fig.add_subplot(gs[0, 0])
    angles = np.linspace(0, 2*np.pi, 100)
    radius = 0.9
    x = radius * np.cos(angles)
    y = radius * np.sin(angles)
    
    ax1.fill_between(angles[:55], 0, radius, transform=ax1.transData, 
                     color=COLORS['success'], alpha=0.7)
    ax1.plot(x, y, color=COLORS['dark'], linewidth=2)
    ax1.set_xlim(-1.1, 1.1)
    ax1.set_ylim(-1.1, 1.1)
    ax1.axis('off')
    ax1.text(0, 0, '-45%', ha='center', va='center', 
            fontsize=24, fontweight='bold', color=COLORS['success'])
    ax1.text(0, -0.3, 'Superficie\ndi attacco', ha='center', va='center', fontsize=10)
    ax1.set_title('Riduzione rischi', fontweight='bold')
    
    # KPI 2: Disponibilità sistema
    ax2 = fig.add_subplot(gs[0, 1])
    availability = [99.3, 99.5, 99.7, 99.96]
    quarters = ['Q1', 'Q2', 'Q3', 'Q4']
    bars = ax2.bar(quarters, availability, color=COLORS['info'], alpha=0.8)
    ax2.axhline(y=99.9, color=COLORS['danger'], linestyle='--', 
                label='Target SLA', linewidth=1)
    ax2.set_ylim(99, 100)
    ax2.set_ylabel('Disponibilità (%)', fontweight='bold')
    ax2.set_title('Uptime progressivo', fontweight='bold')
    ax2.legend(loc='lower right', fontsize=8)
    
    # Aggiungi valori sulle barre
    for bar, val in zip(bars, availability):
        ax2.text(bar.get_x() + bar.get_width()/2, val + 0.02, 
                f'{val}%', ha='center', va='bottom', fontsize=9)
    
    # KPI 3: ROI Timeline
    ax3 = fig.add_subplot(gs[0, 2])
    months = np.arange(0, 37)
    investment = -1000000  # 1M€ investimento iniziale
    monthly_savings = 55000  # 55k€/mese risparmi
    cumulative = [investment + monthly_savings * m for m in months]
    
    ax3.plot(months, cumulative, linewidth=2.5, color=COLORS['accent'])
    ax3.axhline(y=0, color=COLORS['dark'], linestyle='-', alpha=0.5)
    ax3.fill_between(months, 0, cumulative, where=(np.array(cumulative) > 0),
                     color=COLORS['success'], alpha=0.3, label='Profitto')
    ax3.fill_between(months, cumulative, 0, where=(np.array(cumulative) < 0),
                     color=COLORS['danger'], alpha=0.3, label='Investimento')
    
    # Punto di break-even
    break_even = 18
    ax3.plot(break_even, 0, 'go', markersize=10)
    ax3.annotate('Break-even\n18 mesi', xy=(break_even, 0), 
                xytext=(break_even-5, 200000),
                arrowprops=dict(arrowstyle='->', color=COLORS['success']))
    
    ax3.set_xlabel('Mesi', fontweight='bold')
    ax3.set_ylabel('Valore cumulativo (€)', fontweight='bold')
    ax3.set_title('ROI Timeline', fontweight='bold')
    ax3.legend(loc='lower right', fontsize=8)
    ax3.grid(True, alpha=0.3)
    
    # KPI 4: Tempi di conformità
    ax4 = fig.add_subplot(gs[1, 0])
    activities = ['Audit\npreparazione', 'Raccolta\nevidenze', 
                  'Remediation', 'Certificazione']
    before = [30, 45, 60, 20]  # giorni
    after = [10, 15, 20, 10]   # giorni
    
    y_pos = np.arange(len(activities))
    ax4.barh(y_pos - 0.2, before, 0.4, label='Prima', 
             color=COLORS['danger'], alpha=0.7)
    ax4.barh(y_pos + 0.2, after, 0.4, label='Con GIST', 
             color=COLORS['success'], alpha=0.7)
    ax4.set_yticks(y_pos)
    ax4.set_yticklabels(activities)
    ax4.set_xlabel('Giorni', fontweight='bold')
    ax4.set_title('Riduzione tempi conformità (-60%)', fontweight='bold')
    ax4.legend(loc='upper right', fontsize=8)
    
    # KPI 5: Maturità digitale
    ax5 = fig.add_subplot(gs[1, 1])
    categories = ['Sicurezza', 'Architettura', 'Processi', 
                  'Governance', 'Competenze']
    current = [2.5, 2.0, 2.3, 2.8, 2.1]
    target = [4.2, 4.5, 4.0, 4.3, 3.8]
    
    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
    current += current[:1]
    target += target[:1]
    angles += angles[:1]
    
    ax5 = fig.add_subplot(gs[1, 1], projection='polar')
    ax5.plot(angles, current, 'o-', linewidth=2, label='Stato attuale',
            color=COLORS['danger'], alpha=0.7)
    ax5.fill(angles, current, alpha=0.25, color=COLORS['danger'])
    ax5.plot(angles, target, 's-', linewidth=2, label='Target GIST',
            color=COLORS['success'], alpha=0.7)
    ax5.fill(angles, target, alpha=0.25, color=COLORS['success'])
    
    ax5.set_xticks(angles[:-1])
    ax5.set_xticklabels(categories, fontsize=8)
    ax5.set_ylim(0, 5)
    ax5.set_title('Maturità digitale (scala 1-5)', fontweight='bold', pad=20)
    ax5.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=8)
    ax5.grid(True)
    
    # KPI 6: Incidenti di sicurezza
    ax6 = fig.add_subplot(gs[1, 2])
    months_sec = ['Gen', 'Feb', 'Mar', 'Apr', 'Mag', 'Giu', 
                  'Lug', 'Ago', 'Set', 'Ott', 'Nov', 'Dic']
    incidents_before = [12, 15, 18, 14, 16, 20, 19, 17, 15, 16, 14, 13]
    incidents_after = [8, 7, 6, 5, 5, 4, 3, 3, 2, 2, 2, 1]
    
    x = np.arange(len(months_sec))
    width = 0.35
    
    ax6.bar(x - width/2, incidents_before, width, label='Pre-GIST',
           color=COLORS['danger'], alpha=0.7)
    ax6.bar(x + width/2, incidents_after, width, label='Post-GIST',
           color=COLORS['success'], alpha=0.7)
    
    ax6.set_xlabel('Mese', fontweight='bold')
    ax6.set_ylabel('N° incidenti', fontweight='bold')
    ax6.set_title('Riduzione incidenti (-75%)', fontweight='bold')
    ax6.set_xticks(x)
    ax6.set_xticklabels(months_sec, rotation=45, ha='right', fontsize=8)
    ax6.legend(loc='upper right', fontsize=8)
    ax6.grid(True, alpha=0.3, axis='y')
    
    plt.suptitle('Dashboard KPI - Impatto implementazione Framework GIST',
                fontsize=14, fontweight='bold', y=1.02)
    plt.tight_layout()
    return fig

def create_implementation_roadmap():
    """
    Roadmap implementativa GIST in 4 fasi
    """
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.set_xlim(0, 24)
    ax.set_ylim(0, 10)
    
    # Timeline
    ax.axhline(y=5, color=COLORS['dark'], linewidth=3, alpha=0.7)
    
    # Fasi
    phases = [
        {'start': 0, 'end': 3, 'name': 'FASE 1\nAssessment', 
         'color': COLORS['info'], 'y': 6.5,
         'tasks': ['Analisi AS-IS', 'ASSA-GDO scoring', 'Gap analysis']},
        {'start': 3, 'end': 9, 'name': 'FASE 2\nProgettazione', 
         'color': COLORS['secondary'], 'y': 7.5,
         'tasks': ['Architettura target', 'Piano migrazione', 'Risk assessment']},
        {'start': 9, 'end': 18, 'name': 'FASE 3\nImplementazione', 
         'color': COLORS['accent'], 'y': 6.5,
         'tasks': ['Deploy infrastruttura', 'Migrazione servizi', 'Test & validazione']},
        {'start': 18, 'end': 24, 'name': 'FASE 4\nOttimizzazione', 
         'color': COLORS['success'], 'y': 7.5,
         'tasks': ['Tuning performance', 'ML training', 'Continuous improvement']}
    ]
    
    for phase in phases:
        # Box fase
        rect = FancyBboxPatch((phase['start'], phase['y']-0.5), 
                              phase['end']-phase['start'], 1,
                              boxstyle="round,pad=0.05",
                              facecolor=phase['color'], 
                              edgecolor=COLORS['dark'],
                              alpha=0.8, linewidth=2)
        ax.add_patch(rect)
        
        # Nome fase
        ax.text((phase['start']+phase['end'])/2, phase['y'], phase['name'],
                ha='center', va='center', fontweight='bold', 
                fontsize=10, color='white')
        
        # Timeline marker
        ax.plot(phase['start'], 5, 'o', markersize=12, 
               color=phase['color'], markeredgecolor=COLORS['dark'], 
               markeredgewidth=2)
        ax.plot(phase['end'], 5, 'o', markersize=12, 
               color=phase['color'], markeredgecolor=COLORS['dark'], 
               markeredgewidth=2)
        
        # Mese
        ax.text(phase['start'], 4.3, f'Mese {phase["start"]}',
                ha='center', fontsize=9, fontweight='bold')
        if phase['end'] == 24:
            ax.text(phase['end'], 4.3, f'Mese {phase["end"]}',
                    ha='center', fontsize=9, fontweight='bold')
        
        # Tasks
        for i, task in enumerate(phase['tasks']):
            ax.text((phase['start']+phase['end'])/2, 3.5-i*0.5, f'• {task}',
                    ha='center', va='top', fontsize=8, style='italic')
    
    # Milestones principali
    milestones = [
        {'month': 3, 'label': 'Assessment\ncompleto', 'y': 8.5},
        {'month': 9, 'label': 'Architettura\napprovata', 'y': 9},
        {'month': 18, 'label': 'Go-live\nsistema', 'y': 8.5},
        {'month': 24, 'label': 'Regime\noperativo', 'y': 9}
    ]
    
    for ms in milestones:
        ax.plot(ms['month'], 5, 'D', markersize=15, 
               color=COLORS['danger'], markeredgecolor=COLORS['dark'], 
               markeredgewidth=2)
        ax.annotate(ms['label'], xy=(ms['month'], 5), 
                   xytext=(ms['month'], ms['y']),
                   arrowprops=dict(arrowstyle='->', color=COLORS['danger'], 
                                 lw=1.5),
                   ha='center', fontweight='bold', fontsize=9,
                   bbox=dict(boxstyle="round,pad=0.3", 
                           facecolor='white', 
                           edgecolor=COLORS['danger']))
    
    # KPI progressivi
    kpi_box = FancyBboxPatch((0.5, 0.5), 23, 1.5,
                             boxstyle="round,pad=0.1",
                             facecolor=COLORS['light'],
                             edgecolor=COLORS['dark'],
                             linewidth=1)
    ax.add_patch(kpi_box)
    
    ax.text(12, 1.7, 'KPI PROGRESSIVI', ha='center', fontweight='bold', 
           fontsize=10)
    
    kpi_data = [
        'Q1: Assessment completezza 100%',
        'Q2: Architettura validata 100%',
        'Q3: Servizi migrati 60%',
        'Q4: Servizi migrati 100%',
        'Q5: Disponibilità 99.5%',
        'Q6: Disponibilità 99.96%'
    ]
    
    for i, kpi in enumerate(kpi_data):
        x_pos = 2 + (i % 3) * 7
        y_pos = 1.2 if i < 3 else 0.8
        ax.text(x_pos, y_pos, kpi, ha='left', fontsize=8)
    
    ax.set_xlim(-1, 25)
    ax.axis('off')
    plt.title('Roadmap implementativa Framework GIST - Timeline 24 mesi',
              fontsize=14, fontweight='bold', pad=20)
    plt.tight_layout()
    return fig

def create_methodology_figure():
    """
    Figura 1.3: Schema metodologico della ricerca
    """
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis('off')
    
    # Titolo
    ax.text(6, 7.5, 'METODOLOGIA DELLA RICERCA', ha='center', va='center',
            fontsize=14, fontweight='bold', color=COLORS['primary'])
    
    # Fasi principali come flowchart
    phases = [
        {'x': 2, 'y': 5.5, 'title': 'FASE 1\nFondamenti', 
         'color': COLORS['info'], 'width': 2.5, 'height': 1.2},
        {'x': 6, 'y': 5.5, 'title': 'FASE 2\nSviluppo', 
         'color': COLORS['secondary'], 'width': 2.5, 'height': 1.2},
        {'x': 10, 'y': 5.5, 'title': 'FASE 3\nValidazione', 
         'color': COLORS['accent'], 'width': 2.5, 'height': 1.2}
    ]
    
    # Disegna le fasi
    for i, phase in enumerate(phases):
        # Box principale
        rect = FancyBboxPatch((phase['x']-phase['width']/2, phase['y']-phase['height']/2),
                              phase['width'], phase['height'],
                              boxstyle="round,pad=0.05",
                              facecolor=phase['color'],
                              edgecolor=COLORS['dark'],
                              linewidth=2, alpha=0.9)
        ax.add_patch(rect)
        
        # Titolo fase
        ax.text(phase['x'], phase['y'], phase['title'],
                ha='center', va='center', fontweight='bold',
                fontsize=11, color='white')
        
        # Freccia alla fase successiva
        if i < len(phases) - 1:
            arrow = FancyArrowPatch((phase['x']+phase['width']/2, phase['y']),
                                  (phases[i+1]['x']-phases[i+1]['width']/2, phases[i+1]['y']),
                                  arrowstyle='->', mutation_scale=20,
                                  linewidth=2, color=COLORS['dark'])
            ax.add_patch(arrow)
    
    # Dettagli per ogni fase
    details = [
        # Fase 1
        {'x': 2, 'y': 3.8, 'items': [
            '• Revisione letteratura (487 paper)',
            '• Analisi documenti settore',
            '• Definizione framework teorico'
        ]},
        # Fase 2
        {'x': 6, 'y': 3.8, 'items': [
            '• 23 interviste dirigenti IT',
            '• 5 casi studio internazionali',
            '• Sviluppo algoritmi (ASSA-GDO)'
        ]},
        # Fase 3
        {'x': 10, 'y': 3.8, 'items': [
            '• Simulazione Monte Carlo (10k iter)',
            '• Machine Learning (XGBoost)',
            '• Digital Twin (24 mesi dati)'
        ]}
    ]
    
    for detail in details:
        for i, item in enumerate(detail['items']):
            ax.text(detail['x'], detail['y']-i*0.25, item,
                    ha='center', va='top', fontsize=8)
    
    # Metodi utilizzati (in basso)
    methods_box = FancyBboxPatch((0.5, 1.5), 11, 1.5,
                                boxstyle="round,pad=0.05",
                                facecolor=COLORS['light'],
                                edgecolor=COLORS['dark'],
                                linewidth=1)
    ax.add_patch(methods_box)
    
    ax.text(6, 2.6, 'METODI E STRUMENTI', ha='center', va='center',
            fontweight='bold', fontsize=10)
    
    # Colonne di metodi
    methods_cols = [
        {'x': 2, 'title': 'Quantitativi', 
         'items': ['Statistica descrittiva', 'Analisi correlazione', 'Test ipotesi']},
        {'x': 6, 'title': 'Qualitativi',
         'items': ['Codifica tematica', 'Analisi contenuto', 'Triangolazione']},
        {'x': 10, 'title': 'Computazionali',
         'items': ['Python/R', 'Simulazione', 'Machine Learning']}
    ]
    
    for col in methods_cols:
        ax.text(col['x'], 2.2, col['title'], ha='center', va='center',
                fontweight='bold', fontsize=9)
        for i, item in enumerate(col['items']):
            ax.text(col['x'], 1.9-i*0.2, f'• {item}', ha='center', va='center',
                    fontsize=7)
    
    # Output finale
    output_box = FancyBboxPatch((3.5, 0.2), 5, 0.6,
                               boxstyle="round,pad=0.05",
                               facecolor=COLORS['success'],
                               edgecolor=COLORS['dark'],
                               linewidth=2, alpha=0.9)
    ax.add_patch(output_box)
    ax.text(6, 0.5, 'OUTPUT: Framework GIST + 5 Strumenti Computazionali',
            ha='center', va='center', fontweight='bold',
            fontsize=9, color='white')
    
    plt.tight_layout()
    return fig

def save_all_figures():
    """
    Genera e salva tutte le figure
    """
    print("Generazione figure per il Capitolo 1...")
    print("-" * 50)
    
    # Crea directory per le figure se non esiste
    import os
    os.makedirs('/mnt/user-data/outputs/thesis_figures/cap1', exist_ok=True)
    
    figures = [
        ('fig_1_1_attack_evolution', create_attack_evolution_figure()),
        ('fig_threat_landscape', create_threat_landscape_diagram()),
        ('fig_gist_framework', create_gist_framework_diagram()),
        ('table_comparison', create_comparison_table()),
        ('fig_kpi_dashboard', create_kpi_dashboard()),
        ('fig_implementation_roadmap', create_implementation_roadmap())
    ]
    
    for name, fig in figures:
        # Salva in PDF (per LaTeX)
        pdf_path = f'/mnt/user-data/outputs/thesis_figures/cap1/{name}.pdf'
        fig.savefig(pdf_path, dpi=300, bbox_inches='tight', 
                   format='pdf', metadata={'Creator': 'Thesis Chapter 1'})
        print(f"✓ Salvato: {name}.pdf")
        
        # Salva anche in PNG (per preview)
        png_path = f'/mnt/user-data/outputs/thesis_figures/cap1/{name}.png'
        fig.savefig(png_path, dpi=150, bbox_inches='tight', 
                   format='png')
        print(f"✓ Salvato: {name}.png")
        
        plt.close(fig)
    
    print("-" * 50)
    print("✓ Tutte le figure sono state generate con successo!")
    print(f"📁 Percorso: /mnt/user-data/outputs/thesis_figures/cap1/")
    
    return True

if __name__ == "__main__":
    save_all_figures()
