import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
import matplotlib.patches as mpatches

# Dati
anni = np.array([2020, 2021, 2022, 2023, 2024, 2025])
incidenti = np.array([234, 412, 798, 1289, 1698, 2134])  # Proiezione 2025
impatto_medio = np.array([0.8, 1.2, 1.9, 2.4, 2.9, 3.4])  # Milioni di euro

# Creazione figura
fig, ax1 = plt.subplots(figsize=(12, 7))

# Asse primario - Numero incidenti
color = 'tab:blue'
ax1.set_xlabel('Anno', fontsize=12)
ax1.set_ylabel('Numero di Incidenti', color=color, fontsize=12)

# Smooth curve per incidenti
x_smooth = np.linspace(anni.min(), 2024.5, 300)
y_smooth = make_interp_spline(anni[:5], incidenti[:5], k=3)(x_smooth[:250])
ax1.plot(x_smooth[:250], y_smooth, color=color, linewidth=2.5, label='Incidenti Osservati')

# Proiezione 2025 (linea tratteggiata)
x_proj = np.linspace(2024.5, 2025, 50)
y_proj = incidenti[4] + (incidenti[5] - incidenti[4]) * (x_proj - 2024.5) / 0.5
ax1.plot(x_proj, y_proj, '--', color=color, linewidth=2.5, alpha=0.7, label='Proiezione 2025')

ax1.tick_params(axis='y', labelcolor=color)
ax1.grid(True, alpha=0.3)

# Asse secondario - Impatto economico
ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Impatto Economico Medio (M€)', color=color, fontsize=12)
ax2.bar(anni[:-1], impatto_medio[:-1], alpha=0.3, color=color, width=0.6)
ax2.bar(anni[-1], impatto_medio[-1], alpha=0.2, color=color, width=0.6, 
        edgecolor='red', linewidth=2, linestyle='--')
ax2.tick_params(axis='y', labelcolor=color)

# Annotazione incremento 312%
ax1.annotate('', xy=(2023, 1289), xytext=(2021, 412),
            arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))
ax1.text(2022, 850, '+312%', fontsize=14, fontweight='bold', ha='center')

# Titolo e legenda
plt.title('Evoluzione degli Attacchi Cyber nel Settore GDO (2020-2025)', fontsize=14, fontweight='bold')
fig.tight_layout()
ax1.legend(loc='upper left')

plt.savefig('fig_2_1_cyber_evolution.pdf', dpi=300, bbox_inches='tight')
plt.show()