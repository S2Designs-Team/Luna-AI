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
REM +-------------------------------------------------------------------------------------------------+
REM ¦ Table draw chars                                                                                ¦
REM +-------------------------+----------------------+-------------------------+----------------------+
REM ¦ Double lines            ¦ Single line          ¦ Double lined columns    ¦   Double lined rows  ¦
REM +-------------+-----------+----------+-----------+-------------+-----------+----------+-----------+   
REM ¦ Example     ¦ ANSI CHAR ¦ Example  ¦ ANSI CHAR ¦ Example     ¦ ANSI CHAR ¦ Example  ¦ ANSI CHAR ¦
REM +-------------+-----------+----------+-----------+-------------+-----------+----------+-----------+
REM ¦ ++==++==++  ¦ ÉÍËÍ»     ¦ +--+--+  ¦ ÚÄÂÄ¿     ¦ ++--++--++  ¦ ÖÄÒÄ·     ¦ +===+    ¦ ÕÍÑÍ¸     ¦
REM ¦ ¦¦  ¦¦  ¦¦  ¦ º º º     ¦ ¦  ¦  ¦  ¦ ³ ³ ³     ¦ ¦¦  ¦¦  ¦¦  ¦ º º º     ¦ ¦ ¦ ¦    ¦ ³ ³ ³     ¦
REM ¦ ¦+==++==+¦  ¦ ÌÍÎÍ¹     ¦ +--+--+  ¦ ÃÄÅÄ´     ¦ ¦+--++--+¦  ¦ ÇÄ×Ä¶     ¦ ¦=+=¦    ¦ ÆÍØÍµ     ¦
REM ¦ ¦¦  ¦¦  ¦¦  ¦ º º º     ¦ ¦  ¦  ¦  ¦ ³ ³ ³     ¦ ¦¦  ¦¦  ¦¦  ¦ º º º     ¦ ¦ ¦ ¦    ¦ ³ ³ ³     ¦
REM ¦ ++==++==++  ¦ ÈÍÊÍ¼     ¦ +--+--+  ¦ ÀÄÁÄÙ     ¦ ++--++--++  ¦ ÓÄÐÄ½     ¦ +===+    ¦ ÔÍÏÍ¾     ¦
REM +-------------+-----------+----------+-----------+-------------+-----------+----------+-----------+

SETLOCAL ENABLEDELAYEDEXPANSION

@echo off
:: Percorso della directory corrente di main.bat
set "main_dir=%~dp0"


:: =====================================================================
:: = SHOW MESSAGE ======================================================
:: =====================================================================
:: Percorso del file lib_MessageBox.bat
set "lib_messagebox_path=%main_dir%BatchCoreLibs\lib_MessageBox.bat"

:: Verifica che il file lib_MessageBox.bat esista
if not exist "%lib_messagebox_path%" (
    echo Errore: Il file "%lib_messagebox_path%" non è stato trovato.
    pause
    exit /b 1
)
:: Richiama il file lib_MessageBox.bat per visualizzare il messaggio
call "%lib_messagebox_path%"  "Ciao! Questo è un messaggio con effetto digitazione." > log.log 2>&1
:: Pausa per assicurarsi che il messaggio sia visibile
:: pause  

:: =====================================================================
:: = PLAY VIDEO ========================================================
:: =====================================================================
:: Percorso del file lib_PlayVideo.bat
set "lib_playvideo_path=%main_dir%BatchCoreLibs\lib_PlayVideo.bat"

:: Verifica che il file lib_PlayVideo.bat esista
if not exist "%lib_playvideo_path%" (
    echo Errore: Il file "%lib_playvideo_path%" non è stato trovato.
    pause
    exit /b 1
)

:: Percorso del video
set "video_path=%main_dir%\video001.mp4"

:: Verifica che il file video esista
if not exist "%video_path%" (
    echo Errore: Il file "%video_path%" non è stato trovato.
    pause
    exit /b 1
)

:: Richiama il file lib_PlayVideo.bat per riprodurre il video
call "%lib_playvideo_path%" "%video_path%" > log.log 2>&1

:: Controlla il risultato dell'esecuzione
if errorlevel 1 (
    echo Si è verificato un errore. Controlla il file log.log per maggiori dettagli.
    pause
) else (
    echo Video riprodotto correttamente.
    pause
)

ENDLOCAL
exit /b 0

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
