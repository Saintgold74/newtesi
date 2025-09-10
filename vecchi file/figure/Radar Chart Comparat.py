# Codice Python per Radar Chart Comparativo dei Framework
import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Dati per il radar chart (scala 0-5)
frameworks = {
    'GIST': [5, 5, 5, 5, 5, 3, 4, 3, 1, 3, 5, 3],
    'COBIT': [1, 2, 1, 2, 3, 3, 2, 5, 5, 5, 2, 2],
    'TOGAF': [1, 2, 1, 1, 1, 1, 1, 5, 5, 5, 2, 1],
    'SABSA': [1, 1, 3, 1, 1, 3, 3, 4, 3, 3, 2, 2],
    'NIST CSF': [3, 3, 4, 3, 2, 4, 3, 4, 0, 4, 5, 3],
    'ISO 27001': [1, 2, 1, 1, 5, 3, 3, 5, 5, 5, 2, 3]
}

# Categorie
categories = ['Specificità\nGDO', 'Cloud\nNativo', 'Zero Trust\nIntegrato', 
             'Metriche\nQuantitative', 'Compliance\nAutomatizzata', 'ROI/TCO\nModeling',
             'Semplicità\nImplementazione', 'Maturità', 'Certificazione',
             'Tool Support', 'Costo\n(inverso)', 'Curva\nApprendimento\n(inverso)']

# Numero di variabili
N = len(categories)

# Angoli per ogni asse
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]

# Inizializza il plot
fig, axes = plt.subplots(2, 3, figsize=(15, 10), subplot_kw=dict(projection='polar'))
axes = axes.flatten()

# Colori per ogni framework
colors = ['#2ecc71', '#3498db', '#9b59b6', '#e74c3c', '#f39c12', '#95a5a6']

# Plot per ogni framework
for idx, (framework, values) in enumerate(frameworks.items()):
    ax = axes[idx]
    values += values[:1]  # Chiudi il poligono
    
    # Plot
    ax.plot(angles, values, 'o-', linewidth=2, color=colors[idx], label=framework)
    ax.fill(angles, values, alpha=0.25, color=colors[idx])
    
    # Etichette
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, size=8)
    ax.set_ylim(0, 5)
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_yticklabels(['1', '2', '3', '4', '5'], size=7)
    ax.set_title(framework, size=14, fontweight='bold', pad=20, color=colors[idx])
    ax.grid(True)

plt.suptitle('Analisi Comparativa Multidimensionale dei Framework', 
             fontsize=16, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('thesis_figures/cap5/framework_radar_comparison.pdf', 
            dpi=300, bbox_inches='tight')

# Codice per Heatmap di Complementarità
import seaborn as sns
import pandas as pd

# Matrice di complementarità (0-100%)
complementarity = {
    'GIST': [100, 75, 45, 65, 80, 85],
    'COBIT': [75, 100, 70, 55, 60, 65],
    'TOGAF': [45, 70, 100, 75, 40, 45],
    'SABSA': [65, 55, 75, 100, 50, 60],
    'NIST CSF': [80, 60, 40, 50, 100, 75],
    'ISO 27001': [85, 65, 45, 60, 75, 100]
}

df_comp = pd.DataFrame(complementarity, 
                       index=['GIST', 'COBIT', 'TOGAF', 'SABSA', 'NIST CSF', 'ISO 27001'])

fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(df_comp, annot=True, fmt='d', cmap='RdYlGn', 
            vmin=0, vmax=100, square=True, linewidths=1,
            cbar_kws={"shrink": 0.8, "label": "Complementarità (%)"})

ax.set_title('Matrice di Complementarità tra Framework\n(% di sinergia nell\'implementazione congiunta)', 
             fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Framework', fontsize=12)
ax.set_ylabel('Framework', fontsize=12)

# Aggiungi annotazioni per combinazioni ottimali
optimal_combos = [(0, 5), (0, 1), (0, 4)]  # GIST+ISO, GIST+COBIT, GIST+NIST
for (i, j) in optimal_combos:
    rect = plt.Rectangle((j, i), 1, 1, fill=False, edgecolor='blue', lw=3)
    ax.add_patch(rect)

plt.tight_layout()
plt.savefig('thesis_figures/cap5/framework_complementarity_matrix.pdf', 
            dpi=300, bbox_inches='tight')