#!/bin/bash

# ==============================================================================
# Script per la compilazione completa di un documento XeLaTeX con Biblatex/Biber
# ==============================================================================

# Controlla se è stato fornito un nome file come argomento
if [ -z "$1" ]; then
    echo "❌ Errore: Nessun file specificato."
    echo "Uso: ./compila.sh nomefile.tex"
    exit 1
fi

# Estrai il nome del file senza l'estensione .tex
FILENAME="${1%.*}"

# Stampa un messaggio di inizio
echo "🚀 Inizio compilazione completa per: $FILENAME.tex"

# --- INIZIO CICLO DI COMPILAZIONE ---

# 1. Prima passata di XeLaTeX per generare i file ausiliari (.aux, .bcf)
xelatex -interaction=nonstopmode "$FILENAME" &&

# 2. Esecuzione di Biber per processare la bibliografia e creare il file .bbl
biber "$FILENAME" &&

# 3. Seconda passata di XeLaTeX per includere la bibliografia e risolvere le citazioni
xelatex -interaction=nonstopmode "$FILENAME" &&

# 4. Terza passata di XeLaTeX per sistemare tutti i riferimenti incrociati (es. numeri di pagina)
xelatex -interaction=nonstopmode "$FILENAME"

# --- FINE CICLO DI COMPILAZIONE ---

# Controlla l'esito finale
if [ $? -eq 0 ]; then
    echo "✅ Compilazione completata con successo: $FILENAME.pdf è pronto."
else
    echo "❌ Errore durante la compilazione. Controlla il file $FILENAME.log per i dettagli."
fi