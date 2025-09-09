import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Rectangle, FancyArrowPatch

fig, ax = plt.subplots(figsize=(12, 8))
ax.set_xlim(0, 12)
ax.set_ylim(0, 8)
ax.axis('off')

# Stile minimalista
def draw_box(x, y, w, h, text, color='lightblue'):
    rect = Rectangle((x, y), w, h, 
                     facecolor=color, 
                     edgecolor='black', 
                     linewidth=2)
    ax.add_patch(rect)
    ax.text(x + w/2, y + h/2, text, 
           ha='center', va='center', 
           fontsize=11, fontweight='bold')

# Boxes
draw_box(1, 6, 2.5, 1.5, 'FONTI\nITALIANE', '#FFE5B4')
draw_box(5, 6, 2.5, 1.5, 'DIGITAL\nTWIN', '#B4E7CE')
draw_box(9, 6, 2.5, 1.5, 'DATASET\n400K+', '#FFB4B4')

draw_box(1, 3.5, 2.5, 1.5, 'PARAMETRI\nCALIBRATI', '#E5D4FF')
draw_box(5, 3.5, 2.5, 1.5, 'MONTE\nCARLO', '#FFE5CC')
draw_box(9, 3.5, 2.5, 1.5, 'VALIDAZIONE\n83.3%', '#D4E5FF')

draw_box(1, 1, 2.5, 1.5, 'MODELLI\nTEORICI', '#FFDAB9')
draw_box(5, 1, 2.5, 1.5, 'SIMULAZIONE\nATTACCHI', '#E6E6FA')
draw_box(9, 1, 2.5, 1.5, 'RISULTATI\nZT-GDO', '#98FB98')

# Frecce orizzontali
for y in [6.75, 4.25, 1.75]:
    ax.arrow(3.5, y, 1.3, 0, head_width=0.2, head_length=0.1, fc='black', ec='black')
    ax.arrow(7.5, y, 1.3, 0, head_width=0.2, head_length=0.1, fc='black', ec='black')

# Frecce verticali
for x in [2.25, 6.25, 10.25]:
    ax.arrow(x, 5.5, 0, -0.4, head_width=0.15, head_length=0.08, fc='gray', ec='gray')
    ax.arrow(x, 3, 0, -0.4, head_width=0.15, head_length=0.08, fc='gray', ec='gray')

plt.title('Flusso di Validazione Digital Twin GDO', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('digital_twin_flow.pdf', dpi=300, bbox_inches='tight')
plt.show()