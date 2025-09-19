#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script per la generazione delle tabelle del Capitolo 3
Tesi di Laurea in Ingegneria Informatica
Università Niccolò Cusano

Autore: [Nome Studente]
Data: 2024
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Rectangle
import numpy as np

# Configurazione globale per font large
plt.rcParams.update({
    'font.size': 14,
    'axes.titlesize': 16,
    'axes.labelsize': 14,
    'figure.titlesize': 18,
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'DejaVu Sans'],
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.format': 'pdf'
})

# Colori professionali per le tabelle
colors = {
    'header': '#1e88e5',
    'row_even': '#f5f5f5',
    'row_odd': '#ffffff',
    'highlight': '#fff3e0',
    'border': '#263238'
}

def create_table_maturity_levels():
    """
    Tabella 3.1: Livelli di Maturità Infrastrutturale nel settore GDO
    """
    fig, ax = plt.subplots(figsize=(16, 10))
    ax.axis('tight')
    ax.axis('off')
    
    # Titolo
    fig.suptitle('Tabella 3.1 - Livelli di Maturità Infrastrutturale nel settore GDO', 
                fontsize=16, fontweight='bold', y=0.98)
    
    # Dati tabella
    data = {
        'Livello': ['1. Tradizionale', '2. Consolidato', '3. Automatizzato', 
                   '4. Ottimizzato', '5. Adattivo'],
        'Caratteristiche': [
            'Infrastruttura fisica isolata,\ngestione manuale',
            'Virtualizzazione parziale,\nprimi sistemi di monitoraggio',
            'Orchestrazione dei servizi,\ngestione centralizzata',
            'Architetture ibride,\nautomazione avanzata',
            'Infrastruttura intelligente,\nauto-riparazione'
        ],
        'Disponibilità': ['95-97%', '97-98,5%', '98,5-99,5%', '99,5-99,9%', '>99,95%'],
        'Costi Operativi': ['Baseline\n(100%)', '85-90%', '70-75%', '55-60%', '45-50%'],
        'Tempo\nImplementazione': ['--', '12-14 mesi', '14-16 mesi', '16-18 mesi', '18-24 mesi']
    }
    
    df = pd.DataFrame(data)
    
    # Creazione tabella con matplotlib
    table = ax.table(cellText=df.values,
                    colLabels=df.columns,
                    cellLoc='center',
                    loc='center',
                    colWidths=[0.15, 0.35, 0.15, 0.15, 0.20])
    
    # Formattazione
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1.2, 2.5)
    
    # Colori header
    for i in range(len(df.columns)):
        table[(0, i)].set_facecolor(colors['header'])
        table[(0, i)].set_text_props(weight='bold', color='white', size=13)
        table[(0, i)].set_height(0.12)
    
    # Colori righe alternate
    for i in range(1, len(df) + 1):
        for j in range(len(df.columns)):
            if i % 2 == 0:
                table[(i, j)].set_facecolor(colors['row_even'])
            else:
                table[(i, j)].set_facecolor(colors['row_odd'])
            table[(i, j)].set_height(0.15)
            
            # Evidenzia ultima riga (livello 5 - target)
            if i == len(df):
                table[(i, j)].set_facecolor(colors['highlight'])
                table[(i, j)].set_text_props(weight='bold')
    
    # Note
    ax.text(0.5, -0.05, 
           'Nota: Il Livello 5 (Adattivo) rappresenta l\'obiettivo target per le organizzazioni GDO leader di mercato',
           transform=ax.transAxes, ha='center', fontsize=11, style='italic')
    
    plt.tight_layout()
    plt.savefig('tabella_3_1_maturity_levels.pdf', format='pdf', bbox_inches='tight')
    plt.show()
    return fig

def create_table_segmentation_comparison():
    """
    Tabella 3.2: Confronto tra Segmentazione Tradizionale e Micro-segmentazione
    """
    fig, ax = plt.subplots(figsize=(16, 11))
    ax.axis('tight')
    ax.axis('off')
    
    fig.suptitle('Tabella 3.2 - Confronto tra Segmentazione Tradizionale e Micro-segmentazione', 
                fontsize=16, fontweight='bold', y=0.98)
    
    # Dati comparativi
    data = {
        'Aspetto': [
            'Granularità',
            'Implementazione',
            'Gestione',
            'Scalabilità',
            'Visibilità',
            'Tempo deployment',
            'Costo operativo',
            'Efficacia sicurezza'
        ],
        'Segmentazione Tradizionale': [
            'Livello di subnet/VLAN',
            'Firewall perimetrali e ACL',
            'Configurazione statica manuale',
            'Limitata (max 4.094 VLAN)',
            'Traffico est-ovest limitato',
            '2-4 settimane per modifica',
            'Alto (gestione manuale)',
            'Media (60% attacchi bloccati)'
        ],
        'Micro-segmentazione': [
            'Livello di applicazione/workload',
            'Policy distribuite software-defined',
            'Orchestrazione dinamica automatizzata',
            'Virtualmente illimitata',
            'Completa su tutti i flussi',
            'Minuti con automazione',
            'Ridotto del 40% (automazione)',
            'Alta (92% attacchi bloccati)'
        ],
        'Vantaggio\nMicro-seg': [
            '⬆⬆⬆',
            '⬆⬆⬆',
            '⬆⬆⬆',
            '⬆⬆⬆',
            '⬆⬆⬆',
            '⬆⬆⬆',
            '40% ↓',
            '53% ↑'
        ]
    }
    
    df = pd.DataFrame(data)
    
    # Creazione tabella
    table = ax.table(cellText=df.values,
                    colLabels=df.columns,
                    cellLoc='center',
                    loc='center',
                    colWidths=[0.2, 0.35, 0.35, 0.1])
    
    # Formattazione
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1.2, 2.2)
    
    # Header
    for i in range(len(df.columns)):
        table[(0, i)].set_facecolor(colors['header'])
        table[(0, i)].set_text_props(weight='bold', color='white', size=13)
        table[(0, i)].set_height(0.12)
    
    # Righe
    for i in range(1, len(df) + 1):
        # Prima colonna (aspetti) in grassetto
        table[(i, 0)].set_text_props(weight='bold')
        table[(i, 0)].set_facecolor('#e3f2fd')
        
        # Colori alternati per le altre colonne
        for j in range(1, len(df.columns)):
            if i % 2 == 0:
                table[(i, j)].set_facecolor(colors['row_even'])
            else:
                table[(i, j)].set_facecolor(colors['row_odd'])
            
            # Colonna vantaggi con colore evidenziato
            if j == 3:
                table[(i, j)].set_facecolor('#c8e6c9')
                table[(i, j)].set_text_props(weight='bold', color='#2e7d32')
    
    # Legenda
    ax.text(0.5, -0.05, 
           'Legenda: ⬆⬆⬆ = Miglioramento significativo | ↓ = Riduzione | ↑ = Incremento',
           transform=ax.transAxes, ha='center', fontsize=11, style='italic')
    
    plt.tight_layout()
    plt.savefig('tabella_3_2_segmentation_comparison.pdf', format='pdf', bbox_inches='tight')
    plt.show()
    return fig

def create_table_iot_impact():
    """
    Tabella 3.3: Impatto dell'integrazione IoT nella GDO
    """
    fig, ax = plt.subplots(figsize=(15, 9))
    ax.axis('tight')
    ax.axis('off')
    
    fig.suptitle('Tabella 3.3 - Impatto dell\'integrazione IoT nella GDO', 
                fontsize=16, fontweight='bold', y=0.98)
    
    # Dati IoT
    data = {
        'Area Applicativa': [
            'Catena del freddo',
            'Gestione energia',
            'Sicurezza',
            'Customer experience',
            'Gestione inventario',
            'Manutenzione predittiva'
        ],
        'Sensori/Dispositivi': [
            'Termometri wireless\nSensori umidità',
            'Smart meter\nSensori consumo',
            'Videocamere AI\nSensori movimento',
            'Beacon/Contapersone\nHeat maps',
            'Tag RFID\nSensori peso scaffali',
            'Sensori vibrazione\nMonitor prestazioni'
        ],
        'Riduzione\nCosti': [
            '-18%', '-24%', '-31%', '-12%', '-22%', '-28%'
        ],
        'Miglioramento\nKPI': [
            '+99.2% conformità', '+87% efficienza', '+94% detection',
            '+21% soddisfazione', '+96% accuratezza stock', '+89% uptime'
        ],
        'ROI\n(mesi)': [
            '8', '12', '10', '14', '11', '9'
        ]
    }
    
    df = pd.DataFrame(data)
    
    # Creazione tabella
    table = ax.table(cellText=df.values,
                    colLabels=df.columns,
                    cellLoc='center',
                    loc='center',
                    colWidths=[0.22, 0.28, 0.15, 0.25, 0.10])
    
    # Formattazione
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1.2, 2.3)
    
    # Header
    for i in range(len(df.columns)):
        table[(0, i)].set_facecolor(colors['header'])
        table[(0, i)].set_text_props(weight='bold', color='white', size=13)
        table[(0, i)].set_height(0.12)
    
    # Righe con colori per performance
    for i in range(1, len(df) + 1):
        # Area applicativa
        table[(i, 0)].set_text_props(weight='bold')
        table[(i, 0)].set_facecolor('#e8eaf6')
        
        # Altri campi
        for j in range(1, len(df.columns)):
            if j == 2:  # Riduzione costi (rosso/verde)
                table[(i, j)].set_facecolor('#ffebee')
                table[(i, j)].set_text_props(color='#c62828', weight='bold')
            elif j == 3:  # Miglioramento KPI (verde)
                table[(i, j)].set_facecolor('#e8f5e9')
                table[(i, j)].set_text_props(color='#2e7d32', weight='bold')
            elif j == 4:  # ROI
                table[(i, j)].set_facecolor('#fff3e0')
                table[(i, j)].set_text_props(weight='bold')
            else:
                if i % 2 == 0:
                    table[(i, j)].set_facecolor(colors['row_even'])
                else:
                    table[(i, j)].set_facecolor(colors['row_odd'])
    
    # Statistiche aggregate
    ax.text(0.5, -0.08, 
           'Media complessiva: Riduzione costi -22.5% | Miglioramento KPI +91.2% | ROI medio: 10.5 mesi',
           transform=ax.transAxes, ha='center', fontsize=12, 
           weight='bold', bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.3))
    
    plt.tight_layout()
    plt.savefig('tabella_3_3_iot_impact.pdf', format='pdf', bbox_inches='tight')
    plt.show()
    return fig

def create_table_transformation_kpi():
    """
    Tabella 3.4: KPI per la Trasformazione Infrastrutturale
    """
    fig, ax = plt.subplots(figsize=(16, 10))
    ax.axis('tight')
    ax.axis('off')
    
    fig.suptitle('Tabella 3.4 - KPI per la Trasformazione Infrastrutturale', 
                fontsize=16, fontweight='bold', y=0.98)
    
    # Dati KPI
    data = {
        'Indicatore': [
            'Disponibilità Sistema',
            'MTTR (ore)',
            'Riduzione TCO',
            'Incidenti Sicurezza',
            'Efficienza Energetica (PUE)',
            'Automazione Processi',
            'Compliance Score',
            'User Satisfaction'
        ],
        'Baseline\n(Attuale)': [
            '97.5%', '4.2', '--', '100 (index)', '2.1', '20%', '72%', '65%'
        ],
        'Target\nAnno 1': [
            '99.0%', '2.5', '15%', '50', '1.7', '50%', '85%', '75%'
        ],
        'Target\nAnno 2': [
            '99.5%', '1.5', '25%', '30', '1.5', '65%', '92%', '82%'
        ],
        'Target\nAnno 3': [
            '99.95%', '0.8', '35%', '20', '1.4', '80%', '98%', '90%'
        ],
        'Peso\n(%)': [
            '25%', '20%', '20%', '15%', '10%', '10%', '--', '--'
        ],
        'Status': [
            '🟡', '🟡', '🟢', '🟢', '🟡', '🟢', '🟢', '🟡'
        ]
    }
    
    df = pd.DataFrame(data)
    
    # Creazione tabella
    table = ax.table(cellText=df.values,
                    colLabels=df.columns,
                    cellLoc='center',
                    loc='center',
                    colWidths=[0.25, 0.12, 0.12, 0.12, 0.12, 0.10, 0.08])
    
    # Formattazione
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1.2, 2.2)
    
    # Header
    for i in range(len(df.columns)):
        table[(0, i)].set_facecolor(colors['header'])
        table[(0, i)].set_text_props(weight='bold', color='white', size=13)
        table[(0, i)].set_height(0.12)
    
    # Righe
    for i in range(1, len(df) + 1):
        # Prima colonna (KPI) in grassetto
        table[(i, 0)].set_text_props(weight='bold')
        table[(i, 0)].set_facecolor('#e3f2fd')
        
        # Evidenzia i KPI critici (peso >= 20%)
        if i <= 3:  # Prime 3 righe hanno peso >= 20%
            for j in range(len(df.columns)):
                table[(i, j)].set_facecolor('#fff9c4')
        else:
            for j in range(1, len(df.columns)):
                if i % 2 == 0:
                    table[(i, j)].set_facecolor(colors['row_even'])
                else:
                    table[(i, j)].set_facecolor(colors['row_odd'])
        
        # Colonna status con emoji
        table[(i, 6)].set_text_props(size=16)
    
    # Legenda status
    ax.text(0.3, -0.08, '🟢 On Track', transform=ax.transAxes, fontsize=12, weight='bold')
    ax.text(0.5, -0.08, '🟡 Attenzione', transform=ax.transAxes, fontsize=12, weight='bold')
    ax.text(0.7, -0.08, '🔴 Critico', transform=ax.transAxes, fontsize=12, weight='bold')
    
    # Note
    ax.text(0.5, -0.12, 
           'Nota: I KPI con peso ≥20% sono considerati critici per il successo del progetto',
           transform=ax.transAxes, ha='center', fontsize=11, style='italic')
    
    plt.tight_layout()
    plt.savefig('tabella_3_4_transformation_kpi.pdf', format='pdf', bbox_inches='tight')
    plt.show()
    return fig

def create_table_implementation_roadmap():
    """
    Tabella 3.5: Roadmap Implementativa Dettagliata
    """
    fig, ax = plt.subplots(figsize=(16, 12))
    ax.axis('tight')
    ax.axis('off')
    
    fig.suptitle('Tabella 3.5 - Roadmap Implementativa Dettagliata per la Trasformazione Infrastrutturale', 
                fontsize=16, fontweight='bold', y=0.98)
    
    # Dati roadmap
    data = {
        'Fase': [
            'FASE 1\nConsolidamento',
            '',
            '',
            'FASE 2\nModernizzazione',
            '',
            '',
            'FASE 3\nOttimizzazione',
            '',
            ''
        ],
        'Periodo': [
            '0-6 mesi',
            '0-6 mesi',
            '0-6 mesi',
            '6-18 mesi',
            '6-18 mesi',
            '6-18 mesi',
            '18-36 mesi',
            '18-36 mesi',
            '18-36 mesi'
        ],
        'Attività': [
            'Upgrade sistemi alimentazione 2N',
            'Implementazione monitoring',
            'Assessment sicurezza',
            'Deployment SD-WAN completo',
            'Migrazione cloud (30% app)',
            'Zero Trust - Fase 1',
            'Multi-cloud orchestration',
            'Edge computing completo',
            'AI/ML per manutenzione'
        ],
        'Investimento': [
            '€120k',
            '€80k',
            '€150k',
            '€350k',
            '€300k',
            '€200k',
            '€500k',
            '€400k',
            '€300k'
        ],
        'Risultati Attesi': [
            'Disponibilità 99%',
            'Visibilità completa',
            '73% vulnerabilità risolte',
            'MTTR 1.8h',
            'TCO -15%',
            'Security +40%',
            'TCO -35%',
            'Latenza <50ms',
            'Predizione 94%'
        ],
        'ROI': [
            '12 mesi',
            '8 mesi',
            '10 mesi',
            '14 mesi',
            '16 mesi',
            '18 mesi',
            '20 mesi',
            '22 mesi',
            '24 mesi'
        ]
    }
    
    df = pd.DataFrame(data)
    
    # Creazione tabella
    table = ax.table(cellText=df.values,
                    colLabels=['Fase', 'Periodo', 'Attività', 'Investimento', 'Risultati Attesi', 'ROI'],
                    cellLoc='center',
                    loc='center',
                    colWidths=[0.15, 0.12, 0.28, 0.12, 0.20, 0.10])
    
    # Formattazione
    table.auto_set_font_size(False)
    table.set_fontsize(11)
    table.scale(1.2, 2)
    
    # Header
    for i in range(6):
        table[(0, i)].set_facecolor(colors['header'])
        table[(0, i)].set_text_props(weight='bold', color='white', size=12)
        table[(0, i)].set_height(0.12)
    
    # Righe per fase
    fase_colors = {
        'FASE 1': '#e3f2fd',
        'FASE 2': '#fff3e0', 
        'FASE 3': '#e8f5e9'
    }
    
    current_fase = 'FASE 1'
    for i in range(1, len(df) + 1):
        # Identifica la fase corrente
        if 'FASE 1' in str(df.iloc[i-1, 0]):
            current_fase = 'FASE 1'
        elif 'FASE 2' in str(df.iloc[i-1, 0]):
            current_fase = 'FASE 2'
        elif 'FASE 3' in str(df.iloc[i-1, 0]):
            current_fase = 'FASE 3'
        
        # Colora in base alla fase
        if current_fase == 'FASE 1':
            color = '#e3f2fd'
        elif current_fase == 'FASE 2':
            color = '#fff3e0'
        else:
            color = '#e8f5e9'
        
        for j in range(6):
            table[(i, j)].set_facecolor(color)
            
        # Prima colonna (Fase) in grassetto quando presente
        if df.iloc[i-1, 0] != '':
            table[(i, 0)].set_text_props(weight='bold', size=11)
            table[(i, 0)].set_facecolor(colors['header'])
            table[(i, 0)].set_text_props(color='white')
    
    # Totali
    ax.text(0.5, -0.05, 
           'TOTALE INVESTIMENTO: €2.4M | DURATA: 36 mesi | ROI MEDIO: 16 mesi',
           transform=ax.transAxes, ha='center', fontsize=13, weight='bold',
           bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))
    
    plt.tight_layout()
    plt.savefig('tabella_3_5_implementation_roadmap.pdf', format='pdf', bbox_inches='tight')
    plt.show()
    return fig

def create_all_tables():
    """
    Genera tutte le tabelle del Capitolo 3
    """
    print("Generazione Tabelle Capitolo 3 - Tesi di Laurea")
    print("=" * 50)
    
    tables = []
    
    print("\n1. Creazione Tabella 3.1 - Livelli di Maturità...")
    tab1 = create_table_maturity_levels()
    tables.append(tab1)
    print("   ✓ Completata")
    
    print("\n2. Creazione Tabella 3.2 - Confronto Segmentazione...")
    tab2 = create_table_segmentation_comparison()
    tables.append(tab2)
    print("   ✓ Completata")
    
    print("\n3. Creazione Tabella 3.3 - Impatto IoT...")
    tab3 = create_table_iot_impact()
    tables.append(tab3)
    print("   ✓ Completata")
    
    print("\n4. Creazione Tabella 3.4 - KPI Trasformazione...")
    tab4 = create_table_transformation_kpi()
    tables.append(tab4)
    print("   ✓ Completata")
    
    print("\n5. Creazione Tabella 3.5 - Roadmap Implementativa...")
    tab5 = create_table_implementation_roadmap()
    tables.append(tab5)
    print("   ✓ Completata")
    
    print("\n" + "=" * 50)
    print("TUTTE LE TABELLE SONO STATE GENERATE CON SUCCESSO!")
    print("File salvati in formato PDF ad alta risoluzione")
    print("Font size: Large (12-14pt) per ottima leggibilità")
    
    return tables

if __name__ == "__main__":
    # Genera tutte le tabelle
    all_tables = create_all_tables()
    
    # Mostra riepilogo
    print("\n" + "=" * 50)
    print("RIEPILOGO TABELLE GENERATE:")
    print("- tabella_3_1_maturity_levels.pdf")
    print("- tabella_3_2_segmentation_comparison.pdf")
    print("- tabella_3_3_iot_impact.pdf")
    print("- tabella_3_4_transformation_kpi.pdf")
    print("- tabella_3_5_implementation_roadmap.pdf")
    print("\nTutte le tabelle sono pronte per l'inserimento nella tesi!")
