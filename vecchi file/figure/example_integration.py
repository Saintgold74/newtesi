"""
Esempio di integrazione Claude Code + VS Code per generazione grafici tesi
"""
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.patches import Rectangle
import matplotlib.patches as mpatches

# Configurazione stile per tesi
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# Dati esempio: Metriche di sicurezza pre/post implementazione GIST
categories = ['Superficie\nAttacco', 'Tempo\nRilevamento', 'Costi\nCompliance', 'Disponibilità\nServizio']
pre_implementation = [100, 100, 100, 95.5]
post_implementation = [58, 35, 62, 99.95]

# Creazione figura
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Grafico 1: Confronto Pre/Post
x = np.arange(len(categories))
width = 0.35

bars1 = ax1.bar(x - width/2, pre_implementation, width, label='Pre-GIST', color='#ff6b6b', alpha=0.8)
bars2 = ax1.bar(x + width/2, post_implementation, width, label='Post-GIST', color='#4ecdc4', alpha=0.8)

ax1.set_ylabel('Valore (%)', fontsize=12, fontweight='bold')
ax1.set_title('Impatto Framework GIST - Metriche Chiave', fontsize=14, fontweight='bold')
ax1.set_xticks(x)
ax1.set_xticklabels(categories, fontsize=10)
ax1.legend(loc='upper right', fontsize=11)
ax1.grid(True, alpha=0.3)

# Aggiungi valori sopra le barre
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + 1,
                f'{height:.1f}%' if height < 100 else f'{height:.0f}%',
                ha='center', va='bottom', fontsize=9)

# Grafico 2: ROI Timeline
months = np.arange(0, 25)
investment = -2500000  # 2.5M€ investimento iniziale
monthly_savings = 150000  # 150k€ risparmi mensili
cumulative_roi = [investment + monthly_savings * m for m in months]
break_even = next((i for i, v in enumerate(cumulative_roi) if v > 0), None)

ax2.plot(months, cumulative_roi, linewidth=3, color='#5f27cd', label='ROI Cumulativo')
ax2.axhline(y=0, color='red', linestyle='--', alpha=0.5, label='Break-even')
if break_even:
    ax2.scatter(break_even, cumulative_roi[break_even], color='gold', s=200, zorder=5)
    ax2.annotate(f'Break-even\nMese {break_even}', 
                xy=(break_even, cumulative_roi[break_even]),
                xytext=(break_even-3, 500000),
                arrowprops=dict(arrowstyle='->', color='gold', lw=2),
                fontsize=10, fontweight='bold')

ax2.set_xlabel('Mesi', fontsize=12, fontweight='bold')
ax2.set_ylabel('ROI (€)', fontsize=12, fontweight='bold')
ax2.set_title('Proiezione ROI - 24 Mesi', fontsize=14, fontweight='bold')
ax2.grid(True, alpha=0.3)
ax2.legend(loc='lower right', fontsize=11)

# Formattazione asse Y per valori in milioni
ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x/1e6:.1f}M€'))

# Info box
info_text = "Generato con Claude Code + VS Code\nIntegrazione real-time per analisi tesi"
fig.text(0.5, 0.02, info_text, ha='center', fontsize=9, style='italic', 
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))

plt.tight_layout()

# Salva in formato PDF e PNG
output_path = 'C:/Users/saint/newtesi/figure/thesis_figures/cap5/'
plt.savefig(f'{output_path}example_integration.pdf', dpi=300, bbox_inches='tight')
plt.savefig(f'{output_path}example_integration.png', dpi=150, bbox_inches='tight')

print("Grafici generati con successo!")
print(f"Salvati in: {output_path}")
print("Formati: PDF (per LaTeX) e PNG (per preview)")