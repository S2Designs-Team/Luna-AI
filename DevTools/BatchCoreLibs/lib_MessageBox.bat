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
REM � Table draw chars                                                                          �
REM �-------------------------------------------------------------------------------------------�
REM � Double lines         � Single line          � Double lined columns �   Double lined rows  �
REM �----------------------+----------------------+----------------------+----------------------�   
REM � Example  � ANSI CHAR � Example  � ANSI CHAR � Example  � ANSI CHAR � Example  � ANSI CHAR �
REM �----------+-----------+----------+-----------+----------+-----------+----------+-----------�
REM � +---+    � ���ͻ     � +---+    � ���Ŀ     � +---+    � ���ķ     � +---+    � ���͸     �
REM � � � �    � � � �     � � � �    � � � �     � � � �    � � � �     � � � �    � � � �     �
REM � �-+-�    � ���͹     � +-+-�    � ���Ĵ     � �-+-�    � ���Ķ     � �-+-�    � ���͵     �
REM � � � �    � � � �     � � � �    � � � �     � � � �    � � � �     � � � �    � � � �     �
REM � +---+    � ���ͼ     � +---+    � �����     � +---+    � ���Ľ     � +---+    � ���;     �
REM +-------------------------------------------------------------------------------------------+

SETLOCAL ENABLEDELAYEDEXPANSION

@echo off
:: Tool per visualizzare messaggi con effetto digitazione
:: Usage: lib_MessageBox.bat <messaggio>

if "%~1"=="" (
    echo Errore: Specificare un messaggio.
    exit /b 1
)

set "message=%~1"

:: Ciclo per visualizzare ogni carattere con effetto di digitazione
for /l %%i in (0,1,255) do (
    set "char=!message:~%%i,1!"
    if "!char!"=="" goto :done
    set /p "=!char!" <nul
    timeout /t 0.1 >nul
)

:done
echo.
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