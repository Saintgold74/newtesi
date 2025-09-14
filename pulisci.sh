#!/bin/bash

# Script per rimuovere i file ausiliari di LaTeX

echo "🧹 Pulizia dei file ausiliari in corso..."

# Estrai il nome del file principale se fornito, altrimenti cerca un .tex
if [ -z "$1" ]; then
    # Se non viene specificato un file, cerca il primo .tex e usa il suo nome base
    TEXFILE=$(ls *.tex | head -n 1)
    FILENAME="${TEXFILE%.*}"
else
    FILENAME="${1%.*}"
fi

# Rimuovi i file temporanei comuni
rm -f "$FILENAME".aux "$FILENAME".bbl "$FILENAME".bcf "$FILENAME".blg "$FILENAME".log "$FILENAME".out "$FILENAME".run.xml "$FILENAME".toc

echo "✅ Pulizia completata."