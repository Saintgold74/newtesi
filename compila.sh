#!/bin/bash
# Compilazione tesi con XeLaTeX e Biber per BibLaTeX

echo "╔════════════════════════════════════════╗"
echo "║   COMPILAZIONE TESI CON XELATEX       ║"
echo "║         Backend Biber                  ║"
echo "╚════════════════════════════════════════╝"

# Prima compilazione
echo ""
echo "FASE 1: Prima compilazione XeLaTeX..."
xelatex -interaction=nonstopmode main.tex

# Biber per bibliografia
echo ""
echo "FASE 2: Elaborazione bibliografia con Biber..."
if [ -f main.bcf ]; then
    biber main
else
    echo "⚠ File main.bcf non trovato, skip Biber"
fi

# Seconda compilazione
echo ""
echo "FASE 3: Seconda compilazione XeLaTeX..."
xelatex -interaction=nonstopmode main.tex

# Terza compilazione per riferimenti
echo ""
echo "FASE 4: Compilazione finale..."
xelatex -interaction=nonstopmode main.tex

echo ""
echo "✓ Compilazione completata!"
echo "📄 File generato: main.pdf"