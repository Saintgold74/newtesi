"""
Simulazione propagazione Ransomware su infrastruttura GDO
Basato sul modello SIR (Susceptible-Infected-Recovered) adattato
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import glob
import os
import networkx as nx

class RansomwareSimulator:
    """Simula attacco ransomware su rete GDO"""
    
    def __init__(self, transactions, security_events):
        self.transactions = transactions
        self.security_events = security_events
        self.stores = transactions['store_id'].unique()
        self.network = self._build_network_topology()
        
    def _build_network_topology(self):
        """Costruisce topologia di rete basata sui dati"""
        G = nx.Graph()
        
        # Aggiungi nodi (stores)
        for store in self.stores:
            store_trans = self.transactions[self.transactions['store_id'] == store]
            G.add_node(store, 
                      size=len(store_trans),
                      criticality='high' if len(store_trans) > 50000 else 'medium' if len(store_trans) > 20000 else 'low',
                      status='susceptible',
                      infection_time=None)
        
        # Aggiungi edge (connessioni tra store)
        # Assumiamo connessioni basate su pattern transazioni
        for i, store1 in enumerate(self.stores):
            for store2 in self.stores[i+1:]:
                # Probabilità connessione basata su "vicinanza operativa"
                trans1 = len(self.transactions[self.transactions['store_id'] == store1])
                trans2 = len(self.transactions[self.transactions['store_id'] == store2])
                
                # Store simili per volume sono probabilmente connessi
                similarity = 1 - abs(trans1 - trans2) / max(trans1, trans2)
                if similarity > 0.3 or np.random.random() < 0.2:  # 20% chance random connection
                    G.add_edge(store1, store2, weight=similarity)
        
        return G
    
    def simulate_attack(self, patient_zero=None, duration_hours=72, 
                       with_zero_trust=False, with_segmentation=False):
        """
        Simula propagazione ransomware
        
        Args:
            patient_zero: Store inizialmente infetto (None = random)
            duration_hours: Durata simulazione in ore
            with_zero_trust: Se True, simula con Zero Trust
            with_segmentation: Se True, simula con micro-segmentazione
        
        Returns:
            DataFrame con timeline infezione
        """
        
        # Reset network
        for node in self.network.nodes():
            self.network.nodes[node]['status'] = 'susceptible'
            self.network.nodes[node]['infection_time'] = None
            self.network.nodes[node]['encrypted_data'] = 0
            self.network.nodes[node]['ransom_demanded'] = 0
        
        # Seleziona patient zero
        if patient_zero is None:
            # Scegli store con più vulnerabilità
            vuln_scores = {}
            for store in self.stores:
                store_events = self.security_events[self.security_events['store_id'] == store]
                critical_events = (store_events['severity'] == 'critical').sum()
                high_events = (store_events['severity'] == 'high').sum()
                vuln_scores[store] = critical_events * 10 + high_events * 5
            
            patient_zero = max(vuln_scores, key=vuln_scores.get)
        
        print(f"\n🦠 PATIENT ZERO: {patient_zero}")
        print(f"   Criticality: {self.network.nodes[patient_zero]['criticality']}")
        print(f"   Transactions: {self.network.nodes[patient_zero]['size']:,}")
        
        # Infetta patient zero
        self.network.nodes[patient_zero]['status'] = 'infected'
        self.network.nodes[patient_zero]['infection_time'] = 0
        
        # Timeline
        infection_timeline = [{
            'hour': 0,
            'store': patient_zero,
            'action': 'initial_infection',
            'infected_count': 1,
            'susceptible_count': len(self.stores) - 1,
            'recovered_count': 0,
            'encrypted_gb': np.random.uniform(100, 500)
        }]
        
        # Parametri di propagazione
        if with_zero_trust:
            base_spread_prob = 0.05  # 5% con Zero Trust
            detection_rate = 0.90     # 90% detection rate
            recovery_rate = 0.80      # 80% recovery success
        elif with_segmentation:
            base_spread_prob = 0.15  # 15% con segmentazione
            detection_rate = 0.70     # 70% detection
            recovery_rate = 0.60      # 60% recovery
        else:
            base_spread_prob = 0.35  # 35% baseline
            detection_rate = 0.40     # 40% detection
            recovery_rate = 0.30      # 30% recovery
        
        print(f"\n⚙️ PARAMETRI SIMULAZIONE:")
        print(f"   Zero Trust: {'ATTIVO' if with_zero_trust else 'DISATTIVO'}")
        print(f"   Segmentazione: {'ATTIVA' if with_segmentation else 'DISATTIVA'}")
        print(f"   Probabilità propagazione: {base_spread_prob:.0%}")
        print(f"   Tasso detection: {detection_rate:.0%}")
        
        # Simula propagazione ora per ora
        for hour in range(1, duration_hours + 1):
            
            # Trova nodi infetti
            infected_nodes = [n for n, d in self.network.nodes(data=True) 
                            if d['status'] == 'infected']
            
            new_infections = []
            new_recoveries = []
            
            for infected_node in infected_nodes:
                # Tenta di infettare vicini
                neighbors = list(self.network.neighbors(infected_node))
                
                for neighbor in neighbors:
                    if self.network.nodes[neighbor]['status'] == 'susceptible':
                        # Calcola probabilità infezione
                        edge_weight = self.network[infected_node][neighbor].get('weight', 0.5)
                        
                        # Modifica probabilità basata su criticality
                        if self.network.nodes[neighbor]['criticality'] == 'high':
                            infection_prob = base_spread_prob * 1.5 * edge_weight
                        elif self.network.nodes[neighbor]['criticality'] == 'medium':
                            infection_prob = base_spread_prob * 1.0 * edge_weight
                        else:
                            infection_prob = base_spread_prob * 0.7 * edge_weight
                        
                        # Decadimento temporale (più tempo passa, più è probabile detection)
                        time_factor = np.exp(-hour / 24)  # Decay esponenziale
                        infection_prob *= time_factor
                        
                        if np.random.random() < infection_prob:
                            new_infections.append(neighbor)
                            self.network.nodes[neighbor]['status'] = 'infected'
                            self.network.nodes[neighbor]['infection_time'] = hour
                            
                            # Calcola dati crittografati
                            store_size = self.network.nodes[neighbor]['size']
                            encrypted_gb = (store_size / 1000) * np.random.uniform(50, 200)
                            self.network.nodes[neighbor]['encrypted_data'] = encrypted_gb
                
                # Possibilità di recovery/isolamento
                if self.network.nodes[infected_node]['infection_time'] < hour - 3:  # Dopo 3 ore
                    if np.random.random() < detection_rate:
                        # Rilevato!
                        if np.random.random() < recovery_rate:
                            # Recovery riuscito
                            new_recoveries.append(infected_node)
                            self.network.nodes[infected_node]['status'] = 'recovered'
                        else:
                            # Isolato ma non recuperato
                            self.network.nodes[infected_node]['status'] = 'isolated'
            
            # Conta status
            status_counts = {'susceptible': 0, 'infected': 0, 'recovered': 0, 'isolated': 0}
            total_encrypted = 0
            
            for node, data in self.network.nodes(data=True):
                status_counts[data['status']] += 1
                if data['status'] in ['infected', 'isolated']:
                    total_encrypted += data.get('encrypted_data', 0)
            
            # Aggiungi a timeline
            infection_timeline.append({
                'hour': hour,
                'new_infections': len(new_infections),
                'new_recoveries': len(new_recoveries),
                'infected_count': status_counts['infected'],
                'susceptible_count': status_counts['susceptible'],
                'recovered_count': status_counts['recovered'],
                'isolated_count': status_counts['isolated'],
                'total_encrypted_gb': total_encrypted,
                'infection_rate': len(new_infections) / max(status_counts['susceptible'], 1)
            })
            
            # Log eventi importanti
            if len(new_infections) > 0:
                print(f"   Ora {hour:2d}: {len(new_infections)} nuove infezioni - {new_infections}")
            
            if len(new_recoveries) > 0:
                print(f"   Ora {hour:2d}: {len(new_recoveries)} sistemi recuperati")
            
            # Stop se tutti recovered o isolated
            if status_counts['infected'] == 0 and status_counts['susceptible'] == 0:
                print(f"\n✅ Simulazione terminata: tutti i sistemi gestiti")
                break
        
        return pd.DataFrame(infection_timeline)
    
    def calculate_impact(self, timeline_df):
        """Calcola impatto economico dell'attacco"""
        
        # Metriche chiave
        max_infected = timeline_df['infected_count'].max()
        total_encrypted = timeline_df['total_encrypted_gb'].max()
        duration = len(timeline_df)
        
        # Calcola costi (stime basate su report Sophos 2024)
        cost_per_gb_encrypted = 500  # €500 per GB per recovery
        cost_per_hour_downtime = 10000  # €10k/ora di downtime
        ransom_average = 250000  # €250k ransom medio
        
        # Stima sistemi che pagano ransom (18% secondo statistiche)
        systems_paying_ransom = max_infected * 0.18
        
        total_cost = {
            'data_recovery': total_encrypted * cost_per_gb_encrypted,
            'downtime': duration * cost_per_hour_downtime * (max_infected / len(self.stores)),
            'ransom_paid': systems_paying_ransom * ransom_average,
            'incident_response': 150000,  # Costo fisso IR
            'reputation_damage': 500000 * (max_infected / len(self.stores)),  # Proporzionale
        }
        
        total_cost['total'] = sum(total_cost.values())
        
        return {
            'max_infected': max_infected,
            'infection_rate': max_infected / len(self.stores) * 100,
            'total_encrypted_gb': total_encrypted,
            'attack_duration_hours': duration,
            'economic_impact': total_cost
        }
    
    def visualize_attack(self, timeline_df, save_path='outputs/ransomware_simulation.png'):
        """Visualizza propagazione attacco"""
        
        fig, axes = plt.subplots(2, 3, figsize=(15, 10))
        
        # 1. SIR Curve
        axes[0,0].plot(timeline_df['hour'], timeline_df['susceptible_count'], 
                      label='Susceptible', color='green', linewidth=2)
        axes[0,0].plot(timeline_df['hour'], timeline_df['infected_count'], 
                      label='Infected', color='red', linewidth=2)
        axes[0,0].plot(timeline_df['hour'], timeline_df['recovered_count'], 
                      label='Recovered', color='blue', linewidth=2)
        if 'isolated_count' in timeline_df.columns:
            axes[0,0].plot(timeline_df['hour'], timeline_df['isolated_count'], 
                          label='Isolated', color='orange', linestyle='--')
        
        axes[0,0].set_title('Modello SIR - Propagazione Ransomware', fontweight='bold')
        axes[0,0].set_xlabel('Ore dall\'infezione')
        axes[0,0].set_ylabel('Numero di sistemi')
        axes[0,0].legend()
        axes[0,0].grid(True, alpha=0.3)
        
        # 2. Infection Rate
        axes[0,1].bar(timeline_df['hour'], timeline_df.get('new_infections', 0), 
                     color='red', alpha=0.7)
        axes[0,1].set_title('Nuove Infezioni per Ora', fontweight='bold')
        axes[0,1].set_xlabel('Ore')
        axes[0,1].set_ylabel('Nuove infezioni')
        axes[0,1].grid(True, alpha=0.3, axis='y')
        
        # 3. Data Encrypted
        axes[0,2].fill_between(timeline_df['hour'], 
                              timeline_df['total_encrypted_gb'], 
                              alpha=0.5, color='darkred')
        axes[0,2].plot(timeline_df['hour'], timeline_df['total_encrypted_gb'], 
                      color='darkred', linewidth=2)
        axes[0,2].set_title('Dati Totali Crittografati', fontweight='bold')
        axes[0,2].set_xlabel('Ore')
        axes[0,2].set_ylabel('GB crittografati')
        axes[0,2].grid(True, alpha=0.3)
        
        # 4. Network Graph
        pos = nx.spring_layout(self.network, k=2, iterations=50)
        
        # Colora nodi per status finale
        node_colors = []
        for node in self.network.nodes():
            status = self.network.nodes[node]['status']
            if status == 'infected':
                node_colors.append('red')
            elif status == 'recovered':
                node_colors.append('blue')
            elif status == 'isolated':
                node_colors.append('orange')
            else:
                node_colors.append('green')
        
        nx.draw(self.network, pos, ax=axes[1,0],
                node_color=node_colors,
                node_size=[self.network.nodes[n]['size']/50 for n in self.network.nodes()],
                with_labels=True,
                font_size=8,
                edge_color='gray',
                alpha=0.7)
        
        axes[1,0].set_title('Topologia Rete - Stato Finale', fontweight='bold')
        axes[1,0].axis('off')
        
        # 5. Infection Speed
        if len(timeline_df) > 1:
            speed = timeline_df['infected_count'].diff()
            axes[1,1].plot(timeline_df['hour'][1:], speed[1:], 
                          color='red', marker='o', markersize=4)
            axes[1,1].axhline(y=0, color='black', linestyle='-', linewidth=0.5)
            axes[1,1].set_title('Velocità di Propagazione', fontweight='bold')
            axes[1,1].set_xlabel('Ore')
            axes[1,1].set_ylabel('Δ Infezioni/ora')
            axes[1,1].grid(True, alpha=0.3)
        
        # 6. Recovery Efficiency
        recovery_data = timeline_df.get('new_recoveries', pd.Series([0]*len(timeline_df)))
        axes[1,2].bar(timeline_df['hour'], recovery_data, 
                     color='blue', alpha=0.7)
        axes[1,2].set_title('Efficienza Recovery', fontweight='bold')
        axes[1,2].set_xlabel('Ore')
        axes[1,2].set_ylabel('Sistemi recuperati')
        axes[1,2].grid(True, alpha=0.3, axis='y')
        
        plt.suptitle('Simulazione Attacco Ransomware - Infrastruttura GDO', 
                    fontsize=14, fontweight='bold', y=1.02)
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"\n📊 Grafico salvato: {save_path}")
        
        return fig

def run_comparative_analysis():
    """Esegue analisi comparativa: Baseline vs Zero Trust vs Segmentazione"""
    
    # Carica dati
    print("="*70)
    print("SIMULAZIONE ATTACCO RANSOMWARE - ANALISI COMPARATIVA")
    print("="*70)
    
    trans_file = max(glob.glob('outputs/transactions_*.csv'), key=os.path.getctime)
    sec_file = max(glob.glob('outputs/security_events_*.csv'), key=os.path.getctime)
    
    transactions = pd.read_csv(trans_file)
    security_events = pd.read_csv(sec_file)
    
    print(f"\n📊 Dataset caricato:")
    print(f"   Transazioni: {len(transactions):,}")
    print(f"   Eventi security: {len(security_events):,}")
    
    # Inizializza simulatore
    simulator = RansomwareSimulator(transactions, security_events)
    
    scenarios = [
        ('Baseline (no protezione)', False, False),
        ('Con Micro-Segmentazione', False, True),
        ('Con Zero Trust', True, False),
    ]
    
    results = {}
    
    for scenario_name, zero_trust, segmentation in scenarios:
        print(f"\n{'='*60}")
        print(f"SCENARIO: {scenario_name}")
        print("="*60)
        
        # Simula attacco
        timeline = simulator.simulate_attack(
            duration_hours=48,
            with_zero_trust=zero_trust,
            with_segmentation=segmentation
        )
        
        # Calcola impatto
        impact = simulator.calculate_impact(timeline)
        
        results[scenario_name] = {
            'timeline': timeline,
            'impact': impact
        }
        
        print(f"\n📈 RISULTATI {scenario_name}:")
        print(f"   Sistemi infetti (max): {impact['max_infected']}/{len(simulator.stores)}")
        print(f"   Tasso infezione: {impact['infection_rate']:.1f}%")
        print(f"   Dati crittografati: {impact['total_encrypted_gb']:.0f} GB")
        print(f"   Durata attacco: {impact['attack_duration_hours']} ore")
        print(f"\n💰 IMPATTO ECONOMICO:")
        for cost_type, amount in impact['economic_impact'].items():
            if cost_type != 'total':
                print(f"   {cost_type}: €{amount:,.0f}")
        print(f"   TOTALE: €{impact['economic_impact']['total']:,.0f}")
        
        # Genera visualizzazione
        fig = simulator.visualize_attack(
            timeline, 
            save_path=f'outputs/ransomware_{scenario_name.replace(" ", "_").replace("(", "").replace(")", "")}.png'
        )
        plt.close(fig)
    
    # Confronto finale
    print("\n" + "="*70)
    print("ANALISI COMPARATIVA - RIDUZIONE IMPATTO")
    print("="*70)
    
    baseline_cost = results['Baseline (no protezione)']['impact']['economic_impact']['total']
    
    for scenario_name, data in results.items():
        cost = data['impact']['economic_impact']['total']
        reduction = (baseline_cost - cost) / baseline_cost * 100 if scenario_name != 'Baseline (no protezione)' else 0
        
        print(f"\n{scenario_name}:")
        print(f"  Costo totale: €{cost:,.0f}")
        if reduction > 0:
            print(f"  Riduzione vs baseline: {reduction:.1f}%")
            print(f"  Saving: €{baseline_cost - cost:,.0f}")
    
    # Crea grafico comparativo
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    
    scenarios_names = list(results.keys())
    costs = [results[s]['impact']['economic_impact']['total'] for s in scenarios_names]
    colors = ['red', 'orange', 'green']
    
    bars = ax.bar(range(len(scenarios_names)), costs, color=colors, alpha=0.7)
    
    # Aggiungi valori sopra le barre
    for i, (bar, cost) in enumerate(zip(bars, costs)):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'€{cost/1e6:.1f}M',
                ha='center', va='bottom', fontsize=11, fontweight='bold')
        
        if i > 0:
            reduction = (costs[0] - cost) / costs[0] * 100
            ax.text(bar.get_x() + bar.get_width()/2., height/2,
                   f'-{reduction:.0f}%',
                   ha='center', va='center', fontsize=10, 
                   fontweight='bold', color='white')
    
    ax.set_xticks(range(len(scenarios_names)))
    ax.set_xticklabels(scenarios_names, rotation=15, ha='right')
    ax.set_ylabel('Impatto Economico (€)', fontsize=12)
    ax.set_title('Confronto Impatto Economico - Attacco Ransomware', 
                fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3, axis='y')
    
    # Aggiungi linea baseline
    ax.axhline(y=costs[0], color='red', linestyle='--', alpha=0.5, label='Baseline')
    
    plt.tight_layout()
    plt.savefig('outputs/ransomware_comparison.png', dpi=300, bbox_inches='tight')
    print(f"\n📊 Grafico comparativo salvato: outputs/ransomware_comparison.png")
    
    return results

if __name__ == "__main__":
    # Esegui analisi comparativa completa
    results = run_comparative_analysis()
    
    print("\n" + "="*70)
    print("✅ SIMULAZIONE COMPLETATA")
    print("="*70)
    print("\nFile generati:")
    print("  - ransomware_Baseline_no_protezione.png")
    print("  - ransomware_Con_Micro-Segmentazione.png")
    print("  - ransomware_Con_Zero_Trust.png")
    print("  - ransomware_comparison.png")
    print("\nUsa questi risultati nel Capitolo 2 per validare l'efficacia")
    print("delle contromisure proposte dal framework GIST.")