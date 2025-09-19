#!/usr/bin/env python3
"""
Script per verificare e aggiornare le prime occorrenze dei termini del glossario
per essere in grassetto secondo le convenzioni della tesi.
"""

import re
import os
from pathlib import Path

# File dei capitoli attivi secondo includeonly in main_long.tex
ACTIVE_CHAPTERS = [
    'capitoli/abstract.tex',
    'capitoli/Cap1.tex',
    'capitoli/Cap2.tex',
    'capitoli/Cap3_def1_2.tex',
    'capitoli/Cap3_revisionato.tex',
    'capitoli/Cap4_1.tex',
    'capitoli/Cap5.tex',
    'capitoli/app_metodologia.tex',
    'capitoli/app_scoring.tex'
]

def load_glossary_terms():
    """Carica i termini del glossario dal file"""
    terms = []
    with open('termini_glossario_clean.txt', 'r', encoding='utf-8') as f:
        for line in f:
            term = line.strip()
            if term:
                terms.append(term)
    return terms

def find_gls_occurrences(content, term):
    """Trova tutte le occorrenze di \\gls{term} nel contenuto"""
    pattern = rf'\\gls\{{{re.escape(term)}\}}'
    matches = []
    for match in re.finditer(pattern, content):
        matches.append((match.start(), match.group()))
    return matches

def find_textbf_gls_occurrences(content, term):
    """Trova tutte le occorrenze di \\textbf{\\gls{term}} nel contenuto"""
    pattern = rf'\\textbf\{{\\gls\{{{re.escape(term)}\}}\}}'
    matches = []
    for match in re.finditer(pattern, content):
        matches.append((match.start(), match.group()))
    return matches

def analyze_file(filepath, terms):
    """Analizza un file per le occorrenze dei termini del glossario"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Errore leggendo {filepath}: {e}")
        return {}

    file_results = {}

    for term in terms:
        gls_matches = find_gls_occurrences(content, term)
        textbf_matches = find_textbf_gls_occurrences(content, term)

        if gls_matches or textbf_matches:
            all_matches = []

            # Aggiungi match normali
            for pos, match_text in gls_matches:
                all_matches.append((pos, match_text, 'normal'))

            # Aggiungi match in grassetto
            for pos, match_text in textbf_matches:
                all_matches.append((pos, match_text, 'bold'))

            # Ordina per posizione
            all_matches.sort(key=lambda x: x[0])

            file_results[term] = {
                'total_occurrences': len(all_matches),
                'first_occurrence': all_matches[0] if all_matches else None,
                'all_matches': all_matches
            }

    return file_results

def analyze_all_files():
    """Analizza tutti i file attivi"""
    terms = load_glossary_terms()
    print(f"Analizzando {len(terms)} termini del glossario...")

    # Dizionario per tracciare la prima occorrenza globale di ogni termine
    global_first_occurrences = {}

    # Ordine dei file (importante per determinare la prima occorrenza)
    file_order = {file: idx for idx, file in enumerate(ACTIVE_CHAPTERS)}

    all_results = {}

    for filepath in ACTIVE_CHAPTERS:
        if not os.path.exists(filepath):
            print(f"File non trovato: {filepath}")
            continue

        print(f"\\nAnalizzando {filepath}...")
        file_results = analyze_file(filepath, terms)
        all_results[filepath] = file_results

        # Aggiorna prime occorrenze globali
        for term, data in file_results.items():
            if term not in global_first_occurrences:
                global_first_occurrences[term] = {
                    'file': filepath,
                    'position': data['first_occurrence'][0],
                    'text': data['first_occurrence'][1],
                    'type': data['first_occurrence'][2],
                    'file_order': file_order[filepath]
                }
            else:
                # Confronta con occorrenza esistente
                current = global_first_occurrences[term]
                if (file_order[filepath] < current['file_order'] or
                    (file_order[filepath] == current['file_order'] and
                     data['first_occurrence'][0] < current['position'])):
                    global_first_occurrences[term] = {
                        'file': filepath,
                        'position': data['first_occurrence'][0],
                        'text': data['first_occurrence'][1],
                        'type': data['first_occurrence'][2],
                        'file_order': file_order[filepath]
                    }

    return all_results, global_first_occurrences

def generate_report(all_results, global_first_occurrences):
    """Genera report delle prime occorrenze che necessitano correzione"""
    print("\\n" + "="*60)
    print("REPORT PRIME OCCORRENZE TERMINI GLOSSARIO")
    print("="*60)

    needs_correction = []
    correct_already = []

    for term, data in global_first_occurrences.items():
        if data['type'] == 'normal':
            needs_correction.append((term, data))
        else:
            correct_already.append((term, data))

    print(f"\\nTERMINI CHE NECESSITANO CORREZIONE ({len(needs_correction)}):")
    print("-" * 50)
    for term, data in sorted(needs_correction, key=lambda x: (x[1]['file_order'], x[1]['position'])):
        print(f"* {term}")
        print(f"   File: {data['file']}")
        print(f"   Testo attuale: {data['text']}")
        print(f"   Testo corretto: \\\\textbf{{\\\\gls{{{term}}}}}")
        print()

    print(f"\\nTERMINI GIA' CORRETTI ({len(correct_already)}):")
    print("-" * 50)
    for term, data in sorted(correct_already, key=lambda x: (x[1]['file_order'], x[1]['position'])):
        print(f"+ {term} in {data['file']}")

    print(f"\\nRIEPILOGO:")
    print(f"- Termini trovati: {len(global_first_occurrences)}")
    print(f"- Termini corretti: {len(correct_already)}")
    print(f"- Termini da correggere: {len(needs_correction)}")
    print(f"- Percentuale corretti: {len(correct_already)/len(global_first_occurrences)*100:.1f}%")

    return needs_correction

def fix_first_occurrences(needs_correction):
    """Corregge automaticamente le prime occorrenze"""
    print("\\n" + "="*60)
    print("CORREZIONE AUTOMATICA PRIME OCCORRENZE")
    print("="*60)

    files_to_update = {}

    # Raggruppa correzioni per file
    for term, data in needs_correction:
        filepath = data['file']
        if filepath not in files_to_update:
            files_to_update[filepath] = []
        files_to_update[filepath].append((term, data))

    # Aggiorna ogni file
    for filepath, corrections in files_to_update.items():
        print(f"\\nAggiornando {filepath}...")

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"Errore leggendo {filepath}: {e}")
            continue

        # Ordina correzioni per posizione (dal fondo verso l'inizio per non alterare posizioni)
        corrections.sort(key=lambda x: x[1]['position'], reverse=True)

        modified = False
        for term, data in corrections:
            old_text = f"\\gls{{{term}}}"
            new_text = f"\\textbf{{\\gls{{{term}}}}}"

            # Trova la prima occorrenza e sostituisci
            if old_text in content:
                content = content.replace(old_text, new_text, 1)  # Sostituisci solo la prima
                modified = True
                print(f"  + Corretto: {term}")
            else:
                print(f"  - Non trovato: {term}")

        if modified:
            try:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"  > File salvato: {filepath}")
            except Exception as e:
                print(f"  X Errore salvando {filepath}: {e}")

def main():
    print("Script per verificare prime occorrenze termini glossario")
    print("="*60)

    if not os.path.exists('termini_glossario_clean.txt'):
        print("X File termini_glossario_clean.txt non trovato!")
        return

    # Analizza tutti i file
    all_results, global_first_occurrences = analyze_all_files()

    # Genera report
    needs_correction = generate_report(all_results, global_first_occurrences)

    if needs_correction:
        print(f"\\nTrovati {len(needs_correction)} termini da correggere.")
        print("Procedendo con la correzione automatica...")
        fix_first_occurrences(needs_correction)
        print("\\nCorrezione completata!")
    else:
        print("\\nTutte le prime occorrenze sono gia' corrette!")

if __name__ == "__main__":
    main()