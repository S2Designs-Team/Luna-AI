@echo off
REM Esegui l'analisi del dump di memoria

REM Vai alla cartella del progetto (se necessario)
cd ..

REM Attiva l'ambiente virtuale (se ne stai usando uno)
call venv\Scripts\activate

REM Esegui lo script di analisi del dump
python .\DevTools\Scripts\ANALYZE_TRACEMALLOC_DUMP_FILE.py

REM Disattiva l'ambiente virtuale (opzionale)
deactivate

pause