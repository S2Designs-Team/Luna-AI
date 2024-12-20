@echo off
REM Copyright 2022 S2DesignsTeam (anonimo).
REM
REM Licensed under the Apache License, Version 2.0 (the "License");
REM you may not use this file except in compliance with the License.
REM You may obtain a copy of the License at
REM
REM      http://www.apache.org/licenses/LICENSE-2.0
REM 
REM The above copyright notice and this permission notice shall be included 
REM in all copies or substantial portions of the Software.
REM
REM Unless required by applicable law or agreed to in writing, software
REM distributed under the License is distributed on an "AS IS" BASIS,
REM WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
REM See the License for the specific language governing permissions and
REM limitations under the License.
REM 
REM +-------------------------------------------------------------------------------------------+
REM ฆ Table draw chars                                                                          ฆ
REM ฆ-------------------------------------------------------------------------------------------ฆ
REM ฆ Double lines         ฆ Single line          ฆ Double lined columns ฆ   Double lined rows  ฆ
REM ฆ----------------------+----------------------+----------------------+----------------------ฆ   
REM ฆ Example  ฆ ANSI CHAR ฆ Example  ฆ ANSI CHAR ฆ Example  ฆ ANSI CHAR ฆ Example  ฆ ANSI CHAR ฆ
REM ฆ----------+-----------+----------+-----------+----------+-----------+----------+-----------ฆ
REM ฆ +---+    ฆ ษอหอป     ฆ +---+    ฆ ฺฤยฤฟ     ฆ +---+    ฆ ึฤาฤท     ฆ +---+    ฆ ีอัอธ     ฆ
REM ฆ ฆ ฆ ฆ    ฆ บ บ บ     ฆ ฆ ฆ ฆ    ฆ ณ ณ ณ     ฆ ฆ ฆ ฆ    ฆ บ บ บ     ฆ ฆ ฆ ฆ    ฆ ณ ณ ณ     ฆ
REM ฆ ฆ-+-ฆ    ฆ ฬอฮอน     ฆ +-+-ฆ    ฆ รฤลฤด     ฆ ฆ-+-ฆ    ฆ วฤืฤถ     ฆ ฆ-+-ฆ    ฆ ฦอุอต     ฆ
REM ฆ ฆ ฆ ฆ    ฆ บ บ บ     ฆ ฆ ฆ ฆ    ฆ ณ ณ ณ     ฆ ฆ ฆ ฆ    ฆ บ บ บ     ฆ ฆ ฆ ฆ    ฆ ณ ณ ณ     ฆ
REM ฆ +---+    ฆ ศอสอผ     ฆ +---+    ฆ ภฤมฤู     ฆ +---+    ฆ ำฤะฤฝ     ฆ +---+    ฆ ิอฯอพ     ฆ
REM +-------------------------------------------------------------------------------------------+

SETLOCAL ENABLEDELAYEDEXPANSION

:: Inizializza i formattatori ANSI
call :SET_TEXT_FORMATTERS

echo %fC_Green%ษอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออป%fR% 
echo %fC_Green%บ%fR%                         %fB%%fU%LUNA-AI - MEMORY ALLOCATION%fR%                               %fC_Green%บ%fR% 
echo %fC_Green%บ%fR%                                                                                   %fC_Green%บ%fR% 
echo %fC_Green%ศอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออผ%fR% 
echo La directory corrente e': %CD%
:: Imposta la directory del progetto
set BATCH_DIR=%CD%
PAUSE

REM Esegui l'analisi del dump di memoria

REM Vai alla cartella del progetto (se necessario)
cd ..

REM Attiva l'ambiente virtuale (se ne stai usando uno)
call venv\Scripts\activate

REM Esegui lo script di analisi del dump
python .\DevTools\Scripts\ANALYZE_TRACEMALLOC_DUMP_FILE.py "%CD%\DevTools\TraceMAlloc_dumps\LunaTraceMAlloc.pkl"
PAUSE

REM Disattiva l'ambiente virtuale (opzionale)
deactivate
PAUSE

ENDLOCAL
GOTO :EOF 


:SET_TEXT_FORMATTERS
  :: Definisci il carattere di escape ANSI manualmente
  for /F %%A in ('"prompt $E & for %%B in (1) do rem"') do set "ESC=%%A"

  :: Codici di formattazione carattere
  set "fR=%ESC%[0m"              :: Reset
  set "fB=%ESC%[1m"              :: Bold
  set "fU=%ESC%[4m"              :: Underline
  set "fI=%ESC%[7m"              :: Inverted

  :: Reset individuali (opzionali)
  set "fB_=%ESC%[22m"            :: Bold reset
  set "fU_=%ESC%[24m"            :: Underline reset
  set "fI_=%ESC%[27m"            :: Inverted reset

  :: Codici di formattazione colore font
  set "fC_Black=%ESC%[30m"       :: Font color Black
  set "fC_Red=%ESC%[31m"         :: Font color Red
  set "fC_Green=%ESC%[32m"       :: Font color Green
  set "fC_Yellow=%ESC%[33m"      :: Font color Yellow
  set "fC_Blue=%ESC%[34m"        :: Font color Blue
  set "fC_Magenta=%ESC%[35m"     :: Font color Magenta
  set "fC_Cyan=%ESC%[36m"        :: Font color Cyan
  set "fC_White=%ESC%[37m"       :: Font color White

  :: Codici di formattazione colore font chiaro
  set "fC_LBlack=%ESC%[90m"      :: Font color Light Black
  set "fC_LRed=%ESC%[91m"        :: Font color Light Red
  set "fC_LGreen=%ESC%[92m"      :: Font color Light Green
  set "fC_LYellow=%ESC%[93m"     :: Font color Light Yellow
  set "fC_LBlue=%ESC%[94m"       :: Font color Light Blue
  set "fC_LMagenta=%ESC%[95m"    :: Font color Light Magenta
  set "fC_LCyan=%ESC%[96m"       :: Font color Light Cyan
  set "fC_LWhite=%ESC%[97m"      :: Font color Light White
