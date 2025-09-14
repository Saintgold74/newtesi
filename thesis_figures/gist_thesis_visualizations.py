#!/usr/bin/env python3
"""
GIST Framework - Visualizzazioni per Tesi
Autore: Marco Santoro
Generazione di tutti i grafici e diagrammi per la tesi sulla sicurezza GDO
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.patches import Rectangle, FancyBboxPatch, Circle, FancyArrowPatch
from matplotlib.patches import ConnectionPatch
import matplotlib.patches as patches
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# Configurazione stile generale
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# Colori standard per la tesi
COLORS = {
    'primary': '#0066CC',
    'success': '#00AA44', 
    'danger': '#CC0000',
    'warning': '#FF9900',
    'info': '#00CCCC',
    'dark': '#333333',
    'light': '#F5F5F5',
    'gray': '#666666'
}

class GISTVisualizations:
    """Classe per generare tutte le visualizzazioni della tesi GIST"""
    
    def __init__(self):
        self.colors = COLORS
        plt.rcParams['font.family'] = 'sans-serif'
        plt.rcParams['font.size'] = 10
        plt.rcParams['figure.dpi'] = 150
        
    def create_hybrid_cloud_architecture(self):
        """Figura 3.3: Architettura Pattern GRAF-1 Hybrid Cloud Broker"""
        fig, ax = plt.subplots(figsize=(14, 10))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.axis('off')
        
        # Titolo
        ax.text(5, 9.5, 'Pattern GRAF-1: Hybrid Cloud Broker per GDO', 
                fontsize=16, fontweight='bold', ha='center')
        
        # Layer 1: Decisionale
        decision_box = FancyBboxPatch((0.5, 7.5), 9, 1.5, 
                                      boxstyle="round,pad=0.05",
                                      facecolor='#E8F4FD', 
                                      edgecolor=self.colors['primary'], 
                                      linewidth=2)
        ax.add_patch(decision_box)
        ax.text(5, 8.5, 'LAYER DECISIONALE', fontsize=12, fontweight='bold', ha='center')
        ax.text(5, 8.1, 'Policy Engine & Workload Optimizer', fontsize=10, ha='center')
        ax.text(2.5, 7.8, '• Costo: €/ora per workload', fontsize=8)
        ax.text(2.5, 7.6, '• Latenza: requisiti <50ms per POS', fontsize=8)
        ax.text(6.5, 7.8, '• Compliance: GDPR data residency', fontsize=8)
        ax.text(6.5, 7.6, '• Security: Zero Trust policies', fontsize=8)
        
        # Freccia verso il basso
        arrow1 = FancyArrowPatch((5, 7.4), (5, 6.6), 
                                connectionstyle="arc3", 
                                arrowstyle='->', 
                                mutation_scale=20, 
                                linewidth=2,
                                color=self.colors['dark'])
        ax.add_patch(arrow1)
        
        # Layer 2: Orchestration
        orch_box = FancyBboxPatch((0.5, 5), 9, 1.5, 
                                  boxstyle="round,pad=0.05",
                                  facecolor='#FFF4E6', 
                                  edgecolor=self.colors['warning'], 
                                  linewidth=2)
        ax.add_patch(orch_box)
        ax.text(5, 6, 'ORCHESTRATION LAYER', fontsize=12, fontweight='bold', ha='center')
        
        # Componenti orchestrazione
        components = ['Kubernetes\nFederation', 'Terraform\nIaC', 'Ansible\nConfig', 'Istio\nService Mesh']
        x_positions = [2, 4, 6, 8]
        for comp, x in zip(components, x_positions):
            comp_box = FancyBboxPatch((x-0.4, 5.2), 0.8, 0.5,
                                      boxstyle="round,pad=0.02",
                                      facecolor='white',
                                      edgecolor=self.colors['gray'])
            ax.add_patch(comp_box)
            ax.text(x, 5.45, comp, fontsize=8, ha='center', va='center')
        
        # Freccia verso il basso
        arrow2 = FancyArrowPatch((5, 4.9), (5, 4.1), 
                                connectionstyle="arc3", 
                                arrowstyle='->', 
                                mutation_scale=20,
                                linewidth=2,
                                color=self.colors['dark'])
        ax.add_patch(arrow2)
        
        # Layer 3: Infrastructure
        infra_box = FancyBboxPatch((0.5, 1), 9, 3, 
                                   boxstyle="round,pad=0.05",
                                   facecolor='#F0FFF0', 
                                   edgecolor=self.colors['success'], 
                                   linewidth=2)
        ax.add_patch(infra_box)
        ax.text(5, 3.7, 'INFRASTRUCTURE LAYER', fontsize=12, fontweight='bold', ha='center')
        
        # On-Premise
        onprem_box = FancyBboxPatch((1, 1.5), 2.5, 1.8,
                                    boxstyle="round,pad=0.02",
                                    facecolor='#FFE6E6',
                                    edgecolor=self.colors['danger'])
        ax.add_patch(onprem_box)
        ax.text(2.25, 3, 'On-Premise (35%)', fontsize=10, fontweight='bold', ha='center')
        ax.text(2.25, 2.6, 'Core Systems:', fontsize=9, ha='center')
        ax.text(2.25, 2.3, '• ERP (SAP)', fontsize=8, ha='center')
        ax.text(2.25, 2.1, '• Legacy POS', fontsize=8, ha='center')
        ax.text(2.25, 1.9, '• Oracle DB', fontsize=8, ha='center')
        ax.text(2.25, 1.7, 'Criticità: Alta', fontsize=8, ha='center', style='italic')
        
        # Private Cloud
        private_box = FancyBboxPatch((3.75, 1.5), 2.5, 1.8,
                                     boxstyle="round,pad=0.02",
                                     facecolor='#E6F3FF',
                                     edgecolor=self.colors['info'])
        ax.add_patch(private_box)
        ax.text(5, 3, 'Private Cloud (25%)', fontsize=10, fontweight='bold', ha='center')
        ax.text(5, 2.6, 'VMware vSphere:', fontsize=9, ha='center')
        ax.text(5, 2.3, '• Sensitive Data', fontsize=8, ha='center')
        ax.text(5, 2.1, '• Compliance Apps', fontsize=8, ha='center')
        ax.text(5, 1.9, '• Internal Services', fontsize=8, ha='center')
        ax.text(5, 1.7, 'Controllo: Totale', fontsize=8, ha='center', style='italic')
        
        # Public Cloud
        public_box = FancyBboxPatch((6.5, 1.5), 2.5, 1.8,
                                    boxstyle="round,pad=0.02",
                                    facecolor='#E6FFE6',
                                    edgecolor=self.colors['success'])
        ax.add_patch(public_box)
        ax.text(7.75, 3, 'Public Cloud (40%)', fontsize=10, fontweight='bold', ha='center')
        ax.text(7.75, 2.6, 'AWS + Azure:', fontsize=9, ha='center')
        ax.text(7.75, 2.3, '• Analytics', fontsize=8, ha='center')
        ax.text(7.75, 2.1, '• Web Services', fontsize=8, ha='center')
        ax.text(7.75, 1.9, '• Dev/Test', fontsize=8, ha='center')
        ax.text(7.75, 1.7, 'Scalabilità: ∞', fontsize=8, ha='center', style='italic')
        
        # Metriche chiave in basso
        metrics_box = FancyBboxPatch((1, 0.1), 8, 0.6,
                                     boxstyle="round,pad=0.02",
                                     facecolor='#FFFFCC',
                                     edgecolor=self.colors['warning'],
                                     linewidth=2)
        ax.add_patch(metrics_box)
        ax.text(5, 0.5, 'Metriche Chiave:', fontsize=10, fontweight='bold', ha='center')
        ax.text(2.5, 0.25, '📊 TCO: -34%', fontsize=9, ha='center')
        ax.text(4.5, 0.25, '⏱ Latenza: 47ms', fontsize=9, ha='center')
        ax.text(6.5, 0.25, '✅ SLA: 99.96%', fontsize=9, ha='center')
        ax.text(8, 0.25, '🔒 Security: A+', fontsize=9, ha='center')
        
        plt.tight_layout()
        return fig
    
    def create_cost_comparison_table(self):
        """Tabella comparativa costi cloud providers"""
        
        # Dati della tabella
        data = {
            'Componente': ['COMPUTE', 'VMs (100x)', 'Kubernetes', 'Serverless',
                          'STORAGE', 'Block (50TB)', 'Object (100TB)', 'Backup',
                          'NETWORKING', 'Bandwidth', 'Load Balancer', '',
                          'TOTALE MENSILE', 'TOTALE ANNUALE', 'TCO 3 ANNI', 'RISPARMIO %'],
            'AWS': ['', '€4,200', '€1,200', '€800',
                   '', '€2,500', '€2,100', '€450',
                   '', '€1,800', '€350', '',
                   '€13,400', '€160,800', '€482,400', '52%'],
            'Azure': ['', '€3,900', '€1,100', '€750',
                     '', '€2,300', '€1,950', '€400',
                     '', '€1,650', '€300', '',
                     '€12,350', '€148,200', '€444,600', '56%'],
            'GCP': ['', '€4,100', '€950', '€850',
                   '', '€2,400', '€1,900', '€420',
                   '', '€1,700', '€320', '',
                   '€12,640', '€151,680', '€455,040', '55%'],
            'On-Premise': ['', '€8,500', '€2,500', 'N/A',
                          '', '€4,200', '€6,500', '€1,200',
                          '', '€3,200', '€800', '',
                          '€27,900', '€334,800', '€1,004,400', 'Baseline']
        }
        
        df = pd.DataFrame(data)
        
        fig, ax = plt.subplots(figsize=(14, 10))
        ax.axis('tight')
        ax.axis('off')
        
        # Titolo
        ax.text(0.5, 1.05, 'Analisi Comparativa Costi Cloud Provider per GDO Media (100 PV)',
                fontsize=14, fontweight='bold', ha='center', transform=ax.transAxes)
        
        # Creare la tabella
        table = ax.table(cellText=df.values,
                        colLabels=df.columns,
                        cellLoc='center',
                        loc='center',
                        colWidths=[0.2, 0.15, 0.15, 0.15, 0.2])
        
        # Styling della tabella
        table.auto_set_font_size(False)
        table.set_fontsize(9)
        table.scale(1.2, 2)
        
        # Colorare le celle
        for i in range(len(df)):
            for j in range(len(df.columns)):
                cell = table[(i+1, j)]
                
                # Header
                if i == -1:
                    cell.set_facecolor('#2C3E50')
                    cell.set_text_props(weight='bold', color='white')
                # Sezioni categoria
                elif df.iloc[i, 0] in ['COMPUTE', 'STORAGE', 'NETWORKING']:
                    cell.set_facecolor('#34495E')
                    cell.set_text_props(weight='bold', color='white')
                # Totali
                elif df.iloc[i, 0] in ['TOTALE MENSILE', 'TOTALE ANNUALE', 'TCO 3 ANNI']:
                    cell.set_facecolor('#E8F8F5')
                    cell.set_text_props(weight='bold')
                # Risparmio
                elif df.iloc[i, 0] == 'RISPARMIO %':
                    cell.set_facecolor('#D5F4E6')
                    cell.set_text_props(weight='bold', color='green')
                # On-Premise più costoso
                elif j == 4 and df.iloc[i, j] != '' and df.iloc[i, j] != 'N/A':
                    if '€' in df.iloc[i, j]:
                        cell.set_facecolor('#FADBD8')
        
        # Note in fondo
        note_text = """Note:
• Prezzi basati su commitment 3 anni con Reserved Instances
• Include costi di migrazione ammortizzati su 36 mesi
• Esclude costi di personale (assumendo re-skilling del team esistente)
• Bandwidth calcolata su 500GB/giorno per punto vendita"""
        
        ax.text(0.5, -0.1, note_text, fontsize=8, ha='center', 
                transform=ax.transAxes, style='italic')
        
        plt.tight_layout()
        return fig
    
    def create_assa_dashboard(self):
        """Dashboard ASSA-GDO Real-Time"""
        fig = plt.figure(figsize=(16, 10))
        
        # Titolo principale
        fig.suptitle('ASSA-GDO SECURITY DASHBOARD\n[Data: Real-time | Refresh: 5s]', 
                    fontsize=16, fontweight='bold')
        
        # Griglia personalizzata
        gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)
        
        # 1. Attack Surface Score (grande, top-left)
        ax1 = fig.add_subplot(gs[0, 0])
        ax1.set_title('Attack Surface Score', fontweight='bold')
        
        # Gauge chart simulato
        theta = np.linspace(np.pi, 0, 100)
        r_inner = 0.7
        r_outer = 1.0
        
        # Colori per zone di rischio
        colors_risk = ['green', 'yellow', 'orange', 'red']
        boundaries = [0, 25, 50, 75, 100]
        
        for i in range(len(colors_risk)):
            start = int(boundaries[i])
            end = int(boundaries[i+1]) if i < len(colors_risk)-1 else 100
            ax1.fill_between(theta[start:end], r_inner, r_outer, 
                           color=colors_risk[i], alpha=0.3)
        
        # Valore attuale
        current_value = 512
        baseline_value = 847
        reduction = ((baseline_value - current_value) / baseline_value) * 100
        
        # Indicatore
        angle = np.pi * (1 - current_value/1000)
        ax1.arrow(0, 0, r_inner * np.cos(angle), r_inner * np.sin(angle),
                 head_width=0.1, head_length=0.05, fc='black', ec='black', linewidth=2)
        
        ax1.text(0, -0.3, f'{current_value}', fontsize=28, fontweight='bold', ha='center')
        ax1.text(0, -0.5, f'▼ {reduction:.1f}%', fontsize=14, color='green', ha='center')
        ax1.text(0, -0.65, 'vs baseline', fontsize=10, ha='center')
        
        ax1.set_xlim(-1.2, 1.2)
        ax1.set_ylim(-0.8, 1.2)
        ax1.axis('off')
        
        # 2. Threat Indicators (top-center)
        ax2 = fig.add_subplot(gs[0, 1])
        ax2.set_title('Threat Indicators', fontweight='bold')
        
        threats = {
            '🔴 Critical': 2,
            '🟠 High': 7,
            '🟡 Medium': 23,
            '🟢 Low': 156
        }
        
        y_pos = np.arange(len(threats))
        values = list(threats.values())
        labels = list(threats.keys())
        
        bars = ax2.barh(y_pos, values, color=['#CC0000', '#FF6600', '#FFCC00', '#00AA44'])
        ax2.set_yticks(y_pos)
        ax2.set_yticklabels(labels)
        ax2.set_xlabel('Count')
        
        # Aggiungi valori sulle barre
        for i, (bar, val) in enumerate(zip(bars, values)):
            ax2.text(val + 2, bar.get_y() + bar.get_height()/2, 
                    str(val), va='center', fontweight='bold')
        
        # 3. Network Topology (top-right)
        ax3 = fig.add_subplot(gs[0, 2])
        ax3.set_title('Network Topology', fontweight='bold')
        
        # Nodi della rete
        nodes = {
            'DC-1': (0.5, 0.8),
            'PV1': (0.2, 0.4),
            'PV2': (0.5, 0.4),
            'PV3': (0.8, 0.4),
            'Edge1': (0.2, 0.1),
            'Edge2': (0.5, 0.1),
            'Edge3': (0.8, 0.1)
        }
        
        # Disegna connessioni
        connections = [
            ('DC-1', 'PV1'), ('DC-1', 'PV2'), ('DC-1', 'PV3'),
            ('PV1', 'Edge1'), ('PV2', 'Edge2'), ('PV3', 'Edge3')
        ]
        
        for conn in connections:
            start = nodes[conn[0]]
            end = nodes[conn[1]]
            ax3.plot([start[0], end[0]], [start[1], end[1]], 
                    'b-', alpha=0.5, linewidth=2)
        
        # Disegna nodi
        for name, pos in nodes.items():
            if 'DC' in name:
                color = 'red'
                size = 300
            elif 'PV' in name:
                color = 'blue'
                size = 200
            else:
                color = 'green'
                size = 150
            
            ax3.scatter(pos[0], pos[1], s=size, c=color, alpha=0.7, edgecolors='black')
            ax3.text(pos[0], pos[1]-0.05, name, fontsize=8, ha='center')
        
        ax3.set_xlim(0, 1)
        ax3.set_ylim(0, 1)
        ax3.axis('off')
        
        # 4. Incident Timeline (middle-left, spanning 2 columns)
        ax4 = fig.add_subplot(gs[1, :2])
        ax4.set_title('Incident Timeline (Last 24h)', fontweight='bold')
        
        # Genera timeline eventi
        times = pd.date_range(start='2024-01-15 00:00', periods=24, freq='H')
        incidents = np.random.poisson(2, 24)  # Eventi casuali
        
        # Aggiungi alcuni picchi
        incidents[14] = 8  # Picco alle 14:00
        incidents[15] = 6
        
        ax4.bar(range(24), incidents, color='steelblue', alpha=0.7)
        ax4.plot(range(24), incidents, 'r-', linewidth=2, alpha=0.5)
        
        # Evidenzia orari critici
        ax4.axvspan(14, 16, alpha=0.2, color='red', label='Critical Period')
        
        ax4.set_xlabel('Hour of Day')
        ax4.set_ylabel('Number of Incidents')
        ax4.set_xticks(range(0, 24, 2))
        ax4.set_xticklabels([f'{h:02d}:00' for h in range(0, 24, 2)], rotation=45)
        ax4.legend()
        ax4.grid(True, alpha=0.3)
        
        # 5. Current Alerts (middle-right)
        ax5 = fig.add_subplot(gs[1, 2])
        ax5.set_title('Active Alerts', fontweight='bold')
        
        alerts = [
            ('14:32', 'POS-47', 'Ransomware', 'CONTAINED', 'red'),
            ('14:28', 'Server-12', 'Anomaly', 'INVESTIGATING', 'orange'),
            ('14:15', 'DB-Master', 'High Load', 'MONITORING', 'yellow'),
            ('13:45', 'Gateway-3', 'Port Scan', 'BLOCKED', 'green')
        ]
        
        ax5.axis('off')
        y_position = 0.9
        for alert in alerts:
            time, system, type_alert, status, color = alert
            ax5.text(0.1, y_position, f'{time}', fontsize=9, fontweight='bold')
            ax5.text(0.3, y_position, f'{system}', fontsize=9)
            ax5.text(0.5, y_position, f'{type_alert}', fontsize=9)
            ax5.text(0.7, y_position, f'[{status}]', fontsize=9, 
                    color=color, fontweight='bold')
            y_position -= 0.2
        
        # 6. Propagation Paths (bottom, spanning all columns)
        ax6 = fig.add_subplot(gs[2, :])
        ax6.set_title('Top 5 Critical Propagation Paths', fontweight='bold')
        
        paths = [
            ('POS-12 → Gateway-3 → DB-Master', 0.73),
            ('IoT-Sensor-8 → HVAC → Core-Switch', 0.67),
            ('Guest-WiFi → DMZ → App-Server', 0.61),
            ('Supplier-VPN → ERP → Finance-DB', 0.58),
            ('Cloud-API → K8s-Cluster → Storage', 0.54)
        ]
        
        y_pos = np.arange(len(paths))
        probabilities = [p[1] for p in paths]
        labels = [p[0] for p in paths]
        
        bars = ax6.barh(y_pos, probabilities)
        
        # Colora le barre in base al rischio
        for i, (bar, prob) in enumerate(zip(bars, probabilities)):
            if prob > 0.7:
                bar.set_color('red')
            elif prob > 0.6:
                bar.set_color('orange')
            else:
                bar.set_color('yellow')
            
            # Aggiungi probabilità sulla barra
            ax6.text(prob + 0.01, bar.get_y() + bar.get_height()/2,
                    f'P={prob:.2f}', va='center', fontweight='bold')
        
        ax6.set_yticks(y_pos)
        ax6.set_yticklabels(labels)
        ax6.set_xlabel('Propagation Probability')
        ax6.set_xlim(0, 1)
        ax6.axvline(x=0.6, color='red', linestyle='--', alpha=0.5, label='Risk Threshold')
        ax6.legend()
        ax6.grid(True, alpha=0.3, axis='x')
        
        plt.tight_layout()
        return fig
    
    def create_min_heatmap(self):
        """Matrice MIN - Mappatura Controlli Unificati"""
        fig, ax = plt.subplots(figsize=(14, 10))
        
        # Genera dati di esempio per la heatmap
        np.random.seed(42)
        
        # Dimensioni della matrice
        n_pci = 12
        n_gdpr = 10
        n_controls = 8
        
        # Crea matrice di correlazione
        data = np.zeros((n_gdpr + 3, n_pci))  # +3 per NIS2
        
        # Pattern realistici di mappatura
        # Controllo 1: IAM
        data[0, [0, 2, 4, 7]] = 2  # Copertura completa
        data[0, [1, 5, 8]] = 1     # Copertura parziale
        
        # Controllo 2: Encryption
        data[1, [1, 3, 6, 9]] = 2
        data[1, [0, 2, 7]] = 1
        
        # Controllo 3: Logging
        data[2, [2, 4, 5, 8, 10]] = 2
        data[2, [1, 6]] = 1
        
        # Altri controlli con pattern casuali ma realistici
        for i in range(3, n_gdpr):
            # Copertura completa random
            full_coverage = np.random.choice(n_pci, size=np.random.randint(3, 6), replace=False)
            data[i, full_coverage] = 2
            # Copertura parziale random
            partial_coverage = np.random.choice(n_pci, size=np.random.randint(2, 4), replace=False)
            data[i, partial_coverage] = 1
        
        # Crea heatmap
        cmap = plt.cm.colors.ListedColormap(['white', '#FFE6B3', '#4CAF50'])
        im = ax.imshow(data, cmap=cmap, aspect='auto', vmin=0, vmax=2)
        
        # Etichette
        pci_labels = [f'PCI {i+1}' for i in range(n_pci)]
        gdpr_labels = [f'GDPR Art.{i+25}' for i in range(n_gdpr)]
        nis_labels = ['NIS2 A', 'NIS2 B', 'NIS2 C']
        y_labels = gdpr_labels + nis_labels
        
        control_labels = ['CU-001: IAM', 'CU-002: Encryption', 'CU-003: Logging',
                         'CU-004: Network Seg', 'CU-005: Incident Resp', 
                         'CU-006: Vulnerability', 'CU-007: Data Protection',
                         'CU-008: Access Control', 'CU-009: Monitoring',
                         'CU-010: Backup', 'CU-011: Training', 'CU-012: Audit', 'CU-013: Policy']
        
        ax.set_xticks(np.arange(n_pci))
        ax.set_yticks(np.arange(len(y_labels)))
        ax.set_xticklabels(pci_labels, rotation=45, ha='right')
        ax.set_yticklabels(y_labels[:len(data)])
        
        # Aggiungi etichette controlli sulla destra
        for i, label in enumerate(control_labels[:len(data)]):
            ax.text(n_pci + 0.5, i, label, fontsize=9, va='center')
        
        # Titolo e labels
        ax.set_title('Matrice MIN - Mappatura Controlli Unificati\n891 requisiti → 156 controlli',
                    fontsize=14, fontweight='bold', pad=20)
        ax.set_xlabel('PCI-DSS Requirements →', fontsize=11)
        ax.set_ylabel('← GDPR/NIS2 Requirements', fontsize=11)
        
        # Griglia
        ax.set_xticks(np.arange(n_pci+1)-0.5, minor=True)
        ax.set_yticks(np.arange(len(y_labels)+1)-0.5, minor=True)
        ax.grid(which='minor', color='gray', linestyle='-', linewidth=0.5)
        
        # Legenda
        legend_elements = [
            plt.Rectangle((0,0),1,1, facecolor='white', edgecolor='black', label='Nessuna correlazione'),
            plt.Rectangle((0,0),1,1, facecolor='#FFE6B3', edgecolor='black', label='Copertura parziale'),
            plt.Rectangle((0,0),1,1, facecolor='#4CAF50', edgecolor='black', label='Copertura completa')
        ]
        ax.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(1.15, 1))
        
        # Statistiche
        stats_text = """Statistiche:
• 891 requisiti totali
• 156 controlli unificati
• Riduzione: 82.5%
• Efficienza: 4.22 req/controllo
• Copertura: 95.3%"""
        
        ax.text(1.15, 0.5, stats_text, transform=ax.transAxes, fontsize=10,
               bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
        
        plt.tight_layout()
        return fig
    
    def create_gist_evolution(self):
        """GIST Score Evolution - Roadmap Visuale"""
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), height_ratios=[1, 1])
        
        # Dati temporali
        months = np.arange(0, 37, 1)
        
        # GIST Score evolution (sigmoide per crescita realistica)
        def sigmoid(x, L, k, x0):
            return L / (1 + np.exp(-k*(x-x0)))
        
        baseline = 40
        gist_scores = baseline + sigmoid(months, 45, 0.15, 18)
        
        # Aggiungi rumore realistico
        np.random.seed(42)
        noise = np.random.normal(0, 1, len(months))
        gist_scores = gist_scores + noise * 0.5
        
        # Plot 1: GIST Score Evolution
        ax1.plot(months, gist_scores, 'b-', linewidth=2, label='GIST Score')
        ax1.fill_between(months, baseline, gist_scores, alpha=0.3)
        
        # Milestones
        milestones = {
            6: ('Quick Wins', 50),
            12: ('Modernization', 58),
            18: ('Integration', 68),
            24: ('Optimization', 75),
            36: ('Target', 85)
        }
        
        for month, (label, score) in milestones.items():
            ax1.plot(month, gist_scores[month], 'ro', markersize=10)
            ax1.annotate(f'{label}\n{score} pts', 
                        xy=(month, gist_scores[month]),
                        xytext=(month, gist_scores[month] + 5),
                        ha='center', fontsize=9,
                        bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.7),
                        arrowprops=dict(arrowstyle='->', color='black'))
        
        # Target line
        ax1.axhline(y=85, color='green', linestyle='--', alpha=0.7, label='Target (85 pts)')
        ax1.axhline(y=baseline, color='red', linestyle='--', alpha=0.7, label='Baseline (40 pts)')
        
        ax1.set_ylabel('GIST Score', fontsize=12)
        ax1.set_title('GIST Score Evolution - 36 Month Roadmap', fontsize=14, fontweight='bold')
        ax1.grid(True, alpha=0.3)
        ax1.legend(loc='upper left')
        ax1.set_xlim(0, 36)
        ax1.set_ylim(35, 95)
        
        # Plot 2: Investment & ROI
        # Investimento cumulativo
        investment_monthly = np.array([0.5, 0.5, 0.4, 0.4, 0.3, 0.3,  # Phase 1
                                      0.4, 0.4, 0.3, 0.3, 0.3, 0.3,  # Phase 2
                                      0.2, 0.2, 0.2, 0.2, 0.2, 0.2,  # Phase 3
                                      0.1, 0.1, 0.1, 0.1, 0.1, 0.1,  # Phase 4
                                      0.05, 0.05, 0.05, 0.05, 0.05, 0.05,
                                      0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05])[:37]
        
        investment_cumulative = np.cumsum(investment_monthly)
        
        # ROI (inizia negativo, poi cresce)
        roi_monthly = np.zeros(37)
        for i in range(37):
            if i < 6:
                roi_monthly[i] = -investment_monthly[i]
            elif i < 12:
                roi_monthly[i] = -investment_monthly[i] + 0.1 * i/12
            elif i < 24:
                roi_monthly[i] = -investment_monthly[i] + 0.3 * (i-12)/12
            else:
                roi_monthly[i] = -investment_monthly[i] + 0.5 + 0.2 * (i-24)/12
        
        roi_cumulative = np.cumsum(roi_monthly)
        
        # Barre per investimento
        bars1 = ax2.bar(months, investment_monthly, color='red', alpha=0.6, label='Investment (Monthly)')
        
        # Linea per ROI cumulativo
        ax2_twin = ax2.twinx()
        line1 = ax2_twin.plot(months, roi_cumulative, 'g-', linewidth=2, label='ROI (Cumulative)')
        
        # Payback point
        payback_month = np.where(roi_cumulative > 0)[0]
        if len(payback_month) > 0:
            payback = payback_month[0]
            ax2_twin.plot(payback, roi_cumulative[payback], 'go', markersize=12)
            ax2_twin.annotate(f'Payback\nMonth {payback}',
                            xy=(payback, roi_cumulative[payback]),
                            xytext=(payback-5, roi_cumulative[payback]+1),
                            fontsize=10, fontweight='bold',
                            bbox=dict(boxstyle='round,pad=0.3', facecolor='lightgreen'),
                            arrowprops=dict(arrowstyle='->', color='green'))
        
        # ROI finale
        final_roi = roi_cumulative[-1]
        ax2_twin.text(35, final_roi, f'ROI: {final_roi:.1f}M€\n({final_roi/investment_cumulative[-1]*100:.0f}%)',
                     fontsize=10, fontweight='bold', ha='right',
                     bbox=dict(boxstyle='round,pad=0.3', facecolor='lightgreen'))
        
        ax2.set_xlabel('Months', fontsize=12)
        ax2.set_ylabel('Investment (M€)', fontsize=12, color='red')
        ax2_twin.set_ylabel('ROI (M€)', fontsize=12, color='green')
        ax2.set_title('Investment & Return on Investment Analysis', fontsize=14, fontweight='bold')
        ax2.grid(True, alpha=0.3)
        
        # Legenda combinata
        lines1, labels1 = ax2.get_legend_handles_labels()
        lines2, labels2 = ax2_twin.get_legend_handles_labels()
        ax2.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
        
        ax2.set_xlim(0, 36)
        
        # Fasi colorate di sfondo
        phases = [(0, 6, 'Phase 1:\nFoundation', 'lightblue'),
                 (6, 12, 'Phase 2:\nModernization', 'lightgreen'),
                 (12, 18, 'Phase 3:\nIntegration', 'lightyellow'),
                 (18, 36, 'Phase 4:\nOptimization', 'lightcoral')]
        
        for start, end, label, color in phases:
            ax2.axvspan(start, end, alpha=0.2, color=color)
            ax2.text((start+end)/2, ax2.get_ylim()[1]*0.9, label,
                    ha='center', fontsize=9, style='italic')
        
        plt.tight_layout()
        return fig
    
    def create_network_flow_diagram(self):
        """Diagramma di flusso della rete con Zero Trust"""
        fig, ax = plt.subplots(figsize=(14, 10))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.axis('off')
        
        # Titolo
        ax.text(5, 9.5, 'Zero Trust Network Architecture - GDO Implementation',
                fontsize=16, fontweight='bold', ha='center')
        
        # Zone di sicurezza
        zones = {
            'Internet': {'pos': (1, 7), 'color': '#FF6B6B', 'size': (1.5, 1.5)},
            'DMZ': {'pos': (3, 7), 'color': '#FFA500', 'size': (1.5, 1.5)},
            'Internal': {'pos': (5, 7), 'color': '#4ECDC4', 'size': (1.5, 1.5)},
            'Core': {'pos': (7, 7), 'color': '#45B7D1', 'size': (1.5, 1.5)},
            'PCI Zone': {'pos': (9, 7), 'color': '#96CEB4', 'size': (1.5, 1.5)}
        }
        
        for zone_name, props in zones.items():
            rect = FancyBboxPatch(
                (props['pos'][0] - props['size'][0]/2, props['pos'][1] - props['size'][1]/2),
                props['size'][0], props['size'][1],
                boxstyle="round,pad=0.05",
                facecolor=props['color'],
                alpha=0.3,
                edgecolor='black',
                linewidth=2
            )
            ax.add_patch(rect)
            ax.text(props['pos'][0], props['pos'][1], zone_name,
                   fontsize=11, fontweight='bold', ha='center')
        
        # Policy Enforcement Points
        peps = [
            (2, 5, 'PEP-1\nExternal'),
            (4, 5, 'PEP-2\nApplications'),
            (6, 5, 'PEP-3\nData'),
            (8, 5, 'PEP-4\nPayments')
        ]
        
        for x, y, label in peps:
            circle = Circle((x, y), 0.3, facecolor='yellow', 
                          edgecolor='black', linewidth=2)
            ax.add_patch(circle)
            ax.text(x, y-0.6, label, fontsize=9, ha='center')
        
        # Microsegmentazione
        segments = [
            (1, 3, 'POS\nDevices'),
            (3, 3, 'IoT\nSensors'),
            (5, 3, 'Employee\nWorkstations'),
            (7, 3, 'Servers\nApplications'),
            (9, 3, 'Payment\nSystems')
        ]
        
        for x, y, label in segments:
            rect = Rectangle((x-0.4, y-0.3), 0.8, 0.6,
                           facecolor='lightblue', edgecolor='blue')
            ax.add_patch(rect)
            ax.text(x, y, label, fontsize=8, ha='center', va='center')
        
        # Identity Provider centrale
        idp_circle = Circle((5, 1), 0.5, facecolor='purple', 
                          alpha=0.7, edgecolor='black', linewidth=2)
        ax.add_patch(idp_circle)
        ax.text(5, 1, 'Identity\nProvider', fontsize=10, 
               fontweight='bold', ha='center', va='center', color='white')
        
        # Frecce di verifica continua
        verification_points = [(1, 3), (3, 3), (5, 3), (7, 3), (9, 3)]
        for point in verification_points:
            arrow = FancyArrowPatch(point, (5, 1.5),
                                  connectionstyle="arc3,rad=0.3",
                                  arrowstyle='<->',
                                  mutation_scale=15,
                                  linewidth=1,
                                  color='purple',
                                  alpha=0.5)
            ax.add_patch(arrow)
        
        # Legenda
        legend_elements = [
            plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='yellow',
                      markersize=10, label='Policy Enforcement Point'),
            plt.Rectangle((0,0), 1, 1, facecolor='lightblue', 
                         edgecolor='blue', label='Microsegment'),
            plt.Line2D([0], [0], color='purple', linewidth=2, 
                      label='Continuous Verification')
        ]
        ax.legend(handles=legend_elements, loc='lower center', ncol=3)
        
        # Metriche in basso
        metrics_text = """Key Metrics:
• Lateral Movement: -89%
• Auth Latency: <50ms
• Policy Updates: Real-time
• Compliance: 100%"""
        
        ax.text(0.5, 0.2, metrics_text, fontsize=10,
               bbox=dict(boxstyle='round', facecolor='lightyellow'))
        
        plt.tight_layout()
        return fig
    
    def save_all_figures(self, output_dir='thesis_figures'):
        """Salva tutte le figure in alta risoluzione"""
        import os
        
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        figures = {
            'hybrid_cloud_architecture': self.create_hybrid_cloud_architecture(),
            'cost_comparison_table': self.create_cost_comparison_table(),
            'assa_dashboard': self.create_assa_dashboard(),
            'min_heatmap': self.create_min_heatmap(),
            'gist_evolution': self.create_gist_evolution(),
            'network_flow': self.create_network_flow_diagram()
        }
        
        for name, fig in figures.items():
            filepath = os.path.join(output_dir, f'{name}.png')
            fig.savefig(filepath, dpi=300, bbox_inches='tight')
            print(f"Salvato: {filepath}")
            
            # Salva anche in formato vettoriale per la stampa
            filepath_pdf = os.path.join(output_dir, f'{name}.pdf')
            fig.savefig(filepath_pdf, format='pdf', bbox_inches='tight')
            print(f"Salvato: {filepath_pdf}")
        
        return figures

# Esecuzione principale
if __name__ == "__main__":
    print("Generazione visualizzazioni per tesi GIST Framework...")
    print("=" * 60)
    
    # Crea istanza del generatore
    viz = GISTVisualizations()
    
    # Genera e salva tutte le figure
    figures = viz.save_all_figures()
    
    print("\n" + "=" * 60)
    print(f"✅ Generate {len(figures)} visualizzazioni con successo!")
    print("\nLe figure sono state salvate in:")
    print("  • Formato PNG (300 DPI) per inserimento nella tesi")
    print("  • Formato PDF (vettoriale) per stampa di alta qualità")
    print("\nRicorda di:")
    print("  1. Aggiungere caption dettagliate per ogni figura")
    print("  2. Riferire le figure nel testo principale")
    print("  3. Mantenere numerazione consistente (es. Figura 3.1, 3.2...)")
    print("  4. Verificare la leggibilità nella versione stampata")
    
    # Mostra preview delle figure (opzionale)
    show_preview = input("\nVuoi visualizzare un'anteprima delle figure? (s/n): ")
    if show_preview.lower() == 's':
        plt.show()
