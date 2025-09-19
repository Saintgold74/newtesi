#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script per la generazione delle figure del Capitolo 2 - VERSIONE FONT LARGE
Tesi di Laurea in Ingegneria Informatica
Tema: Sicurezza nella Grande Distribuzione Organizzata
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch
from matplotlib.patches import ConnectionPatch
import numpy as np
import seaborn as sns
from matplotlib import cm
import warnings
warnings.filterwarnings('ignore')

# Configurazione dello stile accademico con FONT LARGE
plt.style.use('seaborn-v0_8-paper')
sns.set_palette("husl")

# FONT AUMENTATI PER MIGLIORE VISIBILITÀ
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['font.size'] = 14  # Era 10
plt.rcParams['axes.labelsize'] = 16  # Era 11
plt.rcParams['axes.titlesize'] = 18  # Era 12
plt.rcParams['xtick.labelsize'] = 13  # Era 9
plt.rcParams['ytick.labelsize'] = 13  # Era 9
plt.rcParams['legend.fontsize'] = 13  # Era 9
plt.rcParams['figure.titlesize'] = 19  # Era 13

# Aumenta anche lo spessore delle linee per coerenza
plt.rcParams['lines.linewidth'] = 2.5  # Default 1.5
plt.rcParams['axes.linewidth'] = 1.5  # Default 1

# Colori coerenti per tutto il documento
COLOR_PRIMARY = '#2E4053'    # Blu scuro professionale
COLOR_SECONDARY = '#E74C3C'  # Rosso per elementi di rischio
COLOR_ACCENT = '#3498DB'     # Blu chiaro per evidenziare
COLOR_SUCCESS = '#27AE60'    # Verde per elementi positivi
COLOR_WARNING = '#F39C12'    # Arancione per warning
COLOR_NEUTRAL = '#95A5A6'    # Grigio neutro

def create_it_ot_convergence():
    """
    Figura 2.2: Architettura convergente IT-OT in un punto vendita
    """
    fig, ax = plt.subplots(1, 1, figsize=(14, 10))  # Aumentato da 12x8
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Titolo
    ax.text(5, 9.5, 'Convergenza IT-OT nel Punto Vendita Moderno', 
            fontsize=20, fontweight='bold', ha='center')  # Era 14
    
    # Layer OT (Operational Technology)
    ot_box = FancyBboxPatch((0.5, 0.5), 4, 3.5,
                            boxstyle="round,pad=0.1",
                            facecolor='#FFE5E5',
                            edgecolor=COLOR_SECONDARY,
                            linewidth=2.5)  # Era 2
    ax.add_patch(ot_box)
    ax.text(2.5, 3.5, 'LIVELLO OT', fontsize=16, fontweight='bold',  # Era 11
            ha='center', color=COLOR_SECONDARY)
    
    # Componenti OT
    ot_components = [
        {'name': 'POS\n(Casse)', 'pos': (1.2, 2.8), 'icon': '□'},
        {'name': 'Sensori\nRFID', 'pos': (2.5, 2.8), 'icon': '◊'},
        {'name': 'Controllo\nAccessi', 'pos': (3.8, 2.8), 'icon': '○'},
        {'name': 'Sistema\nHVAC', 'pos': (1.2, 1.5), 'icon': '△'},
        {'name': 'Bilance\nIntelligenti', 'pos': (2.5, 1.5), 'icon': '◇'},
        {'name': 'Frigoriferi\nConnessi', 'pos': (3.8, 1.5), 'icon': '□'},
    ]
    
    for comp in ot_components:
        # Box componente
        comp_box = FancyBboxPatch((comp['pos'][0]-0.35, comp['pos'][1]-0.35), 
                                  0.7, 0.6,
                                  boxstyle="round,pad=0.05",
                                  facecolor='white',
                                  edgecolor=COLOR_SECONDARY,
                                  linewidth=1.5)  # Era 1
        ax.add_patch(comp_box)
        ax.text(comp['pos'][0], comp['pos'][1], comp['name'], 
               fontsize=11, ha='center', va='center')  # Era 8
    
    # Layer IT (Information Technology)
    it_box = FancyBboxPatch((5.5, 0.5), 4, 3.5,
                            boxstyle="round,pad=0.1",
                            facecolor='#E5F3FF',
                            edgecolor=COLOR_ACCENT,
                            linewidth=2.5)  # Era 2
    ax.add_patch(it_box)
    ax.text(7.5, 3.5, 'LIVELLO IT', fontsize=16, fontweight='bold',  # Era 11
            ha='center', color=COLOR_ACCENT)
    
    # Componenti IT
    it_components = [
        {'name': 'ERP\nAziendale', 'pos': (6.2, 2.8)},
        {'name': 'Gestione\nInventario', 'pos': (7.5, 2.8)},
        {'name': 'Analytics\nVendite', 'pos': (8.8, 2.8)},
        {'name': 'CRM\nClienti', 'pos': (6.2, 1.5)},
        {'name': 'Database\nCentrale', 'pos': (7.5, 1.5)},
        {'name': 'Server\nLocale', 'pos': (8.8, 1.5)},
    ]
    
    for comp in it_components:
        comp_box = FancyBboxPatch((comp['pos'][0]-0.35, comp['pos'][1]-0.35), 
                                  0.7, 0.6,
                                  boxstyle="round,pad=0.05",
                                  facecolor='white',
                                  edgecolor=COLOR_ACCENT,
                                  linewidth=1.5)  # Era 1
        ax.add_patch(comp_box)
        ax.text(comp['pos'][0], comp['pos'][1], comp['name'], 
               fontsize=11, ha='center', va='center')  # Era 8
    
    # Gateway di Integrazione
    gateway_box = FancyBboxPatch((4.2, 4.5), 1.6, 1.2,
                                 boxstyle="round,pad=0.1",
                                 facecolor='#FFF9E5',
                                 edgecolor=COLOR_WARNING,
                                 linewidth=2.5)  # Era 2
    ax.add_patch(gateway_box)
    ax.text(5, 5.1, 'GATEWAY\nINTEGRAZIONE', fontsize=14, fontweight='bold',  # Era 10
            ha='center', color=COLOR_WARNING)
    ax.text(5, 4.7, 'Firewall + IDS', fontsize=11, ha='center', style='italic')  # Era 8
    
    # Connessioni
    # OT verso Gateway
    for comp in ot_components[:3]:
        arrow = FancyArrowPatch(comp['pos'], (4.5, 4.8),
                               connectionstyle="arc3,rad=0.2",
                               arrowstyle='->,head_width=0.15,head_length=0.15',
                               color=COLOR_SECONDARY, alpha=0.6, linewidth=1.5)  # Era 1
        ax.add_patch(arrow)
    
    # IT verso Gateway
    for comp in it_components[:3]:
        arrow = FancyArrowPatch(comp['pos'], (5.5, 4.8),
                               connectionstyle="arc3,rad=-0.2",
                               arrowstyle='->,head_width=0.15,head_length=0.15',
                               color=COLOR_ACCENT, alpha=0.6, linewidth=1.5)  # Era 1
        ax.add_patch(arrow)
    
    # Cloud/Sede Centrale
    cloud_box = FancyBboxPatch((4, 7), 2, 1.2,
                               boxstyle="round,pad=0.1",
                               facecolor='#F0F0F0',
                               edgecolor=COLOR_PRIMARY,
                               linewidth=2.5)  # Era 2
    ax.add_patch(cloud_box)
    ax.text(5, 7.6, 'SEDE CENTRALE', fontsize=14, fontweight='bold',  # Era 10
            ha='center', color=COLOR_PRIMARY)
    ax.text(5, 7.2, 'Cloud Infrastructure', fontsize=11, ha='center', style='italic')  # Era 8
    
    # Connessione Gateway-Cloud
    arrow_cloud = FancyArrowPatch((5, 5.7), (5, 6.9),
                                 arrowstyle='<->,head_width=0.2,head_length=0.2',
                                 color=COLOR_PRIMARY, linewidth=2.5)  # Era 2
    ax.add_patch(arrow_cloud)
    ax.text(5.3, 6.3, 'VPN\nCifrata', fontsize=11, ha='left')  # Era 8
    
    # Indicatori di rischio
    risk_points = [
        {'pos': (2.5, 4.2), 'label': 'Punto critico:\nDati sensibili'},
        {'pos': (7.5, 4.2), 'label': 'Punto critico:\nAccessi privilegiati'},
    ]
    
    for risk in risk_points:
        circle = Circle(risk['pos'], 0.15, color=COLOR_SECONDARY, alpha=0.3)
        ax.add_patch(circle)
        ax.text(risk['pos'][0], risk['pos'][1]-0.5, risk['label'], 
               fontsize=10, ha='center', color=COLOR_SECONDARY, style='italic')  # Era 7
    
    # Legenda
    legend_items = [
        {'color': COLOR_SECONDARY, 'label': 'Sistemi Operativi (OT)'},
        {'color': COLOR_ACCENT, 'label': 'Sistemi Informatici (IT)'},
        {'color': COLOR_WARNING, 'label': 'Punto di Integrazione'},
        {'color': COLOR_PRIMARY, 'label': 'Connessione Remota'},
    ]
    
    for i, item in enumerate(legend_items):
        y_pos = 0.3 - i*0.15
        rect = patches.Rectangle((8.5, y_pos), 0.3, 0.1, 
                                facecolor=item['color'], alpha=0.5)
        ax.add_patch(rect)
        ax.text(8.9, y_pos+0.05, item['label'], fontsize=11, va='center')  # Era 8
    
    plt.tight_layout()
    return fig

def create_orchestration_system():
    """
    Figura 2.4: Sistema di orchestrazione della risposta a tre livelli
    """
    fig, ax = plt.subplots(1, 1, figsize=(14, 10))  # Aumentato da 12x8
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Titolo
    ax.text(5, 9.5, 'Architettura di Orchestrazione della Risposta agli Incidenti', 
            fontsize=20, fontweight='bold', ha='center')  # Era 14
    
    # Livello 1 - Risposta Locale
    level1_y = 1.5
    for i in range(5):
        x_pos = 1 + i * 2
        store_box = FancyBboxPatch((x_pos-0.4, level1_y-0.4), 0.8, 0.8,
                                   boxstyle="round,pad=0.05",
                                   facecolor='#E8F6F3',
                                   edgecolor=COLOR_SUCCESS,
                                   linewidth=2)  # Era 1.5
        ax.add_patch(store_box)
        ax.text(x_pos, level1_y, f'PdV\n{i+1}', fontsize=12, ha='center', va='center')  # Era 9
        
        # Indicatore tempo di risposta
        ax.text(x_pos, level1_y-0.7, '<1 min', fontsize=10,  # Era 7
               ha='center', color=COLOR_SUCCESS, style='italic')
    
    ax.text(5, 0.5, 'LIVELLO 1: Risposta Automatica Locale', 
            fontsize=15, fontweight='bold', ha='center', color=COLOR_SUCCESS)  # Era 11
    ax.text(5, 0.1, 'Isolamento immediato • Contenimento locale • Alert automatici', 
            fontsize=11, ha='center', style='italic')  # Era 8
    
    # Livello 2 - Coordinamento Regionale
    level2_y = 4.5
    regional_centers = [
        {'pos': (2.5, level2_y), 'label': 'Centro\nNord'},
        {'pos': (5, level2_y), 'label': 'Centro\nCentro'},
        {'pos': (7.5, level2_y), 'label': 'Centro\nSud'},
    ]
    
    for center in regional_centers:
        regional_box = FancyBboxPatch((center['pos'][0]-0.6, center['pos'][1]-0.5), 
                                      1.2, 1,
                                      boxstyle="round,pad=0.05",
                                      facecolor='#FFF5E6',
                                      edgecolor=COLOR_WARNING,
                                      linewidth=2.5)  # Era 2
        ax.add_patch(regional_box)
        ax.text(center['pos'][0], center['pos'][1], center['label'], 
               fontsize=13, ha='center', va='center', fontweight='bold')  # Era 10
        ax.text(center['pos'][0], center['pos'][1]-0.8, '<15 min', 
               fontsize=10, ha='center', color=COLOR_WARNING, style='italic')  # Era 7
        
        # Connessioni dal livello 1 al livello 2
        if center['pos'][0] == 2.5:  # Nord
            for i in range(2):
                arrow = FancyArrowPatch((1+i*2, level1_y+0.4), 
                                       (center['pos'][0], center['pos'][1]-0.5),
                                       connectionstyle="arc3,rad=0.2",
                                       arrowstyle='->,head_width=0.1',
                                       color=COLOR_NEUTRAL, alpha=0.5, linewidth=1.5)  # Era 1
                ax.add_patch(arrow)
    
    ax.text(5, 3.5, 'LIVELLO 2: Coordinamento Regionale', 
            fontsize=15, fontweight='bold', ha='center', color=COLOR_WARNING)  # Era 11
    ax.text(5, 3.1, 'Analisi pattern • Correlazione eventi • Escalation controllata', 
            fontsize=11, ha='center', style='italic')  # Era 8
    
    # Livello 3 - SOC Centrale
    level3_y = 7.5
    soc_box = FancyBboxPatch((3.5, level3_y-0.6), 3, 1.2,
                             boxstyle="round,pad=0.1",
                             facecolor='#FFE5E5',
                             edgecolor=COLOR_SECONDARY,
                             linewidth=3)  # Era 2.5
    ax.add_patch(soc_box)
    ax.text(5, level3_y, 'SOC CENTRALE', fontsize=16,  # Era 12
           fontweight='bold', ha='center', color=COLOR_SECONDARY)
    ax.text(5, level3_y-0.4, 'Security Operations Center', 
           fontsize=12, ha='center', style='italic')  # Era 9
    ax.text(5, level3_y-0.9, '<60 min', fontsize=10,  # Era 7
           ha='center', color=COLOR_SECONDARY, style='italic')
    
    # Connessioni dal livello 2 al livello 3
    for center in regional_centers:
        arrow = FancyArrowPatch((center['pos'][0], center['pos'][1]+0.5), 
                               (5, level3_y-0.6),
                               connectionstyle="arc3,rad=0.2",
                               arrowstyle='->,head_width=0.15',
                               color=COLOR_WARNING, alpha=0.6, linewidth=2)  # Era 1.5
        ax.add_patch(arrow)
    
    ax.text(5, 6.5, 'LIVELLO 3: Orchestrazione Centrale', 
            fontsize=15, fontweight='bold', ha='center', color=COLOR_SECONDARY)  # Era 11
    ax.text(5, 6.1, 'Visione sistemica • Risposta coordinata • Intelligence globale', 
            fontsize=11, ha='center', style='italic')  # Era 8
    
    # Flusso di informazioni (frecce bidirezionali)
    ax.annotate('', xy=(9.2, 2), xytext=(9.2, 7),
                arrowprops=dict(arrowstyle='<->', color=COLOR_PRIMARY, lw=2.5))  # Era 2
    ax.text(9.5, 4.5, 'Flusso\nBidirezionale\nInformazioni', 
           fontsize=11, ha='left', va='center', color=COLOR_PRIMARY)  # Era 8
    
    # Metriche di performance
    metrics_box = FancyBboxPatch((0.2, 8.5), 2.5, 1.2,
                                 boxstyle="round,pad=0.05",
                                 facecolor='white',
                                 edgecolor=COLOR_PRIMARY,
                                 linewidth=1.5)  # Era 1
    ax.add_patch(metrics_box)
    ax.text(1.45, 9.4, 'METRICHE CHIAVE', fontsize=12,  # Era 9
           fontweight='bold', ha='center', color=COLOR_PRIMARY)
    ax.text(0.4, 9.0, '• MTTD: 24h → 1h', fontsize=11)  # Era 8
    ax.text(0.4, 8.7, '• Contenimento: 77%', fontsize=11)  # Era 8
    
    # Timeline di risposta
    timeline_y = 2.8
    timeline_points = [
        {'x': 1, 'label': 'T₀', 'desc': 'Rilevamento'},
        {'x': 3, 'label': 'T₀+1\'', 'desc': 'Isolamento'},
        {'x': 5, 'label': 'T₀+15\'', 'desc': 'Analisi'},
        {'x': 7, 'label': 'T₀+60\'', 'desc': 'Risposta'},
        {'x': 9, 'label': 'T₀+4h', 'desc': 'Ripristino'},
    ]
    
    # Linea temporale
    ax.plot([0.8, 9.2], [timeline_y, timeline_y], 
           color=COLOR_NEUTRAL, linewidth=2.5, alpha=0.5)  # Era 2
    
    for point in timeline_points:
        ax.plot(point['x'], timeline_y, 'o', color=COLOR_PRIMARY, markersize=10)  # Era 8
        ax.text(point['x'], timeline_y+0.2, point['label'], 
               fontsize=11, ha='center', fontweight='bold')  # Era 8
        ax.text(point['x'], timeline_y-0.2, point['desc'], 
               fontsize=10, ha='center', style='italic')  # Era 7
    
    plt.tight_layout()
    return fig

def create_attack_evolution():
    """
    Figura aggiuntiva: Evoluzione temporale degli attacchi
    """
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))  # Aumentato da 12x8
    
    # Dati simulati basati sui valori del capitolo
    years = np.array([2020, 2021, 2022, 2023, 2024, 2025])
    
    # Tipologie di attacco
    payment_attacks = np.array([45, 48, 52, 58, 65, 72])  # 43% media
    ransomware = np.array([25, 28, 35, 42, 48, 55])       # 31% media
    supply_chain = np.array([10, 12, 15, 20, 25, 30])     # 18% media
    other = np.array([20, 17, 15, 12, 10, 8])             # altri
    
    # Grafico 1: Evoluzione per tipologia
    ax1.fill_between(years, 0, payment_attacks, 
                     color=COLOR_SECONDARY, alpha=0.7, label='Attacchi ai sistemi di pagamento')
    ax1.fill_between(years, payment_attacks, payment_attacks + ransomware, 
                     color=COLOR_WARNING, alpha=0.7, label='Ransomware')
    ax1.fill_between(years, payment_attacks + ransomware, 
                    payment_attacks + ransomware + supply_chain,
                    color=COLOR_ACCENT, alpha=0.7, label='Supply chain')
    ax1.fill_between(years, payment_attacks + ransomware + supply_chain,
                    payment_attacks + ransomware + supply_chain + other,
                    color=COLOR_NEUTRAL, alpha=0.5, label='Altri')
    
    ax1.set_xlabel('Anno', fontsize=15)  # Era 11
    ax1.set_ylabel('Numero di incidenti', fontsize=15)  # Era 11
    ax1.set_title('Evoluzione delle Tipologie di Attacco nella GDO (2020-2025)', 
                 fontsize=17, fontweight='bold')  # Era 12
    ax1.legend(loc='upper left', fontsize=12)  # Era 9
    ax1.grid(True, alpha=0.3, linestyle='--')
    ax1.set_xlim(2020, 2025)
    ax1.tick_params(axis='both', which='major', labelsize=12)  # Nuovo
    
    # Aggiungi annotazione per il trend
    ax1.annotate('Crescita esponenziale\nattacchi mirati\n(+156% dal 2023)',
                xy=(2023, 100), xytext=(2021.5, 120),
                arrowprops=dict(arrowstyle='->', color=COLOR_SECONDARY, lw=2),  # Era 1.5
                fontsize=12, ha='center',  # Era 9
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white', 
                         edgecolor=COLOR_SECONDARY))
    
    # Grafico 2: Pattern stagionale
    months = np.arange(1, 13)
    month_names = ['Gen', 'Feb', 'Mar', 'Apr', 'Mag', 'Giu', 
                   'Lug', 'Ago', 'Set', 'Ott', 'Nov', 'Dic']
    
    # Probabilità basata sull'equazione del capitolo
    P_0 = 0.031
    seasonal_pattern = P_0 * (1 + 0.25 * np.sin(2 * np.pi * months / 12 - np.pi/2))
    
    bars = ax2.bar(months, seasonal_pattern, color=COLOR_PRIMARY, alpha=0.7)
    
    # Evidenzia i picchi
    bars[6].set_color(COLOR_WARNING)  # Luglio
    bars[10].set_color(COLOR_SECONDARY)  # Novembre
    bars[11].set_color(COLOR_SECONDARY)  # Dicembre
    
    ax2.set_xlabel('Mese', fontsize=15)  # Era 11
    ax2.set_ylabel('Probabilità di attacco', fontsize=15)  # Era 11
    ax2.set_title('Stagionalità degli Attacchi nella GDO', 
                 fontsize=17, fontweight='bold')  # Era 12
    ax2.set_xticks(months)
    ax2.set_xticklabels(month_names, fontsize=12)  # Aumentato
    ax2.grid(True, axis='y', alpha=0.3, linestyle='--')
    ax2.tick_params(axis='y', which='major', labelsize=12)  # Nuovo
    
    # Aggiungi linea media
    ax2.axhline(y=P_0, color=COLOR_NEUTRAL, linestyle='--', 
               linewidth=2, label=f'Media annuale ({P_0:.3f})')  # Era 1.5
    
    # Evidenzia i periodi critici
    ax2.text(7, seasonal_pattern[6] + 0.002, 'Picco estivo', 
            fontsize=11, ha='center', fontweight='bold')  # Era 8
    ax2.text(11.5, seasonal_pattern[11] + 0.002, 'Picco natalizio', 
            fontsize=11, ha='center', fontweight='bold')  # Era 8
    
    ax2.legend(loc='upper right', fontsize=12)  # Era 9
    
    plt.tight_layout()
    return fig

def create_attack_surface_model():
    """
    Figura aggiuntiva: Modello della superficie di attacco distribuita
    """
    fig, ax = plt.subplots(1, 1, figsize=(14, 9))  # Aumentato da 12x8
    
    # Dati dal capitolo
    sizes = ['Piccola\n(10-50)', 'Media\n(51-200)', 'Grande\n(201-500)', 'Enterprise\n(>500)']
    base_surface = np.array([100, 100, 100, 100])  # Normalizzato a 100
    amplification = np.array([15, 31, 47, 68])  # Percentuali di incremento
    zerotrust_reduction = 42.7  # Riduzione con Zero Trust
    
    x = np.arange(len(sizes))
    width = 0.35
    
    # Barre per confronto
    bars1 = ax.bar(x - width/2, base_surface, width, 
                   label='Architettura Centralizzata', color=COLOR_SUCCESS, alpha=0.7)
    bars2 = ax.bar(x + width/2, base_surface + amplification, width,
                   label='Architettura Distribuita', color=COLOR_SECONDARY, alpha=0.7)
    
    # Aggiungi pattern Zero Trust
    for i in range(len(x)):
        zt_value = (base_surface[i] + amplification[i]) * (1 - zerotrust_reduction/100)
        ax.bar(x[i] + width/2, zt_value, width, 
              bottom=0, color='none', edgecolor=COLOR_PRIMARY, 
              linewidth=3, linestyle='--', label='Con Zero Trust' if i == 0 else '')  # Era 2
    
    ax.set_xlabel('Dimensione Organizzazione', fontsize=15)  # Era 11
    ax.set_ylabel('Superficie di Attacco Relativa', fontsize=15)  # Era 11
    ax.set_title('Impatto della Distribuzione sulla Superficie di Attacco', 
                fontsize=17, fontweight='bold')  # Era 12
    ax.set_xticks(x)
    ax.set_xticklabels(sizes, fontsize=13)  # Aumentato
    ax.legend(loc='upper left', fontsize=12)  # Era 9
    ax.grid(True, axis='y', alpha=0.3, linestyle='--')
    ax.tick_params(axis='y', which='major', labelsize=12)  # Nuovo
    
    # Aggiungi percentuali di amplificazione
    for i in range(len(x)):
        height = base_surface[i] + amplification[i]
        ax.text(x[i] + width/2, height + 2, f'+{amplification[i]}%', 
               ha='center', fontsize=12, fontweight='bold', color=COLOR_SECONDARY)  # Era 8
    
    # Annotazione per Zero Trust
    ax.annotate(f'Riduzione del {zerotrust_reduction}%\ncon Zero Trust',
               xy=(3 + width/2, 120), xytext=(2.5, 140),
               arrowprops=dict(arrowstyle='->', color=COLOR_PRIMARY, lw=2),  # Era 1.5
               fontsize=12, ha='center',  # Era 9
               bbox=dict(boxstyle='round,pad=0.3', facecolor='white', 
                        edgecolor=COLOR_PRIMARY))
    
    # Formula nel grafico
    ax.text(0.5, 155, r'$SAD = N \times (C + A + Au)$', 
           fontsize=15, style='italic',  # Era 11
           bbox=dict(boxstyle='round,pad=0.3', facecolor='#F0F0F0'))
    
    plt.tight_layout()
    return fig

def create_cost_breakdown():
    """
    Figura aggiuntiva: Breakdown dei costi di un incidente
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))  # Aumentato da 12x6
    
    # Grafico a torta per la composizione dei costi
    costs = [45, 30, 15, 10]
    labels = ['Costi Diretti\n(Perdita fatturato)', 
              'Costi di Recupero\n(Ripristino sistemi)',
              'Impatto Reputazionale\n(Calo vendite)',
              'Costi di Conformità\n(Sanzioni GDPR)']
    colors = [COLOR_SECONDARY, COLOR_WARNING, COLOR_ACCENT, COLOR_NEUTRAL]
    explode = (0.1, 0, 0, 0)  # Evidenzia i costi diretti
    
    wedges, texts, autotexts = ax1.pie(costs, labels=labels, colors=colors, 
                                        explode=explode, autopct='%1.1f%%',
                                        shadow=True, startangle=90,
                                        textprops={'fontsize': 12})  # Aumentato
    
    # Migliora i testi
    for text in texts:
        text.set_fontsize(12)  # Era 9
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontsize(13)  # Era 10
        autotext.set_fontweight('bold')
    
    ax1.set_title('Composizione dei Costi di un Incidente Tipo', 
                 fontsize=15, fontweight='bold')  # Era 11
    
    # Grafico temporale del recupero
    months = np.arange(0, 19)
    baseline = 100
    
    # Simulazione dell'impatto e recupero
    impact = np.zeros(19)
    impact[0:3] = baseline
    impact[3] = baseline * 0.927  # -7.3% immediato
    
    # Recupero graduale
    for i in range(4, 19):
        recovery_rate = 0.05 * np.exp(-0.1 * (i-4))  # Recupero esponenziale decrescente
        impact[i] = min(baseline, impact[i-1] * (1 + recovery_rate))
    
    ax2.plot(months, impact, linewidth=3, color=COLOR_PRIMARY, marker='o',  # Era 2.5
            markersize=8, markevery=3)  # Era 6
    ax2.axhline(y=baseline, color=COLOR_NEUTRAL, linestyle='--', alpha=0.5, linewidth=2)
    ax2.fill_between(months[3:], impact[3:], baseline, 
                     where=(impact[3:] < baseline), color=COLOR_SECONDARY, alpha=0.2)
    
    ax2.set_xlabel('Mesi dopo l\'incidente', fontsize=14)  # Era 10
    ax2.set_ylabel('Fatturato (% del normale)', fontsize=14)  # Era 10
    ax2.set_title('Impatto Temporale sul Fatturato Post-Incidente', 
                 fontsize=15, fontweight='bold')  # Era 11
    ax2.grid(True, alpha=0.3, linestyle='--')
    ax2.set_xlim(0, 18)
    ax2.set_ylim(85, 105)
    ax2.tick_params(axis='both', which='major', labelsize=12)  # Nuovo
    
    # Aggiungi annotazioni
    ax2.annotate('Incidente', xy=(3, impact[3]), xytext=(3, 80),
                arrowprops=dict(arrowstyle='->', color=COLOR_SECONDARY, lw=2.5),  # Era 2
                fontsize=12, ha='center', fontweight='bold')  # Era 9
    
    ax2.annotate('Recupero completo\n(6-18 mesi)', 
                xy=(15, baseline), xytext=(12, 103),
                arrowprops=dict(arrowstyle='->', color=COLOR_SUCCESS, lw=2),  # Era 1.5
                fontsize=12, ha='center')  # Era 9
    
    # Area di perdita
    ax2.text(8, 94, 'Area = Perdita\nCumulativa', fontsize=11,  # Era 8
            ha='center', color=COLOR_SECONDARY, fontweight='bold')
    
    plt.tight_layout()
    return fig

def create_assa_gdo_model():
    """
    Figura: Modello ASSA GDO con visualizzazione dei fattori moltiplicativi
    """
    fig = plt.figure(figsize=(16, 11))  # Aumentato da 14x10
    
    # Crea una griglia di subplot
    gs = fig.add_gridspec(3, 2, height_ratios=[1, 1.2, 0.8], 
                         width_ratios=[1, 1], hspace=0.3, wspace=0.3)
    
    # Subplot 1: Formula e componenti
    ax1 = fig.add_subplot(gs[0, :])
    ax1.axis('off')
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 3)
    
    # Titolo
    ax1.text(5, 2.7, 'Modello ASSA GDO: Adjusted Security Surface Area per la Grande Distribuzione',
             fontsize=18, fontweight='bold', ha='center')  # Era 13
    
    # Formula principale
    formula_box = FancyBboxPatch((1, 1.3), 8, 1,
                                 boxstyle="round,pad=0.1",
                                 facecolor='#F0F0F0',
                                 edgecolor=COLOR_PRIMARY,
                                 linewidth=2.5)  # Era 2
    ax1.add_patch(formula_box)
    
    ax1.text(5, 1.8, r'$ASSA_{GDO} = SAD \times (1 + T_p) \times (1 + H_v) \times (1 + I_s) \times (1 + P_c)$',
             fontsize=18, ha='center', style='italic')  # Era 14
    
    # Componenti base SAD
    sad_box = FancyBboxPatch((0.5, 0.2), 2, 0.8,
                             boxstyle="round,pad=0.05",
                             facecolor='#E5F3FF',
                             edgecolor=COLOR_ACCENT,
                             linewidth=2)  # Era 1.5
    ax1.add_patch(sad_box)
    ax1.text(1.5, 0.6, 'SAD Base\n(N × Fattori)', 
             fontsize=12, ha='center', fontweight='bold')  # Era 9
    
    # Freccia da SAD alla formula
    arrow1 = FancyArrowPatch((2.5, 0.6), (3, 1.5),
                            arrowstyle='->,head_width=0.15',
                            color=COLOR_ACCENT, linewidth=2)  # Era 1.5
    ax1.add_patch(arrow1)
    
    # Fattori moltiplicativi
    factors = [
        {'pos': (3, 0.2), 'label': 'Tp\nPressione\nTemporale', 'color': COLOR_SECONDARY},
        {'pos': (4.5, 0.2), 'label': 'Hv\nEterogeneità\nVendor', 'color': COLOR_WARNING},
        {'pos': (6, 0.2), 'label': 'Is\nIntegrazione\nServizi', 'color': COLOR_SUCCESS},
        {'pos': (7.5, 0.2), 'label': 'Pc\nComplessità\nPagamenti', 'color': COLOR_PRIMARY},
    ]
    
    for factor in factors:
        factor_box = FancyBboxPatch((factor['pos'][0]-0.4, factor['pos'][1]-0.15), 
                                    0.8, 0.7,
                                    boxstyle="round,pad=0.05",
                                    facecolor='white',
                                    edgecolor=factor['color'],
                                    linewidth=2)  # Era 1.5
        ax1.add_patch(factor_box)
        ax1.text(factor['pos'][0], factor['pos'][1]+0.2, factor['label'],
                fontsize=11, ha='center', va='center')  # Era 8
        
        # Frecce verso la formula
        arrow = FancyArrowPatch((factor['pos'][0], factor['pos'][1]+0.55), 
                               (factor['pos'][0], 1.3),
                               arrowstyle='->,head_width=0.1',
                               color=factor['color'], alpha=0.6, linewidth=1.5)  # Era 1
        ax1.add_patch(arrow)
    
    # Subplot 2: Radar chart dei fattori per le tre catene
    ax2 = fig.add_subplot(gs[1, 0], projection='polar')
    
    # Dati delle catene
    categories = ['Pressione\nTemporale', 'Eterogeneità\nVendor', 
                 'Integrazione\nServizi', 'Complessità\nPagamenti']
    
    catena_alpha = [0.45, 0.60, 0.40, 0.50]
    catena_beta = [0.30, 0.35, 0.25, 0.35]
    catena_gamma = [0.15, 0.20, 0.10, 0.25]
    
    # Angoli per il radar
    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
    catena_alpha += catena_alpha[:1]
    catena_beta += catena_beta[:1]
    catena_gamma += catena_gamma[:1]
    angles += angles[:1]
    
    # Plot
    ax2.plot(angles, catena_alpha, 'o-', linewidth=2.5, label='Alpha (Premium)',  # Era 2
             color=COLOR_SECONDARY)
    ax2.fill(angles, catena_alpha, alpha=0.25, color=COLOR_SECONDARY)
    
    ax2.plot(angles, catena_beta, 'o-', linewidth=2.5, label='Beta (Standard)',  # Era 2
             color=COLOR_WARNING)
    ax2.fill(angles, catena_beta, alpha=0.25, color=COLOR_WARNING)
    
    ax2.plot(angles, catena_gamma, 'o-', linewidth=2.5, label='Gamma (Discount)',  # Era 2
             color=COLOR_SUCCESS)
    ax2.fill(angles, catena_gamma, alpha=0.25, color=COLOR_SUCCESS)
    
    # Configurazione assi
    ax2.set_xticks(angles[:-1])
    ax2.set_xticklabels(categories, fontsize=12)  # Era 9
    ax2.set_ylim(0, 0.7)
    ax2.set_yticks([0.2, 0.4, 0.6])
    ax2.set_yticklabels(['0.2', '0.4', '0.6'], fontsize=11)  # Era 8
    ax2.grid(True)
    
    ax2.set_title('Profili di Rischio per Tipologia di Catena', 
                 fontsize=15, fontweight='bold', pad=20)  # Era 11
    ax2.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=12)  # Era 9
    
    # Subplot 3: Moltiplicatore ASSA risultante
    ax3 = fig.add_subplot(gs[1, 1])
    
    catene = ['Alpha\n(Premium)', 'Beta\n(Standard)', 'Gamma\n(Discount)', 'Media\nSettore']
    moltiplicatori = [3.78, 2.41, 1.87, 2.52]
    colors = [COLOR_SECONDARY, COLOR_WARNING, COLOR_SUCCESS, COLOR_PRIMARY]
    
    bars = ax3.bar(range(len(catene)), moltiplicatori, color=colors, alpha=0.7)
    
    # Aggiungi valori sulle barre
    for i, (bar, val) in enumerate(zip(bars, moltiplicatori)):
        ax3.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
                f'{val:.2f}×', ha='center', fontsize=13, fontweight='bold')  # Era 10
    
    # Linea media
    ax3.axhline(y=2.52, color=COLOR_PRIMARY, linestyle='--', 
               linewidth=2.5, alpha=0.5, label='Media Settore')  # Era 2
    
    ax3.set_xlabel('Tipologia Catena', fontsize=14)  # Era 10
    ax3.set_ylabel('Moltiplicatore ASSA', fontsize=14)  # Era 10
    ax3.set_title('Amplificazione della Superficie di Attacco', 
                 fontsize=15, fontweight='bold')  # Era 11
    ax3.set_xticks(range(len(catene)))
    ax3.set_xticklabels(catene, fontsize=12)  # Era 9
    ax3.set_ylim(0, 4.5)
    ax3.grid(True, axis='y', alpha=0.3, linestyle='--')
    ax3.tick_params(axis='y', which='major', labelsize=12)  # Nuovo
    
    # Annotazione per il valore massimo
    ax3.annotate('Rischio massimo\ndurante i picchi:\n4.2×',
                xy=(0, 3.78), xytext=(-0.5, 4.2),
                arrowprops=dict(arrowstyle='->', color=COLOR_SECONDARY, lw=2),  # Era 1.5
                fontsize=11, ha='center',  # Era 8
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white', 
                         edgecolor=COLOR_SECONDARY))
    
    # Subplot 4: Breakdown contributi percentuali
    ax4 = fig.add_subplot(gs[2, :])
    
    # Dati dei contributi
    contributi = ['Complessità Pagamenti', 'Eterogeneità Vendor', 
                 'Pressione Temporale', 'Integrazione Servizi']
    percentuali = [37, 38, 15, 10]
    colors_contrib = [COLOR_PRIMARY, COLOR_WARNING, COLOR_SECONDARY, COLOR_SUCCESS]
    
    # Crea barre orizzontali cumulative
    left = 0
    for i, (contrib, perc, color) in enumerate(zip(contributi, percentuali, colors_contrib)):
        ax4.barh(0, perc, left=left, height=0.5, color=color, alpha=0.7)
        
        # Aggiungi testo
        ax4.text(left + perc/2, 0, f'{contrib}\n{perc}%', 
                ha='center', va='center', fontsize=12, fontweight='bold')  # Era 9
        left += perc
    
    ax4.set_xlim(0, 100)
    ax4.set_ylim(-0.5, 0.8)
    ax4.set_xlabel('Contributo Percentuale all\'Amplificazione (%)', fontsize=14)  # Era 10
    ax4.set_title('Decomposizione dei Fattori di Rischio nel Modello ASSA GDO', 
                 fontsize=15, fontweight='bold')  # Era 11
    ax4.set_yticks([])
    ax4.grid(True, axis='x', alpha=0.3, linestyle='--')
    ax4.tick_params(axis='x', which='major', labelsize=12)  # Nuovo
    
    # Note metodologiche
    ax4.text(50, -0.35, 
            'Nota: Valori calibrati su 47 organizzazioni GDO italiane (periodo 2023-2024)',
            fontsize=11, ha='center', style='italic', color=COLOR_NEUTRAL)  # Era 8
    
    plt.suptitle('', fontsize=1)  # Rimuove il titolo generale se presente
    plt.tight_layout()
    
    return fig

def create_temporal_risk_heatmap():
    """
    Figura aggiuntiva: Heatmap del rischio temporale nella GDO
    """
    fig, ax = plt.subplots(1, 1, figsize=(14, 8))  # Aumentato da 12x6
    
    # Dati per la heatmap
    mesi = ['Gen', 'Feb', 'Mar', 'Apr', 'Mag', 'Giu', 
            'Lug', 'Ago', 'Set', 'Ott', 'Nov', 'Dic']
    ore = [f'{h:02d}:00' for h in range(0, 24, 2)]
    
    # Genera matrice di rischio (simulata ma basata su pattern reali)
    np.random.seed(42)
    risk_matrix = np.zeros((12, 12))
    
    # Pattern base
    for m in range(12):
        for h in range(12):
            # Rischio base
            base_risk = 0.3
            
            # Incremento per mesi di picco
            if m in [6, 10, 11]:  # Luglio, Novembre, Dicembre
                base_risk += 0.3
            
            # Incremento per orari di punta
            if h in [5, 6, 7, 8]:  # 10:00-18:00
                base_risk += 0.2
            
            # Variazione casuale
            risk_matrix[h, m] = base_risk + np.random.uniform(-0.1, 0.1)
    
    # Normalizza tra 0 e 1
    risk_matrix = np.clip(risk_matrix, 0, 1)
    
    # Crea heatmap
    im = ax.imshow(risk_matrix, cmap='YlOrRd', aspect='auto', vmin=0, vmax=1)
    
    # Configura assi
    ax.set_xticks(np.arange(len(mesi)))
    ax.set_yticks(np.arange(len(ore)))
    ax.set_xticklabels(mesi, fontsize=13)  # Aumentato
    ax.set_yticklabels(ore, fontsize=13)  # Aumentato
    
    # Ruota etichette
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
    
    # Aggiungi colorbar
    cbar = plt.colorbar(im, ax=ax)
    cbar.set_label('Indice di Rischio Normalizzato', rotation=270, labelpad=25, fontsize=14)  # Aumentato
    cbar.ax.tick_params(labelsize=12)  # Nuovo
    
    # Titolo e etichette
    ax.set_title('Mappa Temporale del Rischio: Pattern Orari e Stagionali nella GDO',
                fontsize=17, fontweight='bold', pad=20)  # Era 12
    ax.set_xlabel('Mese', fontsize=15)  # Era 11
    ax.set_ylabel('Ora del Giorno', fontsize=15)  # Era 11
    
    # Aggiungi annotazioni per i picchi
    ax.text(6.5, 6, 'PICCO\nESTIVO', fontsize=12, fontweight='bold',  # Era 9
           ha='center', va='center', color='white',
           bbox=dict(boxstyle='round,pad=0.3', facecolor=COLOR_SECONDARY, alpha=0.8))
    
    ax.text(11, 7, 'PICCO\nNATALIZIO', fontsize=12, fontweight='bold',  # Era 9
           ha='center', va='center', color='white',
           bbox=dict(boxstyle='round,pad=0.3', facecolor=COLOR_SECONDARY, alpha=0.8))
    
    # Griglia leggera
    ax.set_xticks(np.arange(len(mesi))-.5, minor=True)
    ax.set_yticks(np.arange(len(ore))-.5, minor=True)
    ax.grid(which="minor", color="white", linestyle='-', linewidth=2.5)  # Era 2
    ax.tick_params(which="minor", size=0)
    
    plt.tight_layout()
    return fig

# Funzione principale per generare tutte le figure
def main():
    print("Generazione figure per il Capitolo 2 con FONT LARGE...")
    
    # Figura 2.2: Convergenza IT-OT
    print("Creando Figura 2.2: Convergenza IT-OT...")
    fig1 = create_it_ot_convergence()
    fig1.savefig('/mnt/user-data/outputs/fig_2_2_convergenza_it_ot.pdf', 
                 dpi=300, bbox_inches='tight', format='pdf')
    fig1.savefig('/mnt/user-data/outputs/fig_2_2_convergenza_it_ot.png', 
                 dpi=150, bbox_inches='tight')
    plt.close(fig1)
    
    # Figura 2.4: Sistema di Orchestrazione
    print("Creando Figura 2.4: Sistema di Orchestrazione...")
    fig2 = create_orchestration_system()
    fig2.savefig('/mnt/user-data/outputs/fig_2_4_orchestrazione.pdf', 
                 dpi=300, bbox_inches='tight', format='pdf')
    fig2.savefig('/mnt/user-data/outputs/fig_2_4_orchestrazione.png', 
                 dpi=150, bbox_inches='tight')
    plt.close(fig2)
    
    # Figure aggiuntive
    print("Creando Figura aggiuntiva: Evoluzione Attacchi...")
    fig3 = create_attack_evolution()
    fig3.savefig('/mnt/user-data/outputs/fig_2_3_evoluzione_attacchi.pdf', 
                 dpi=300, bbox_inches='tight', format='pdf')
    fig3.savefig('/mnt/user-data/outputs/fig_2_3_evoluzione_attacchi.png', 
                 dpi=150, bbox_inches='tight')
    plt.close(fig3)
    
    print("Creando Figura aggiuntiva: Modello Superficie di Attacco...")
    fig4 = create_attack_surface_model()
    fig4.savefig('/mnt/user-data/outputs/fig_2_1_superficie_attacco.pdf', 
                 dpi=300, bbox_inches='tight', format='pdf')
    fig4.savefig('/mnt/user-data/outputs/fig_2_1_superficie_attacco.png', 
                 dpi=150, bbox_inches='tight')
    plt.close(fig4)
    
    print("Creando Figura aggiuntiva: Breakdown Costi...")
    fig5 = create_cost_breakdown()
    fig5.savefig('/mnt/user-data/outputs/fig_2_5_costi_incidente.pdf', 
                 dpi=300, bbox_inches='tight', format='pdf')
    fig5.savefig('/mnt/user-data/outputs/fig_2_5_costi_incidente.png', 
                 dpi=150, bbox_inches='tight')
    plt.close(fig5)
    
    print("Creando Figura ASSA GDO Model...")
    fig6 = create_assa_gdo_model()
    fig6.savefig('/mnt/user-data/outputs/fig_2_6_assa_gdo_model.pdf', 
                 dpi=300, bbox_inches='tight', format='pdf')
    fig6.savefig('/mnt/user-data/outputs/fig_2_6_assa_gdo_model.png', 
                 dpi=150, bbox_inches='tight')
    plt.close(fig6)
    
    print("Creando Heatmap del Rischio Temporale...")
    fig7 = create_temporal_risk_heatmap()
    fig7.savefig('/mnt/user-data/outputs/fig_2_7_temporal_risk_heatmap.pdf', 
                 dpi=300, bbox_inches='tight', format='pdf')
    fig7.savefig('/mnt/user-data/outputs/fig_2_7_temporal_risk_heatmap.png', 
                 dpi=150, bbox_inches='tight')
    plt.close(fig7)
    
    print("\n✓ Tutte le figure sono state generate con successo con FONT LARGE!")
    print("\nFile creati (versione aggiornata):")
    print("- fig_2_1_superficie_attacco.pdf/png")
    print("- fig_2_2_convergenza_it_ot.pdf/png")
    print("- fig_2_3_evoluzione_attacchi.pdf/png")
    print("- fig_2_4_orchestrazione.pdf/png")
    print("- fig_2_5_costi_incidente.pdf/png")
    print("- fig_2_6_assa_gdo_model.pdf/png")
    print("- fig_2_7_temporal_risk_heatmap.pdf/png")

if __name__ == "__main__":
    main()
