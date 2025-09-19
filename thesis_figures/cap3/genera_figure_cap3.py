#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Principale per Generazione Figure e Tabelle Capitolo 3
Tesi di Laurea in Ingegneria Informatica
Università Niccolò Cusano

Esegue la generazione di tutte le figure e tabelle necessarie per il Capitolo 3

Utilizzo:
    python genera_figure_cap3.py

Autore: [Nome Studente]
Data: 2024
"""

import os
import sys
import warnings
warnings.filterwarnings('ignore')

# Importa gli script per figure e tabelle
try:
    from figure_cap3_python import create_all_figures
    from tabelle_cap3_python import create_all_tables
except ImportError:
    print("ERRORE: Assicurarsi che i file 'figure_cap3_python.py' e 'tabelle_cap3_python.py'")
    print("        siano nella stessa directory di questo script.")
    sys.exit(1)

def print_header():
    """Stampa l'intestazione del programma"""
    print("\n" + "="*70)
    print(" " * 10 + "GENERATORE FIGURE E TABELLE - CAPITOLO 3")
    print(" " * 15 + "Tesi di Laurea in Ingegneria Informatica")
    print(" " * 20 + "Università Niccolò Cusano")
    print("="*70)

def check_requirements():
    """Verifica che tutti i moduli necessari siano installati"""
    required_modules = ['matplotlib', 'numpy', 'pandas', 'seaborn']
    missing_modules = []
    
    print("\n📋 Controllo dipendenze...")
    for module in required_modules:
        try:
            __import__(module)
            print(f"   ✓ {module} installato")
        except ImportError:
            missing_modules.append(module)
            print(f"   ✗ {module} NON installato")
    
    if missing_modules:
        print("\n⚠️  ATTENZIONE: Moduli mancanti!")
        print("   Installare con: pip install " + " ".join(missing_modules))
        return False
    
    print("   ✓ Tutte le dipendenze sono installate")
    return True

def create_output_directory():
    """Crea la directory di output se non esiste"""
    output_dir = "figure_cap3_output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"\n📁 Creata directory di output: {output_dir}/")
    else:
        print(f"\n📁 Directory di output esistente: {output_dir}/")
    return output_dir

def main():
    """Funzione principale"""
    print_header()
    
    # Controllo requisiti
    if not check_requirements():
        print("\n❌ Impossibile procedere senza le dipendenze richieste.")
        sys.exit(1)
    
    # Crea directory di output
    output_dir = create_output_directory()
    
    # Cambia directory di lavoro
    original_dir = os.getcwd()
    try:
        os.chdir(output_dir)
    except:
        print(f"⚠️  Impossibile accedere alla directory {output_dir}")
        print("   I file verranno salvati nella directory corrente.")
    
    print("\n" + "="*70)
    print("INIZIO GENERAZIONE FIGURE E TABELLE")
    print("="*70)
    
    # Genera figure
    print("\n📊 GENERAZIONE FIGURE")
    print("-"*40)
    try:
        figures = create_all_figures()
        print(f"\n✅ Generate {len(figures)} figure con successo!")
    except Exception as e:
        print(f"\n❌ Errore durante la generazione delle figure: {e}")
        figures = []
    
    # Genera tabelle
    print("\n📋 GENERAZIONE TABELLE")
    print("-"*40)
    try:
        tables = create_all_tables()
        print(f"\n✅ Generate {len(tables)} tabelle con successo!")
    except Exception as e:
        print(f"\n❌ Errore durante la generazione delle tabelle: {e}")
        tables = []
    
    # Torna alla directory originale
    os.chdir(original_dir)
    
    # Riepilogo finale
    print("\n" + "="*70)
    print("RIEPILOGO GENERAZIONE COMPLETATA")
    print("="*70)
    
    print("\n📊 FILE FIGURE GENERATI:")
    figure_files = [
        "figura_3_1_architettura_alimentazione.pdf",
        "figura_3_2_evoluzione_rete.pdf",
        "figura_3_3_maturity_levels.pdf",
        "figura_3_4_edge_architecture.pdf",
        "figura_3_5_gist_framework.pdf"
    ]
    for f in figure_files:
        file_path = os.path.join(output_dir, f)
        if os.path.exists(file_path):
            size = os.path.getsize(file_path) / 1024  # KB
            print(f"   ✓ {f} ({size:.1f} KB)")
        else:
            print(f"   ⚠️  {f} (non trovato)")
    
    print("\n📋 FILE TABELLE GENERATI:")
    table_files = [
        "tabella_3_1_maturity_levels.pdf",
        "tabella_3_2_segmentation_comparison.pdf",
        "tabella_3_3_iot_impact.pdf",
        "tabella_3_4_transformation_kpi.pdf",
        "tabella_3_5_implementation_roadmap.pdf"
    ]
    for f in table_files:
        file_path = os.path.join(output_dir, f)
        if os.path.exists(file_path):
            size = os.path.getsize(file_path) / 1024  # KB
            print(f"   ✓ {f} ({size:.1f} KB)")
        else:
            print(f"   ⚠️  {f} (non trovato)")
    
    # Istruzioni finali
    print("\n" + "="*70)
    print("📝 ISTRUZIONI PER L'USO NEL DOCUMENTO LATEX:")
    print("="*70)
    print("""
Per includere le figure nel documento LaTeX:

\\begin{figure}[htbp]
    \\centering
    \\includegraphics[width=\\textwidth]{figure_cap3_output/figura_3_1_architettura_alimentazione.pdf}
    \\caption{Architettura ridondante 2N per sistemi di alimentazione critica}
    \\label{fig:power_architecture}
\\end{figure}

Per includere le tabelle generate come immagini:

\\begin{figure}[htbp]
    \\centering
    \\includegraphics[width=\\textwidth]{figure_cap3_output/tabella_3_1_maturity_levels.pdf}
    \\caption{Livelli di Maturità Infrastrutturale nel settore GDO}
    \\label{tab:maturity_levels}
\\end{figure}
    """)
    
    print("\n✅ PROCESSO COMPLETATO CON SUCCESSO!")
    print(f"   Tutti i file sono stati salvati in: {output_dir}/")
    print("\n" + "="*70)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Processo interrotto dall'utente")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Errore imprevisto: {e}")
        sys.exit(1)
