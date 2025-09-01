# %==========================================================================
# % CODICE PYTHON PER GENERAZIONE GRAFICI SUGGERITI
# %==========================================================================
# % Nota per l'implementazione: Di seguito il codice Python per generare
# % i grafici e le visualizzazioni suggerite

# %\begin{comment}
# Codice Python per Figura 5.2 - Diagramma Effetti Sinergici
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.patches as mpatches

fig, ax = plt.subplots(1, 1, figsize=(12, 8))

# Posizioni delle componenti
components = {
    'Physical': (2, 6),
    'Architectural': (6, 6), 
    'Security': (2, 2),
    'Compliance': (6, 2)
}

# Disegna le componenti
for name, (x, y) in components.items():
    box = FancyBboxPatch((x-0.8, y-0.4), 1.6, 0.8,
                         boxstyle="round,pad=0.1",
                         facecolor='lightblue',
                         edgecolor='darkblue',
                         linewidth=2)
    ax.add_patch(box)
    ax.text(x, y, name, ha='center', va='center', fontsize=11, fontweight='bold')

# Aggiungi frecce con percentuali di amplificazione
synergies = [
    (components['Physical'], components['Architectural'], '+27%'),
    (components['Architectural'], components['Security'], '+34%'),
    (components['Security'], components['Compliance'], '+41%'),
    (components['Physical'], components['Security'], '+18%'),
    (components['Architectural'], components['Compliance'], '+22%'),
    (components['Physical'], components['Compliance'], '+15%')
]

for (start, end, label) in synergies:
    arrow = FancyArrowPatch(start, end,
                           connectionstyle="arc3,rad=0.3",
                           arrowstyle='<->',
                           mutation_scale=20,
                           color='green',
                           linewidth=1.5)
    ax.add_patch(arrow)
    
    # Calcola posizione etichetta
    mid_x = (start[0] + end[0]) / 2
    mid_y = (start[1] + end[1]) / 2
    ax.text(mid_x, mid_y, label, ha='center', va='center',
           bbox=dict(boxstyle="round,pad=0.3", facecolor='white', edgecolor='green'),
           fontsize=9)

# Aggiungi box centrale per effetto totale
center_box = FancyBboxPatch((3.2, 3.8), 1.6, 0.6,
                           boxstyle="round,pad=0.1",
                           facecolor='gold',
                           edgecolor='darkorange',
                           linewidth=2)
ax.add_patch(center_box)
ax.text(4, 4.1, 'Sistema Totale\n+52%', ha='center', va='center',
       fontsize=10, fontweight='bold')

ax.set_xlim(0, 8)
ax.set_ylim(0, 8)
ax.axis('off')
ax.set_title('Effetti Sinergici tra Componenti GIST', fontsize=14, fontweight='bold')

plt.tight_layout()
plt.savefig('thesis_figures/cap5/fig_5_2_synergies.pdf', dpi=300, bbox_inches='tight')

# Codice Python per Innovation Box - Heatmap Correlazioni
import seaborn as sns
import pandas as pd

# Dati di correlazione tra componenti
correlation_data = np.array([
    [1.00, 0.27, 0.18, 0.15],
    [0.27, 1.00, 0.34, 0.22],
    [0.18, 0.34, 1.00, 0.41],
    [0.15, 0.22, 0.41, 1.00]
])

components = ['Physical', 'Architectural', 'Security', 'Compliance']
df_corr = pd.DataFrame(correlation_data, index=components, columns=components)

fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(df_corr, annot=True, fmt='.2f', cmap='YlOrRd',
           vmin=0, vmax=1, square=True, linewidths=1,
           cbar_kws={"shrink": 0.8})
ax.set_title('Matrice di Amplificazione Sinergica GIST', fontsize=12, fontweight='bold')
plt.tight_layout()
plt.savefig('thesis_figures/cap5/innovation_box_heatmap.pdf', dpi=300)
# %\end{comment}