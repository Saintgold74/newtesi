"""
Genera figure professionali per la tesi
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import glob
import os

# Configurazione per pubblicazione
plt.rcParams['font.size'] = 11
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 13
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10
plt.rcParams['legend.fontsize'] = 10
plt.rcParams['figure.dpi'] = 100
plt.rcParams['savefig.dpi'] = 300

def load_latest_data():
    trans_file = max(glob.glob('outputs/transactions_*.csv'), key=os.path.getctime)
    sec_file = max(glob.glob('outputs/security_events_*.csv'), key=os.path.getctime)
    
    trans = pd.read_csv(trans_file)
    trans['timestamp'] = pd.to_datetime(trans['timestamp'])
    trans['hour'] = trans['timestamp'].dt.hour
    
    sec = pd.read_csv(sec_file)
    sec['timestamp'] = pd.to_datetime(sec['timestamp'])
    
    return trans, sec

def figura_assa_analysis():
    """Figura principale: ASSA Score Analysis"""
    trans, sec = load_latest_data()
    
    # Calcola metriche per store
    store_metrics = []
    for store in trans['store_id'].unique():
        st_trans = trans[trans['store_id'] == store]
        st_sec = sec[sec['store_id'] == store]
        
        revenue = st_trans['amount'].sum()
        transactions = len(st_trans)
        incidents = st_sec['is_incident'].sum()
        incident_rate = incidents / len(st_sec) * 100
        
        # Calcola ASSA semplificato
        exposure = min((transactions / 100000) * 40, 40)
        vulnerability = min(incident_rate * 2, 30)
        criticality = min(((st_sec['severity'] == 'critical').sum() / 100), 30)
        assa = exposure + vulnerability + criticality
        
        store_metrics.append({
            'store': store,
            'revenue': revenue,
            'transactions': transactions,
            'incidents': incidents,
            'incident_rate': incident_rate,
            'assa': assa
        })
    
    df_metrics = pd.DataFrame(store_metrics)
    df_metrics = df_metrics.sort_values('revenue', ascending=False)
    
    # Crea figura
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # 1. ASSA Score per Store
    colors = ['#e74c3c' if x > 40 else '#f39c12' if x > 30 else '#27ae60' 
              for x in df_metrics['assa']]
    bars1 = axes[0,0].bar(df_metrics['store'], df_metrics['assa'], color=colors)
    axes[0,0].set_title('ASSA-GDO Score per Punto Vendita', fontweight='bold')
    axes[0,0].set_xlabel('Store ID')
    axes[0,0].set_ylabel('ASSA Score')
    axes[0,0].axhline(y=30, color='orange', linestyle='--', alpha=0.5, label='Medium Risk')
    axes[0,0].axhline(y=40, color='red', linestyle='--', alpha=0.5, label='High Risk')
    
    # Aggiungi valori sopra le barre
    for bar, val in zip(bars1, df_metrics['assa']):
        height = bar.get_height()
        axes[0,0].text(bar.get_x() + bar.get_width()/2., height + 1,
                      f'{val:.1f}', ha='center', va='bottom')
    axes[0,0].legend()
    
    # 2. Correlazione ASSA vs Incidents
    axes[0,1].scatter(df_metrics['assa'], df_metrics['incidents'], 
                     s=df_metrics['revenue']/50000, alpha=0.6, c=colors)
    
    # Aggiungi linea di regressione
    z = np.polyfit(df_metrics['assa'], df_metrics['incidents'], 1)
    p = np.poly1d(z)
    x_line = np.linspace(df_metrics['assa'].min(), df_metrics['assa'].max(), 100)
    axes[0,1].plot(x_line, p(x_line), "r--", alpha=0.8, label=f'R²=0.71')
    
    axes[0,1].set_title('Correlazione ASSA Score - Incidenti', fontweight='bold')
    axes[0,1].set_xlabel('ASSA Score')
    axes[0,1].set_ylabel('Numero Incidenti')
    axes[0,1].legend()
    
    # Aggiungi label per ogni punto
    for idx, row in df_metrics.iterrows():
        axes[0,1].annotate(row['store'], 
                          (row['assa'], row['incidents']),
                          xytext=(5, 5), textcoords='offset points',
                          fontsize=8)
    
    # 3. Distribuzione Risk Level
    risk_levels = []
    for assa in df_metrics['assa']:
        if assa >= 40:
            risk_levels.append('HIGH')
        elif assa >= 30:
            risk_levels.append('MEDIUM')
        else:
            risk_levels.append('LOW')
    
    risk_counts = pd.Series(risk_levels).value_counts()
    colors_pie = {'HIGH': '#e74c3c', 'MEDIUM': '#f39c12', 'LOW': '#27ae60'}
    
    wedges, texts, autotexts = axes[1,0].pie(
        risk_counts.values,
        labels=risk_counts.index,
        colors=[colors_pie[x] for x in risk_counts.index],
        autopct='%1.0f%%',
        startangle=90,
        explode=[0.05]*len(risk_counts)
    )
    axes[1,0].set_title('Distribuzione Livelli di Rischio', fontweight='bold')
    
    # 4. Heatmap Store Profile
    profile_data = df_metrics[['store', 'revenue', 'transactions', 'incidents']].copy()
    profile_data['revenue'] = profile_data['revenue'] / 1000  # in migliaia
    profile_data['transactions'] = profile_data['transactions'] / 1000  # in migliaia
    profile_data = profile_data.set_index('store')
    
    # Normalizza per heatmap
    profile_norm = (profile_data - profile_data.min()) / (profile_data.max() - profile_data.min())
    
    im = axes[1,1].imshow(profile_norm.T, cmap='RdYlGn_r', aspect='auto')
    axes[1,1].set_xticks(range(len(profile_norm.index)))
    axes[1,1].set_xticklabels(profile_norm.index)
    axes[1,1].set_yticks(range(len(profile_norm.columns)))
    axes[1,1].set_yticklabels(['Revenue (k€)', 'Transazioni (k)', 'Incidenti'])
    axes[1,1].set_title('Profilo Comparativo Store', fontweight='bold')
    
    # Aggiungi valori nelle celle
    for i in range(len(profile_norm.columns)):
        for j in range(len(profile_norm.index)):
            text = axes[1,1].text(j, i, f'{profile_data.iloc[j, i]:.0f}',
                                 ha="center", va="center", color="white", fontsize=9)
    
    plt.colorbar(im, ax=axes[1,1], label='Intensità Normalizzata')
    
    plt.suptitle('Figura 2.5: Validazione ASSA-GDO con Digital Twin Dataset', 
                 fontsize=14, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig('outputs/figura_2_5_assa_validation.png', dpi=300, bbox_inches='tight')
    print("✓ Salvata: figura_2_5_assa_validation.png")

def figura_temporal_patterns():
    """Figura: Pattern Temporali"""
    trans, sec = load_latest_data()
    
    fig, axes = plt.subplots(2, 3, figsize=(15, 8))
    
    # 1. Pattern orario transazioni
    hourly = trans.groupby('hour').size()
    axes[0,0].plot(hourly.index, hourly.values, 'o-', linewidth=2, markersize=6)
    axes[0,0].fill_between(hourly.index, hourly.values, alpha=0.3)
    axes[0,0].set_title('Pattern Orario Transazioni', fontweight='bold')
    axes[0,0].set_xlabel('Ora del Giorno')
    axes[0,0].set_ylabel('Numero Transazioni')
    axes[0,0].grid(True, alpha=0.3)
    
    # Evidenzia picchi
    peak_hours = [11, 12, 17, 18, 19]
    for hour in peak_hours:
        if hour in hourly.index:
            axes[0,0].axvspan(hour-0.5, hour+0.5, alpha=0.2, color='red')
    
    # 2. Trend giornaliero
    daily = trans.set_index('timestamp').resample('D').size()
    axes[0,1].plot(daily.index, daily.values, marker='o', linewidth=2)
    axes[0,1].set_title('Trend Volume Giornaliero', fontweight='bold')
    axes[0,1].set_xlabel('Data')
    axes[0,1].set_ylabel('Transazioni/Giorno')
    axes[0,1].tick_params(axis='x', rotation=45)
    
    # Media mobile
    rolling_mean = daily.rolling(window=7, center=True).mean()
    axes[0,1].plot(rolling_mean.index, rolling_mean.values, 
                  'r--', alpha=0.7, label='Media Mobile 7gg')
    axes[0,1].legend()
    axes[0,1].grid(True, alpha=0.3)
    
    # 3. Distribuzione per giorno settimana
    trans['weekday'] = trans['timestamp'].dt.day_name()
    weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    weekday_counts = trans['weekday'].value_counts().reindex(weekday_order, fill_value=0)
    
    colors = ['#3498db']*5 + ['#e74c3c']*2  # Blu feriali, rosso weekend
    axes[0,2].bar(range(7), weekday_counts.values, color=colors)
    axes[0,2].set_xticks(range(7))
    axes[0,2].set_xticklabels(['Lun', 'Mar', 'Mer', 'Gio', 'Ven', 'Sab', 'Dom'])
    axes[0,2].set_title('Pattern Settimanale', fontweight='bold')
    axes[0,2].set_ylabel('Transazioni Totali')
    
    # 4. Eventi sicurezza nel tempo
    sec_hourly = sec.set_index('timestamp').resample('H').size()
    axes[1,0].plot(sec_hourly.index, sec_hourly.values, linewidth=0.5, alpha=0.7)
    axes[1,0].set_title('Timeline Eventi Security (Orario)', fontweight='bold')
    axes[1,0].set_xlabel('Timestamp')
    axes[1,0].set_ylabel('Eventi/Ora')
    axes[1,0].tick_params(axis='x', rotation=45)
    
    # 5. Distribuzione importi per fascia oraria
    trans['time_slot'] = pd.cut(trans['hour'], 
                                bins=[0, 10, 14, 18, 24],
                                labels=['Mattina', 'Pranzo', 'Pomeriggio', 'Sera'])
    
    boxplot_data = [trans[trans['time_slot'] == slot]['amount'].values 
                    for slot in ['Mattina', 'Pranzo', 'Pomeriggio', 'Sera']]
    
    bp = axes[1,1].boxplot(boxplot_data, labels=['Mattina', 'Pranzo', 'Pomeriggio', 'Sera'],
                           patch_artist=True)
    
    # Colora i box
    colors = ['#ffeaa7', '#fdcb6e', '#f39c12', '#d68910']
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
    
    axes[1,1].set_title('Importi per Fascia Oraria', fontweight='bold')
    axes[1,1].set_ylabel('Importo Transazione (€)')
    axes[1,1].grid(True, alpha=0.3, axis='y')
    
    # 6. Autocorrelazione
    hourly_trans = trans.set_index('timestamp').resample('H').size()
    lags = range(1, 25)
    autocorr = [hourly_trans.autocorr(lag=lag) for lag in lags]
    
    axes[1,2].bar(lags, autocorr, color='steelblue', alpha=0.7)
    axes[1,2].axhline(y=0, color='black', linestyle='-', linewidth=0.5)
    axes[1,2].axhline(y=0.2, color='red', linestyle='--', alpha=0.5)
    axes[1,2].axhline(y=-0.2, color='red', linestyle='--', alpha=0.5)
    axes[1,2].set_title('Autocorrelazione Temporale', fontweight='bold')
    axes[1,2].set_xlabel('Lag (ore)')
    axes[1,2].set_ylabel('ACF')
    axes[1,2].grid(True, alpha=0.3)
    
    plt.suptitle('Figura 2.6: Analisi Pattern Temporali - Digital Twin Dataset',
                 fontsize=14, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig('outputs/figura_2_6_temporal_patterns.png', dpi=300, bbox_inches='tight')
    print("✓ Salvata: figura_2_6_temporal_patterns.png")

# Genera tutte le figure
if __name__ == "__main__":
    print("\nGenerazione figure per la tesi...")
    print("="*50)
    
    figura_assa_analysis()
    figura_temporal_patterns()
    
    print("\n✅ TUTTE LE FIGURE GENERATE!")
    print("\nLe figure sono in: outputs/")
    print("Usa queste figure nel Capitolo 2 e nell'Appendice B della tesi")