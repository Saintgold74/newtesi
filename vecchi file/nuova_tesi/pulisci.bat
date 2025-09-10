@echo off
chcp 65001 >nul
title Pulizia File Temporanei

echo ╔════════════════════════════════════════╗
echo ║    PULIZIA FILE TEMPORANEI LATEX       ║
echo ╚════════════════════════════════════════╝
echo.

echo Eliminazione file temporanei...

:: File temporanei LaTeX
del /Q *.aux 2>nul
del /Q *.bbl 2>nul
del /Q *.blg 2>nul
del /Q *.log 2>nul
del /Q *.out 2>nul
del /Q *.toc 2>nul
del /Q *.lof 2>nul
del /Q *.lot 2>nul
del /Q *.synctex.gz 2>nul
del /Q *.xdv 2>nul

:: File bibunits
del /Q bu*.aux 2>nul
del /Q bu*.bbl 2>nul
del /Q bu*.blg 2>nul

:: File temporanei nei capitoli
del /Q capitoli\*.aux 2>nul

echo.
echo ✓ Pulizia completata

:: Chiedi se eliminare anche il PDF
echo.
choice /C SN /M "Eliminare anche main.pdf? (S/N)"
if errorlevel 2 goto :end
if errorlevel 1 del /Q main.pdf 2>nul

:end
echo.
pause