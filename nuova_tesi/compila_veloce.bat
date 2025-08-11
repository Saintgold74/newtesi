@echo off
chcp 65001 >nul
title Compilazione Veloce - Solo XeLaTeX

echo ╔════════════════════════════════════════╗
echo ║     COMPILAZIONE VELOCE (NO BIB)       ║
echo ╚════════════════════════════════════════╝
echo.

xelatex -interaction=nonstopmode main.tex

if exist main.pdf (
    echo ✓ PDF generato
    start "" main.pdf
) else (
    echo ❌ Errore nella compilazione
)

pause