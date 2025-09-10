import matplotlib.pyplot as plt
import numpy as np
from matplotlib_venn import venn3
import seaborn as sns
from matplotlib.patches import Rectangle, FancyBboxPatch
import matplotlib.patches as mpatches

# Configurazione generale per grafici pubblicazione-ready
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.labelsize'] = 11
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['legend.fontsize'] = 9
plt.rcParams['figure.dpi'] = 300

# Palette colori coerente per tutta la tesi
colors = {
    'primary': '#1e3a8a',      # Blu scuro
    'secondary': '#3b82f6',    # Blu medio
    'tertiary': '#93c5fd',     # Blu chiaro
    'accent': '#f59e0b',       # Arancione
    'success': '#10b981',      # Verde
    'danger': '#ef4444',       # Rosso
    'neutral': '#6b7280'       # Grigio
}

# ===============================================
# Figura 1: Diagramma di Venn Sovrapposizioni Normative
# ===============================================

fig, ax = plt.subplots(figsize=(10, 8))

# Dati delle sovrapposizioni (dal testo)
# PCI-DSS: 389 requisiti
# GDPR: 344 controlli tecnici
# NIS2: 156 controlli tecnici
# Comuni a tutti: 128 controlli

# Creiamo il diagramma di Venn
v = venn3(subsets=(261, 216, 45, 28, 45, 66, 128), 
          set_labels=('PCI-DSS\n(389 req.)', 'GDPR\n(344 controlli)', 'NIS2\n(156 controlli)'),
          ax=ax)

# Colori personalizzati
v.get_patch_by_id('100').set_color(colors['primary'])
v.get_patch_by_id('100').set_alpha(0.7)
v.get_patch_by_id('010').set_color(colors['secondary'])
v.get_patch_by_id('010').set_alpha(0.7)
v.get_patch_by_id('001').set_color(colors['tertiary'])
v.get_patch_by_id('001').set_alpha(0.7)

# Evidenziamo l'area comune a tutti
v.get_patch_by_id('111').set_color(colors['accent'])
v.get_patch_by_id('111').set_alpha(0.9)

# Aggiungiamo annotazioni con percentuali
ax.annotate('14.4%\ncomuni a tutti', xy=(0, 0), xytext=(0, -1.5),
            ha='center', fontsize=11, fontweight='bold',
            bbox=dict(boxstyle="round,pad=0.3", facecolor=colors['accent'], alpha=0.7))

ax.annotate('43%\ncon sovrapposizioni', xy=(0, 1.8), xytext=(0, 1.8),
            ha='center', fontsize=12, fontweight='bold')

ax.set_title('Sovrapposizioni tra Framework Normativi nella GDO', fontsize=14, pad=20)
plt.tight_layout()
plt.savefig('figura_4_1_venn_normative.pdf', bbox_inches='tight')
plt.show()

# ===============================================
# Figura 2: ROI della Compliance Integrata
# ===============================================

fig, ax = plt.subplots(figsize=(12, 8))

# Dati per tre categorie di organizzazioni
mesi = np.arange(0, 37)  # 36 mesi (3 anni)

# Funzioni ROI basate sui dati del testo
def roi_grande(t):
    # Organizzazioni grandi: ROI più rapido
    return -100 + 180 * (1 - np.exp(-t/8))

def roi_media(t):
    # Organizzazioni medie: ROI moderato
    return -100 + 165 * (1 - np.exp(-t/10))

def roi_piccola(t):
    # Organizzazioni piccole: ROI più lento
    return -100 + 150 * (1 - np.exp(-t/12))

# Plot delle curve
ax.plot(mesi, [roi_grande(t) for t in mesi], 
        color=colors['primary'], linewidth=3, label='Grandi (>500 PdV)')
ax.plot(mesi, [roi_media(t) for t in mesi], 
        color=colors['secondary'], linewidth=3, label='Medie (50-500 PdV)')
ax.plot(mesi, [roi_piccola(t) for t in mesi], 
        color=colors['tertiary'], linewidth=3, label='Piccole (<50 PdV)')

# Linea di break-even
ax.axhline(y=0, color=colors['neutral'], linestyle='--', alpha=0.7, label='Break-even')

# Area di ROI positivo
ax.fill_between(mesi, 0, 300, where=([roi_media(t) for t in mesi] > np.zeros(len(mesi))), 
                alpha=0.1, color=colors['success'])

# Annotazioni per payback period
payback_grande = 7.2
payback_media = 9.5
payback_piccola = 11.8

ax.plot([payback_grande, payback_grande], [-100, 0], 
        color=colors['primary'], linestyle=':', alpha=0.7)
ax.plot([payback_media, payback_media], [-100, 0], 
        color=colors['secondary'], linestyle=':', alpha=0.7)
ax.plot([payback_piccola, payback_piccola], [-100, 0], 
        color=colors['tertiary'], linestyle=':', alpha=0.7)

# ROI target a 24 mesi (247% medio dal testo)
ax.plot([24, 24], [-100, 147], color=colors['accent'], linestyle='-', linewidth=2, alpha=0.8)
ax.annotate('ROI medio\n247% @ 24 mesi', xy=(24, 147), xytext=(26, 170),
            arrowprops=dict(arrowstyle='->', color=colors['accent']),
            bbox=dict(boxstyle="round,pad=0.3", facecolor='white', edgecolor=colors['accent']))

ax.set_xlabel('Mesi dall\'implementazione', fontsize=12)
ax.set_ylabel('Return on Investment (%)', fontsize=12)
ax.set_title('ROI della Compliance Integrata per Dimensione Organizzativa', fontsize=14, pad=20)
ax.grid(True, alpha=0.3)
ax.legend(loc='upper left', frameon=True, fancybox=True, shadow=True)
ax.set_xlim(0, 36)
ax.set_ylim(-120, 200)

plt.tight_layout()
plt.savefig('figura_4_2_roi_compliance.pdf', bbox_inches='tight')
plt.show()

# ===============================================
# Figura 3: Timeline Incidente Cyber-Fisico
# ===============================================

fig, ax = plt.subplots(figsize=(14, 8))

# Eventi e timeline
events = [
    ('Initial Compromise\nBMS Access', 0, 4, colors['danger']),
    ('Reconnaissance\nNetwork Mapping', 4, 28, colors['accent']),
    ('Lateral Movement\nOT Systems', 28, 52, colors['accent']),
    ('IT Penetration\nCorporate Network', 52, 72, colors['danger']),
    ('Detection\n& Response', 72, 76, colors['success']),
]

# Disegniamo la timeline
y_pos = 1
for i, (event, start, end, color) in enumerate(events):
    # Barra dell'evento
    ax.barh(y_pos, end - start, left=start, height=0.3, 
            color=color, alpha=0.8, edgecolor='black', linewidth=1)
    
    # Testo dell'evento
    ax.text((start + end) / 2, y_pos, event, 
            ha='center', va='center', fontsize=10, fontweight='bold')
    
    # Durata
    ax.text((start + end) / 2, y_pos - 0.25, f'{end - start}h', 
            ha='center', va='top', fontsize=9, style='italic')

# Milestone critici
milestones = [
    (0, 'Shodan Scan'),
    (4, 'Default Creds'),
    (28, 'VLAN Discovery'),
    (52, 'Jump Server Compromise'),
    (72, 'Temperature Alert'),
    (76, 'Ransomware Blocked')
]

for hour, desc in milestones:
    ax.plot([hour, hour], [0.5, 1.5], 'k--', alpha=0.5)
    ax.text(hour, 0.4, desc, ha='center', va='top', 
            fontsize=8, rotation=45, bbox=dict(boxstyle="round,pad=0.2", 
                                              facecolor='white', alpha=0.8))

# Indicatori di giorni
for day in range(4):
    ax.axvspan(day*24, (day+1)*24, alpha=0.1, color=colors['neutral'])
    ax.text(day*24 + 12, 1.7, f'Giorno {day}', ha='center', fontsize=10)

ax.set_xlim(-2, 78)
ax.set_ylim(0, 2)
ax.set_xlabel('Ore dall\'inizio dell\'attacco', fontsize=12)
ax.set_title('Timeline dell\'Incidente Cyber-Fisico: Dal Compromise alla Detection', 
             fontsize=14, pad=20)
ax.set_yticks([])
ax.grid(True, axis='x', alpha=0.3)

# Legenda
danger_patch = mpatches.Patch(color=colors['danger'], label='Fase critica')
accent_patch = mpatches.Patch(color=colors['accent'], label='Espansione')
success_patch = mpatches.Patch(color=colors['success'], label='Rilevamento')
ax.legend(handles=[danger_patch, accent_patch, success_patch], 
          loc='upper right', frameon=True)

plt.tight_layout()
plt.savefig('figura_4_3_timeline_incidente.pdf', bbox_inches='tight')
plt.show()

# ===============================================
# Figura 4: Confronto Costi Compliance
# ===============================================

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Grafico 1: Breakdown dei costi
categories = ['Tecnologia', 'Personale', 'Consulenza', 'Audit', 'Training']
frammentato = [234, 456, 189, 123, 78]  # in migliaia di euro
integrato = [156, 267, 89, 67, 45]

x = np.arange(len(categories))
width = 0.35

bars1 = ax1.bar(x - width/2, frammentato, width, label='Approccio Frammentato', 
                 color=colors['danger'], alpha=0.8)
bars2 = ax1.bar(x + width/2, integrato, width, label='Approccio Integrato', 
                 color=colors['success'], alpha=0.8)

# Aggiungiamo i valori sopra le barre
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax1.annotate(f'€{height}K',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=8)

ax1.set_xlabel('Categoria di Costo', fontsize=11)
ax1.set_ylabel('Costo Annuale (€ migliaia)', fontsize=11)
ax1.set_title('Confronto Costi per Categoria', fontsize=12)
ax1.set_xticks(x)
ax1.set_xticklabels(categories, rotation=15, ha='right')
ax1.legend()
ax1.grid(True, axis='y', alpha=0.3)

# Grafico 2: Saving percentuale per fonte
saving_sources = ['Eliminazione\nDuplicazioni', 'Automazione\nProcessi', 
                  'Economia\ndi Scala', 'Riduzione\nErrori']
saving_perc = [42, 31, 19, 8]
colors_pie = [colors['primary'], colors['secondary'], colors['tertiary'], colors['accent']]

wedges, texts, autotexts = ax2.pie(saving_perc, labels=saving_sources, colors=colors_pie,
                                    autopct='%1.0f%%', startangle=90)

# Miglioriamo l'aspetto del pie chart
for text in texts:
    text.set_fontsize(10)
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')
    autotext.set_fontsize(11)

ax2.set_title('Fonti di Risparmio nell\'Approccio Integrato', fontsize=12)

# Aggiungiamo il risparmio totale
total_frammentato = sum(frammentato)
total_integrato = sum(integrato)
saving_totale = ((total_frammentato - total_integrato) / total_frammentato) * 100

fig.suptitle(f'Analisi Economica della Compliance: Risparmio Totale {saving_totale:.1f}%', 
             fontsize=14, y=1.02)

plt.tight_layout()
plt.savefig('figura_4_4_confronto_costi.pdf', bbox_inches='tight')
plt.show()

# ===============================================
# Figura 5: Modello di Maturità della Compliance
# ===============================================

fig, ax = plt.subplots(figsize=(12, 8))

# Dati del modello di maturità
levels = ['Livello 1\nIniziale', 'Livello 2\nGestito', 'Livello 3\nDefinito', 
          'Livello 4\nQuantificato', 'Livello 5\nOttimizzato']
percentages = [0, 47, 33, 13, 7]  # Distribuzione delle organizzazioni

# Caratteristiche per livello (per il colore)
colors_maturity = [colors['danger'], colors['accent'], colors['neutral'], 
                   colors['secondary'], colors['success']]

# Creiamo un grafico a scala
y_positions = np.arange(len(levels))
for i, (level, pct, color) in enumerate(zip(levels, percentages, colors_maturity)):
    # Barra orizzontale per ogni livello
    ax.barh(i, 100, height=0.8, color=color, alpha=0.3, edgecolor='black')
    
    # Percentuale di organizzazioni
    if pct > 0:
        ax.barh(i, pct, height=0.8, color=color, alpha=0.8, edgecolor='black', linewidth=2)
        ax.text(pct + 2, i, f'{pct}%', va='center', fontweight='bold', fontsize=11)
    
    # Nome del livello
    ax.text(-2, i, level, ha='right', va='center', fontsize=11, fontweight='bold')

# Descrizioni dei livelli
descriptions = [
    'Approccio reattivo, silos',
    'Processi strutturati ma frammentati',
    'Integrazione iniziale, controlli comuni',
    'Metriche e automazione avanzate',
    'Compliance come vantaggio competitivo'
]

for i, desc in enumerate(descriptions):
    ax.text(102, i, desc, ha='left', va='center', fontsize=9, style='italic')

# Indicatori di benefici
benefit_positions = [0, 20, 40, 60, 80]
benefit_labels = ['Baseline', '-20% costi', '-40% effort', 'ROI positivo', 'Innovazione']
for pos, label in zip(benefit_positions, benefit_labels):
    ax.axvline(x=pos, color='gray', linestyle=':', alpha=0.5)
    ax.text(pos, -0.7, label, ha='center', va='top', fontsize=8, rotation=0)

ax.set_xlim(-20, 180)
ax.set_ylim(-1, len(levels))
ax.set_xlabel('Progression →', fontsize=12)
ax.set_title('Modello di Maturità della Compliance Integrata: Distribuzione delle Organizzazioni GDO', 
             fontsize=14, pad=20)
ax.set_yticks([])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

plt.tight_layout()
plt.savefig('figura_4_5_modello_maturita.pdf', bbox_inches='tight')
plt.show()

print("Tutti i grafici sono stati generati con successo!")
print("File salvati:")
print("- figura_4_1_venn_normative.pdf")
print("- figura_4_2_roi_compliance.pdf") 
print("- figura_4_3_timeline_incidente.pdf")
print("- figura_4_4_confronto_costi.pdf")
print("- figura_4_5_modello_maturita.pdf")