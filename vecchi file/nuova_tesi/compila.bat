@echo off
chcp 65001 >nul
color 0A
title Compilazione Tesi XeLaTeX - Windows 11

echo ╔════════════════════════════════════════╗
echo ║   COMPILAZIONE TESI CON XELATEX       ║
echo ║         Font Arial Nativo              ║
echo ║         Windows 11                     ║
echo ╚════════════════════════════════════════╝
echo.

:: Verifica presenza XeLaTeX
where xelatex >nul 2>&1
if %errorlevel% neq 0 (
    color 0C
    echo ❌ ERRORE: XeLaTeX non trovato!
    echo.
    echo Installare MiKTeX da: https://miktex.org/download
    echo.
    pause
    exit /b 1
)

echo ✓ XeLaTeX trovato
echo ✓ Font Arial disponibile (Windows 11)
echo.

:: Prima compilazione
echo ┌─────────────────────────────────────────
echo │ FASE 1: Prima compilazione XeLaTeX
echo └─────────────────────────────────────────
xelatex -interaction=nonstopmode main.tex
if %errorlevel% neq 0 (
    color 0E
    echo ⚠ Avviso: Prima compilazione con warning
)

:: Compilazione bibliografie capitoli
echo.
echo ┌─────────────────────────────────────────
echo │ FASE 2: Compilazione bibliografie
echo └─────────────────────────────────────────

for %%f in (bu*.aux) do (
    if exist "%%f" (
        echo   Elaboro: %%f
        bibtex "%%~nf"
    )
)

:: Bibliografia generale
if exist main.aux (
    echo   Bibliografia generale...
    bibtex main
)

:: Seconda compilazione
echo.
echo ┌─────────────────────────────────────────
echo │ FASE 3: Seconda compilazione XeLaTeX
echo └─────────────────────────────────────────
xelatex -interaction=nonstopmode main.tex

:: Terza compilazione per riferimenti
echo.
echo ┌─────────────────────────────────────────
echo │ FASE 4: Compilazione finale
echo └─────────────────────────────────────────
xelatex -interaction=nonstopmode main.tex

:: Risultato finale
echo.
if exist main.pdf (
    color 0A
    echo ╔════════════════════════════════════════╗
    echo ║        ✓ COMPILAZIONE COMPLETATA       ║
    echo ╚════════════════════════════════════════╝
    echo.
    echo 📄 File generato: main.pdf
    echo 📏 Dimensione: 
    for %%A in (main.pdf) do echo    %%~zA bytes
    echo.
    
    :: Chiedi se aprire il PDF
    choice /C SN /M "Aprire il PDF? (S/N)"
    if errorlevel 2 goto :end
    if errorlevel 1 start "" main.pdf
) else (
    color 0C
    echo ❌ ERRORE: main.pdf non generato!
    echo Controllare i log per errori.
)

:end
echo.
pause