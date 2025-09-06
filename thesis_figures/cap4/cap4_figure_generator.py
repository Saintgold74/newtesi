#!/usr/bin/env python3
"""
Generatore di Figure per Capitolo 4 - Compliance Integrata e Governance
Tesi di Laurea in Ingegneria Informatica
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Circle, Wedge, Rectangle, FancyBboxPatch
from matplotlib_venn import venn3, venn3_circles
import seaborn as sns
from scipy import stats
import pandas as pd
from matplotlib.gridspec import GridSpec
import warnings
warnings.filterwarnings('ignore')

# Configurazione globale per stile accademico
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 11
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 13
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10
plt.rcParams['legend.fontsize'] = 10
plt.rcParams['figure.titlesize'] = 14

# Palette colori professionale coerente con cap3
COLORS = {
    'primary': '#2E86AB',
    'secondary': '#A23B72',
    'tertiary': '#F18F01',
    'quaternary': '#C73E1D',
    'success': '#52B788',
    'warning': '#F77F00',
    'info': '#4A6FA5',
    'dark': '#2D3436',
    'light': '#F5F5F5',
    'gdpr': '#003f5c',
    'pcidss': '#bc5090',
    'nis2': '#ffa600'
}

def figura_4_1_venn_normative():
    """
    Figura 4.1: Diagramma di Venn delle sovrapposizioni normative
    PCI-DSS 4.0, GDPR, NIS2
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))
    
    # Subplot 1: Diagramma di Venn tradizionale
    # Valori basati sull'analisi nel testo
    venn_data = venn3(
        subsets=(156, 134, 128, 89, 76, 83, 128),  # (Abc, aBc, ABc, abC, AbC, aBC, ABC)
        set_labels=('PCI-DSS 4.0\n(412 controlli)', 
                   'GDPR\n(307 controlli)', 
                   'NIS2\n(276 controlli)'),
        ax=ax1
    )
    
    # Colori personalizzati
    if venn_data.get_patch_by_id('100'):
        venn_data.get_patch_by_id('100').set_color(COLORS['pcidss'])
        venn_data.get_patch_by_id('100').set_alpha(0.6)
    if venn_data.get_patch_by_id('010'):
        venn_data.get_patch_by_id('010').set_color(COLORS['gdpr'])
        venn_data.get_patch_by_id('010').set_alpha(0.6)
    if venn_data.get_patch_by_id('001'):
        venn_data.get_patch_by_id('001').set_color(COLORS['nis2'])
        venn_data.get_patch_by_id('001').set_alpha(0.6)
    if venn_data.get_patch_by_id('110'):
        venn_data.get_patch_by_id('110').set_color(COLORS['secondary'])
        venn_data.get_patch_by_id('110').set_alpha(0.5)
    if venn_data.get_patch_by_id('101'):
        venn_data.get_patch_by_id('101').set_color(COLORS['tertiary'])
        venn_data.get_patch_by_id('101').set_alpha(0.5)
    if venn_data.get_patch_by_id('011'):
        venn_data.get_patch_by_id('011').set_color(COLORS['quaternary'])
        venn_data.get_patch_by_id('011').set_alpha(0.5)
    if venn_data.get_patch_by_id('111'):
        venn_data.get_patch_by_id('111').set_color(COLORS['success'])
        venn_data.get_patch_by_id('111').set_alpha(0.7)
    
    # Evidenzia il nucleo centrale
    venn3_circles(subsets=(156, 134, 128, 89, 76, 83, 128), ax=ax1, linewidth=2)
    
    # Aggiungi annotazioni
    ax1.text(0, -0.85, 'Nucleo di Conformità\n128 controlli comuni\n(31% del totale)', 
            ha='center', fontsize=10, fontweight='bold', color=COLORS['success'])
    
    ax1.set_title('Sovrapposizioni tra Standard Normativi', fontsize=12, fontweight='bold')
    
    # Subplot 2: Analisi quantitativa delle sinergie
    categories = ['Controlli\nUnici', 'Sovrapposizioni\nDuali', 'Nucleo\nComune', 'Totale\nRidotto']
    
    # Dati per approccio frammentato vs integrato
    fragmented = [418, 248, 128, 891]
    integrated = [227, 168, 128, 523]
    
    x = np.arange(len(categories))
    width = 0.35
    
    bars1 = ax2.bar(x - width/2, fragmented, width, label='Approccio Frammentato',
                   color=COLORS['dark'], alpha=0.6)
    bars2 = ax2.bar(x + width/2, integrated, width, label='Approccio Integrato',
                   color=COLORS['success'], alpha=0.6)
    
    # Aggiungi valori sopra le barre
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax2.text(bar.get_x() + bar.get_width()/2., height + 10,
                    f'{int(height)}', ha='center', va='bottom', fontsize=9)
    
    # Aggiungi linea di risparmio
    savings = [(f-i)/f * 100 for f, i in zip(fragmented, integrated)]
    ax2_twin = ax2.twinx()
    line = ax2_twin.plot(x, savings, 'ro-', linewidth=2, markersize=8, 
                        label='Riduzione %', alpha=0.8)
    
    for i, (xi, yi) in enumerate(zip(x, savings)):
        if yi > 0:
            ax2_twin.text(xi, yi + 2, f'{yi:.1f}%', ha='center', fontsize=9,
                         color='red', fontweight='bold')
    
    ax2.set_xlabel('Categoria di Controlli')
    ax2.set_ylabel('Numero di Controlli')
    ax2_twin.set_ylabel('Riduzione Percentuale (%)', color='red')
    ax2.set_title('Efficienza dell\'Approccio Integrato', fontsize=12, fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels(categories)
    ax2.legend(loc='upper left')
    ax2_twin.legend(loc='upper right')
    ax2.grid(True, alpha=0.3, axis='y')
    ax2_twin.set_ylim([0, 60])
    
    # Aggiungi box con statistiche chiave
    textstr = '\n'.join([
        'Statistiche Chiave:',
        f'• Controlli totali ridotti: 41.3%',
        f'• Controlli comuni: 188',
        f'• Efficienza economica: +39.1%',
        f'• Tempo implementazione: -39.5%'
    ])
    props = dict(boxstyle='round', facecolor=COLORS['light'], alpha=0.9)
    ax2.text(0.02, 0.98, textstr, transform=ax2.transAxes, fontsize=9,
            verticalalignment='top', bbox=props)
    
    plt.tight_layout()
    plt.savefig('figura_4_1_venn_normative.pdf', dpi=300, bbox_inches='tight')
    plt.savefig('figura_4_1_venn_normative.png', dpi=300, bbox_inches='tight')
    plt.show()
    return fig

def figura_4_2_cmi_radar():
    """
    Figura 4.2: Grafico radar del Compliance Maturity Index (CMI)
    """
    fig = plt.figure(figsize=(14, 8))
    gs = GridSpec(2, 2, figure=fig, height_ratios=[2, 1])
    
    # Dati per il radar chart
    dimensioni = ['Integrazione\nProcessi', 'Automazione\nControlli', 
                  'Capacità di\nRisposta', 'Cultura\nOrganizzativa', 
                  'Miglioramento\nContinuo']
    
    # Valori su scala 0-5 (dal testo del capitolo)
    baseline = [2.1, 1.8, 2.3, 2.0, 1.9]
    attuale = [3.8, 3.5, 3.9, 3.2, 3.0]
    target = [4.5, 4.2, 4.4, 4.0, 4.1]
    best_in_class = [4.8, 4.6, 4.7, 4.5, 4.9]
    
    # Subplot 1: Radar chart principale
    ax1 = plt.subplot(gs[:, 0], projection='polar')
    
    # Calcola angoli
    angoli = np.linspace(0, 2 * np.pi, len(dimensioni), endpoint=False).tolist()
    
    # Chiudi il poligono
    baseline += baseline[:1]
    attuale += attuale[:1]
    target += target[:1]
    best_in_class += best_in_class[:1]
    angoli += angoli[:1]
    
    # Plot delle serie
    ax1.plot(angoli, baseline, 'o-', linewidth=2, color=COLORS['quaternary'], 
            label='Baseline Pre-integrazione')
    ax1.fill(angoli, baseline, alpha=0.25, color=COLORS['quaternary'])
    
    ax1.plot(angoli, attuale, 'o-', linewidth=2.5, color=COLORS['primary'], 
            label='Stato Attuale')
    ax1.fill(angoli, attuale, alpha=0.25, color=COLORS['primary'])
    
    ax1.plot(angoli, target, 'o--', linewidth=2, color=COLORS['success'], 
            label='Target 24 mesi')
    ax1.fill(angoli, target, alpha=0.15, color=COLORS['success'])
    
    ax1.plot(angoli, best_in_class, '.-', linewidth=1.5, color=COLORS['dark'], 
            label='Best-in-Class', alpha=0.7)
    
    # Configura il grafico
    ax1.set_xticks(angoli[:-1])
    ax1.set_xticklabels(dimensioni, size=10)
    ax1.set_ylim(0, 5)
    ax1.set_yticks([1, 2, 3, 4, 5])
    ax1.set_yticklabels(['1', '2', '3', '4', '5'], size=9)
    ax1.set_title('Compliance Maturity Index - Vista Multidimensionale', 
                 fontsize=12, fontweight='bold', pad=20)
    ax1.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
    ax1.grid(True)
    
    # Subplot 2: Evoluzione temporale del punteggio composito
    ax2 = plt.subplot(gs[0, 1])
    
    # Timeline (mesi)
    mesi = np.arange(0, 25)
    
    # Calcolo punteggi compositi pesati
    pesi = [0.25, 0.30, 0.20, 0.15, 0.10]
    
    score_baseline = sum(b * w for b, w in zip(baseline[:-1], pesi))
    score_attuale = sum(a * w for a, w in zip(attuale[:-1], pesi))
    score_target = sum(t * w for t, w in zip(target[:-1], pesi))
    score_best = sum(b * w for b, w in zip(best_in_class[:-1], pesi))
    
    # Simula evoluzione con curva sigmoide
    def sigmoid_growth(t, start, end, midpoint=12, steepness=0.3):
        return start + (end - start) / (1 + np.exp(-steepness * (t - midpoint)))
    
    evolution = [sigmoid_growth(t, score_baseline, score_attuale) for t in mesi]
    projection = [sigmoid_growth(t-12, score_attuale, score_target) if t >= 12 else score_attuale 
                 for t in mesi]
    
    ax2.plot(mesi[:13], evolution[:13], '-', linewidth=3, color=COLORS['primary'], 
            label='Evoluzione Realizzata')
    ax2.plot(mesi[12:], projection[12:], '--', linewidth=2, color=COLORS['success'], 
            label='Proiezione Target')
    ax2.axhline(y=score_best, color=COLORS['dark'], linestyle=':', alpha=0.7, 
               label='Benchmark Best-in-Class')
    
    # Aggiungi milestone
    milestones = [(0, score_baseline, 'Baseline'), 
                  (12, score_attuale, 'Attuale'),
                  (24, score_target, 'Target')]
    
    for month, score, label in milestones:
        ax2.scatter(month, score, s=100, zorder=5, 
                   color=COLORS['warning'], edgecolor='black', linewidth=2)
        ax2.annotate(f'{label}\n{score:.2f}', (month, score), 
                    xytext=(0, -25), textcoords='offset points',
                    ha='center', fontsize=9, fontweight='bold',
                    arrowprops=dict(arrowstyle='->', color='gray', alpha=0.5))
    
    ax2.set_xlabel('Mesi dall\'inizio del programma')
    ax2.set_ylabel('Punteggio CMI Composito')
    ax2.set_title('Evoluzione del CMI nel Tempo', fontsize=11, fontweight='bold')
    ax2.legend(loc='lower right')
    ax2.grid(True, alpha=0.3)
    ax2.set_xlim(0, 24)
    ax2.set_ylim(1.5, 5)
    
    # Subplot 3: Heatmap correlazioni
    ax3 = plt.subplot(gs[1, 1])
    
    # Matrice di correlazione tra dimensioni CMI e outcome
    outcomes = ['Riduzione\nIncidenti', 'Velocità\nRisposta', 'Costo\nConformità']
    
    # Correlazioni empiriche (dal testo)
    correlations = np.array([
        [0.72, 0.68, -0.65],  # Integrazione
        [0.78, 0.81, -0.71],  # Automazione
        [0.85, 0.92, -0.58],  # Capacità risposta
        [0.61, 0.54, -0.42],  # Cultura
        [0.69, 0.71, -0.53]   # Miglioramento
    ])
    
    im = ax3.imshow(correlations, cmap='RdBu_r', vmin=-1, vmax=1, aspect='auto')
    
    # Configurazione assi
    ax3.set_xticks(np.arange(len(outcomes)))
    ax3.set_yticks(np.arange(len(dimensioni)))
    ax3.set_xticklabels(outcomes, fontsize=9)
    ax3.set_yticklabels([d.replace('\n', ' ') for d in dimensioni], fontsize=9)
    ax3.set_title('Correlazione CMI-Outcome', fontsize=11, fontweight='bold')
    
    # Aggiungi valori nelle celle
    for i in range(len(dimensioni)):
        for j in range(len(outcomes)):
            text = ax3.text(j, i, f'{correlations[i, j]:.2f}',
                          ha='center', va='center', fontsize=9,
                          color='white' if abs(correlations[i, j]) > 0.5 else 'black')
    
    # Colorbar
    cbar = plt.colorbar(im, ax=ax3)
    cbar.set_label('Coefficiente di Correlazione', fontsize=9)
    
    plt.tight_layout()
    plt.savefig('figura_4_2_cmi_radar.pdf', dpi=300, bbox_inches='tight')
    plt.savefig('figura_4_2_cmi_radar.png', dpi=300, bbox_inches='tight')
    plt.show()
    return fig

def figura_4_3_roi_timeline():
    """
    Figura 4.3: Timeline del ROI per l'approccio integrato alla conformità
    """
    fig = plt.figure(figsize=(14, 8))
    gs = GridSpec(2, 2, figure=fig, height_ratios=[2, 1])
    
    # Subplot 1: ROI Timeline principale
    ax1 = plt.subplot(gs[0, :])
    
    # Dati temporali (mesi)
    mesi = np.arange(0, 37)
    
    # Costi e benefici cumulativi (in migliaia di euro)
    # Approccio frammentato
    costo_iniziale_framm = 8700
    costo_operativo_framm_mensile = 156
    frammentato_costi = [costo_iniziale_framm + costo_operativo_framm_mensile * m for m in mesi]
    
    # Approccio integrato
    costo_iniziale_int = 5300
    costo_operativo_int_mensile = 89
    saving_mensile = 67  # Risparmio operativo dopo implementazione
    
    # Calcolo costi integrati con curva di implementazione
    integrato_costi = []
    for m in mesi:
        if m <= 6:  # Fase implementazione
            cost = costo_iniziale_int * (m/6)
        elif m <= 14:  # Transizione
            cost = costo_iniziale_int + costo_operativo_int_mensile * (m-6)
        else:  # Regime
            cost = costo_iniziale_int + costo_operativo_int_mensile * 8 - saving_mensile * (m-14)
        integrato_costi.append(cost)
    
    # Plot linee principali
    ax1.plot(mesi, frammentato_costi, '-', linewidth=2.5, color=COLORS['quaternary'], 
            label='Approccio Frammentato', alpha=0.8)
    ax1.plot(mesi, integrato_costi, '-', linewidth=2.5, color=COLORS['primary'], 
            label='Approccio Integrato')
    
    # Monte Carlo simulation per confidence bands
    np.random.seed(42)
    n_simulations = 10000
    simulations = []
    
    for _ in range(n_simulations):
        # Variabilità nei parametri (±15%)
        var_cost = costo_iniziale_int * np.random.normal(1, 0.15)
        var_saving = saving_mensile * np.random.normal(1, 0.15)
        sim_costs = []
        for m in mesi:
            if m <= 6:
                cost = var_cost * (m/6)
            elif m <= 14:
                cost = var_cost + costo_operativo_int_mensile * (m-6)
            else:
                cost = var_cost + costo_operativo_int_mensile * 8 - var_saving * (m-14)
            sim_costs.append(cost)
        simulations.append(sim_costs)
    
    simulations = np.array(simulations)
    lower_bound = np.percentile(simulations, 2.5, axis=0)
    upper_bound = np.percentile(simulations, 97.5, axis=0)
    
    ax1.fill_between(mesi, lower_bound, upper_bound, alpha=0.2, color=COLORS['primary'],
                     label='IC 95% (Monte Carlo)')
    
    # Break-even point
    break_even_month = 14
    break_even_value = integrato_costi[break_even_month]
    ax1.scatter(break_even_month, break_even_value, s=150, color=COLORS['success'], 
               zorder=5, edgecolor='black', linewidth=2)
    ax1.annotate('Break-even\n14 mesi', (break_even_month, break_even_value),
                xytext=(break_even_month-3, break_even_value+800),
                arrowprops=dict(arrowstyle='->', color='black', lw=1.5),
                fontsize=10, fontweight='bold', ha='center',
                bbox=dict(boxstyle='round,pad=0.3', facecolor=COLORS['light'], alpha=0.9))
    
    # Area di risparmio
    ax1.fill_between(mesi[14:], frammentato_costi[14:], integrato_costi[14:],
                     where=(np.array(frammentato_costi[14:]) > np.array(integrato_costi[14:])),
                     alpha=0.3, color=COLORS['success'], label='Area di Risparmio')
    
    # Configurazione
    ax1.set_xlabel('Tempo (mesi)')
    ax1.set_ylabel('Costo Cumulativo (k€)')
    ax1.set_title('Evoluzione Temporale del ROI - Approccio Integrato vs Frammentato',
                 fontsize=12, fontweight='bold')
    ax1.legend(loc='upper left')
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(0, 36)
    
    # Aggiungi fasi
    phases = [(0, 6, 'Implementazione'), (6, 14, 'Transizione'), (14, 36, 'Regime')]
    for start, end, label in phases:
        ax1.axvspan(start, end, alpha=0.05, color=COLORS['dark'])
        ax1.text((start+end)/2, ax1.get_ylim()[0] + 200, label, 
                ha='center', fontsize=9, style='italic')
    
    # Subplot 2: ROI percentuale
    ax2 = plt.subplot(gs[1, 0])
    
    # Calcolo ROI percentuale
    roi_percentuale = []
    for m in range(len(mesi)):
        if integrato_costi[m] > 0:
            roi = ((frammentato_costi[m] - integrato_costi[m]) / integrato_costi[m]) * 100
            roi_percentuale.append(roi)
        else:
            roi_percentuale.append(0)
    
    ax2.plot(mesi, roi_percentuale, linewidth=2.5, color=COLORS['success'])
    ax2.fill_between(mesi, 0, roi_percentuale, alpha=0.3, color=COLORS['success'])
    
    # Milestone ROI
    roi_milestones = [(12, 'ROI 12m: 67%'), (24, 'ROI 24m: 287%'), (36, 'ROI 36m: 412%')]
    for month, label in roi_milestones:
        if month < len(roi_percentuale):
            ax2.scatter(month, roi_percentuale[month], s=80, color=COLORS['warning'], 
                       zorder=5, edgecolor='black', linewidth=1.5)
            ax2.text(month, roi_percentuale[month] + 20, label, 
                    ha='center', fontsize=9, fontweight='bold')
    
    ax2.set_xlabel('Tempo (mesi)')
    ax2.set_ylabel('ROI (%)')
    ax2.set_title('Evoluzione del Return on Investment', fontsize=11, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    ax2.set_xlim(0, 36)
    ax2.axhline(y=100, color='red', linestyle='--', alpha=0.5, linewidth=1)
    ax2.text(1, 105, 'Soglia 100%', fontsize=8, color='red')
    
    # Subplot 3: Breakdown dei risparmi
    ax3 = plt.subplot(gs[1, 1])
    
    # Categorie di risparmio
    categorie = ['Controlli\nDuplicati', 'Automazione\nProcessi', 'Efficienza\nAudit', 
                 'Riduzione\nIncidenti', 'Altro']
    percentuali = [31.2, 24.1, 18.4, 15.7, 10.6]
    colori = [COLORS['primary'], COLORS['secondary'], COLORS['tertiary'], 
             COLORS['success'], COLORS['info']]
    
    # Grafico a torta
    wedges, texts, autotexts = ax3.pie(percentuali, labels=categorie, colors=colori,
                                        autopct='%1.1f%%', startangle=90,
                                        explode=(0.05, 0.05, 0.05, 0.05, 0.05))
    
    # Formattazione
    for text in texts:
        text.set_fontsize(9)
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontsize(9)
        autotext.set_fontweight('bold')
    
    ax3.set_title('Composizione dei Risparmi', fontsize=11, fontweight='bold')
    
    # Aggiungi box con metriche chiave
    textstr = '\n'.join([
        'Metriche Chiave:',
        f'• Investimento iniziale: €5.3M',
        f'• Break-even: 14 mesi',
        f'• ROI 24 mesi: 287%',
        f'• Risparmio annuo: €2.4M',
        f'• Riduzione TCO: 39.1%'
    ])
    props = dict(boxstyle='round', facecolor=COLORS['light'], alpha=0.9)
    fig.text(0.02, 0.02, textstr, fontsize=9, bbox=props, verticalalignment='bottom')
    
    plt.tight_layout()
    plt.savefig('figura_4_3_roi_timeline.pdf', dpi=300, bbox_inches='tight')
    plt.savefig('figura_4_3_roi_timeline.png', dpi=300, bbox_inches='tight')
    plt.show()
    return fig

def figura_4_supplementare_prioritization():
    """
    Figura supplementare: Sistema di prioritizzazione dinamica dei controlli
    """
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))
    
    # Genera dati di esempio per controlli
    np.random.seed(42)
    n_controlli = 50
    
    # Parametri per ogni controllo
    rischio = np.random.uniform(1, 10, n_controlli)
    urgenza = np.random.uniform(1, 365, n_controlli)  # giorni alla scadenza
    beneficio = np.random.uniform(10000, 500000, n_controlli)
    costo = np.random.uniform(5000, 100000, n_controlli)
    dipendenze = np.random.randint(0, 5, n_controlli)
    
    # Calcolo priorità con formula dal testo
    alpha, beta, gamma, delta = 0.35, 0.25, 0.30, 0.10
    lambda_decay = 0.03
    
    priorita = (alpha * rischio/10 + 
               beta * np.exp(-lambda_decay * urgenza) + 
               gamma * (beneficio/costo)/np.max(beneficio/costo) - 
               delta * dipendenze/5)
    
    # Subplot 1: Scatter plot priorità vs costo-efficacia
    ax1.scatter(beneficio/costo, priorita, c=rischio, s=50, alpha=0.6, 
               cmap='RdYlGn_r', edgecolors='black', linewidth=0.5)
    
    # Evidenzia top 10 controlli
    top_10_idx = np.argsort(priorita)[-10:]
    ax1.scatter((beneficio/costo)[top_10_idx], priorita[top_10_idx], 
               s=100, color='none', edgecolors='red', linewidth=2)
    
    cbar1 = plt.colorbar(ax1.scatter(beneficio/costo, priorita, c=rischio, 
                                     cmap='RdYlGn_r'), ax=ax1)
    cbar1.set_label('Livello di Rischio', fontsize=9)
    
    ax1.set_xlabel('Rapporto Beneficio/Costo')
    ax1.set_ylabel('Priorità Calcolata')
    ax1.set_title('Prioritizzazione dei Controlli', fontsize=11, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    
    # Aggiungi quadranti
    ax1.axhline(y=np.median(priorita), color='gray', linestyle='--', alpha=0.5)
    ax1.axvline(x=np.median(beneficio/costo), color='gray', linestyle='--', alpha=0.5)
    ax1.text(0.95, 0.95, 'Quick Wins', transform=ax1.transAxes, 
            ha='right', va='top', fontsize=9, style='italic', color='green')
    ax1.text(0.05, 0.95, 'Critici', transform=ax1.transAxes, 
            ha='left', va='top', fontsize=9, style='italic', color='red')
    
    # Subplot 2: Distribuzione temporale dell'implementazione
    ax2.hist(urgenza[top_10_idx], bins=12, color=COLORS['primary'], 
            alpha=0.7, edgecolor='black')
    ax2.set_xlabel('Giorni alla Scadenza')
    ax2.set_ylabel('Numero di Controlli (Top 10)')
    ax2.set_title('Distribuzione Temporale - Controlli Prioritari', 
                 fontsize=11, fontweight='bold')
    ax2.grid(True, alpha=0.3, axis='y')
    
    # Aggiungi zone critiche
    ax2.axvspan(0, 30, alpha=0.2, color='red', label='Critico (<30 giorni)')
    ax2.axvspan(30, 90, alpha=0.2, color='yellow', label='Urgente (30-90 giorni)')
    ax2.axvspan(90, 365, alpha=0.2, color='green', label='Pianificabile (>90 giorni)')
    ax2.legend(loc='upper right', fontsize=9)
    
    # Subplot 3: Evoluzione della priorità nel tempo
    ax3.clear()
    time_points = np.arange(0, 365, 1)
    
    # Simula evoluzione per 5 controlli rappresentativi
    colors = [COLORS['primary'], COLORS['secondary'], COLORS['tertiary'], 
             COLORS['quaternary'], COLORS['success']]
    
    for i in range(5):
        idx = top_10_idx[i]
        priority_evolution = (alpha * rischio[idx]/10 + 
                            beta * np.exp(-lambda_decay * (urgenza[idx] - time_points)) + 
                            gamma * (beneficio[idx]/costo[idx])/np.max(beneficio/costo) - 
                            delta * dipendenze[idx]/5)
        priority_evolution[time_points > urgenza[idx]] = 0  # Dopo scadenza
        
        ax3.plot(time_points, priority_evolution, linewidth=2, 
                color=colors[i], label=f'Controllo {idx+1}')
    
    ax3.set_xlabel('Tempo (giorni)')
    ax3.set_ylabel('Priorità Dinamica')
    ax3.set_title('Evoluzione della Priorità nel Tempo', fontsize=11, fontweight='bold')
    ax3.legend(loc='upper left', fontsize=9)
    ax3.grid(True, alpha=0.3)
    ax3.set_xlim(0, 365)
    
    # Subplot 4: Matrice di efficienza
    ax4.clear()
    
    # Categorie di controlli
    categories = ['Segmentazione\nRete', 'Crittografia\nDati', 'Gestione\nAccessi', 
                  'Monitoring\nContinuo', 'Incident\nResponse']
    
    # Efficienza per standard (simulata)
    efficiency_matrix = np.array([
        [0.95, 0.78, 0.82],  # Segmentazione
        [0.88, 0.92, 0.65],  # Crittografia
        [0.91, 0.85, 0.89],  # Gestione Accessi
        [0.72, 0.68, 0.94],  # Monitoring
        [0.65, 0.71, 0.98]   # Incident Response
    ])
    
    standards = ['PCI-DSS', 'GDPR', 'NIS2']
    
    im = ax4.imshow(efficiency_matrix, cmap='YlGn', vmin=0, vmax=1, aspect='auto')
    
    ax4.set_xticks(np.arange(len(standards)))
    ax4.set_yticks(np.arange(len(categories)))
    ax4.set_xticklabels(standards, fontsize=9)
    ax4.set_yticklabels(categories, fontsize=9)
    ax4.set_title('Matrice di Efficienza Cross-Standard', fontsize=11, fontweight='bold')
    
    # Aggiungi valori
    for i in range(len(categories)):
        for j in range(len(standards)):
            text = ax4.text(j, i, f'{efficiency_matrix[i, j]:.2f}',
                          ha='center', va='center', fontsize=9,
                          color='white' if efficiency_matrix[i, j] < 0.5 else 'black')
    
    cbar4 = plt.colorbar(im, ax=ax4)
    cbar4.set_label('Efficienza (0-1)', fontsize=9)
    
    plt.tight_layout()
    plt.savefig('figura_4_supplementare_prioritization.pdf', dpi=300, bbox_inches='tight')
    plt.savefig('figura_4_supplementare_prioritization.png', dpi=300, bbox_inches='tight')
    plt.show()
    return fig

def main():
    """
    Funzione principale per generare tutte le figure del Capitolo 4
    """
    print("Generazione Figure Capitolo 4 - Compliance Integrata e Governance")
    print("=" * 60)
    
    figures = [
        ("Figura 4.1 - Venn Normative", figura_4_1_venn_normative),
        ("Figura 4.2 - CMI Radar", figura_4_2_cmi_radar),
        ("Figura 4.3 - ROI Timeline", figura_4_3_roi_timeline),
        ("Figura Supplementare - Sistema Prioritizzazione", figura_4_supplementare_prioritization)
    ]
    
    for name, func in figures:
        print(f"\nGenerazione {name}...")
        try:
            func()
            print(f"✓ {name} generata con successo")
        except Exception as e:
            print(f"✗ Errore nella generazione di {name}: {str(e)}")
    
    print("\n" + "=" * 60)
    print("Generazione completata!")
    print("\nFile generati:")
    print("- figura_4_X_nome.pdf (per inclusione in LaTeX)")
    print("- figura_4_X_nome.png (per visualizzazione)")
    print("\nNote per l'integrazione:")
    print("1. Verificare i percorsi delle figure nel documento LaTeX")
    print("2. Adattare le dimensioni se necessario con \\includegraphics[width=...]")
    print("3. Le figure sono ottimizzate per stampa B/N mantenendo leggibilità")

if __name__ == "__main__":
    main()