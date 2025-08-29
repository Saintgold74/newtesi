import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Rectangle
import matplotlib.patches as mpatches

fig, axes = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle('Dashboard KPI Framework GIST - Real-time Monitoring', fontsize=16)

# KPI 1: Availability Gauge
ax1 = axes[0, 0]
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)
availability = 99.96
angle = (availability - 99) * 180 / 1  # Scale 99-100%
wedge = mpatches.Wedge((5, 5), 4, 0, angle, fc='green', alpha=0.7)
ax1.add_patch(wedge)
ax1.text(5, 5, f'{availability}%', ha='center', va='center', fontsize=20)
ax1.set_title('Disponibilità Sistema')
ax1.axis('off')

# KPI 2: ASSA Reduction Bar
ax2 = axes[0, 1]
reduction = 42.7
target = 35
ax2.barh(['Target', 'Attuale'], [target, reduction], color=['orange', 'green'])
ax2.set_xlim(0, 50)
ax2.set_xlabel('Riduzione ASSA (%)')
ax2.set_title('Riduzione Superficie Attacco')

# KPI 3: TCO Trend
ax3 = axes[0, 2]
months = np.arange(0, 37, 6)
tco_baseline = 100 * np.ones(len(months))
tco_actual = 100 - (38.2/36) * months
ax3.plot(months, tco_baseline, 'r--', label='Baseline')
ax3.plot(months, tco_actual, 'g-', linewidth=2, label='Attuale')
ax3.fill_between(months, tco_baseline, tco_actual, alpha=0.3, color='green')
ax3.set_xlabel('Mesi')
ax3.set_ylabel('TCO Relativo (%)')
ax3.set_title('Evoluzione TCO')
ax3.legend()
ax3.grid(True, alpha=0.3)

# KPI 4: Latency Distribution
ax4 = axes[1, 0]
latencies = np.random.lognormal(3.1, 0.35, 1000)  # Mean ~23ms
ax4.hist(latencies, bins=30, density=True, alpha=0.7, color='blue')
ax4.axvline(50, color='red', linestyle='--', label='Soglia critica')
ax4.axvline(23, color='green', linestyle='-', label='Media')
ax4.set_xlabel('Latenza (ms)')
ax4.set_ylabel('Densità')
ax4.set_title('Distribuzione Latenza Zero Trust')
ax4.legend()

# KPI 5: Multi-cloud Distribution Pie
ax5 = axes[1, 1]
sizes = [35, 40, 25]
labels = ['AWS\n35%', 'Azure\n40%', 'GCP\n25%']
colors = ['#FF9900', '#0078D4', '#EA4335']
ax5.pie(sizes, labels=labels, colors=colors, autopct='', startangle=90)
ax5.set_title('Distribuzione Workload Multi-Cloud')

# KPI 6: Maturity Score
ax6 = axes[1, 2]
categories = ['Fisica', 'Rete', 'Cloud', 'Security', 'Compliance']
scores = [85, 72, 68, 61, 54]
colors_mat = ['green' if s >= 70 else 'orange' if s >= 50 else 'red' for s in scores]
bars = ax6.bar(categories, scores, color=colors_mat)
ax6.set_ylim(0, 100)
ax6.set_ylabel('Maturità (%)')
ax6.set_title('GIST Maturity Assessment')
ax6.axhline(70, color='gray', linestyle='--', alpha=0.5)
for bar, score in zip(bars, scores):
    ax6.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, 
             f'{score}%', ha='center', va='bottom')

plt.tight_layout()
plt.savefig('gist_dashboard.pdf', dpi=300)
plt.show()