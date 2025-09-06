import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Creazione della figura
fig, ax = plt.subplots(figsize=(12, 12))
ax.set_aspect('equal')
ax.axis('off')

# --- Elementi del Diagramma ---

# 1. Scudo di Resilienza (cerchio esterno)
shield = patches.Circle((0.5, 0.5), 0.45, facecolor='#EBF5FB', edgecolor='#85C1E9', linewidth=2, linestyle='--')
ax.add_patch(shield)
ax.text(0.5, 0.98, 'Cyber-Resilience Shield', ha='center', va='center', fontsize=18, color='#34495E', weight='bold')

# 2. Nodo Centrale: GIST Framework
center_node = patches.Circle((0.5, 0.5), 0.15, facecolor='#1ABC9C', edgecolor='white', linewidth=3)
ax.add_patch(center_node)
ax.text(0.5, 0.5, 'GIST\nFramework', ha='center', va='center', fontsize=16, color='white', weight='bold')

# 3. Nodi dell'Ecosistema (disposti in cerchio)
ecosystem_nodes = {
    'Smart Retail': {'pos': (0.5, 0.8), 'color': '#3498DB'},
    'Resilient Supply Chain': {'pos': (0.2, 0.35), 'color': '#9B59B6'},
    'Personalized Experience': {'pos': (0.8, 0.35), 'color': '#E67E22'}
}

for name, attrs in ecosystem_nodes.items():
    node = patches.FancyBboxPatch((attrs['pos'][0]-0.1, attrs['pos'][1]-0.06), 0.2, 0.12,
                                  boxstyle="round,pad=0.02", fc=attrs['color'], ec='white', lw=2)
    ax.add_patch(node)
    ax.text(attrs['pos'][0], attrs['pos'][1], name.replace(' ', '\n'),
            ha='center', va='center', fontsize=11, color='white', weight='bold')
    
    # Connessioni dal centro ai nodi
    arrow = patches.FancyArrowPatch((0.5, 0.5), attrs['pos'],
                                    connectionstyle="arc3,rad=0.1",
                                    color='#17202A', lw=1.5, arrowstyle='->,head_length=8,head_width=5')
    ax.add_patch(arrow)

# 4. Elementi Esterni (Minacce e Normative)
external_nodes = {
    'Evolving Threats\n(AI-driven, APT)': {'pos': (0.1, 0.9), 'color': '#E74C3C'},
    'Dynamic Regulations\n(AI Act, CRA)': {'pos': (0.9, 0.9), 'color': '#E74C3C'}
}

for name, attrs in external_nodes.items():
    ax.text(attrs['pos'][0], attrs['pos'][1], name, ha='center', va='center', fontsize=12,
            bbox=dict(boxstyle="round,pad=0.4", fc=attrs['color'], ec='white', lw=2, alpha=0.9),
            color='white', weight='bold')
    
    # Frecce delle minacce verso lo scudo
    arrow_in = patches.FancyArrowPatch(attrs['pos'], (attrs['pos'][0]*0.4 + 0.3, attrs['pos'][1]*0.4 + 0.3), # Punta verso il bordo dello scudo
                                     connectionstyle="arc3,rad=-0.2",
                                     color='#C0392B', lw=3, arrowstyle='->,head_length=10,head_width=7')
    ax.add_patch(arrow_in)


# Titolo
plt.suptitle('Figura 5.4: Vision 2030 - Ecosistema GDO Cyber-Resiliente', fontsize=20, y=0.95, weight='bold')

# Salvataggio
output_filename = 'figura_5_4_vision_2030_matplotlib.png'
plt.savefig(output_filename, dpi=300, bbox_inches='tight')

print(f"Diagramma salvato come: {output_filename}")