@echo off
chcp 65001 >nul
color 0B
title Verifica Sistema - LaTeX e Font

echo ╔════════════════════════════════════════╗
echo ║      DIAGNOSTICA SISTEMA LATEX         ║
echo ╚════════════════════════════════════════╝
echo.

echo ═══ VERSIONI INSTALLATE ═══
echo.

:: XeLaTeX
echo XeLaTeX:
xelatex --version | findstr /i "xetex" || echo   ❌ Non trovato

echo.
echo BibTeX:
bibtex --version | findstr /i "bibtex" || echo   ❌ Non trovato

echo.
echo ═══ FONT ARIAL ═══
echo.

:: Verifica Arial
if exist "C:\Windows\Fonts\arial.ttf" (
    echo ✓ arial.ttf trovato
) else (
    echo ❌ arial.ttf NON trovato
)

if exist "C:\Windows\Fonts\arialbd.ttf" (
    echo ✓ arialbd.ttf (Bold) trovato
) else (
    echo ❌ arialbd.ttf NON trovato
)

if exist "C:\Windows\Fonts\ariali.ttf" (
    echo ✓ ariali.ttf (Italic) trovato
) else (
    echo ❌ ariali.ttf NON trovato
)

if exist "C:\Windows\Fonts\arialbi.ttf" (
    echo ✓ arialbi.ttf (Bold Italic) trovato
) else (
    echo ❌ arialbi.ttf NON trovato
)

echo.
echo ═══ DISTRIBUZIONE TEX ═══
echo.

:: Controllo MiKTeX
where miktex-console >nul 2>&1
if %errorlevel% equ 0 (
    echo ✓ MiKTeX installato
    miktex-console --version | findstr /i "miktex"
) else (
    :: Controllo TeX Live
    where tlmgr >nul 2>&1
    if %errorlevel% equ 0 (
        echo ✓ TeX Live installato
        tlmgr --version | findstr /i "texlive"
    ) else (
        echo ⚠ Distribuzione TeX non identificata
    )
)

echo.
echo ═══ FILE PROGETTO ═══
echo.

if exist main.tex (
    echo ✓ main.tex presente
) else (
    echo ❌ main.tex NON trovato
)

if exist capitoli (
    echo ✓ Cartella capitoli\ presente
) else (
    echo ⚠ Cartella capitoli\ NON trovata
)

if exist bibliografia (
    echo ✓ Cartella bibliografia\ presente
) else (
    echo ⚠ Cartella bibliografia\ NON trovata
)

echo.
echo ═══════════════════════════════════════════
echo.
pause