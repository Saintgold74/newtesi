import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mticker

# Dati estratti dalla sua tabella
anni = ['2019', '2020', '2021', '2022', '2023', '2024', '2025*', '2026*']
data_breach = np.array([55, 50, 42, 35, 28, 23, 20, 17])
disruption = np.array([20, 23, 28, 32, 35, 37, 38, 39])
cyber_fisici = np.array([25, 27, 30, 33, 37, 40, 42, 44])

# Colori e stili migliorati
colors = {
    'Data Breach': '#2980B9',     # Blu leggermente più scuro
    'Disruption': '#E74C3C',      # Rosso vivace
    'Cyber-Fisici': '#27AE60'     # Verde più deciso
}
markers = {'Data Breach': 'o', 'Disruption': 's', 'Cyber-Fisici': '^'}
linestyles = {'Data Breach': '-', 'Disruption': '--', 'Cyber-Fisici': '-.'}

# Creazione del grafico
fig, ax = plt.subplots(figsize=(14, 8)) # Aumentiamo leggermente le dimensioni

# Disegna una linea per ogni categoria
lines = []
for label, data in zip(['Data Breach', 'Disruption', 'Cyber-Fisici'], [data_breach, disruption, cyber_fisici]):
    line, = ax.plot(anni, data, color=colors[label], marker=markers[label], 
                    linestyle=linestyles[label], linewidth=3, markersize=8, label=label)
    lines.append(line)
    
    # Aggiungi etichette dirette per i valori iniziali e finali
    ax.text(anni[0], data[0] + (2 if label=='Data Breach' else -3 if label=='Cyber-Fisici' else 0), 
            f'{data[0]}%', color=colors[label], ha='center', va='bottom' if label=='Data Breach' else 'top', 
            fontsize=10, weight='bold')
    ax.text(anni[-1], data[-1] + (2 if label=='Cyber-Fisici' else -3 if label=='Data Breach' else 0), 
            f'{data[-1]}%', color=colors[label], ha='center', va='bottom' if label=='Cyber-Fisici' else 'top', 
            fontsize=10, weight='bold')


# Abbellimenti e personalizzazioni
ax.set_title('Evoluzione e Confronto dei Trend per Tipologia di Attacco nel Settore GDO', 
             fontsize=18, weight='bold', pad=25)
ax.set_ylabel('Percentuale sul Totale Incidenti (%)', fontsize=13, labelpad=10)
ax.set_xlabel('Anno', fontsize=13, labelpad=10)
ax.legend(loc='center left', bbox_to_anchor=(0.8,0.1), fontsize=12, frameon=True, facecolor='white', framealpha=0.9,
          title="Legenda Tipologia Attacco")
ax.grid(axis='y', linestyle='--', alpha=0.6)
ax.set_ylim(0, 65) # Regola il limite superiore per ospitare le etichette
ax.margins(x=0.03)

# Formatta l'asse Y per mostrare il simbolo %
ax.yaxis.set_major_formatter(mticker.PercentFormatter())
ax.tick_params(axis='both', which='major', labelsize=11)

# Aggiunge una linea verticale per separare i dati reali dalle proiezioni
projection_x_pos = 5.5
plt.axvline(x=projection_x_pos, color='grey', linestyle=':', linewidth=1.8, zorder=0)
ax.text(projection_x_pos + 0.1, ax.get_ylim()[1]*0.95, 'Proiezioni', 
        fontsize=12, rotation=90, va='top', ha='left', color='grey', weight='bold')

# Rimuove la cornice superiore e destra per un look più pulito
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(1.2)
ax.spines['bottom'].set_linewidth(1.2)

# Annotazione chiave per l'incrocio tra Data Breach e Cyber-Fisici
# Troviamo l'anno dell'incrocio (approssimativamente tra 2023 e 2024)
intersection_year_index = np.where(data_breach <= cyber_fisici)[0][0] # Il primo punto dove Cyber-Fisici supera o eguaglia Data Breach
intersection_year = anni[intersection_year_index]
# Stimiamo il punto medio per l'annotazione visiva
# intersection_x = intersection_year_index - 0.5 if data_breach[intersection_year_index-1] > cyber_fisici[intersection_year_index-1] else intersection_year_index
# intersection_y = (data_breach[intersection_year_index] + cyber_fisici[intersection_year_index]) / 2

# Aggiungi un cerchio per evidenziare l'incrocio sul grafico
ax.plot(anni[intersection_year_index], data_breach[intersection_year_index], 'o', color='black', markersize=8, zorder=10)
ax.plot(anni[intersection_year_index], cyber_fisici[intersection_year_index], 'o', color='black', markersize=8, zorder=10)


ax.annotate(f'Punto di Sorpasso\n(CF > DB nel {anni[intersection_year_index]})',
            xy=(intersection_year_index, cyber_fisici[intersection_year_index]),
            xytext=(intersection_year_index + 0.5, 58), # Posizione del testo
            arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=8),
            fontsize=11, weight='bold', color='#17202A', ha='center', va='bottom')


# Salvataggio del file
output_filename = 'evoluzione_attacchi_linee_abbellito.png'
plt.savefig(output_filename, dpi=300, bbox_inches='tight')
plt.show()