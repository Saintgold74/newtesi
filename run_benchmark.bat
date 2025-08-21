@echo off
echo ========================================
echo AVVIO BENCHMARK SISTEMA
echo ========================================
echo.
echo Questo script eseguira' una suite completa di benchmark per testare:
echo - CPU (processore)
echo - RAM (memoria)
echo - DISCO (storage)
echo - Informazioni sistema
echo.
echo Il processo potrebbe richiedere alcuni minuti.
echo Chiudi altre applicazioni per risultati piu' accurati.
echo.
pause

python benchmark_completo.py

echo.
echo ========================================
echo BENCHMARK COMPLETATO
echo ========================================
pause