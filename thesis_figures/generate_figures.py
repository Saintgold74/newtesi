#!/usr/bin/env python3
"""
Script per generare automaticamente i PDF delle figure della tesi GIST
Autore: Framework GIST - Tesi di Laurea in Ingegneria Informatica
Università: Cusano
Data: 2025
"""

import os
import subprocess
import sys
from pathlib import Path

# Template LaTeX per figura singola
LATEX_TEMPLATE = r"""
\documentclass[11pt,a4paper]{{standalone}}
\usepackage[utf8]{{inputenc}}
\usepackage[italian]{{babel}}
\usepackage{{tikz}}
\usepackage{{pgfplots}}
\usepackage{{amsmath}}
\pgfplotsset{{compat=1.18}}

% Definizione colori
\definecolor{{gdoblue}}{{RGB}}{{0, 102, 204}}
\definecolor{{gdogreen}}{{RGB}}{{76, 175, 80}}
\definecolor{{gdored}}{{RGB}}{{244, 67, 54}}
\definecolor{{gdoorange}}{{RGB}}{{255, 152, 0}}
\definecolor{{gdopurple}}{{RGB}}{{156, 39, 176}}
\definecolor{{gdogray}}{{RGB}}{{158, 158, 158}}
\definecolor{{gdolightblue}}{{RGB}}{{179, 229, 252}}
\definecolor{{gdodarkblue}}{{RGB}}{{25, 32, 102}}

% Librerie TikZ
\usetikzlibrary{{arrows.meta,positioning,calc,patterns,decorations.pathreplacing,shadows,shapes.geometric,backgrounds,fit,shapes.symbols}}

\begin{{document}}
{figure_content}
\end{{document}}
"""

# Definizione delle figure
FIGURES = {
    'cap1': {
        'evoluzione_attacchi': {
            'description': 'Evoluzione della composizione percentuale delle tipologie di attacco',
            'code': r"""
\begin{tikzpicture}
\begin{axis}[
    width=14cm,
    height=8cm,
    area style,
    xlabel={Anno},
    ylabel={Percentuale (\%)},
    xmin=2019, xmax=2026,
    ymin=0, ymax=100,
    xtick={2019,2020,2021,2022,2023,2024,2025,2026},
    ytick={0,20,40,60,80,100},
    legend style={
        at={(1.02,0.5)},
        anchor=west,
        font=\small,
        draw=none,
        fill=white,
        fill opacity=0.8
    },
    grid=major,
    grid style={dashed,gray!30},
    axis lines=left,
    axis line style={->,thick},
    tick label style={font=\small},
    label style={font=\normalsize}
]

\addplot+[
    fill=gdoblue!70,
    draw=gdoblue,
    thick,
    area legend,
    forget plot
] coordinates {
    (2019,65) (2020,58) (2021,52) (2022,45) (2023,38) (2024,32) (2025,28) (2026,25)
} \closedcycle;

\addplot+[
    fill=gdored!70,
    draw=gdored,
    thick,
    area legend,
    forget plot
] coordinates {
    (2019,80) (2020,75) (2021,72) (2022,70) (2023,68) (2024,67) (2025,68) (2026,70)
} \closedcycle;

\addplot+[
    fill=gdogreen!70,
    draw=gdogreen,
    thick,
    area legend,
    forget plot
] coordinates {
    (2019,100) (2020,100) (2021,100) (2022,100) (2023,100) (2024,100) (2025,100) (2026,100)
} \closedcycle;

\draw[dashed,thick,gdodarkblue] (axis cs:2024,0) -- (axis cs:2024,100);
\node[anchor=north,font=\footnotesize] at (axis cs:2024,0) {Dati storici};
\node[anchor=north,font=\footnotesize] at (axis cs:2025.5,0) {Proiezioni};

\node[font=\small,white] at (axis cs:2021,26) {Furto Dati};
\node[font=\small,white] at (axis cs:2021,62) {Disruzione};
\node[font=\small,white] at (axis cs:2021,86) {Cyber-Fisici};

\legend{Attacchi tradizionali (Furto dati),Disruzione operativa,Compromissione informatico-fisica}

\end{axis}
\end{tikzpicture}
"""
        },
        'thesis_structure': {
            'description': 'Struttura della tesi e flusso logico',
            'code': r"""
\begin{tikzpicture}[
    node distance=2cm,
    chapter/.style={
        rectangle,
        draw=gdoblue,
        fill=gdolightblue!30,
        text width=3.5cm,
        minimum height=2cm,
        align=center,
        font=\small\bfseries,
        drop shadow
    },
    framework/.style={
        ellipse,
        draw=gdogreen,
        fill=gdogreen!20,
        text width=3cm,
        minimum height=1.8cm,
        align=center,
        font=\small,
        drop shadow
    },
    arrow/.style={
        ->,
        thick,
        gdoblue,
        >=Stealth
    },
    feedback/.style={
        <->,
        dashed,
        gdogray,
        >=Stealth
    }
]

\node[chapter] (cap1) {Capitolo 1\\Introduzione\\e Contesto};
\node[chapter, right=of cap1] (cap2) {Capitolo 2\\Minacce e\\ASSA-GDO};
\node[chapter, right=of cap2] (cap3) {Capitolo 3\\Architetture\\GRAF};
\node[chapter, below=of cap2] (cap4) {Capitolo 4\\Conformità\\MIN};
\node[chapter, right=of cap4] (cap5) {Capitolo 5\\Framework\\GIST};

\node[framework, below=1cm of cap2] (assa) {ASSA-GDO\\28\%};
\node[framework, below=1cm of cap3] (graf) {GRAF\\35\%};
\node[framework, below=1cm of cap4] (min) {MIN\\37\%};

\node[
    rectangle,
    draw=gdored,
    fill=gdored!10,
    text width=4cm,
    minimum height=2.5cm,
    align=center,
    font=\large\bfseries,
    drop shadow,
    below=3.5cm of cap3
] (gist) {Framework\\GIST\\Score: 0-100};

\draw[arrow] (cap1) -- (cap2);
\draw[arrow] (cap2) -- (cap3);
\draw[arrow] (cap3) -- (cap5);
\draw[arrow] (cap2) -- (cap4);
\draw[arrow] (cap4) -- (cap5);

\draw[arrow,gdogreen] (cap2) -- (assa);
\draw[arrow,gdogreen] (cap3) -- (graf);
\draw[arrow,gdogreen] (cap4) -- (min);

\draw[arrow,gdored] (assa) -- (gist);
\draw[arrow,gdored] (graf) -- (gist);
\draw[arrow,gdored] (min) -- (gist);

\draw[feedback] (cap5) to[bend right=30] (cap2);
\draw[feedback] (cap5) to[bend left=30] (cap3);

\node[
    text width=3cm,
    align=center,
    font=\footnotesize\itshape,
    above=0.5cm of cap1
] {Identificazione\\del problema};

\node[
    text width=3cm,
    align=center,
    font=\footnotesize\itshape,
    right=0.5cm of cap5
] {Validazione\\empirica};

\node[
    draw=gdogray,
    dashed,
    text width=5cm,
    align=left,
    font=\footnotesize,
    below right=0.5cm and 1cm of gist
] {
    Pesi nel GIST Score:\\
    • ASSA-GDO: 28\%\\
    • GRAF: 35\%\\
    • MIN: 37\%
};

\end{tikzpicture}
"""
        }
    }
}

def generate_figure(chapter, figure_name, figure_data, output_dir):
    """
    Genera un singolo file PDF per una figura
    
    Args:
        chapter: nome del capitolo (es. 'cap1')
        figure_name: nome della figura (es. 'evoluzione_attacchi')
        figure_data: dizionario con 'description' e 'code'
        output_dir: directory di output per i PDF
    """
    # Crea la directory se non esiste
    chapter_dir = output_dir / chapter
    chapter_dir.mkdir(parents=True, exist_ok=True)
    
    # Crea il file LaTeX temporaneo
    tex_file = chapter_dir / f"{figure_name}.tex"
    pdf_file = chapter_dir / f"{figure_name}.pdf"
    
    # Scrivi il contenuto LaTeX
    latex_content = LATEX_TEMPLATE.format(figure_content=figure_data['code'])
    
    with open(tex_file, 'w', encoding='utf-8') as f:
        f.write(latex_content)
    
    print(f"Generando {chapter}/{figure_name}.pdf...")
    
    # Compila con pdflatex
    try:
        # Prima compilazione
        result = subprocess.run(
            ['pdflatex', '-interaction=nonstopmode', '-output-directory', str(chapter_dir), str(tex_file)],
            capture_output=True,
            text=True,
            cwd=str(chapter_dir)
        )
        
        # Seconda compilazione per riferimenti
        result = subprocess.run(
            ['pdflatex', '-interaction=nonstopmode', '-output-directory', str(chapter_dir), str(tex_file)],
            capture_output=True,
            text=True,
            cwd=str(chapter_dir)
        )
        
        if pdf_file.exists():
            print(f"  ✓ Generato: {pdf_file}")
            
            # Pulisci i file temporanei
            for ext in ['.aux', '.log', '.out']:
                temp_file = chapter_dir / f"{figure_name}{ext}"
                if temp_file.exists():
                    temp_file.unlink()
        else:
            print(f"  ✗ Errore nella generazione di {figure_name}")
            print(f"    Log: {result.stderr}")
    
    except FileNotFoundError:
        print(f"  ✗ pdflatex non trovato. Assicurarsi che LaTeX sia installato.")
        return False
    except Exception as e:
        print(f"  ✗ Errore: {e}")
        return False
    
    return True

def main():
    """
    Funzione principale per generare tutte le figure
    """
    # Directory di output
    output_dir = Path("thesis_figures")
    output_dir.mkdir(exist_ok=True)
    
    print("=" * 60)
    print("GENERATORE DI FIGURE PER TESI GIST")
    print("=" * 60)
    print()
    
    # Genera le figure
    total_figures = sum(len(figs) for figs in FIGURES.values())
    generated = 0
    
    for chapter, figures in FIGURES.items():
        print(f"\n{chapter.upper()}:")
        print("-" * 40)
        
        for figure_name, figure_data in figures.items():
            if generate_figure(chapter, figure_name, figure_data, output_dir):
                generated += 1
    
    # Riepilogo
    print("\n" + "=" * 60)
    print(f"RIEPILOGO: {generated}/{total_figures} figure generate con successo")
    print("=" * 60)
    
    if generated == total_figures:
        print("\n✓ Tutte le figure sono state generate correttamente!")
        print(f"  Le figure si trovano in: {output_dir.absolute()}")
    else:
        print(f"\n⚠ Alcune figure non sono state generate.")
        print(f"  Verificare i messaggi di errore sopra.")
    
    # Crea anche un Makefile per la compilazione
    create_makefile(output_dir)
    
    return generated == total_figures

def create_makefile(output_dir):
    """
    Crea un Makefile per compilare tutte le figure
    """
    makefile_content = """# Makefile per la generazione delle figure della tesi GIST

LATEX = pdflatex
LATEX_FLAGS = -interaction=nonstopmode

# Directory
CAP1_DIR = cap1
CAP2_DIR = cap2

# Figure Capitolo 1
CAP1_FIGS = evoluzione_attacchi thesis_structure

# Figure Capitolo 2  
CAP2_FIGS = topologia_rete evoluzione_ransomware zero_trust_architecture confronto_metriche roi_analysis

# Target principale
all: cap1 cap2

cap1: $(CAP1_FIGS:%=$(CAP1_DIR)/%.pdf)

cap2: $(CAP2_FIGS:%=$(CAP2_DIR)/%.pdf)

# Regola generica per compilare i PDF
%.pdf: %.tex
	$(LATEX) $(LATEX_FLAGS) -output-directory=$(dir $@) $<
	$(LATEX) $(LATEX_FLAGS) -output-directory=$(dir $@) $<

# Pulizia
clean:
	rm -f $(CAP1_DIR)/*.aux $(CAP1_DIR)/*.log $(CAP1_DIR)/*.out
	rm -f $(CAP2_DIR)/*.aux $(CAP2_DIR)/*.log $(CAP2_DIR)/*.out

clean-all: clean
	rm -f $(CAP1_DIR)/*.pdf
	rm -f $(CAP2_DIR)/*.pdf

.PHONY: all cap1 cap2 clean clean-all
"""
    
    makefile_path = output_dir / "Makefile"
    with open(makefile_path, 'w') as f:
        f.write(makefile_content)
    
    print(f"\n✓ Creato Makefile in: {makefile_path}")
    print("  Usa 'make all' per compilare tutte le figure")

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
