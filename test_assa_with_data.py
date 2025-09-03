"""
Test ASSA-GDO con dati del Digital Twin - VERSIONE CORRETTA
"""
import pandas as pd
import numpy as np
import glob
import os

def load_latest_data():
    trans_files = glob.glob('outputs/transactions_*.csv')
    sec_files = glob.glob('outputs/security_events_*.csv')
    
    latest_trans = max(trans_files, key=os.path.getctime)
    latest_sec = max(sec_files, key=os.path.getctime)
    
    print(f"Carico: {latest_trans}")
    transactions = pd.read_csv(latest_trans)
    
    print(f"Carico: {latest_sec}")
    security = pd.read_csv(latest_sec)
    
    return transactions, security

def calculate_assa_score(transactions, security):
    """
    Calcola ASSA score BILANCIATO per ogni store
    Formula corretta con normalizzazione
    """
    stores = transactions['store_id'].unique()
    
    # Prima calcola i massimi per normalizzazione
    max_trans = transactions.groupby('store_id').size().max()
    
    assa_scores = {}
    
    for store in stores:
        # Metriche dal store
        store_trans = transactions[transactions['store_id'] == store]
        store_sec = security[security['store_id'] == store]
        
        # 1. EXPOSURE (0-40 punti)
        # Basato su volume transazioni e valore medio
        transaction_volume = len(store_trans)
        normalized_volume = (transaction_volume / max_trans) * 20
        
        avg_value = store_trans['amount'].mean()
        value_score = min(avg_value / 50, 1) * 10  # Normalizza su €50
        
        payment_diversity = store_trans['payment_method'].nunique()
        diversity_score = min(payment_diversity / 5, 1) * 10  # Max 5 metodi
        
        exposure = normalized_volume + value_score + diversity_score
        
        # 2. VULNERABILITY (0-30 punti)
        # Basato su tasso incidenti e eventi anomali
        total_events = len(store_sec)
        if total_events > 0:
            incidents = store_sec['is_incident'].sum()
            incident_rate = (incidents / total_events) * 20
            
            # Eventi fuori orario (proxy per anomalie)
            store_trans = store_trans.copy()  # Crea copia esplicita
            store_trans['hour'] = pd.to_datetime(store_trans['timestamp']).dt.hour
            after_hours = ((store_trans['hour'] < 8) | (store_trans['hour'] > 21)).sum()
            after_hours_rate = (after_hours / len(store_trans)) * 10
            
            vulnerability = incident_rate + after_hours_rate
        else:
            vulnerability = 0
        
        # 3. CRITICALITY (0-30 punti)
        # Basato su severity degli eventi (normalizzato)
        if total_events > 0:
            critical_rate = (store_sec['severity'] == 'critical').mean() * 100
            high_rate = (store_sec['severity'] == 'high').mean() * 50
            medium_rate = (store_sec['severity'] == 'medium').mean() * 20
            
            # Normalizza su scala 0-30
            criticality = min((critical_rate + high_rate + medium_rate) / 5, 30)
        else:
            criticality = 0
        
        # ASSA TOTALE (0-100)
        assa = exposure + vulnerability + criticality
        
        # Determina risk level con soglie realistiche
        if assa >= 70:
            risk_level = 'CRITICAL'
        elif assa >= 50:
            risk_level = 'HIGH'
        elif assa >= 30:
            risk_level = 'MEDIUM'
        else:
            risk_level = 'LOW'
        
        assa_scores[store] = {
            'exposure': round(exposure, 2),
            'vulnerability': round(vulnerability, 2),
            'criticality': round(criticality, 2),
            'total_assa': round(assa, 2),
            'risk_level': risk_level,
            'transactions': transaction_volume,
            'incidents': incidents if total_events > 0 else 0,
            'incident_rate': round((incidents/total_events*100) if total_events > 0 else 0, 2)
        }
    
    return assa_scores

def analyze_store_profiles(transactions):
    """
    Analizza i profili degli store per contesto
    """
    stores = transactions['store_id'].unique()
    profiles = {}
    
    for store in stores:
        store_trans = transactions[transactions['store_id'] == store]
        
        profiles[store] = {
            'total_transactions': len(store_trans),
            'avg_transaction_value': round(store_trans['amount'].mean(), 2),
            'total_revenue': round(store_trans['amount'].sum(), 2),
            'unique_payment_methods': store_trans['payment_method'].nunique(),
            'peak_hour': store_trans.groupby('hour').size().idxmax() if 'hour' in store_trans.columns else 'N/A'
        }
    
    return profiles

# Esegui analisi
trans, sec = load_latest_data()

# Aggiungi colonna hour se manca
if 'hour' not in trans.columns:
    trans['timestamp'] = pd.to_datetime(trans['timestamp'])
    trans['hour'] = trans['timestamp'].dt.hour

scores = calculate_assa_score(trans, sec)
profiles = analyze_store_profiles(trans)

print("\n" + "="*60)
print("ANALISI PROFILI STORE")
print("="*60)

# Ordina per revenue totale per identificare store size
sorted_stores = sorted(profiles.items(), key=lambda x: x[1]['total_revenue'], reverse=True)

for i, (store, profile) in enumerate(sorted_stores):
    size = 'LARGE' if i == 0 else 'MEDIUM' if i <= 2 else 'SMALL'
    print(f"\n{store} ({size} STORE):")
    print(f"  Transazioni totali: {profile['total_transactions']:,}")
    print(f"  Valore medio: €{profile['avg_transaction_value']}")
    print(f"  Revenue totale: €{profile['total_revenue']:,.2f}")

print("\n" + "="*60)
print("ASSA-GDO SCORES (NORMALIZZATI 0-100)")
print("="*60)

# Ordina per ASSA score
sorted_scores = sorted(scores.items(), key=lambda x: x[1]['total_assa'], reverse=True)

for store, metrics in sorted_scores:
    # Determina size basato su transazioni
    trans_count = metrics['transactions']
    if trans_count > 50000:
        size = "LARGE"
    elif trans_count > 35000:
        size = "MEDIUM"
    else:
        size = "SMALL"
    
    print(f"\n{store} ({size}):")
    print(f"  Exposure Score: {metrics['exposure']:.1f}/40")
    print(f"  Vulnerability Score: {metrics['vulnerability']:.1f}/30")
    print(f"  Criticality Score: {metrics['criticality']:.1f}/30")
    print(f"  ─────────────────────────")
    print(f"  TOTAL ASSA: {metrics['total_assa']:.1f}/100")
    print(f"  Risk Level: {metrics['risk_level']}")
    print(f"  ")
    print(f"  [Dettagli: {metrics['transactions']:,} trans, {metrics['incidents']} incidenti ({metrics['incident_rate']}%)]")

# Statistiche aggregate
print("\n" + "="*60)
print("STATISTICHE AGGREGATE")
print("="*60)

assa_values = [s['total_assa'] for s in scores.values()]
print(f"ASSA Medio: {np.mean(assa_values):.1f}")
print(f"ASSA Min: {np.min(assa_values):.1f}")
print(f"ASSA Max: {np.max(assa_values):.1f}")
print(f"Deviazione Standard: {np.std(assa_values):.1f}")

risk_distribution = {}
for s in scores.values():
    risk = s['risk_level']
    risk_distribution[risk] = risk_distribution.get(risk, 0) + 1

print("\nDistribuzione Risk Level:")
for risk, count in sorted(risk_distribution.items()):
    print(f"  {risk}: {count} store ({count/len(scores)*100:.0f}%)")

# Correlazione
incidents = [s['incidents'] for s in scores.values()]
assa_vals = [s['total_assa'] for s in scores.values()]
if len(set(incidents)) > 1:  # Solo se c'è variabilità
    correlation = np.corrcoef(incidents, assa_vals)[0, 1]
    print(f"\nCorrelazione ASSA-Incidenti: {correlation:.3f}")