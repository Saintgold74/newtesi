#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator di Figure per il Capitolo 3 della Tesi
Infrastruttura e Architetture nella Grande Distribuzione Organizzata
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch
import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib.patches import Rectangle, FancyBboxPatch, ConnectionPatch
import matplotlib.lines as mlines

# Configurazione generale per aspetto accademico
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman', 'DejaVu Serif']
plt.rcParams['font.size'] = 11
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10
plt.rcParams['legend.fontsize'] = 10
plt.rcParams['figure.titlesize'] = 16

# Palette colori professionali
colors = {
    'primary': '#2E4057',      # Blu scuro professionale
    'secondary': '#048A81',    # Verde acqua
    'accent': '#F18F01',       # Arancione
    'danger': '#C73E1D',       # Rosso
    'success': '#6A994E',      # Verde
    'info': '#3D5A80',         # Blu medio
    'light': '#F5F5F5',        # Grigio chiaro
    'dark': '#1A1A1A'          # Nero
}

def create_power_architecture_2n():
    """
    Figura 1: Architettura di Alimentazione Ridondante 2N
    """
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Titolo
    ax.text(7, 9.5, 'Architettura Alimentazione Ridondante 2N', 
            fontsize=16, fontweight='bold', ha='center')
    
    # Sistema A (Superiore)
    # Rete Elettrica Primaria
    rect1 = FancyBboxPatch((0.5, 6.5), 2, 1.5, 
                           boxstyle="round,pad=0.1",
                           facecolor='#E8F4F8', edgecolor=colors['primary'], linewidth=2)
    ax.add_patch(rect1)
    ax.text(1.5, 7.25, 'Rete Elettrica\nPrimaria', ha='center', va='center', fontweight='bold')
    
    # UPS Sistema A
    ups_a1 = FancyBboxPatch((3.5, 7), 1.8, 1, 
                            boxstyle="round,pad=0.05",
                            facecolor='#E8F8E8', edgecolor=colors['success'], linewidth=2)
    ax.add_patch(ups_a1)
    ax.text(4.4, 7.5, 'UPS 1A\n100kW', ha='center', va='center', fontsize=10)
    
    ups_a2 = FancyBboxPatch((3.5, 5.5), 1.8, 1, 
                            boxstyle="round,pad=0.05",
                            facecolor='#E8F8E8', edgecolor=colors['success'], linewidth=2)
    ax.add_patch(ups_a2)
    ax.text(4.4, 6, 'UPS 1B\n100kW', ha='center', va='center', fontsize=10)
    
    # PDU Sistema A
    pdu_a = FancyBboxPatch((7, 6.25), 2, 1.5, 
                          boxstyle="round,pad=0.05",
                          facecolor='#FFF8E8', edgecolor=colors['accent'], linewidth=2)
    ax.add_patch(pdu_a)
    ax.text(8, 7, 'PDU\nLato A', ha='center', va='center', fontweight='bold')
    
    # Sistema B (Inferiore)
    # Rete Elettrica Secondaria
    rect2 = FancyBboxPatch((0.5, 2), 2, 1.5, 
                           boxstyle="round,pad=0.1",
                           facecolor='#E8F4F8', edgecolor=colors['primary'], linewidth=2)
    ax.add_patch(rect2)
    ax.text(1.5, 2.75, 'Rete Elettrica\nSecondaria', ha='center', va='center', fontweight='bold')
    
    # UPS Sistema B
    ups_b1 = FancyBboxPatch((3.5, 2.5), 1.8, 1, 
                            boxstyle="round,pad=0.05",
                            facecolor='#E8F8E8', edgecolor=colors['success'], linewidth=2)
    ax.add_patch(ups_b1)
    ax.text(4.4, 3, 'UPS 2A\n100kW', ha='center', va='center', fontsize=10)
    
    ups_b2 = FancyBboxPatch((3.5, 1), 1.8, 1, 
                            boxstyle="round,pad=0.05",
                            facecolor='#E8F8E8', edgecolor=colors['success'], linewidth=2)
    ax.add_patch(ups_b2)
    ax.text(4.4, 1.5, 'UPS 2B\n100kW', ha='center', va='center', fontsize=10)
    
    # PDU Sistema B
    pdu_b = FancyBboxPatch((7, 1.75), 2, 1.5, 
                          boxstyle="round,pad=0.05",
                          facecolor='#FFF8E8', edgecolor=colors['accent'], linewidth=2)
    ax.add_patch(pdu_b)
    ax.text(8, 2.5, 'PDU\nLato B', ha='center', va='center', fontweight='bold')
    
    # Server con Dual PSU
    server = FancyBboxPatch((10.5, 3.5), 2.5, 2, 
                           boxstyle="round,pad=0.05",
                           facecolor='#FFE8E8', edgecolor=colors['danger'], linewidth=2.5)
    ax.add_patch(server)
    ax.text(11.75, 4.5, 'SERVER\nDual PSU', ha='center', va='center', 
            fontweight='bold', fontsize=12)
    
    # Frecce di connessione
    # Sistema A
    ax.arrow(2.5, 7.25, 0.9, 0.25, head_width=0.15, head_length=0.1, 
             fc=colors['primary'], ec=colors['primary'])
    ax.arrow(2.5, 7.25, 0.9, -1.25, head_width=0.15, head_length=0.1, 
             fc=colors['primary'], ec=colors['primary'])
    ax.arrow(5.3, 7.5, 1.6, -0.3, head_width=0.15, head_length=0.1, 
             fc=colors['success'], ec=colors['success'])
    ax.arrow(5.3, 6, 1.6, 0.8, head_width=0.15, head_length=0.1, 
             fc=colors['success'], ec=colors['success'])
    
    # Sistema B
    ax.arrow(2.5, 2.75, 0.9, 0.25, head_width=0.15, head_length=0.1, 
             fc=colors['primary'], ec=colors['primary'])
    ax.arrow(2.5, 2.75, 0.9, -1.25, head_width=0.15, head_length=0.1, 
             fc=colors['primary'], ec=colors['primary'])
    ax.arrow(5.3, 3, 1.6, -0.3, head_width=0.15, head_length=0.1, 
             fc=colors['success'], ec=colors['success'])
    ax.arrow(5.3, 1.5, 1.6, 0.8, head_width=0.15, head_length=0.1, 
             fc=colors['success'], ec=colors['success'])
    
    # Connessioni ai server
    ax.arrow(9, 6.8, 1.4, -1.8, head_width=0.15, head_length=0.1, 
             fc=colors['accent'], ec=colors['accent'])
    ax.text(9.8, 5.5, 'PSU1', fontsize=10, rotation=-45)
    ax.arrow(9, 2.5, 1.4, 1.5, head_width=0.15, head_length=0.1, 
             fc=colors['accent'], ec=colors['accent'])
    ax.text(9.8, 3.5, 'PSU2', fontsize=10, rotation=40)
    
    # Etichette Sistema
    ax.text(4.5, 8.5, 'SISTEMA A', fontsize=14, fontweight='bold', 
            color=colors['primary'], ha='center')
    ax.text(4.5, 0.3, 'SISTEMA B', fontsize=14, fontweight='bold', 
            color=colors['primary'], ha='center')
    
    # Box metriche
    metrics_box = FancyBboxPatch((10.5, 0.5), 2.5, 2, 
                                 boxstyle="round,pad=0.1",
                                 facecolor=colors['light'], edgecolor=colors['dark'], 
                                 linewidth=1.5)
    ax.add_patch(metrics_box)
    ax.text(11.75, 1.8, 'METRICHE', fontweight='bold', ha='center', fontsize=11)
    ax.text(11.75, 1.4, 'Disponibilità:', fontweight='bold', ha='center', fontsize=10)
    ax.text(11.75, 1.1, '99.94%', ha='center', fontsize=12, color=colors['success'])
    ax.text(11.75, 0.8, 'MTBF: 87,600h', ha='center', fontsize=9)
    
    plt.tight_layout()
    return fig

def create_multicloud_orchestration():
    """
    Figura 2: Architettura Orchestrazione Multi-Cloud
    """
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Titolo
    ax.text(7, 9.5, 'Architettura Orchestrazione Multi-Cloud', 
            fontsize=16, fontweight='bold', ha='center')
    
    # Orchestratore Centrale
    orch = FancyBboxPatch((5.5, 6.5), 3, 1.5, 
                          boxstyle="round,pad=0.1",
                          facecolor='#F0E6FF', edgecolor='#6B46C1', linewidth=2.5)
    ax.add_patch(orch)
    ax.text(7, 7.25, 'ORCHESTRATORE\nKubernetes Federation', 
            ha='center', va='center', fontweight='bold', fontsize=11)
    
    # Ottimizzatore RL
    opt = FancyBboxPatch((1, 6.5), 2.5, 1.5, 
                        boxstyle="round,pad=0.1",
                        facecolor='#FFE6E6', edgecolor=colors['danger'], linewidth=2)
    ax.add_patch(opt)
    ax.text(2.25, 7.25, 'Ottimizzatore\nRL-Based', ha='center', va='center', fontsize=10)
    
    # Sistema Metriche
    metrics = FancyBboxPatch((10.5, 6.5), 2.5, 1.5, 
                            boxstyle="round,pad=0.1",
                            facecolor='#E6E6E6', edgecolor=colors['dark'], linewidth=2)
    ax.add_patch(metrics)
    ax.text(11.75, 7.25, 'Metriche\nPrometheus', ha='center', va='center', fontsize=10)
    
    # Cloud Providers
    # AWS
    aws = patches.Ellipse((2, 3.5), 2.8, 1.8, 
                         facecolor='#FFE6CC', edgecolor='#FF9900', linewidth=2)
    ax.add_patch(aws)
    ax.text(2, 3.5, 'AWS\nEU Region', ha='center', va='center', fontweight='bold')
    
    # Azure
    azure = patches.Ellipse((7, 3.5), 2.8, 1.8, 
                           facecolor='#CCE6FF', edgecolor='#0078D4', linewidth=2)
    ax.add_patch(azure)
    ax.text(7, 3.5, 'Azure\nEU Region', ha='center', va='center', fontweight='bold')
    
    # GCP
    gcp = patches.Ellipse((12, 3.5), 2.8, 1.8, 
                         facecolor='#E6FFE6', edgecolor='#34A853', linewidth=2)
    ax.add_patch(gcp)
    ax.text(12, 3.5, 'GCP\nEU Region', ha='center', va='center', fontweight='bold')
    
    # On-Premise
    onprem = FancyBboxPatch((5.5, 0.5), 3, 1.2, 
                           boxstyle="round,pad=0.1",
                           facecolor='#FFE6E6', edgecolor=colors['accent'], linewidth=2)
    ax.add_patch(onprem)
    ax.text(7, 1.1, 'Data Center\nOn-Premise', ha='center', va='center', fontweight='bold')
    
    # Workloads
    workloads = [
        (2, 4.8, 'Web\nApps'),
        (7, 4.8, 'Database\nCluster'),
        (12, 4.8, 'ML\nPipeline')
    ]
    
    for x, y, label in workloads:
        wl = FancyBboxPatch((x-0.7, y-0.3), 1.4, 0.8, 
                           boxstyle="round,pad=0.05",
                           facecolor='#FFFACD', edgecolor='#DAA520', linewidth=1)
        ax.add_patch(wl)
        ax.text(x, y, label, ha='center', va='center', fontsize=9)
    
    # Connessioni
    # Da orchestratore a cloud
    connections = [
        (6.5, 6.5, 2.5, 4.4),    # to AWS
        (7, 6.5, 7, 4.4),        # to Azure
        (7.5, 6.5, 11.5, 4.4),   # to GCP
        (7, 6.5, 7, 1.7)         # to On-Prem
    ]
    
    for x1, y1, x2, y2 in connections:
        ax.plot([x1, x2], [y1, y2], 'k-', linewidth=2, alpha=0.6)
        ax.plot([x1, x2], [y1, y2], 'ko', markersize=6)
    
    # Connessioni ottimizzatore e metriche
    ax.annotate('', xy=(5.5, 7.25), xytext=(3.5, 7.25),
                arrowprops=dict(arrowstyle='<->', connectionstyle="arc3,rad=0.3",
                              color=colors['danger'], lw=2))
    ax.annotate('', xy=(8.5, 7.25), xytext=(10.5, 7.25),
                arrowprops=dict(arrowstyle='<->', connectionstyle="arc3,rad=-0.3",
                              color=colors['dark'], lw=2))
    
    # Box risultati
    results_box = FancyBboxPatch((0.5, 0.5), 3, 2, 
                                boxstyle="round,pad=0.1",
                                facecolor=colors['light'], edgecolor=colors['dark'], 
                                linewidth=1.5)
    ax.add_patch(results_box)
    ax.text(2, 2, 'RISULTATI', fontweight='bold', ha='center', fontsize=11)
    ax.text(2, 1.6, '• Costi: -31%', ha='center', fontsize=10, color=colors['success'])
    ax.text(2, 1.3, '• Latenza: -23%', ha='center', fontsize=10, color=colors['success'])
    ax.text(2, 1.0, '• Violaz. SLA: -67%', ha='center', fontsize=10, color=colors['success'])
    ax.text(2, 0.7, 'ROI: 24 mesi', ha='center', fontsize=9)
    
    plt.tight_layout()
    return fig

def create_gist_framework():
    """
    Figura 3: Framework GIST - 5 Livelli di Maturità
    """
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 11)
    ax.axis('off')
    
    # Titolo
    ax.text(7, 10.5, 'Framework GIST - Maturità Infrastrutturale', 
            fontsize=16, fontweight='bold', ha='center')
    ax.text(7, 10, 'Grande Distribuzione Infrastructure Security Transformation', 
            fontsize=11, ha='center', style='italic')
    
    # Livelli del framework
    levels = [
        (1.5, '#FFE6E6', colors['danger'], 'Livello 1: Fondamenta Fisiche',
         'Alimentazione 2N • Raffreddamento • Monitoraggio', 'Uptime 99.9%', '0-6 mesi'),
        (3.2, '#FFE6CC', colors['accent'], 'Livello 2: Software-Defined',
         'SDN • Virtualizzazione • Automazione Base', 'MTTR <2h', '6-12 mesi'),
        (4.9, '#FFFFE6', '#DAA520', 'Livello 3: Cloud Ibrido',
         'IaaS/PaaS • Multi-Cloud • Container', 'TCO -30%', '12-18 mesi'),
        (6.6, '#E6FFE6', colors['success'], 'Livello 4: Zero Trust',
         'Micro-segmentazione • ABAC • Continuous Verification', 'MTTD <24h', '18-24 mesi'),
        (8.3, '#E6E6FF', colors['info'], 'Livello 5: Intelligenza',
         'Edge Computing • AI/ML • Automazione Cognitiva', 'Auto 80%', '24-36 mesi')
    ]
    
    for y, facecolor, edgecolor, title, desc, kpi, timeline in levels:
        # Box principale del livello
        level_box = FancyBboxPatch((2, y-0.6), 8, 1.2, 
                                   boxstyle="round,pad=0.05",
                                   facecolor=facecolor, edgecolor=edgecolor, 
                                   linewidth=2, alpha=0.9)
        ax.add_patch(level_box)
        
        # Testi del livello
        ax.text(6, y+0.15, title, ha='center', va='center', 
                fontweight='bold', fontsize=12)
        ax.text(6, y-0.25, desc, ha='center', va='center', 
                fontsize=9, style='italic')
        
        # KPI box
        kpi_box = FancyBboxPatch((10.5, y-0.4), 2.5, 0.8, 
                                 boxstyle="round,pad=0.05",
                                 facecolor='white', edgecolor=edgecolor, 
                                 linewidth=1.5)
        ax.add_patch(kpi_box)
        ax.text(11.75, y, kpi, ha='center', va='center', 
                fontsize=9, fontweight='bold', color=edgecolor)
        
        # Timeline
        ax.text(1.3, y, timeline, ha='right', va='center', 
                fontsize=9, color=colors['dark'])
    
    # Frecce tra i livelli
    for i in range(len(levels)-1):
        y1 = levels[i][0] + 0.6
        y2 = levels[i+1][0] - 0.6
        arrow = FancyArrowPatch((6, y1), (6, y2),
                               arrowstyle='->', mutation_scale=25,
                               color=colors['dark'], linewidth=2, alpha=0.7)
        ax.add_patch(arrow)
    
    # Legenda laterale
    ax.text(0.5, 9, 'TIMELINE', fontweight='bold', fontsize=10, rotation=90, va='center')
    ax.text(12.5, 9, 'KPI TARGET', fontweight='bold', fontsize=10, rotation=90, va='center')
    
    # Box riassuntivo in basso
    summary_box = FancyBboxPatch((2, 0.2), 8, 0.8, 
                                 boxstyle="round,pad=0.1",
                                 facecolor=colors['light'], edgecolor=colors['dark'], 
                                 linewidth=1.5)
    ax.add_patch(summary_box)
    ax.text(6, 0.6, 'Risultati Validati: Disponibilità 99.97% • TCO -34.2% • MTTD 3.4 giorni • ROI 24 mesi', 
            ha='center', va='center', fontsize=10, fontweight='bold')
    
    plt.tight_layout()
    return fig

def create_maintenance_comparison():
    """
    Figura 4: Confronto Manutenzione Tradizionale vs Predittiva IA
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 8))
    
    # Dati per il confronto
    metrics = ['Accuratezza\nPredizione', 'Anticipo\nAvviso', 'Riduzione\nDowntime', 
               'Riduzione\nCosti', 'ROI']
    traditional = [66, 12, 0, 0, 0]
    ai_based = [94.3, 72, 67, 42, 100]  # ROI normalizzato a 100 per 8 mesi
    
    x = np.arange(len(metrics))
    width = 0.35
    
    # Grafico a barre
    bars1 = ax1.bar(x - width/2, traditional, width, label='Sistema Tradizionale',
                    color=colors['danger'], alpha=0.8)
    bars2 = ax1.bar(x + width/2, ai_based, width, label='Sistema IA',
                    color=colors['success'], alpha=0.8)
    
    ax1.set_xlabel('Metriche', fontweight='bold')
    ax1.set_ylabel('Valore (%/ore)', fontweight='bold')
    ax1.set_title('Confronto Sistemi di Manutenzione', fontweight='bold', fontsize=14)
    ax1.set_xticks(x)
    ax1.set_xticklabels(metrics)
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Aggiungere valori sopra le barre
    for bar in bars1:
        height = bar.get_height()
        if height > 0:
            ax1.text(bar.get_x() + bar.get_width()/2., height + 1,
                    f'{height:.0f}', ha='center', va='bottom', fontsize=9)
    
    for bar in bars2:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + 1,
                f'{height:.1f}', ha='center', va='bottom', fontsize=9)
    
    # Grafico timeline guasti
    ax2.set_title('Timeline Predizione Guasti', fontweight='bold', fontsize=14)
    ax2.set_xlabel('Tempo (giorni)', fontweight='bold')
    ax2.set_ylabel('Probabilità Guasto (%)', fontweight='bold')
    
    # Simulazione curva predizione
    days = np.linspace(0, 10, 100)
    prob_traditional = np.where(days > 9, 100, 0)  # Rilevamento solo al guasto
    prob_ai = 100 / (1 + np.exp(-2*(days - 7)))  # Curva sigmoide
    
    ax2.plot(days, prob_traditional, '--', color=colors['danger'], 
             linewidth=2, label='Tradizionale')
    ax2.plot(days, prob_ai, '-', color=colors['success'], 
             linewidth=2, label='IA Predittiva')
    
    # Aree di interesse
    ax2.axvspan(7-3, 7, alpha=0.2, color=colors['success'], label='Finestra Intervento IA')
    ax2.axvline(x=7, color='red', linestyle=':', linewidth=2, label='Guasto Effettivo')
    
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 105)
    ax2.legend(loc='upper left')
    ax2.grid(True, alpha=0.3)
    
    plt.suptitle('Manutenzione Predittiva con Intelligenza Artificiale', 
                 fontsize=16, fontweight='bold', y=1.02)
    plt.tight_layout()
    return fig

def create_security_metrics():
    """
    Figura 5: Metriche di Sicurezza Pre e Post Zero Trust
    """
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # Dati
    categories = ['MTTD\n(giorni)', 'Movimenti\nLaterali (%)', 'Accessi\nNon Autorizzati', 
                  'Superficie\nAttacco', 'Costo\nIncidente (k€)']
    pre_zt = [197, 73, 3, 1247, 127]
    post_zt = [3.4, 12, 47, 89, 23]
    
    # Normalizzare per visualizzazione
    pre_norm = [100, 100, 10, 100, 100]  # Normalizzati per confronto visuale
    post_norm = [1.7, 16.4, 100, 7.1, 18.1]  # Proporzionali ai miglioramenti
    
    # Radar chart
    ax = axes[0, 0]
    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
    pre_norm += pre_norm[:1]
    post_norm += post_norm[:1]
    angles += angles[:1]
    
    ax = plt.subplot(221, projection='polar')
    ax.plot(angles, pre_norm, 'o-', linewidth=2, color=colors['danger'], label='Pre Zero Trust')
    ax.fill(angles, pre_norm, alpha=0.25, color=colors['danger'])
    ax.plot(angles, post_norm, 'o-', linewidth=2, color=colors['success'], label='Post Zero Trust')
    ax.fill(angles, post_norm, alpha=0.25, color=colors['success'])
    
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, size=9)
    ax.set_ylim(0, 100)
    ax.set_title('Radar Comparativo Sicurezza', fontweight='bold', fontsize=12, pad=20)
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
    
    # Timeline riduzione MTTD
    ax2 = axes[0, 1]
    months = np.arange(0, 19)
    mttd_reduction = 197 - (197 - 3.4) * (1 - np.exp(-0.3 * months))
    
    ax2.plot(months, mttd_reduction, '-', color=colors['info'], linewidth=3)
    ax2.fill_between(months, mttd_reduction, 197, alpha=0.3, color=colors['info'])
    ax2.set_xlabel('Mesi dall\'Implementazione', fontweight='bold')
    ax2.set_ylabel('MTTD (giorni)', fontweight='bold')
    ax2.set_title('Evoluzione Tempo di Rilevamento', fontweight='bold', fontsize=12)
    ax2.grid(True, alpha=0.3)
    ax2.set_xlim(0, 18)
    
    # Riduzione superficie di attacco
    ax3 = axes[1, 0]
    components = ['Endpoint\nEsposti', 'Porte\nAperte', 'Servizi\nPubblici', 
                  'Accessi\nPrivilegiati', 'Connessioni\nNon Cifrate']
    pre_values = [1247, 89, 45, 234, 567]
    post_values = [89, 12, 8, 23, 0]
    
    x = np.arange(len(components))
    width = 0.35
    
    bars1 = ax3.bar(x - width/2, pre_values, width, label='Pre Zero Trust',
                    color=colors['danger'], alpha=0.8)
    bars2 = ax3.bar(x + width/2, post_values, width, label='Post Zero Trust',
                    color=colors['success'], alpha=0.8)
    
    ax3.set_ylabel('Numero', fontweight='bold')
    ax3.set_title('Riduzione Superficie di Attacco', fontweight='bold', fontsize=12)
    ax3.set_xticks(x)
    ax3.set_xticklabels(components, fontsize=9)
    ax3.legend()
    ax3.grid(True, alpha=0.3, axis='y')
    
    # Cost savings
    ax4 = axes[1, 1]
    years = ['Anno 0', 'Anno 1', 'Anno 2', 'Anno 3']
    investment = [-350, -50, -30, -20]  # Costi negativi
    savings = [0, 180, 220, 250]  # Risparmi positivi
    cumulative = [-350, -220, -30, 200]  # Cumulativo
    
    x = np.arange(len(years))
    width = 0.35
    
    bars1 = ax4.bar(x - width/2, investment, width, label='Investimento',
                    color=colors['danger'], alpha=0.8)
    bars2 = ax4.bar(x + width/2, savings, width, label='Risparmi',
                    color=colors['success'], alpha=0.8)
    
    ax4_twin = ax4.twinx()
    ax4_twin.plot(x, cumulative, 'o-', color=colors['info'], linewidth=2, 
                  markersize=8, label='ROI Cumulativo')
    ax4_twin.axhline(y=0, color='black', linestyle='--', alpha=0.5)
    
    ax4.set_xlabel('Periodo', fontweight='bold')
    ax4.set_ylabel('Flusso di Cassa (k€)', fontweight='bold')
    ax4_twin.set_ylabel('ROI Cumulativo (k€)', fontweight='bold')
    ax4.set_title('Analisi ROI Zero Trust', fontweight='bold', fontsize=12)
    ax4.set_xticks(x)
    ax4.set_xticklabels(years)
    ax4.legend(loc='upper left')
    ax4_twin.legend(loc='upper right')
    ax4.grid(True, alpha=0.3, axis='y')
    
    plt.suptitle('Impatto dell\'Architettura Zero Trust sulla Sicurezza', 
                 fontsize=16, fontweight='bold')
    plt.tight_layout()
    return fig

def create_cloud_migration_matrix():
    """
    Figura 6: Matrice Decisionale per Migrazione Cloud
    """
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Dati per la matrice
    applications = ['ERP Core', 'E-commerce', 'Analytics', 'Email', 'Backup', 
                   'Dev/Test', 'CRM', 'Supply Chain', 'POS Systems', 'Mobile App']
    
    criticality = [10, 9, 6, 4, 5, 2, 7, 8, 10, 6]
    variability = [3, 9, 8, 2, 4, 10, 6, 5, 2, 8]
    
    # Colori basati sulla decisione
    decisions = ['On-Premise', 'Hybrid', 'Hybrid', 'SaaS', 'Cloud', 
                'Cloud', 'Hybrid', 'On-Premise', 'Edge', 'Cloud']
    
    color_map = {
        'On-Premise': colors['danger'],
        'Cloud': colors['success'],
        'Hybrid': colors['accent'],
        'Edge': colors['info'],
        'SaaS': colors['secondary']
    }
    
    colors_list = [color_map[d] for d in decisions]
    
    # Creare scatter plot
    scatter = ax.scatter(variability, criticality, s=500, c=colors_list, 
                        alpha=0.6, edgecolors='black', linewidth=2)
    
    # Aggiungere etichette
    for i, app in enumerate(applications):
        ax.annotate(app, (variability[i], criticality[i]), 
                   ha='center', va='center', fontsize=9, fontweight='bold')
    
    # Quadranti
    ax.axvline(x=5, color='gray', linestyle='--', alpha=0.5)
    ax.axhline(y=5, color='gray', linestyle='--', alpha=0.5)
    
    # Etichette quadranti
    ax.text(2.5, 9, 'CRITICO\nSTABILE', ha='center', va='center', 
            fontsize=11, alpha=0.5, fontweight='bold', 
            bbox=dict(boxstyle="round,pad=0.3", facecolor='red', alpha=0.1))
    ax.text(7.5, 9, 'CRITICO\nVARIABILE', ha='center', va='center', 
            fontsize=11, alpha=0.5, fontweight='bold',
            bbox=dict(boxstyle="round,pad=0.3", facecolor='orange', alpha=0.1))
    ax.text(2.5, 1, 'NON CRITICO\nSTABILE', ha='center', va='center', 
            fontsize=11, alpha=0.5, fontweight='bold',
            bbox=dict(boxstyle="round,pad=0.3", facecolor='lightblue', alpha=0.1))
    ax.text(7.5, 1, 'NON CRITICO\nVARIABILE', ha='center', va='center', 
            fontsize=11, alpha=0.5, fontweight='bold',
            bbox=dict(boxstyle="round,pad=0.3", facecolor='lightgreen', alpha=0.1))
    
    # Configurazione assi
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 11)
    ax.set_xlabel('Variabilità del Carico →', fontsize=12, fontweight='bold')
    ax.set_ylabel('← Criticità del Dato', fontsize=12, fontweight='bold')
    ax.set_title('Matrice Decisionale per Deployment Applicazioni', 
                fontsize=14, fontweight='bold', pad=20)
    
    # Legenda
    legend_elements = [plt.scatter([], [], s=200, c=color, alpha=0.6, 
                                  edgecolors='black', linewidth=2, label=decision)
                      for decision, color in color_map.items()]
    ax.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(1.02, 1), 
             title='Decisione\nDeployment', title_fontsize=10, fontsize=10)
    
    # Grid
    ax.grid(True, alpha=0.2)
    
    # Note
    ax.text(5.5, -1, 'Dimensione bolla = Costo annuale relativo', 
           ha='center', fontsize=9, style='italic')
    
    plt.tight_layout()
    return fig

def save_all_figures():
    """
    Genera e salva tutte le figure
    """
    print("Generazione figure per il Capitolo 3...")
    
    # Figura 1: Architettura alimentazione
    fig1 = create_power_architecture_2n()
    fig1.savefig('fig_3_1_power_architecture.pdf', dpi=300, bbox_inches='tight')
    fig1.savefig('fig_3_1_power_architecture.png', dpi=300, bbox_inches='tight')
    print("✓ Figura 1: Architettura alimentazione 2N")
    
    # Figura 2: Orchestrazione Multi-Cloud
    fig2 = create_multicloud_orchestration()
    fig2.savefig('fig_3_2_multicloud.pdf', dpi=300, bbox_inches='tight')
    fig2.savefig('fig_3_2_multicloud.png', dpi=300, bbox_inches='tight')
    print("✓ Figura 2: Orchestrazione Multi-Cloud")
    
    # Figura 3: Framework GIST
    fig3 = create_gist_framework()
    fig3.savefig('fig_3_3_gist_framework.pdf', dpi=300, bbox_inches='tight')
    fig3.savefig('fig_3_3_gist_framework.png', dpi=300, bbox_inches='tight')
    print("✓ Figura 3: Framework GIST")
    
    # Figura 4: Confronto Manutenzione
    fig4 = create_maintenance_comparison()
    fig4.savefig('fig_3_4_maintenance.pdf', dpi=300, bbox_inches='tight')
    fig4.savefig('fig_3_4_maintenance.png', dpi=300, bbox_inches='tight')
    print("✓ Figura 4: Confronto Manutenzione Predittiva")
    
    # Figura 5: Metriche Sicurezza
    fig5 = create_security_metrics()
    fig5.savefig('fig_3_5_security_metrics.pdf', dpi=300, bbox_inches='tight')
    fig5.savefig('fig_3_5_security_metrics.png', dpi=300, bbox_inches='tight')
    print("✓ Figura 5: Metriche Sicurezza Zero Trust")
    
    # Figura 6: Matrice Cloud
    fig6 = create_cloud_migration_matrix()
    fig6.savefig('fig_3_6_cloud_matrix.pdf', dpi=300, bbox_inches='tight')
    fig6.savefig('fig_3_6_cloud_matrix.png', dpi=300, bbox_inches='tight')
    print("✓ Figura 6: Matrice Decisionale Cloud")
    
    print("\n✓ Tutte le figure sono state generate con successo!")
    print("  Formati disponibili: PDF (per LaTeX) e PNG (per visualizzazione)")
    
    # Chiudere tutte le figure per liberare memoria
    plt.close('all')

if __name__ == "__main__":
    save_all_figures()
