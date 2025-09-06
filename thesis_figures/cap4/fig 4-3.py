import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
import numpy as np

fig, ax = plt.subplots(figsize=(14, 10))

# Definizione nodi
nodes = {
    'root': (7, 9, 'Compromissione\nCatena del Freddo'),
    'phase1': (3, 7, 'Accesso Iniziale\n(Giorni 0-3)'),
    'phase2': (7, 7, 'Movimento Laterale\n(Giorni 4-11)'),
    'phase3': (11, 7, 'Escalation OT\n(Giorni 12-18)'),
    'phase4': (7, 5, 'Manipolazione SCADA\n(Giorni 19-21)'),
    'tech1': (1, 5, 'Spear Phishing\n12% successo'),
    'tech2': (5, 5, 'Credenziali\nCompromesse'),
    'tech3': (9, 5, 'Living off\nthe Land'),
    'tech4': (13, 5, 'Mancanza\nSegmentazione'),
    'impact': (7, 3, 'IMPATTO:\n3.7M€ danni\n2.39M€ sanzioni')
}

# Disegno nodi
for key, (x, y, text) in nodes.items():
    if key == 'root':
        color = 'red'
        style = 'round,pad=0.3'
    elif key == 'impact':
        color = 'darkred'
        style = 'round,pad=0.3'
    elif 'phase' in key:
        color = 'orange'
        style = 'round,pad=0.2'
    else:
        color = 'lightblue'
        style = 'round,pad=0.1'
    
    bbox = FancyBboxPatch((x-0.8, y-0.3), 1.6, 0.6,
                          boxstyle=style,
                          facecolor=color, 
                          edgecolor='black',
                          alpha=0.7)
    ax.add_patch(bbox)
    ax.text(x, y, text, ha='center', va='center', fontsize=9, weight='bold')

# Connessioni
connections = [
    ('root', 'phase1'), ('root', 'phase2'), ('root', 'phase3'),
    ('phase1', 'tech1'), ('phase1', 'tech2'),
    ('phase2', 'tech3'), ('phase3', 'tech4'),
    ('phase1', 'phase4'), ('phase2', 'phase4'), 
    ('phase3', 'phase4'), ('phase4', 'impact')
]

for start, end in connections:
    x1, y1, _ = nodes[start]
    x2, y2, _ = nodes[end]
    ax.arrow(x1, y1-0.3, x2-x1, y2-y1+0.6, 
             head_width=0.15, head_length=0.1, fc='black', ec='black', alpha=0.6)

ax.set_xlim(0, 14)
ax.set_ylim(2, 10)
ax.axis('off')
ax.set_title('Attack Tree: Compromissione Cyber-Fisica RetailCo', fontsize=14, weight='bold')
plt.tight_layout()
plt.savefig('attack_tree_retailco.pdf', dpi=300, bbox_inches='tight')
plt.show()