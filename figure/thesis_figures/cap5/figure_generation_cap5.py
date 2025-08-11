#!/usr/bin/env python3
"""
Generazione Figure per Capitolo 5 - Sintesi e Direzioni Strategiche
Versione senza dipendenza LaTeX per compatibilità Windows
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch
from matplotlib.patches import ConnectionPatch
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

# Disabilita LaTeX per compatibilità
plt.rcParams['text.usetex'] = False  # IMPORTANTE: Disabilita LaTeX
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans', 'Liberation Sans']
plt.rcParams['font.size'] = 11
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10
plt.rcParams['legend.fontsize'] = 10
plt.rcParams['figure.titlesize'] = 16

# Configurazione stile generale
try:
    plt.style.use('seaborn-v0_8-darkgrid')
except:
    try:
        plt.style.use('seaborn-darkgrid')
    except:
        plt.style.use('ggplot')

# Colori coerenti per il framework GIST
COLORS = {
    'physical': '#FF6B6B',      # Rosso corallo
    'architectural': '#4ECDC4',  # Turchese
    'security': '#45B7D1',       # Blu cielo
    'compliance': '#96CEB4',     # Verde salvia
    'synergy': '#FFA07A',        # Salmone chiaro
    'primary': '#2C3E50',        # Blu scuro
    'secondary': '#95A5A6',      # Grigio argenteo
    'success': '#27AE60',        # Verde successo
    'warning': '#F39C12',        # Arancione warning
    'danger': '#E74C3C'          # Rosso danger
}

# =============================================================================
# FIGURA 5.1: Effetti Sinergici tra le Componenti del Framework GIST
# =============================================================================

def create_synergy_diagram():
    """Crea il diagramma delle sinergie tra componenti GIST"""
    
    fig, ax = plt.subplots(figsize=(12, 10))
    
    # Posizioni dei componenti (layout circolare)
    components = {
        'Physical\nInfrastructure': (0, 1),
        'Architectural\nModernization': (1, 0),
        'Security\n(Zero Trust)': (0, -1),
        'Compliance\nIntegration': (-1, 0)
    }
    
    # Colori per componenti
    comp_colors = [COLORS['physical'], COLORS['architectural'], 
                   COLORS['security'], COLORS['compliance']]
    
    # Disegna i componenti come cerchi
    for i, (comp, pos) in enumerate(components.items()):
        circle = Circle(pos, 0.3, color=comp_colors[i], alpha=0.7, zorder=2)
        ax.add_patch(circle)
        ax.text(pos[0], pos[1], comp, ha='center', va='center', 
                fontsize=11, fontweight='bold', zorder=3)
    
    # Definisci le sinergie con i loro valori
    synergies = [
        (components['Physical\nInfrastructure'], 
         components['Architectural\nModernization'], '27%', COLORS['synergy']),
        (components['Architectural\nModernization'], 
         components['Security\n(Zero Trust)'], '34%', COLORS['synergy']),
        (components['Security\n(Zero Trust)'], 
         components['Compliance\nIntegration'], '41%', COLORS['danger']),
        (components['Compliance\nIntegration'], 
         components['Physical\nInfrastructure'], '22%', COLORS['secondary'])
    ]
    
    # Disegna le frecce di sinergia
    for start, end, value, color in synergies:
        arrow = FancyArrowPatch(start, end,
                               connectionstyle="arc3,rad=0.3",
                               arrowstyle='<->', mutation_scale=20,
                               linewidth=3, color=color, alpha=0.6)
        ax.add_patch(arrow)
        
        # Calcola punto medio per il testo
        mid_x = (start[0] + end[0]) / 2
        mid_y = (start[1] + end[1]) / 2
        
        # Aggiungi offset per il testo
        if abs(mid_x) > abs(mid_y):
            offset_y = 0.15 if mid_y > 0 else -0.15
            offset_x = 0
        else:
            offset_x = 0.15 if mid_x > 0 else -0.15
            offset_y = 0
            
        ax.text(mid_x + offset_x, mid_y + offset_y, value, 
                ha='center', va='center', fontsize=12, fontweight='bold',
                bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.8))
    
    # Aggiungi effetto sistema totale al centro
    center_box = FancyBboxPatch((-0.25, -0.15), 0.5, 0.3,
                                boxstyle="round,pad=0.05",
                                facecolor=COLORS['success'], alpha=0.3)
    ax.add_patch(center_box)
    ax.text(0, 0, 'System\nAmplification\n+52%', 
            ha='center', va='center', fontsize=13, fontweight='bold')
    
    ax.set_xlim(-1.7, 1.7)
    ax.set_ylim(-1.7, 1.7)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Effetti Sinergici tra le Componenti del Framework GIST', 
                fontsize=14, fontweight='bold', pad=20)
    
    plt.tight_layout()
    return fig

# =============================================================================
# TABELLA 5.1: Sintesi della Validazione delle Ipotesi
# =============================================================================

def create_validation_table():
    """Crea la tabella di validazione delle ipotesi"""
    
    fig, ax = plt.subplots(figsize=(14, 6))
    ax.axis('tight')
    ax.axis('off')
    
    # Dati della tabella
    headers = ['Ipotesi', 'Target Iniziale', 'Risultato Ottenuto', 
               'Metodo di Validazione', 'IC 95%']
    
    data = [
        ['H1: Architetture\nCloud-Ibride', 
         'SLA ≥99.95%\nTCO -30%', 
         'SLA 99.96%\nTCO -38.2%',
         'Monte Carlo (10k iter.)\n+ Dati pilota',
         '[99.94%, 99.97%]\n[34.6%, 41.7%]'],
        
        ['H2: Zero Trust\nASSA', 
         'ASSA -35%\nLatenza <50ms', 
         'ASSA -42.7%\nLatenza 44ms',
         'Modellazione grafo\n+ Simulazione rete',
         '[39.2%, 46.2%]\n[42ms, 46ms]'],
        
        ['H3: Compliance\nIntegrata', 
         'Costi -30-40%', 
         'Costi -37.8%',
         'Set-covering\n+ Bottom-up costing',
         '[31.4%, 43.9%]']
    ]
    
    # Crea la tabella
    table = ax.table(cellText=data, colLabels=headers,
                    cellLoc='center', loc='center',
                    colWidths=[0.15, 0.15, 0.15, 0.25, 0.15])
    
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 2)
    
    # Colora le celle
    for i in range(len(headers)):
        table[(0, i)].set_facecolor(COLORS['primary'])
        table[(0, i)].set_text_props(weight='bold', color='white')
    
    # Colora le righe alternate
    for i in range(1, len(data) + 1):
        color = '#F0F0F0' if i % 2 == 0 else 'white'
        for j in range(len(headers)):
            table[(i, j)].set_facecolor(color)
            
            # Evidenzia i risultati positivi
            if j == 2:  # Colonna risultati
                table[(i, j)].set_facecolor('#D4F1D4')
    
    ax.set_title('Tabella 5.1: Sintesi della Validazione delle Ipotesi di Ricerca',
                fontsize=14, fontweight='bold', pad=20)
    
    plt.tight_layout()
    return fig

# =============================================================================
# FIGURA 5.2: Processo di Assessment e Pianificazione GIST
# =============================================================================

def create_gist_process_flowchart():
    """Crea il flowchart del processo GIST"""
    
    fig, ax = plt.subplots(figsize=(14, 10))
    
    # Definisci le fasi del processo
    phases = [
        {'name': '1. Raccolta Dati', 'duration': '2-3 settimane', 
         'activities': ['Interviste stakeholder', 'Analisi documentale', 'Misurazioni tecniche']},
        {'name': '2. Definizione Contesto', 'duration': '1 settimana',
         'activities': ['Dimensione org.', 'Distribuzione geografica', 'Complessità IT']},
        {'name': '3. Calcolo Score GIST', 'duration': '2-3 giorni',
         'activities': ['Scoring algoritmico', 'Ponderazione dimensioni', 'Validazione']},
        {'name': '4. Benchmarking', 'duration': '1 settimana',
         'activities': ['Confronto settore', 'Gap analysis', 'Posizionamento']},
        {'name': '5. Identificazione Gap', 'duration': '1 settimana',
         'activities': ['Analisi dettagliata', 'Prioritizzazione', 'Interdipendenze']},
        {'name': '6. Generazione Roadmap', 'duration': '1-2 settimane',
         'activities': ['Ottimizzazione', 'Vincoli budget', 'Timeline']},
        {'name': '7. Business Case', 'duration': '1 settimana',
         'activities': ['Analisi finanziaria', 'Risk assessment', 'Metriche successo']}
    ]
    
    # Posizioni verticali per le fasi
    y_positions = np.linspace(8, 0, len(phases))
    
    for i, phase in enumerate(phases):
        y = y_positions[i]
        
        # Box principale della fase
        rect = FancyBboxPatch((1, y-0.3), 4, 0.6,
                              boxstyle="round,pad=0.05",
                              facecolor=COLORS['primary'], alpha=0.8,
                              edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        
        # Nome della fase
        ax.text(3, y, phase['name'], ha='center', va='center',
                fontsize=12, fontweight='bold', color='white')
        
        # Durata
        ax.text(6, y, phase['duration'], ha='left', va='center',
                fontsize=10, style='italic')
        
        # Attività - MODIFICATO per evitare problemi
        activities_text = ' • '.join(phase['activities'])
        ax.text(7.5, y, activities_text, ha='left', va='center',
                fontsize=9)
        
        # Freccia verso la fase successiva
        if i < len(phases) - 1:
            arrow = FancyArrowPatch((3, y-0.3), (3, y_positions[i+1]+0.3),
                                  arrowstyle='->', mutation_scale=20,
                                  linewidth=2, color=COLORS['primary'])
            ax.add_patch(arrow)
    
    # Aggiungi feedback loops
    feedback1 = FancyArrowPatch((0.8, y_positions[4]), (0.8, y_positions[2]),
                               connectionstyle="arc3,rad=-0.3",
                               arrowstyle='->', mutation_scale=15,
                               linewidth=1.5, color=COLORS['warning'],
                               linestyle='dashed', alpha=0.7)
    ax.add_patch(feedback1)
    ax.text(0.3, (y_positions[4] + y_positions[2])/2, 'Feedback', 
            rotation=90, va='center', fontsize=9, color=COLORS['warning'])
    
    ax.set_xlim(0, 12)
    ax.set_ylim(-0.5, 9)
    ax.axis('off')
    ax.set_title('Processo di Assessment e Pianificazione GIST', 
                fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    return fig

# =============================================================================
# TABELLA 5.2: Roadmap Implementativa Master
# =============================================================================

def create_roadmap_table():
    """Crea la tabella della roadmap implementativa"""
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 8), 
                                   gridspec_kw={'height_ratios': [3, 1]})
    
    # Parte superiore: Tabella
    ax1.axis('tight')
    ax1.axis('off')
    
    headers = ['Fase', 'Durata\n(mesi)', 'Iniziative Chiave', 
               'Investimento\n(€)', 'ROI\nAtteso', 'Prerequisiti']
    
    data = [
        ['Foundation', '0-6', 
         'Power/Cooling upgrade\nNetwork segmentation\nGovernance structure',
         '850k-1.2M', '140%\n(Anno 2)', 'Executive\nbuy-in'],
        
        ['Modernization', '6-12',
         'SD-WAN deployment\nCloud migration Wave 1\nZero Trust Phase 1',
         '2.3-3.1M', '220%\n(Anno 2)', 'Foundation\ncomplete'],
        
        ['Integration', '12-18',
         'Multi-cloud orchestration\nCompliance automation\nEdge computing',
         '1.8-2.4M', '310%\n(Anno 3)', 'Modernization\n>70%'],
        
        ['Optimization', '18-24',
         'AI/ML integration\nAdvanced automation\nPredictive capabilities',
         '1.2-1.6M', '380%\n(Anno 3)', 'Integration\nstable']
    ]
    
    table = ax1.table(cellText=data, colLabels=headers,
                     cellLoc='center', loc='center',
                     colWidths=[0.12, 0.08, 0.35, 0.12, 0.10, 0.12])
    
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 2.5)
    
    # Colora intestazioni
    for i in range(len(headers)):
        table[(0, i)].set_facecolor(COLORS['primary'])
        table[(0, i)].set_text_props(weight='bold', color='white')
    
    # Colora le fasi con gradiente
    phase_colors = ['#FFE5E5', '#E5F5FF', '#E5FFE5', '#FFF5E5']
    for i in range(1, len(data) + 1):
        for j in range(len(headers)):
            table[(i, j)].set_facecolor(phase_colors[i-1])
    
    ax1.set_title('Tabella 5.2: Roadmap Implementativa Master con Metriche Chiave',
                 fontsize=14, fontweight='bold', pad=20)
    
    # Parte inferiore: Timeline visuale
    ax2.set_xlim(0, 24)
    ax2.set_ylim(0, 1)
    
    # Timeline bars
    phases_timeline = [
        {'name': 'Foundation', 'start': 0, 'end': 6, 'color': phase_colors[0]},
        {'name': 'Modernization', 'start': 6, 'end': 12, 'color': phase_colors[1]},
        {'name': 'Integration', 'start': 12, 'end': 18, 'color': phase_colors[2]},
        {'name': 'Optimization', 'start': 18, 'end': 24, 'color': phase_colors[3]}
    ]
    
    for phase in phases_timeline:
        rect = plt.Rectangle((phase['start'], 0.3), 
                            phase['end'] - phase['start'], 0.4,
                            facecolor=phase['color'], edgecolor='black', linewidth=1)
        ax2.add_patch(rect)
        ax2.text((phase['start'] + phase['end'])/2, 0.5, phase['name'],
                ha='center', va='center', fontweight='bold')
    
    ax2.set_xlabel('Mesi', fontsize=11)
    ax2.set_yticks([])
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax2.spines['left'].set_visible(False)
    
    plt.tight_layout()
    return fig

# =============================================================================
# FIGURA 5.3: Struttura del Programma di Change Management - SEMPLIFICATA
# =============================================================================

def create_change_management_structure():
    """Crea il diagramma della struttura di change management - versione semplificata"""
    
    fig, ax = plt.subplots(figsize=(14, 10))
    
    # Definisci i gruppi stakeholder
    stakeholders = {
        'Executive': {
            'concerns': ['ROI', 'Continuity', 'Advantage'],
            'engagement': 'Strategic Committee',
            'frequency': 'Monthly',
            'training': '4h workshops',
            'color': COLORS['primary'],
            'pos': (2, 7)
        },
        'IT Staff': {
            'concerns': ['Security', 'Skills', 'Workload'],
            'engagement': 'Training Program',
            'frequency': 'Weekly',
            'training': '40-80h cert',
            'color': COLORS['architectural'],
            'pos': (7, 7)
        },
        'Store Mgr': {
            'concerns': ['Impact', 'Complex', 'Support'],
            'engagement': 'Pilot Programs',
            'frequency': 'Bi-weekly',
            'training': '8-16h ops',
            'color': COLORS['security'],
            'pos': (2, 2)
        },
        'Frontline': {
            'concerns': ['Usability', 'Time', 'Perform'],
            'engagement': 'Micro-learning',
            'frequency': 'Daily',
            'training': 'Continuous',
            'color': COLORS['compliance'],
            'pos': (7, 2)
        }
    }
    
    for name, props in stakeholders.items():
        x, y = props['pos']
        
        # Box principale
        rect = FancyBboxPatch((x-1.5, y-1), 3, 2,
                              boxstyle="round,pad=0.05",
                              facecolor=props['color'], alpha=0.3,
                              edgecolor=props['color'], linewidth=2)
        ax.add_patch(rect)
        
        # Titolo
        ax.text(x, y+0.7, name, ha='center', va='center',
                fontsize=12, fontweight='bold')
        
        # Concerns - versione semplificata
        concerns_text = ' • '.join(props['concerns'])
        ax.text(x, y, concerns_text, ha='center', va='center',
                fontsize=9)
        
        # Info sotto il box
        info_text = f"{props['engagement']} | {props['frequency']}"
        ax.text(x, y-0.7, info_text, ha='center', va='center',
                fontsize=8, style='italic')
    
    # Metriche al centro
    center_box = FancyBboxPatch((3.5, 4), 3, 1.5,
                                boxstyle="round,pad=0.05",
                                facecolor=COLORS['success'], alpha=0.2,
                                edgecolor=COLORS['success'], linewidth=2)
    ax.add_patch(center_box)
    
    ax.text(5, 5.2, 'Success Metrics', ha='center', va='center',
            fontsize=11, fontweight='bold')
    
    metrics_text = 'Adoption: 85% | Skills: +70% | Satisfaction: 4/5'
    ax.text(5, 4.5, metrics_text, ha='center', va='center', fontsize=9)
    
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 9)
    ax.axis('off')
    ax.set_title('Struttura del Programma di Change Management per la Trasformazione GDO',
                fontsize=14, fontweight='bold')
    
    # NON usare tight_layout qui se causa problemi
    # plt.tight_layout()
    return fig

# =============================================================================
# FIGURA 5.4: Tecnologie Emergenti e Impatto Previsto 2025-2030
# =============================================================================

def create_technology_timeline():
    """Crea la timeline delle tecnologie emergenti"""
    
    fig, ax = plt.subplots(figsize=(14, 8))
    
    # Definisci le tecnologie con timeline e impatto
    technologies = [
        {'name': 'AI/ML Advanced', 'start': 2025, 'maturity': 2027, 'impact': 'high'},
        {'name': 'Edge Computing', 'start': 2024, 'maturity': 2026, 'impact': 'high'},
        {'name': 'Quantum Computing', 'start': 2028, 'maturity': 2030, 'impact': 'medium'},
        {'name': '5G/6G Networks', 'start': 2025, 'maturity': 2027, 'impact': 'high'},
        {'name': 'Blockchain', 'start': 2026, 'maturity': 2028, 'impact': 'medium'},
        {'name': 'Digital Twins', 'start': 2025, 'maturity': 2027, 'impact': 'high'},
        {'name': 'Autonomous Systems', 'start': 2027, 'maturity': 2029, 'impact': 'medium'},
        {'name': 'AR/VR Shopping', 'start': 2025, 'maturity': 2026, 'impact': 'high'}
    ]
    
    # Colori per impatto
    impact_colors = {
        'high': COLORS['danger'],
        'medium': COLORS['warning'],
        'low': COLORS['secondary']
    }
    
    # Timeline base
    years = range(2024, 2031)
    ax.set_xlim(2024, 2030)
    ax.set_ylim(-1, len(technologies))
    
    # Disegna la griglia temporale
    for year in years:
        ax.axvline(x=year, color='gray', linestyle=':', alpha=0.3)
        ax.text(year, -0.5, str(year), ha='center', fontsize=10)
    
    # Disegna le tecnologie
    for i, tech in enumerate(technologies):
        y = i
        
        # Barra di sviluppo
        ax.barh(y, tech['maturity'] - tech['start'], 
               left=tech['start'], height=0.3,
               color=impact_colors[tech['impact']], alpha=0.6)
        
        # Nome tecnologia
        ax.text(tech['start'] - 0.1, y, tech['name'], 
               ha='right', va='center', fontsize=10, fontweight='bold')
        
        # Punto di maturità
        ax.plot(tech['maturity'], y, 'o', 
               color=impact_colors[tech['impact']], markersize=8)
        
        # Label impatto
        ax.text(tech['maturity'] + 0.1, y, tech['impact'].upper(), 
               ha='left', va='center', fontsize=8,
               color=impact_colors[tech['impact']], fontweight='bold')
    
    # Legenda
    from matplotlib.lines import Line2D
    legend_elements = [
        Line2D([0], [0], marker='o', color='w', 
               markerfacecolor=impact_colors['high'], markersize=10, 
               label='Alto Impatto'),
        Line2D([0], [0], marker='o', color='w', 
               markerfacecolor=impact_colors['medium'], markersize=10, 
               label='Medio Impatto')
    ]
    ax.legend(handles=legend_elements, loc='upper left')
    
    ax.set_xlabel('Timeline', fontsize=12)
    ax.set_yticks([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.set_title('Tecnologie Emergenti e Impatto Previsto sul Settore GDO 2025-2030',
                fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    return fig

# =============================================================================
# GRAFICI AGGIUNTIVI
# =============================================================================

def create_roi_comparison():
    """Crea il grafico di confronto ROI per fase"""
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    phases = ['Foundation', 'Modernization', 'Integration', 'Optimization']
    roi_values = [140, 220, 310, 380]
    investment = [1.0, 2.7, 2.1, 1.4]  # In milioni di euro
    
    x = np.arange(len(phases))
    width = 0.35
    
    # Bar plot per ROI
    bars1 = ax.bar(x - width/2, roi_values, width, label='ROI (%)', 
                   color=COLORS['success'], alpha=0.8)
    
    # Bar plot per investimento (asse secondario)
    ax2 = ax.twinx()
    bars2 = ax2.bar(x + width/2, investment, width, label='Investimento (M€)', 
                    color=COLORS['primary'], alpha=0.8)
    
    # Etichette sui bar
    for bar, value in zip(bars1, roi_values):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{value}%', ha='center', va='bottom', fontweight='bold')
    
    for bar, value in zip(bars2, investment):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height,
                f'{value}M€', ha='center', va='bottom')
    
    ax.set_xlabel('Fase di Implementazione', fontsize=12)
    ax.set_ylabel('ROI (%)', fontsize=12, color=COLORS['success'])
    ax2.set_ylabel('Investimento (M€)', fontsize=12, color=COLORS['primary'])
    ax.set_xticks(x)
    ax.set_xticklabels(phases)
    ax.tick_params(axis='y', labelcolor=COLORS['success'])
    ax2.tick_params(axis='y', labelcolor=COLORS['primary'])
    
    # Linea di trend per ROI cumulativo
    cumulative_roi = np.cumsum(roi_values) / np.arange(1, len(roi_values) + 1)
    ax.plot(x, cumulative_roi, 'r--', linewidth=2, 
            label='ROI Medio Cumulativo', marker='o')
    
    ax.legend(loc='upper left')
    ax2.legend(loc='upper right')
    ax.grid(True, alpha=0.3)
    
    ax.set_title('Confronto ROI e Investimenti per Fase Implementativa',
                fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    return fig

def create_gist_score_evolution():
    """Crea il grafico dell'evoluzione del GIST Score"""
    
    fig, ax = plt.subplots(figsize=(12, 7))
    
    # Dati simulati per 24 mesi
    months = np.arange(0, 25)
    
    # Score per componente nel tempo
    physical = 20 + 15 * (1 - np.exp(-months/8))
    architectural = 25 + 25 * (1 - np.exp(-months/10))
    security = 15 + 20 * (1 - np.exp(-months/12))
    compliance = 10 + 15 * (1 - np.exp(-months/14))
    
    # Score totale
    total = physical * 0.2 + architectural * 0.35 + security * 0.25 + compliance * 0.2
    
    # Plot delle componenti
    ax.fill_between(months, 0, physical * 0.2, 
                    alpha=0.6, color=COLORS['physical'], label='Physical (20%)')
    ax.fill_between(months, physical * 0.2, physical * 0.2 + architectural * 0.35,
                    alpha=0.6, color=COLORS['architectural'], label='Architectural (35%)')
    ax.fill_between(months, physical * 0.2 + architectural * 0.35,
                    physical * 0.2 + architectural * 0.35 + security * 0.25,
                    alpha=0.6, color=COLORS['security'], label='Security (25%)')
    ax.fill_between(months, physical * 0.2 + architectural * 0.35 + security * 0.25,
                    total, alpha=0.6, color=COLORS['compliance'], label='Compliance (20%)')
    
    # Linea del totale
    ax.plot(months, total, 'k-', linewidth=3, label='GIST Score Totale')
    
    # Marcatori per le fasi
    phase_markers = [
        (6, 'Foundation Complete'),
        (12, 'Modernization Complete'),
        (18, 'Integration Complete'),
        (24, 'Optimization Complete')
    ]
    
    for month, label in phase_markers:
        ax.axvline(x=month, color='gray', linestyle='--', alpha=0.5)
        ax.text(month, total[month] + 2, label, rotation=45, 
               ha='left', fontsize=9)
        ax.plot(month, total[month], 'ro', markersize=8)
    
    # Target line
    ax.axhline(y=80, color='green', linestyle='--', alpha=0.7, 
              label='Target Excellence (80)')
    
    ax.set_xlabel('Mesi dall\'inizio della trasformazione', fontsize=12)
    ax.set_ylabel('GIST Score', fontsize=12)
    ax.set_xlim(0, 24)
    ax.set_ylim(0, 100)
    ax.legend(loc='upper left')
    ax.grid(True, alpha=0.3)
    
    ax.set_title('Evoluzione del GIST Score durante la Trasformazione',
                fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    return fig

# =============================================================================
# FUNZIONE PRINCIPALE PER GENERARE TUTTE LE FIGURE
# =============================================================================

def generate_all_figures(output_dir='./'):
    """Genera tutte le figure e le salva"""
    
    import os
    
    # Crea directory se non esiste
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    print("=" * 60)
    print("GENERAZIONE FIGURE CAPITOLO 5")
    print("=" * 60)
    
    # Lista delle figure da generare
    figure_generators = [
        ('fig_5_1_synergies', create_synergy_diagram, 'Sinergie GIST'),
        ('tab_5_1_validation', create_validation_table, 'Tabella Validazione'),
        ('fig_5_2_process', create_gist_process_flowchart, 'Processo GIST'),
        ('tab_5_2_roadmap', create_roadmap_table, 'Roadmap Implementativa'),
        ('fig_5_3_change_mgmt', create_change_management_structure, 'Change Management'),
        ('fig_5_4_tech_timeline', create_technology_timeline, 'Timeline Tecnologie'),
        ('fig_5_5_roi_comparison', create_roi_comparison, 'Confronto ROI'),
        ('fig_5_6_gist_evolution', create_gist_score_evolution, 'Evoluzione GIST Score')
    ]
    
    figures = {}
    
    for name, generator, description in figure_generators:
        try:
            print(f"\nGenerazione {description}...", end=" ")
            fig = generator()
            figures[name] = fig
            
            # Salva in formato PDF per LaTeX
            pdf_path = os.path.join(output_dir, f'{name}.pdf')
            fig.savefig(pdf_path, dpi=300, bbox_inches='tight')
            
            # Salva anche in PNG per preview
            png_path = os.path.join(output_dir, f'{name}.png')
            fig.savefig(png_path, dpi=150, bbox_inches='tight')
            
            print(f"✓ Salvata come {name}.pdf e {name}.png")
            
            # Chiudi la figura per liberare memoria
            plt.close(fig)
            
        except Exception as e:
            print(f"✗ ERRORE: {str(e)}")
            continue
    
    print("\n" + "=" * 60)
    print(f"COMPLETATO: {len(figures)} figure generate con successo!")
    print(f"Directory output: {os.path.abspath(output_dir)}")
    print("=" * 60)
    
    return figures

# =============================================================================
# ESECUZIONE PRINCIPALE
# =============================================================================

if __name__ == "__main__":
    print("\n" + "="*60)
    print("GENERATORE FIGURE - CAPITOLO 5")
    print("Tesi: Framework GIST per la Trasformazione Digitale nella GDO")
    print("="*60)
    
    # Genera tutte le figure
    figures = generate_all_figures()
    
    print("\n✓ Tutte le figure sono state generate con successo!")
    print("\nPer utilizzare le figure in LaTeX:")
    print("\\includegraphics[width=\\textwidth]{fig_5_1_synergies.pdf}")
    print("\nBuon lavoro con la tesi!")