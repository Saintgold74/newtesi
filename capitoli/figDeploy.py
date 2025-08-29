import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrow
import numpy as np

fig, ax = plt.subplots(figsize=(14, 10))

# Colori
colors = {
    'central': '#2E86AB',
    'regional': '#A23B72',
    'local': '#F18F01',
    'flow': '#C73E1D'
}

# Repository Centrale
central = FancyBboxPatch((6, 8), 2, 1.2, 
                         boxstyle="round,pad=0.1",
                         facecolor=colors['central'],
                         edgecolor='black', linewidth=2)
ax.add_patch(central)
ax.text(7, 8.6, 'Policy Repository\nCentrale (Git)', 
        ha='center', va='center', fontsize=11, fontweight='bold', color='white')

# Cache Regionali (3)
regions = [(2, 5), (7, 5), (12, 5)]
for i, (x, y) in enumerate(regions):
    regional = FancyBboxPatch((x-0.8, y-0.5), 1.6, 1, 
                              boxstyle="round,pad=0.05",
                              facecolor=colors['regional'],
                              edgecolor='black', linewidth=1.5)
    ax.add_patch(regional)
    ax.text(x, y, f'Cache\nRegionale {i+1}', 
            ha='center', va='center', fontsize=10, color='white')

# Punti Vendita (9 totali, 3 per regione)
stores = [(1, 2), (2, 2), (3, 2),  # Regione 1
          (6, 2), (7, 2), (8, 2),  # Regione 2
          (11, 2), (12, 2), (13, 2)]  # Regione 3

for i, (x, y) in enumerate(stores):
    store = Circle((x, y), 0.3, facecolor=colors['local'], 
                   edgecolor='black', linewidth=1)
    ax.add_patch(store)
    ax.text(x, y, f'PV\n{i+1}', ha='center', va='center', 
            fontsize=8, color='white')

# Frecce di propagazione
# Dal centrale alle regionali
for x, y in regions:
    arrow = FancyArrow(7, 7.8, x-7, y-7.8+0.5, 
                      width=0.05, head_width=0.15, 
                      color=colors['flow'], alpha=0.6)
    ax.add_patch(arrow)

# Dalle regionali ai punti vendita
for i, (rx, ry) in enumerate(regions):
    for j in range(3):
        sx = stores[i*3 + j][0]
        sy = stores[i*3 + j][1]
        arrow = FancyArrow(rx, ry-0.5, sx-rx, sy-ry+0.8,
                          width=0.03, head_width=0.1,
                          color=colors['flow'], alpha=0.4)
        ax.add_patch(arrow)

# Meccanismo di Failover (linee tratteggiate)
ax.plot([1, 3], [2.3, 2.3], 'k--', alpha=0.3, linewidth=1)
ax.plot([6, 8], [2.3, 2.3], 'k--', alpha=0.3, linewidth=1)
ax.plot([11, 13], [2.3, 2.3], 'k--', alpha=0.3, linewidth=1)

# Legenda
ax.text(7, 0.5, 'Flusso Normale', ha='center', fontsize=10)
ax.text(7, 0.2, 'Failover P2P', ha='center', fontsize=10, style='italic')

# Tempi di cache
ax.text(14, 8.5, 'TTL Cache:', fontsize=10, fontweight='bold')
ax.text(14, 8.2, 'Centrale: ∞', fontsize=9)
ax.text(14, 7.9, 'Regionale: 24h', fontsize=9)
ax.text(14, 7.6, 'Locale: 72h', fontsize=9)

# Configurazione assi
ax.set_xlim(0, 15)
ax.set_ylim(0, 10)
ax.axis('off')
ax.set_title('Architettura Distribuita del Policy Engine con Meccanismi di Resilienza', 
             fontsize=14, fontweight='bold', pad=20)

plt.tight_layout()
plt.savefig('fig_2_3_policy_architecture.pdf', dpi=300, bbox_inches='tight')
plt.show()