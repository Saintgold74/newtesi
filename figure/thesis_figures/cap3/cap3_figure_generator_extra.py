#!/usr/bin/env python3
"""
Generazione Figure per Capitolo 3 - Evoluzione Infrastrutturale
Tesi di Laurea Magistrale in Ingegneria Informatica
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.patches import Circle, Rectangle, Wedge, FancyBboxPatch
import matplotlib.patches as mpatches
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# Configurazione generale matplotlib per tesi
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Computer Modern Roman', 'Times New Roman']
plt.rcParams['font.size'] = 10
plt.rcParams['axes.labelsize'] = 11
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['xtick.labelsize'] = 9
plt.rcParams['ytick.labelsize'] = 9
plt.rcParams['legend.fontsize'] = 9
plt.rcParams['figure.dpi'] = 300

# ============================================================================
# FIGURA 1: Matrice di Correlazione Cloud Provider (Heatmap)
# ============================================================================

def create_cloud_correlation_matrix():
    """Genera heatmap della correlazione downtime tra cloud provider"""
    
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Dati di correlazione empirici
    data = {
        'AWS': [1.00, 0.12, 0.09],
        'Azure': [0.12, 1.00, 0.14],
        'GCP': [0.09, 0.14, 1.00]
    }
    
    df = pd.DataFrame(data, index=['AWS', 'Azure', 'GCP'])
    
    # Crea heatmap
    sns.heatmap(df, annot=True, fmt='.2f', cmap='coolwarm', 
                center=0.5, vmin=0, vmax=1, square=True, 
                linewidths=1, cbar_kws={"shrink": 0.8},
                annot_kws={'fontsize': 11, 'weight': 'bold'})
    
    plt.title('Matrice di Correlazione Downtime Cloud Provider\n(2020-2024)', 
              fontsize=14, pad=20)
    plt.xlabel('')
    plt.ylabel('')
    
    # Aggiungi note
    plt.text(0.5, -0.15, 
             'Correlazioni < 0.15 indicano indipendenza statistica dei guasti',
             ha='center', transform=ax.transAxes, fontsize=9, style='italic')
    
    plt.tight_layout()
    plt.savefig('figura_3_7_cloud_correlation.pdf', bbox_inches='tight')
    plt.show()
    
    return fig

# ============================================================================
# FIGURA 2: Dashboard KPI Real-time GIST
# ============================================================================

def create_gist_dashboard():
    """Crea dashboard multi-panel con KPI del framework GIST"""
    
    fig = plt.figure(figsize=(16, 10))
    fig.suptitle('Dashboard KPI Framework GIST - Monitoring Real-time', 
                 fontsize=16, fontweight='bold', y=0.98)
    
    # Crea griglia per subplots
    gs = fig.add_gridspec(3, 4, hspace=0.3, wspace=0.3)
    
    # --- Panel 1: Availability Gauge ---
    ax1 = fig.add_subplot(gs[0, 0])
    availability = 99.96
    create_gauge(ax1, availability, 'Disponibilità Sistema', 
                 min_val=99.0, max_val=100.0, target=99.95)
    
    # --- Panel 2: ASSA Reduction Bar ---
    ax2 = fig.add_subplot(gs[0, 1])
    reduction_actual = 42.7
    reduction_target = 35.0
    create_reduction_bar(ax2, reduction_actual, reduction_target, 
                        'Riduzione ASSA (%)')
    
    # --- Panel 3: TCO Evolution ---
    ax3 = fig.add_subplot(gs[0, 2:4])
    create_tco_evolution(ax3)
    
    # --- Panel 4: Latency Distribution ---
    ax4 = fig.add_subplot(gs[1, 0:2])
    create_latency_distribution(ax4)
    
    # --- Panel 5: Multi-cloud Pie ---
    ax5 = fig.add_subplot(gs[1, 2])
    create_multicloud_pie(ax5)
    
    # --- Panel 6: PUE Trend ---
    ax6 = fig.add_subplot(gs[1, 3])
    create_pue_trend(ax6)
    
    # --- Panel 7: Maturity Radar ---
    ax7 = fig.add_subplot(gs[2, 0:2], projection='polar')
    create_maturity_radar(ax7)
    
    # --- Panel 8: Cost Breakdown ---
    ax8 = fig.add_subplot(gs[2, 2:4])
    create_cost_breakdown(ax8)
    
    plt.tight_layout()
    plt.savefig('figura_3_8_gist_dashboard.pdf', bbox_inches='tight', dpi=300)
    plt.show()
    
    return fig

def create_gauge(ax, value, title, min_val=0, max_val=100, target=None):
    """Crea un gauge meter circolare"""
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 0.5)
    ax.set_aspect('equal')
    
    # Arco di sfondo
    theta = np.linspace(np.pi, 0, 100)
    x = np.cos(theta)
    y = np.sin(theta)
    ax.plot(x, y, 'lightgray', linewidth=20, solid_capstyle='round')
    
    # Arco del valore
    angle = np.pi * (1 - (value - min_val) / (max_val - min_val))
    theta_val = np.linspace(np.pi, angle, 50)
    x_val = np.cos(theta_val)
    y_val = np.sin(theta_val)
    
    # Colore basato su target
    if target and value >= target:
        color = 'green'
    elif target and value >= target * 0.95:
        color = 'orange'
    else:
        color = 'red'
    
    ax.plot(x_val, y_val, color, linewidth=20, solid_capstyle='round')
    
    # Valore al centro
    ax.text(0, -0.3, f'{value:.2f}%', ha='center', va='center', 
            fontsize=20, fontweight='bold')
    
    # Target line se specificato
    if target:
        target_angle = np.pi * (1 - (target - min_val) / (max_val - min_val))
        ax.plot([0.8*np.cos(target_angle), 1.1*np.cos(target_angle)],
                [0.8*np.sin(target_angle), 1.1*np.sin(target_angle)],
                'red', linewidth=2, linestyle='--')
    
    ax.set_title(title, fontsize=11, pad=10)
    ax.axis('off')

def create_reduction_bar(ax, actual, target, title):
    """Crea grafico a barre per confronto actual vs target"""
    categories = ['Target', 'Attuale']
    values = [target, actual]
    colors = ['#FFA500', '#00AA00'] if actual >= target else ['#FFA500', '#FF0000']
    
    bars = ax.barh(categories, values, color=colors, alpha=0.8)
    
    # Aggiungi valori sulle barre
    for bar, val in zip(bars, values):
        ax.text(val + 1, bar.get_y() + bar.get_height()/2, 
                f'{val:.1f}%', va='center', fontsize=10, fontweight='bold')
    
    ax.set_xlim(0, 50)
    ax.set_xlabel(title, fontsize=10)
    ax.axvline(x=target, color='red', linestyle='--', alpha=0.5, label='Target')
    ax.grid(True, alpha=0.3, axis='x')
    ax.set_title('Riduzione Superficie Attacco', fontsize=11, pad=10)

def create_tco_evolution(ax):
    """Crea grafico evoluzione TCO nel tempo"""
    months = np.arange(0, 37, 3)
    tco_baseline = np.ones(len(months)) * 100
    
    # Simulazione riduzione progressiva TCO
    tco_actual = 100 - (38.2/36) * months * (1 - np.exp(-months/12))
    tco_forecast = 100 - (38.2/36) * months * (1 - np.exp(-months/12)) * 1.05
    
    # Area di incertezza
    uncertainty = 5 * np.sin(months/6) * np.exp(-months/36)
    
    ax.plot(months, tco_baseline, 'r--', linewidth=2, label='Baseline', alpha=0.7)
    ax.plot(months, tco_actual, 'g-', linewidth=2.5, label='Attuale')
    ax.plot(months[months>=18], tco_forecast[months>=18], 'b:', 
            linewidth=2, label='Forecast')
    
    ax.fill_between(months, tco_baseline, tco_actual, 
                     where=(tco_actual <= tco_baseline),
                     color='green', alpha=0.2, label='Saving Cumulativo')
    
    ax.fill_between(months, tco_actual - uncertainty, tco_actual + uncertainty,
                     color='gray', alpha=0.2)
    
    # Milestone markers
    milestones = [6, 18, 36]
    for m in milestones:
        ax.plot(m, tco_actual[months == m], 'ko', markersize=8)
        saving = 100 - tco_actual[months == m][0]
        ax.annotate(f'-{saving:.1f}%', xy=(m, tco_actual[months == m]),
                   xytext=(m, tco_actual[months == m] - 5),
                   ha='center', fontsize=9, fontweight='bold')
    
    ax.set_xlabel('Mesi dall\'implementazione', fontsize=10)
    ax.set_ylabel('TCO Relativo (%)', fontsize=10)
    ax.set_title('Evoluzione TCO con Forecast', fontsize=11, pad=10)
    ax.set_xlim(0, 36)
    ax.set_ylim(55, 105)
    ax.legend(loc='upper right', fontsize=9)
    ax.grid(True, alpha=0.3)

def create_latency_distribution(ax):
    """Crea istogramma distribuzione latenza"""
    np.random.seed(42)
    
    # Genera dati con distribuzione lognormale (media ~23ms)
    latencies_zt = np.random.lognormal(3.1, 0.35, 5000)
    latencies_legacy = np.random.lognormal(3.8, 0.45, 5000)
    
    # Istogrammi
    ax.hist(latencies_legacy, bins=50, density=True, alpha=0.5, 
            color='red', label='Legacy', edgecolor='darkred')
    ax.hist(latencies_zt, bins=50, density=True, alpha=0.7, 
            color='blue', label='Zero Trust', edgecolor='darkblue')
    
    # Linee di riferimento
    ax.axvline(50, color='red', linestyle='--', linewidth=2, 
               label='Soglia Critica (50ms)')
    ax.axvline(np.median(latencies_zt), color='green', linestyle='-', 
               linewidth=2, label=f'Mediana ZT ({np.median(latencies_zt):.1f}ms)')
    
    # Annotazioni percentili
    p95_zt = np.percentile(latencies_zt, 95)
    p99_zt = np.percentile(latencies_zt, 99)
    ax.annotate(f'P95: {p95_zt:.1f}ms', xy=(p95_zt, 0.001), 
                xytext=(p95_zt+10, 0.015),
                arrowprops=dict(arrowstyle='->', color='blue'))
    
    ax.set_xlabel('Latenza (ms)', fontsize=10)
    ax.set_ylabel('Densità di Probabilità', fontsize=10)
    ax.set_title('Distribuzione Latenza: Legacy vs Zero Trust', fontsize=11, pad=10)
    ax.set_xlim(0, 100)
    ax.legend(loc='upper right', fontsize=9)
    ax.grid(True, alpha=0.3)

def create_multicloud_pie(ax):
    """Crea pie chart distribuzione multi-cloud"""
    sizes = [35, 40, 25]
    labels = ['AWS\n(35%)', 'Azure\n(40%)', 'GCP\n(25%)']
    colors = ['#FF9900', '#0078D4', '#EA4335']
    explode = (0.05, 0.05, 0.05)
    
    wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors,
                                       explode=explode, autopct='',
                                       startangle=90, shadow=True)
    
    # Personalizza testo
    for text in texts:
        text.set_fontsize(10)
        text.set_fontweight('bold')
    
    ax.set_title('Distribuzione Workload\nMulti-Cloud', fontsize=11, pad=10)

def create_pue_trend(ax):
    """Crea grafico trend PUE"""
    months = np.arange(0, 13)
    pue_values = 1.82 - 0.035 * months + 0.05 * np.sin(months * np.pi / 6)
    pue_target = np.ones(len(months)) * 1.50
    
    ax.plot(months, pue_values, 'b-', linewidth=2.5, marker='o', 
            markersize=5, label='PUE Attuale')
    ax.plot(months, pue_target, 'r--', linewidth=2, label='Target', alpha=0.7)
    
    ax.fill_between(months, 1.0, pue_values, alpha=0.3, color='lightblue')
    
    # Evidenzia area sotto target
    ax.fill_between(months, 1.0, pue_target, alpha=0.1, color='green')
    
    ax.set_xlabel('Mese', fontsize=10)
    ax.set_ylabel('PUE', fontsize=10)
    ax.set_title('Trend PUE (12 mesi)', fontsize=11, pad=10)
    ax.set_ylim(1.0, 2.0)
    ax.legend(loc='upper right', fontsize=9)
    ax.grid(True, alpha=0.3)

def create_maturity_radar(ax):
    """Crea radar chart per maturity assessment"""
    categories = ['Infrastruttura\nFisica', 'Rete\nSDN', 'Cloud\nAdoption', 
                  'Security\nZT', 'Compliance\nAutomation']
    scores = [85, 72, 68, 61, 54]
    
    # Numero di variabili
    num_vars = len(categories)
    
    # Calcola angoli
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    scores_plot = scores + scores[:1]
    angles += angles[:1]
    
    # Plot
    ax.plot(angles, scores_plot, 'o-', linewidth=2, color='blue', label='Attuale')
    ax.fill(angles, scores_plot, alpha=0.25, color='blue')
    
    # Target line
    target_scores = [80] * (num_vars + 1)
    ax.plot(angles, target_scores, 'r--', linewidth=1.5, label='Target', alpha=0.7)
    
    # Setup
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=9)
    ax.set_ylim(0, 100)
    ax.set_yticks([20, 40, 60, 80, 100])
    ax.set_yticklabels(['20', '40', '60', '80', '100'], fontsize=8)
    ax.set_title('GIST Maturity Assessment', fontsize=11, pad=20)
    ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1), fontsize=9)
    ax.grid(True)

def create_cost_breakdown(ax):
    """Crea stacked bar chart per breakdown costi"""
    categories = ['Baseline', 'Fase 1\n(6m)', 'Fase 2\n(18m)', 'Fase 3\n(36m)']
    
    # Componenti di costo (in percentuale del baseline)
    infrastructure = np.array([40, 38, 32, 25])
    operations = np.array([30, 27, 22, 18])
    security = np.array([20, 18, 16, 14])
    compliance = np.array([10, 9, 7, 5])
    
    # Posizioni delle barre
    x = np.arange(len(categories))
    width = 0.6
    
    # Stacked bars
    p1 = ax.bar(x, infrastructure, width, label='Infrastruttura', color='#FF6B6B')
    p2 = ax.bar(x, operations, width, bottom=infrastructure, 
                label='Operations', color='#4ECDC4')
    p3 = ax.bar(x, security, width, bottom=infrastructure+operations,
                label='Security', color='#45B7D1')
    p4 = ax.bar(x, compliance, width, bottom=infrastructure+operations+security,
                label='Compliance', color='#96CEB4')
    
    # Totali sopra le barre
    totals = infrastructure + operations + security + compliance
    for i, (xi, total) in enumerate(zip(x, totals)):
        ax.text(xi, total + 1, f'{total}%', ha='center', fontweight='bold')
        if i > 0:
            saving = 100 - total
            ax.text(xi, -5, f'-{saving}%', ha='center', color='green', 
                   fontweight='bold', fontsize=10)
    
    ax.set_ylabel('Costo Relativo (%)', fontsize=10)
    ax.set_title('Breakdown e Riduzione Costi per Fase', fontsize=11, pad=10)
    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    ax.set_ylim(0, 110)
    ax.legend(loc='upper right', fontsize=9)
    ax.grid(True, alpha=0.3, axis='y')

# ============================================================================
# FIGURA 3: Confronto Performance Cooling Strategies
# ============================================================================

def create_cooling_comparison():
    """Crea confronto visuale strategie di raffreddamento"""
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Analisi Comparativa Strategie di Raffreddamento Data Center', 
                 fontsize=14, fontweight='bold')
    
    # Dati
    technologies = ['CRAC\nTrad.', 'In-Row\nCooling', 'Free\nCooling', 
                    'Liquid\nCooling', 'Hybrid\nAI-Opt']
    pue_values = [1.82, 1.65, 1.40, 1.22, 1.35]
    pue_errors = [0.12, 0.09, 0.08, 0.06, 0.07]
    
    capex = [850, 1100, 1450, 1870, 1280]
    opex = [187, 162, 124, 98, 118]
    payback = [0, 28, 36, 42, 24]  # 0 per baseline
    co2_saving = [0, 234, 892, 1456, 978]
    
    # Panel 1: PUE Comparison
    ax1 = axes[0, 0]
    bars1 = ax1.bar(technologies, pue_values, yerr=pue_errors, 
                    capsize=5, color='skyblue', edgecolor='navy', alpha=0.7)
    ax1.axhline(y=1.5, color='red', linestyle='--', label='Target PUE')
    ax1.set_ylabel('PUE', fontsize=10)
    ax1.set_title('Power Usage Effectiveness', fontsize=11)
    ax1.set_ylim(1.0, 2.0)
    ax1.legend(fontsize=9)
    ax1.grid(True, alpha=0.3, axis='y')
    
    # Colora barre sotto target
    for bar, val in zip(bars1, pue_values):
        if val <= 1.5:
            bar.set_color('lightgreen')
    
    # Panel 2: Cost Analysis
    ax2 = axes[0, 1]
    x = np.arange(len(technologies))
    width = 0.35
    bars2_1 = ax2.bar(x - width/2, capex, width, label='CAPEX (€/kW)', 
                      color='orange', alpha=0.7)
    bars2_2 = ax2.bar(x + width/2, [o*10 for o in opex], width, 
                      label='OPEX×10 (€/kW/yr)', color='green', alpha=0.7)
    
    ax2.set_xlabel('Tecnologia', fontsize=10)
    ax2.set_ylabel('Costo (€)', fontsize=10)
    ax2.set_title('Analisi CAPEX vs OPEX', fontsize=11)
    ax2.set_xticks(x)
    ax2.set_xticklabels(technologies, fontsize=9)
    ax2.legend(fontsize=9)
    ax2.grid(True, alpha=0.3, axis='y')
    
    # Panel 3: Payback Period
    ax3 = axes[1, 0]
    colors_pb = ['gray' if p == 0 else 'green' if p <= 30 else 'orange' if p <= 40 else 'red' 
                 for p in payback]
    bars3 = ax3.bar(technologies, payback, color=colors_pb, alpha=0.7, edgecolor='black')
    ax3.axhline(y=36, color='orange', linestyle='--', label='Threshold 36 mesi')
    ax3.set_ylabel('Mesi', fontsize=10)
    ax3.set_title('Periodo di Payback', fontsize=11)
    ax3.legend(fontsize=9)
    ax3.grid(True, alpha=0.3, axis='y')
    
    # Aggiungi valori sulle barre
    for bar, val in zip(bars3, payback):
        if val > 0:
            ax3.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                    f'{val}m', ha='center', fontsize=9)
    
    # Panel 4: CO2 Savings
    ax4 = axes[1, 1]
    bars4 = ax4.bar(technologies, co2_saving, color='forestgreen', alpha=0.7, 
                    edgecolor='darkgreen')
    ax4.set_ylabel('CO₂ Risparmiata (ton/anno)', fontsize=10)
    ax4.set_title('Impatto Ambientale - Riduzione CO₂', fontsize=11)
    ax4.grid(True, alpha=0.3, axis='y')
    
    # Aggiungi target EU
    ax4.axhline(y=1000, color='blue', linestyle='--', 
                label='Target EU 2030')
    ax4.legend(fontsize=9)
    
    # Valori sulle barre
    for bar, val in zip(bars4, co2_saving):
        if val > 0:
            ax4.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 20,
                    f'{val:.0f}', ha='center', fontsize=9)
    
    plt.tight_layout()
    plt.savefig('figura_3_9_cooling_comparison.pdf', bbox_inches='tight')
    plt.show()
    
    return fig

# ============================================================================
# FIGURA 4: Zero Trust Maturity Model
# ============================================================================

def create_zero_trust_maturity():
    """Crea visualizzazione del modello di maturità Zero Trust"""
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle('Zero Trust Architecture: Maturity Model e Impatto', 
                 fontsize=14, fontweight='bold')
    
    # Panel 1: Maturity Levels
    ax1 = axes[0]
    
    levels = ['Legacy\nPerimeter', 'Initial\nZT', 'Developing\nZT', 
              'Advanced\nZT', 'Optimized\nZT']
    assa_reduction = [0, 12, 24, 35, 42.7]
    latency_impact = [0, 8, 15, 20, 23]
    
    x = np.arange(len(levels))
    width = 0.35
    
    bars1 = ax1.bar(x - width/2, assa_reduction, width, 
                    label='ASSA Reduction (%)', color='green', alpha=0.7)
    bars2 = ax1.bar(x + width/2, latency_impact, width,
                    label='Latency Impact (ms)', color='orange', alpha=0.7)
    
    ax1.set_xlabel('Livello di Maturità', fontsize=10)
    ax1.set_ylabel('Valore (%/ms)', fontsize=10)
    ax1.set_title('Trade-off Sicurezza vs Performance', fontsize=11)
    ax1.set_xticks(x)
    ax1.set_xticklabels(levels, fontsize=9)
    ax1.legend(fontsize=9)
    ax1.grid(True, alpha=0.3, axis='y')
    
    # Linea target ASSA
    ax1.axhline(y=35, color='green', linestyle='--', alpha=0.5)
    ax1.text(4.5, 35.5, 'Target', fontsize=8, color='green')
    
    # Panel 2: Implementation Timeline
    ax2 = axes[1]
    
    # Dati timeline
    phases = ['Assessment\n& Planning', 'Identity\nFoundation', 
              'Network\nSegmentation', 'Device\nTrust', 
              'Data\nProtection', 'Analytics\n& Automation']
    duration = [2, 4, 6, 4, 3, 5]  # mesi
    start = [0, 2, 6, 12, 16, 19]
    
    # Gantt chart
    for i, (phase, dur, st) in enumerate(zip(phases, duration, start)):
        ax2.barh(i, dur, left=st, height=0.5, 
                color=plt.cm.viridis(i/len(phases)), alpha=0.7)
        ax2.text(st + dur/2, i, f'{dur}m', ha='center', va='center', 
                color='white', fontweight='bold', fontsize=9)
    
    ax2.set_yticks(range(len(phases)))
    ax2.set_yticklabels(phases, fontsize=9)
    ax2.set_xlabel('Mesi dall\'inizio', fontsize=10)
    ax2.set_title('Timeline Implementazione Zero Trust', fontsize=11)
    ax2.set_xlim(0, 24)
    ax2.grid(True, alpha=0.3, axis='x')
    
    # Milestones
    milestones = {'Quick Wins': 6, 'Core Security': 12, 'Full ZT': 24}
    for label, month in milestones.items():
        ax2.axvline(x=month, color='red', linestyle='--', alpha=0.5)
        ax2.text(month, len(phases), label, rotation=45, 
                fontsize=8, ha='right')
    
    plt.tight_layout()
    plt.savefig('figura_3_10_zero_trust_maturity.pdf', bbox_inches='tight')
    plt.show()
    
    return fig

# ============================================================================
# MAIN: Genera tutte le figure
# ============================================================================

if __name__ == "__main__":
    print("Generazione Figure Capitolo 3...")
    
    # Genera tutte le figure
    print("1. Creando Matrice Correlazione Cloud...")
    create_cloud_correlation_matrix()
    
    print("2. Creando Dashboard GIST...")
    create_gist_dashboard()
    
    print("3. Creando Confronto Cooling Strategies...")
    create_cooling_comparison()
    
    print("4. Creando Zero Trust Maturity Model...")
    create_zero_trust_maturity()
    
    print("\nTutte le figure sono state generate con successo!")
    print("File salvati:")
    print("  - figura_3_7_cloud_correlation.pdf")
    print("  - figura_3_8_gist_dashboard.pdf") 
    print("  - figura_3_9_cooling_comparison.pdf")
    print("  - figura_3_10_zero_trust_maturity.pdf")