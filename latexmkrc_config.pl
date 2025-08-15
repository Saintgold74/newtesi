# .latexmkrc - Configurazione per latexmk
# Posizionare questo file nella directory del progetto

# Usa XeLaTeX come motore di compilazione
$pdf_mode = 5;  # 5 = usa xelatex

# Configurazione XeLaTeX
$xelatex = 'xelatex -synctex=1 -interaction=nonstopmode -file-line-error %O %S';

# Usa Biber per la bibliografia
$biber = 'biber %O %S';
$bibtex_use = 2;  # 2 = usa biber

# Pulisci questi file aggiuntivi
$clean_ext = 'synctex.gz synctex.gz(busy) run.xml tex.bak bbl bcf fdb_latexmk';

# Visualizzatore PDF (Windows)
if ($^O eq 'MSWin32') {
    $pdf_previewer = 'start %O %S';
} elsif ($^O eq 'darwin') {
    # macOS
    $pdf_previewer = 'open %O %S';
} else {
    # Linux
    $pdf_previewer = 'evince %O %S';
}

# Abilita la modalità di anteprima continua (opzionale)
# $preview_continuous_mode = 1;

# Directory di output (opzionale)
# $out_dir = 'build';

# Modalità silenziosa (meno output)
# $silent = 1;

# Numero massimo di iterazioni
$max_repeat = 5;

# Gestione degli errori
$force_mode = 0;  # 0 = ferma su errori, 1 = continua comunque

# Encoding per i file
$xelatex = 'xelatex -synctex=1 -interaction=nonstopmode -file-line-error -output-driver="xdvipdfmx -z 9" %O %S';