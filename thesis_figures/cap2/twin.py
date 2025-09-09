import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.patches as mpatches

# Configurazione figura
fig, ax = plt.subplots(1, 1, figsize=(14, 10))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')

# Colori
col_input = '#E8F4FD'
col_twin = '#B8E0D2'
col_output = '#FFDDC1'
col_validation = '#F8B4B4'

# TITOLO
ax.text(7, 9.5, 'Architettura Digital Twin GDO', fontsize=18, fontweight='bold', ha='center')

# SEZIONE 1: PARAMETRI DI INPUT (sinistra)
input_box = FancyBboxPatch((0.5, 5), 3, 3.5, 
                           boxstyle="round,pad=0.1", 
                           facecolor=col_input, 
                           edgecolor='navy', linewidth=2)
ax.add_patch(input_box)
ax.text(2, 8, 'PARAMETRI REALI', fontsize=11, fontweight='bold', ha='center')
ax.text(2, 7.5, '• ISTAT 2023', fontsize=9, ha='center')
ax.text(2, 7.1, '• Banca d\'Italia 2023', fontsize=9, ha='center')
ax.text(2, 6.7, '• ENISA Threat 2023', fontsize=9, ha='center')
ax.text(2, 6.3, '• Federdistribuzione', fontsize=9, ha='center')
ax.text(2, 5.9, '• Gartner Benchmarks', fontsize=9, ha='center')
ax.text(2, 5.5, '• Kaspersky Reports', fontsize=9, ha='center')

# SEZIONE 2: DIGITAL TWIN ENGINE (centro)
twin_box = FancyBboxPatch((4.5, 3), 5, 5, 
                          boxstyle="round,pad=0.1", 
                          facecolor=col_twin, 
                          edgecolor='darkgreen', linewidth=3)
ax.add_patch(twin_box)
ax.text(7, 7.5, 'DIGITAL TWIN ENGINE', fontsize=13, fontweight='bold', ha='center')

# Componenti interni
comp1 = FancyBboxPatch((5, 6.3), 1.8, 0.8, 
                       boxstyle="round,pad=0.05", 
                       facecolor='white', edgecolor='gray')
ax.add_patch(comp1)
ax.text(5.9, 6.7, 'Transaction', fontsize=9, ha='center')
ax.text(5.9, 6.5, 'Generator', fontsize=9, ha='center')

comp2 = FancyBboxPatch((7.2, 6.3), 1.8, 0.8, 
                       boxstyle="round,pad=0.05", 
                       facecolor='white', edgecolor='gray')
ax.add_patch(comp2)
ax.text(8.1, 6.7, 'Security Event', fontsize=9, ha='center')
ax.text(8.1, 6.5, 'Simulator', fontsize=9, ha='center')

comp3 = FancyBboxPatch((5, 5.2), 1.8, 0.8, 
                       boxstyle="round,pad=0.05", 
                       facecolor='white', edgecolor='gray')
ax.add_patch(comp3)
ax.text(5.9, 5.6, 'Network', fontsize=9, ha='center')
ax.text(5.9, 5.4, 'Topology', fontsize=9, ha='center')

comp4 = FancyBboxPatch((7.2, 5.2), 1.8, 0.8, 
                       boxstyle="round,pad=0.05", 
                       facecolor='white', edgecolor='gray')
ax.add_patch(comp4)
ax.text(8.1, 5.6, 'Attack', fontsize=9, ha='center')
ax.text(8.1, 5.4, 'Propagation', fontsize=9, ha='center')

comp5 = FancyBboxPatch((6.1, 4.1), 1.8, 0.8, 
                       boxstyle="round,pad=0.05", 
                       facecolor='yellow', edgecolor='orange', alpha=0.3)
ax.add_patch(comp5)
ax.text(7, 4.5, 'Monte Carlo', fontsize=9, ha='center', fontweight='bold')
ax.text(7, 4.3, 'Engine', fontsize=9, ha='center')

# Parametri generati
ax.text(7, 3.8, '5 stores × 30 giorni', fontsize=8, ha='center', style='italic')
ax.text(7, 3.5, '215.458 transazioni', fontsize=8, ha='center', style='italic')
ax.text(7, 3.2, '187.500 eventi security', fontsize=8, ha='center', style='italic')

# SEZIONE 3: OUTPUT (destra superiore)
output_box = FancyBboxPatch((10.5, 5.5), 3, 2.5, 
                            boxstyle="round,pad=0.1", 
                            facecolor=col_output, 
                            edgecolor='darkorange', linewidth=2)
ax.add_patch(output_box)
ax.text(12, 7.7, 'DATASET OUTPUT', fontsize=11, fontweight='bold', ha='center')
ax.text(12, 7.2, '• Transactions.csv', fontsize=9, ha='center')
ax.text(12, 6.8, '  90.2 MB', fontsize=8, ha='center', style='italic')
ax.text(12, 6.4, '• Security_events.csv', fontsize=9, ha='center')
ax.text(12, 6.0, '  213.4 MB', fontsize=8, ha='center', style='italic')

# SEZIONE 4: VALIDAZIONE (destra inferiore)
valid_box = FancyBboxPatch((10.5, 2), 3, 2.5, 
                           boxstyle="round,pad=0.1", 
                           facecolor=col_validation, 
                           edgecolor='darkred', linewidth=2)
ax.add_patch(valid_box)
ax.text(12, 4.2, 'VALIDAZIONE', fontsize=11, fontweight='bold', ha='center')
ax.text(12, 3.7, '✓ Benford Test', fontsize=9, ha='center')
ax.text(12, 3.3, '✓ Temporal Pattern', fontsize=9, ha='center')
ax.text(12, 2.9, '✓ Autocorrelation', fontsize=9, ha='center')
ax.text(12, 2.5, 'Success: 83.3%', fontsize=10, ha='center', fontweight='bold', color='darkgreen')

# FRECCE
# Input -> Twin
arrow1 = FancyArrowPatch((3.5, 6.5), (4.5, 6.5),
                        connectionstyle="arc3", 
                        arrowstyle='->', 
                        mutation_scale=20, 
                        linewidth=2, color='navy')
ax.add_patch(arrow1)

# Twin -> Output
arrow2 = FancyArrowPatch((9.5, 6.8), (10.5, 6.8),
                        connectionstyle="arc3", 
                        arrowstyle='->', 
                        mutation_scale=20, 
                        linewidth=2, color='darkorange')
ax.add_patch(arrow2)

# Twin -> Validation
arrow3 = FancyArrowPatch((9.5, 4.5), (10.5, 3.5),
                        connectionstyle="arc3,rad=0.3", 
                        arrowstyle='->', 
                        mutation_scale=20, 
                        linewidth=2, color='darkred')
ax.add_patch(arrow3)

# Feedback loop (Validation -> Twin)
arrow4 = FancyArrowPatch((10.5, 2.5), (7, 3),
                        connectionstyle="arc3,rad=-0.3", 
                        arrowstyle='->', 
                        mutation_scale=15, 
                        linewidth=1.5, 
                        linestyle='--', 
                        color='gray')
ax.add_patch(arrow4)
ax.text(8.5, 1.8, 'feedback loop', fontsize=8, style='italic', color='gray')

# METRICHE CHIAVE (in basso)
metrics_box = FancyBboxPatch((2, 0.2), 10, 1.2, 
                             boxstyle="round,pad=0.05", 
                             facecolor='#F0F0F0', 
                             edgecolor='black', 
                             linewidth=1, 
                             linestyle='--')
ax.add_patch(metrics_box)
ax.text(7, 1.0, 'METRICHE CHIAVE', fontsize=10, fontweight='bold', ha='center')
ax.text(3.5, 0.5, '400K+ record', fontsize=9, ha='center')
ax.text(7, 0.5, '10K simulazioni Monte Carlo', fontsize=9, ha='center')
ax.text(10.5, 0.5, 'Fattore scala: 910x', fontsize=9, ha='center')

plt.title('Digital Twin GDO - Framework di Validazione', fontsize=16, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig('digital_twin_architecture.pdf', dpi=300, bbox_inches='tight')
plt.show()