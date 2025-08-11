#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generazione Figure per Capitolo 4 - Compliance Integrata e Governance
Tesi di Laurea in Ingegneria Informatica
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib_venn import venn3, venn3_circles
import numpy as np
import seaborn as sns
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle, FancyArrow
import matplotlib.patches as mpatches

# Configurazione generale per pubblicazione accademica
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman', 'DejaVu Serif']
plt.rcParams['font.size'] = 11
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 13
plt.rcParams['legend.fontsize'] = 10
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['savefig.bbox'] = 'tight'
plt.rcParams['savefig.pad_inches'] = 0.1

# Colori professionali per la tesi
colors = {
    'pci': '#1E3A8A',      # Blu scuro
    'gdpr': '#DC2626',     # Rosso
    'nis2': '#059669',     # Verde
    'overlap': '#F59E0B',  # Arancione
    'gist1': '#6366F1',    # Indaco
    'gist2': '#8B5CF6',    # Viola
    'gist3': '#EC4899',    # Rosa
    'gist4': '#10B981',    # Verde smeraldo
    'neutral': '#6B7280'   # Grigio
}

# ====================
# FIGURA 4.1: Diagramma di Venn - Sovrapposizioni Normative
# ====================

def create_venn_diagram():
    """
    Crea il diagramma di Venn per le sovrapposizioni tra PCI-DSS, GDPR e NIS2
    """
    fig, ax = plt.subplots(1, 1, figsize=(10, 8))
    
    # Dati delle sovrapposizioni (basati sui dati della tesi)
    # Set sizes: PCI-DSS, GDPR, NIS2
    # Intersections: PCI∩GDPR, PCI∩NIS2, GDPR∩NIS2, PCI∩GDPR∩NIS2
    v = venn3(subsets=(264, 173, 112, 82, 47, 31, 28), 
              set_labels=('PCI-DSS 4.0\n264 requisiti', 
                         'GDPR\n173 requisiti', 
                         'NIS2\n112 requisiti'),
              ax=ax,
              set_colors=(colors['pci'], colors['gdpr'], colors['nis2']),
              alpha=0.6)
    
    # Personalizzazione del diagramma
    venn3_circles(subsets=(264, 173, 112, 82, 47, 31, 28), 
                  linewidth=2, 
                  linestyle='solid',
                  ax=ax)
    
    # Etichette per le intersezioni con percentuali
    if v.get_label_by_id('100'):
        v.get_label_by_id('100').set_text('154\n(58%)')
    if v.get_label_by_id('010'):
        v.get_label_by_id('010').set_text('60\n(35%)')
    if v.get_label_by_id('001'):
        v.get_label_by_id('001').set_text('34\n(30%)')
    if v.get_label_by_id('110'):
        v.get_label_by_id('110').set_text('82\n(31%)')
    if v.get_label_by_id('101'):
        v.get_label_by_id('101').set_text('47\n(18%)')
    if v.get_label_by_id('011'):
        v.get_label_by_id('011').set_text('31\n(18%)')
    if v.get_label_by_id('111'):
        v.get_label_by_id('111').set_text('28\n(11%)')
    
    # Titolo e annotazioni
    ax.set_title('Sovrapposizioni tra Requisiti Normativi nel Settore GDO', 
                 fontsize=14, fontweight='bold', pad=20)
    
    # Box informativi
    info_text = "Controlli comuni identificati: 188 (31% del totale)\n" \
                "Potenziale riduzione effort: 39.1%\n" \
                "Tempo risparmiato per audit: 52.3%"
    
    ax.text(0.02, 0.98, info_text,
            transform=ax.transAxes,
            fontsize=10,
            verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))
    
    # Legenda per le percentuali
    legend_elements = [
        mpatches.Patch(color=colors['overlap'], alpha=0.6, 
                      label='Area di sovrapposizione = Opportunità di integrazione'),
        mpatches.Patch(color='none', label='Numeri: Requisiti unici'),
        mpatches.Patch(color='none', label='Percentuali: Overlap sul totale dello standard')
    ]
    ax.legend(handles=legend_elements, loc='lower right', frameon=True, fancybox=True)
    
    plt.tight_layout()
    plt.savefig('figura_4_1_venn_normative.pdf', format='pdf', bbox_inches='tight')
    plt.savefig('figura_4_1_venn_normative.png', format='png', bbox_inches='tight')
    plt.show()
    
    return fig

# ====================
# FIGURA 4.2: Compliance Maturity Index - Grafico Radar
# ====================

def create_cmi_radar():
    """
    Crea il grafico radar per il Compliance Maturity Index
    """
    # Dimensioni del CMI
    categories = ['Process\nMaturity', 'Technical\nControls', 'Governance\nEffectiveness', 
                  'Operational\nEfficiency', 'Continuous\nImprovement']
    N = len(categories)
    
    # Dati per tre profili: Baseline, Current, Target
    baseline = [2.1, 2.4, 1.9, 2.2, 1.8]
    current = [3.4, 3.8, 3.2, 3.5, 3.1]
    target = [4.5, 4.7, 4.3, 4.6, 4.4]
    
    # Angoli per il radar
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    baseline += baseline[:1]
    current += current[:1]
    target += target[:1]
    angles += angles[:1]
    
    # Creazione del grafico
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7), 
                                    subplot_kw=dict(projection='polar'))
    
    # Grafico 1: Evoluzione della maturità
    ax1.set_theta_offset(np.pi / 2)
    ax1.set_theta_direction(-1)
    
    # Griglia e etichette
    ax1.set_xticks(angles[:-1])
    ax1.set_xticklabels(categories)
    ax1.set_ylim(0, 5)
    ax1.set_yticks([1, 2, 3, 4, 5])
    ax1.set_yticklabels(['1\nAd-hoc', '2\nManaged', '3\nDefined', '4\nQuantified', '5\nOptimized'], 
                        fontsize=8)
    ax1.grid(True, alpha=0.3)
    
    # Plot delle tre curve
    ax1.plot(angles, baseline, 'o-', linewidth=2, label='Baseline (Pre-integrazione)', 
             color=colors['neutral'])
    ax1.fill(angles, baseline, alpha=0.15, color=colors['neutral'])
    
    ax1.plot(angles, current, 'o-', linewidth=2, label='Stato Attuale', 
             color=colors['gist2'])
    ax1.fill(angles, current, alpha=0.20, color=colors['gist2'])
    
    ax1.plot(angles, target, 'o--', linewidth=2, label='Target (24 mesi)', 
             color=colors['gist1'])
    ax1.fill(angles, target, alpha=0.10, color=colors['gist1'])
    
    ax1.set_title('Evoluzione del Compliance Maturity Index', 
                  fontsize=13, fontweight='bold', pad=30)
    ax1.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
    
    # Grafico 2: Distribuzione del settore
    ax2.set_theta_offset(np.pi / 2)
    ax2.set_theta_direction(-1)
    
    # Media del settore e top performer
    sector_avg = [2.8, 3.1, 2.7, 2.9, 2.5]
    top_performer = [4.2, 4.5, 4.1, 4.3, 4.0]
    sector_avg += sector_avg[:1]
    top_performer += top_performer[:1]
    
    ax2.set_xticks(angles[:-1])
    ax2.set_xticklabels(categories)
    ax2.set_ylim(0, 5)
    ax2.set_yticks([1, 2, 3, 4, 5])
    ax2.set_yticklabels(['1', '2', '3', '4', '5'], fontsize=8)
    ax2.grid(True, alpha=0.3)
    
    ax2.plot(angles, sector_avg, 'o-', linewidth=2, label='Media Settore GDO', 
             color=colors['nis2'])
    ax2.fill(angles, sector_avg, alpha=0.20, color=colors['nis2'])
    
    ax2.plot(angles, top_performer, 'o-', linewidth=2, label='Top 10% Performer', 
             color=colors['pci'])
    ax2.fill(angles, top_performer, alpha=0.15, color=colors['pci'])
    
    ax2.plot(angles, current, 'o--', linewidth=2, label='RetailCo (Case Study)', 
             color=colors['gdpr'])
    
    ax2.set_title('Benchmark di Settore', fontsize=13, fontweight='bold', pad=30)
    ax2.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
    
    # Aggiunta di metriche chiave
    fig.text(0.5, 0.02, 
             'CMI Score: Baseline=2.1 | Attuale=3.4 (+62%) | Target=4.5 | ROI Atteso: 287% @ 24 mesi',
             ha='center', fontsize=10, style='italic',
             bbox=dict(boxstyle='round', facecolor='lightgray', alpha=0.3))
    
    plt.tight_layout()
    plt.savefig('figura_4_2_cmi_radar.pdf', format='pdf', bbox_inches='tight')
    plt.savefig('figura_4_2_cmi_radar.png', format='png', bbox_inches='tight')
    plt.show()
    
    return fig

# ====================
# FIGURA 4.3: Modello Integrato GIST - Framework Completo
# ====================

def create_gist_framework():
    """
    Crea il diagramma del framework GIST integrato
    """
    fig, ax = plt.subplots(1, 1, figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Titolo principale
    ax.text(7, 9.5, 'Framework GIST - GDO Integrated Security Transformation', 
            fontsize=16, fontweight='bold', ha='center')
    ax.text(7, 9, 'Modello Integrato per la Trasformazione Sicura della GDO', 
            fontsize=12, ha='center', style='italic')
    
    # I quattro pilastri principali
    pillar_positions = [(2, 6.5), (5, 6.5), (9, 6.5), (12, 6.5)]
    pillar_colors = [colors['gist1'], colors['gist2'], colors['gist3'], colors['gist4']]
    pillar_labels = ['Physical\nInfrastructure', 'Architectural\nMaturity', 
                     'Security\nPosture', 'Compliance\nIntegration']
    
    # Disegno dei pilastri
    for i, (x, y) in enumerate(pillar_positions):
        # Pilastro principale
        rect = FancyBboxPatch((x-1.2, y-2), 2.4, 2, 
                              boxstyle="round,pad=0.1",
                              facecolor=pillar_colors[i], 
                              edgecolor='black',
                              alpha=0.7,
                              linewidth=2)
        ax.add_patch(rect)
        
        # Etichetta del pilastro
        ax.text(x, y-1, pillar_labels[i], 
                fontsize=11, fontweight='bold', 
                ha='center', va='center', color='white')
        
        # Metriche chiave sotto ogni pilastro
        metrics = [
            ['• PUE < 1.4', '• Uptime 99.95%', '• CAPEX -30%'],
            ['• Cloud Native 60%', '• Microservices', '• API-first'],
            ['• Zero Trust', '• ASSA -42.7%', '• MTTR < 2h'],
            ['• Multi-standard', '• Automation 70%', '• Cost -39.1%']
        ]
        
        for j, metric in enumerate(metrics[i]):
            ax.text(x, y-2.5-j*0.3, metric, 
                   fontsize=9, ha='center', color='darkgray')
    
    # Layer di integrazione centrale
    integration_box = FancyBboxPatch((1, 3.5), 12, 1.2,
                                     boxstyle="round,pad=0.05",
                                     facecolor=colors['overlap'],
                                     alpha=0.3,
                                     linewidth=2,
                                     edgecolor='black',
                                     linestyle='--')
    ax.add_patch(integration_box)
    
    ax.text(7, 4.1, 'Integration Layer', fontsize=12, fontweight='bold', ha='center')
    ax.text(7, 3.7, 'Orchestration • Automation • Analytics • Continuous Monitoring', 
            fontsize=10, ha='center', style='italic')
    
    # Frecce di interconnessione
    arrow_pairs = [
        (pillar_positions[0], pillar_positions[1]),
        (pillar_positions[1], pillar_positions[2]),
        (pillar_positions[2], pillar_positions[3])
    ]
    
    for start, end in arrow_pairs:
        arrow = FancyArrow(start[0]+1, start[1]-1, 
                          end[0]-start[0]-2, 0,
                          width=0.1, head_width=0.2, head_length=0.1,
                          fc='gray', ec='gray', alpha=0.5)
        ax.add_patch(arrow)
    
    # Formula GIST
    formula_text = r'GIST = Σ(wi × Ci) × KGDO × (1+I)'
    ax.text(7, 2.5, formula_text, fontsize=12, 
            ha='center', style='italic',
            bbox=dict(boxstyle='round', facecolor='white', edgecolor='black'))
    
    ax.text(7, 2, 'dove: Ci ∈ {Physical, Architectural, Security, Compliance}', 
            fontsize=9, ha='center', color='gray')
    
    # Box dei risultati attesi
    results_box = FancyBboxPatch((2, 0.3), 10, 1.2,
                                 boxstyle="round,pad=0.05",
                                 facecolor='lightgreen',
                                 alpha=0.2,
                                 linewidth=1,
                                 edgecolor='green')
    ax.add_patch(results_box)
    
    ax.text(7, 1.2, 'Risultati Validati', fontsize=11, fontweight='bold', ha='center')
    ax.text(3.5, 0.7, '✓ TCO: -38.2%', fontsize=10, color='darkgreen')
    ax.text(6, 0.7, '✓ SLA: 99.96%', fontsize=10, color='darkgreen')
    ax.text(8.5, 0.7, '✓ ASSA: -42.7%', fontsize=10, color='darkgreen')
    ax.text(11, 0.7, '✓ Compliance: -39.1%', fontsize=10, color='darkgreen')
    
    # Timeline di implementazione
    ax.text(1, 8.2, 'Roadmap Implementativa:', fontsize=11, fontweight='bold')
    timeline_items = [
        ('Wave 1 (0-6m):', 'Quick Wins & Foundation'),
        ('Wave 2 (6-12m):', 'Core Transformation'),
        ('Wave 3 (12-18m):', 'Optimization & Scale')
    ]
    
    for i, (phase, desc) in enumerate(timeline_items):
        ax.text(1+i*4, 7.7, phase, fontsize=9, fontweight='bold')
        ax.text(1+i*4, 7.4, desc, fontsize=8, style='italic', color='gray')
    
    plt.tight_layout()
    plt.savefig('figura_4_3_gist_framework.pdf', format='pdf', bbox_inches='tight')
    plt.savefig('figura_4_3_gist_framework.png', format='png', bbox_inches='tight')
    plt.show()
    
    return fig

# ====================
# FIGURA SUPPLEMENTARE: Timeline ROI Compliance
# ====================

def create_roi_timeline():
    """
    Crea il grafico della timeline del ROI per la compliance integrata
    """
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)
    
    # Dati temporali
    months = np.arange(0, 25)
    
    # ROI cumulativo (curva logistica)
    L = 312  # Asintoto
    k = 0.074  # Growth rate  
    t0 = 11  # Inflection point
    roi_cumulative = L / (1 + np.exp(-k * (months - t0))) - 100
    
    # Assicuriamoci che il ROI inizi da valori realistici
    roi_cumulative[0] = -100  # Investimento iniziale al 100%
    
    # Costi e benefici mensili
    costs = np.zeros(25)
    costs[0:6] = [180, 150, 120, 90, 70, 60]  # Investimento iniziale decrescente
    costs[6:12] = [40, 35, 30, 30, 25, 25]    # Stabilizzazione
    costs[12:] = 20  # Costi operativi steady-state
    
    benefits = np.zeros(25)
    # Corretto: 22 valori per riempire dall'indice 3 alla fine (posizioni 3-24)
    benefits[3:] = [20, 40, 60, 80, 100, 120, 140, 150, 160, 
                   170, 175, 180, 185, 190, 195, 200, 205, 210, 215, 220, 225, 230]
    
    # Grafico 1: ROI Cumulativo
    ax1.plot(months, roi_cumulative, linewidth=3, color=colors['gist1'], label='ROI Cumulativo')
    ax1.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
    ax1.fill_between(months, 0, roi_cumulative, where=(roi_cumulative > 0), 
                     color='green', alpha=0.2, label='ROI Positivo')
    ax1.fill_between(months, roi_cumulative, 0, where=(roi_cumulative <= 0), 
                     color='red', alpha=0.2, label='Investimento')
    
    # Punti chiave
    positive_roi = np.where(roi_cumulative > 0)[0]
    if len(positive_roi) > 0:
        breakeven_month = positive_roi[0]
        ax1.plot(breakeven_month, 0, 'ro', markersize=10)
        ax1.annotate(f'Breakeven\n(Mese {breakeven_month})', 
                    xy=(breakeven_month, 0), xytext=(breakeven_month+2, 30),
                    arrowprops=dict(arrowstyle='->', color='red'),
                    fontsize=10, ha='left')
    
    ax1.set_ylabel('ROI (%)', fontsize=11)
    ax1.set_title('Evoluzione del ROI nella Compliance Integrata', fontsize=13, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    ax1.legend(loc='upper left')
    ax1.set_ylim(-120, 250)
    
    # Grafico 2: Costi vs Benefici Mensili
    width = 0.35
    x_pos = months - width/2
    
    bars1 = ax2.bar(x_pos, costs, width, label='Costi', color=colors['gdpr'], alpha=0.7)
    bars2 = ax2.bar(x_pos + width, benefits, width, label='Benefici', color=colors['nis2'], alpha=0.7)
    
    # Linea del saldo netto
    net = benefits - costs
    ax2.plot(months, net, 'k-', linewidth=2, label='Saldo Netto', marker='o', markersize=4)
    ax2.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
    
    # Annotazioni delle fasi
    phases = [
        (3, 'Investimento\nIniziale'),
        (9, 'Stabilizzazione'),
        (18, 'Ottimizzazione')
    ]
    
    for month, label in phases:
        ax2.annotate(label, xy=(month, 180), fontsize=9,
                    ha='center', va='bottom',
                    bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.3))
    
    ax2.set_xlabel('Mesi dall\'Implementazione', fontsize=11)
    ax2.set_ylabel('Valore (k€)', fontsize=11)
    ax2.set_title('Analisi Costi-Benefici Mensile', fontsize=13, fontweight='bold')
    ax2.grid(True, alpha=0.3, axis='y')
    ax2.legend(loc='upper left')
    ax2.set_xlim(-0.5, 24.5)
    
    plt.tight_layout()
    plt.savefig('figura_4_supplementare_roi_timeline.pdf', format='pdf', bbox_inches='tight')
    plt.savefig('figura_4_supplementare_roi_timeline.png', format='png', bbox_inches='tight')
    plt.show()
    
    return fig

# ====================
# TABELLA: Matrice di Integrazione Normativa
# ====================

def create_integration_matrix():
    """
    Crea la matrice di integrazione tra standard normativi
    """
    fig, ax = plt.subplots(1, 1, figsize=(14, 10))
    ax.axis('off')
    
    # Titolo
    ax.text(0.5, 0.95, 'Matrice di Integrazione Normativa PCI-DSS / GDPR / NIS2',
            fontsize=14, fontweight='bold', ha='center', transform=ax.transAxes)
    
    # Headers
    col_headers = ['Area di Controllo', 'PCI-DSS 4.0', 'GDPR', 'NIS2', 'Controllo Unificato', 'Saving']
    row_data = [
        ['Gestione Accessi', 'Req 7.1-7.3\n8.1-8.6', 'Art. 32\nArt. 5.1.f', 'Art. 21(2)(d)\nAnnex I.2', 
         'IAM + MFA + PAM', '43%'],
        ['Crittografia', 'Req 3.5-3.7\n4.2', 'Art. 32.1.a\nArt. 34', 'Art. 21(2)(g)', 
         'HSM + TLS 1.3', '38%'],
        ['Logging & Monitoring', 'Req 10.1-10.7', 'Art. 33\nArt. 32.1.d', 'Art. 21(3)\nAnnex I.3', 
         'SIEM Centralizzato', '52%'],
        ['Incident Response', 'Req 12.10', 'Art. 33-34', 'Art. 23\nArt. 21(4)', 
         'SOC 24/7', '47%'],
        ['Risk Assessment', 'Req 12.3-12.4', 'Art. 35\nArt. 32.2', 'Art. 21(1)', 
         'GRC Platform', '41%'],
        ['Business Continuity', 'Req 12.5', 'Art. 32.1.b-c', 'Art. 21(2)(c)\nAnnex I.4', 
         'DR Multi-site', '35%'],
        ['Vendor Management', 'Req 12.8', 'Art. 28\nArt. 32', 'Art. 21(2)(j)', 
         'TPRM System', '39%'],
        ['Training & Awareness', 'Req 12.6', 'Art. 39\nArt. 47', 'Art. 21(2)(g)', 
         'LMS Integrato', '31%']
    ]
    
    # Creazione della tabella
    table = ax.table(cellText=[['']+col_headers] + [[f'{i+1}']+row for i, row in enumerate(row_data)],
                    cellLoc='left',
                    loc='center',
                    colWidths=[0.05, 0.20, 0.15, 0.15, 0.15, 0.20, 0.10])
    
    table.auto_set_font_size(False)
    table.set_fontsize(9)
    table.scale(1, 2.5)
    
    # Styling delle celle
    for i in range(len(row_data) + 1):
        for j in range(len(col_headers) + 1):
            cell = table[(i, j)]
            if i == 0:  # Header row
                cell.set_facecolor('#E5E7EB')
                cell.set_text_props(weight='bold')
            elif j == 0:  # Index column
                cell.set_facecolor('#F3F4F6')
            elif j == len(col_headers):  # Saving column
                saving = row_data[i-1][j-1] if i > 0 else ''
                if saving and int(saving[:-1]) > 40:
                    cell.set_facecolor('#D1FAE5')
                elif saving and int(saving[:-1]) > 35:
                    cell.set_facecolor('#FEF3C7')
                else:
                    cell.set_facecolor('#FEE2E2')
            elif j == len(col_headers) - 1:  # Unified control column
                cell.set_facecolor('#DBEAFE')
    
    # Note in fondo
    note_text = ("Note: I saving percentuali rappresentano la riduzione dell'effort rispetto a implementazioni separate.\n"
                "Fonte: Analisi su 47 implementazioni GDO europee (2023-2024)")
    ax.text(0.5, 0.05, note_text, fontsize=9, ha='center', style='italic',
           transform=ax.transAxes, bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))
    
    plt.tight_layout()
    plt.savefig('tabella_4_1_matrice_integrazione.pdf', format='pdf', bbox_inches='tight')
    plt.savefig('tabella_4_1_matrice_integrazione.png', format='png', bbox_inches='tight')
    plt.show()
    
    return fig

# ====================
# ESECUZIONE PRINCIPALE
# ====================

if __name__ == "__main__":
    print("Generazione Figure per Capitolo 4 - Compliance Integrata e Governance")
    print("=" * 70)
    
    # Genera tutte le figure
    print("\n1. Generazione Figura 4.1: Diagramma di Venn...")
    fig1 = create_venn_diagram()
    print("   ✓ Figura 4.1 salvata come 'figura_4_1_venn_normative.pdf/png'")
    
    print("\n2. Generazione Figura 4.2: Compliance Maturity Index...")
    fig2 = create_cmi_radar()
    print("   ✓ Figura 4.2 salvata come 'figura_4_2_cmi_radar.pdf/png'")
    
    print("\n3. Generazione Figura 4.3: Framework GIST...")
    fig3 = create_gist_framework()
    print("   ✓ Figura 4.3 salvata come 'figura_4_3_gist_framework.pdf/png'")
    
    print("\n4. Generazione Figura Supplementare: ROI Timeline...")
    fig4 = create_roi_timeline()
    print("   ✓ Figura supplementare salvata come 'figura_4_supplementare_roi_timeline.pdf/png'")
    
    print("\n5. Generazione Tabella: Matrice di Integrazione...")
    fig5 = create_integration_matrix()
    print("   ✓ Tabella salvata come 'tabella_4_1_matrice_integrazione.pdf/png'")
    
    print("\n" + "=" * 70)
    print("Tutte le figure sono state generate con successo!")
    print("\nPer integrarle in LaTeX, utilizzare:")
    print("\\includegraphics[width=\\textwidth]{figura_4_1_venn_normative.pdf}")
    print("\nAssicurarsi che i file PDF siano nella stessa directory del documento LaTeX")
    print("o specificare il percorso completo.")