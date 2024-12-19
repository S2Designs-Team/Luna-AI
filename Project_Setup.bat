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
echo %fC_Green%บ%fR%                           %fB%%fU%LUNA-AI - Environment setup%fR%                             %fC_Green%บ%fR% 
echo %fC_Green%บ%fR%                                                                                   %fC_Green%บ%fR% 
echo %fC_Green%ฬอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออน%fR% 
echo %fC_Green%บ%fR% LUNA-AI Project setup procedure                                                   %fC_Green%บ%fR%
echo %fC_Green%ศอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออผ%fR% 
echo La directory corrente e': %CD%
:: Imposta la directory del progetto
set PROJECT_DIR=%CD%
pause

CLS
echo %fC_Green%ษอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออป%fR% 
echo %fC_Green%บ%fR%                           %fB%%fU%LUNA-AI - Environment setup%fR%                             %fC_Green%บ%fR% 
echo %fC_Green%บ%fR%                                                                                   %fC_Green%บ%fR% 
echo %fC_Green%ฬอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออน%fR% 
echo %fC_Green%บ%fR% Installazione o Aggiornamento di pip...                                           %fC_Green%บ%fR%
echo %fC_Green%ศอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออผ%fR% 
python -m pip install --upgrade pip
call :CHECK_FAIL
echo Fatto.
pause

CLS
echo %fC_Green%ษอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออป%fR% 
echo %fC_Green%บ%fR%                           %fB%%fU%LUNA-AI - Environment setup%fR%                             %fC_Green%บ%fR% 
echo %fC_Green%บ%fR%                                                                                   %fC_Green%บ%fR% 
echo %fC_Green%ฬอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออน%fR% 
echo %fC_Green%บ%fR% Installazione virtualenv...                                                       %fC_Green%บ%fR%
echo %fC_Green%ศอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออผ%fR% 
echo Installazione virtualenv
python -m pip install virtualenv
call :CHECK_FAIL
echo Fatto.
pause

CLS
echo %fC_Green%ษอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออป%fR% 
echo %fC_Green%บ%fR%                           %fB%%fU%LUNA-AI - Environment setup%fR%                             %fC_Green%บ%fR% 
echo %fC_Green%บ%fR%                                                                                   %fC_Green%บ%fR% 
echo %fC_Green%ฬอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออน%fR% 
echo %fC_Green%บ%fR% Creazione dell'environment virtuale per Luna-AI...                                %fC_Green%บ%fR%
echo %fC_Green%ศอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออผ%fR% 
python -m venv venv
call :CHECK_FAIL
echo Fatto.
pause

CLS
echo %fC_Green%ษอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออป%fR% 
echo %fC_Green%บ%fR%                           %fB%%fU%LUNA-AI - Environment setup%fR%                             %fC_Green%บ%fR%  
echo %fC_Green%บ%fR%                                                                                   %fC_Green%บ%fR% 
echo %fC_Green%ฬอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออน%fR% 
echo %fC_Green%บ%fR% Verifico se Git e' inizializzato...                                               %fC_Green%บ%fR%
echo %fC_Green%ศอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออผ%fR% 
:: Verifica se Git   inizializzato
if not exist ".git" (
    echo Inizializzo il repository Git...
    git init
	call :CHECK_FAIL
)

echo %fC_Green%ษอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออป%fR% 
echo %fC_Green%บ%fR%                           %fB%%fU%LUNA-AI - Environment setup%fR%                             %fC_Green%บ%fR% 
echo %fC_Green%บ%fR%                                                                                   %fC_Green%บ%fR% 
echo %fC_Green%ฬอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออน%fR% 
echo %fC_Green%บ%fR% Configuro il repository remoto...                                                 %fC_Green%บ%fR%
echo %fC_Green%ศอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออผ%fR% 
:: Configura il repository remoto
git remote remove origin 2>nul
call :CHECK_FAIL

git remote add origin https://github.com/Phobetor1999/LUNA-AI.git
call :CHECK_FAIL
echo Fatto.
pause

CLS
echo %fC_Green%ษอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออป%fR% 
echo %fC_Green%บ%fR%                           %fB%%fU%LUNA-AI - Environment setup%fR%                             %fC_Green%บ%fR% 
echo %fC_Green%บ%fR%                                                                                   %fC_Green%บ%fR% 
echo %fC_Green%ฬอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออน%fR% 
echo %fC_Green%บ%fR% Verifico la configurazione del repository remoto...                               %fC_Green%บ%fR%
echo %fC_Green%ศอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออผ%fR% 
:: Verifica la configurazione del repository
git remote -v
call :CHECK_FAIL
echo Fatto.
pause

CLS
echo %fC_Green%ษอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออป%fR% 
echo %fC_Green%บ%fR%                           %fB%%fU%LUNA-AI - Environment setup%fR%                             %fC_Green%บ%fR% 
echo %fC_Green%บ%fR%                                                                                   %fC_Green%บ%fR% 
echo %fC_Green%ฬอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออน%fR% 
echo %fC_Green%บ%fR% Preparazione dei settaggi dell'ambiente di sviluppo (Visual Studio Code)...       %fC_Green%บ%fR%
echo %fC_Green%ศอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออผ%fR% 

:: Crea la directory .vscode se non esiste
if not exist ".vscode" (
    mkdir .vscode
	call :CHECK_FAIL
)


echo %fC_Green%ษอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออป%fR% 
echo %fC_Green%บ%fR%                           %fB%%fU%LUNA-AI - Environment setup%fR%                             %fC_Green%บ%fR%  
echo %fC_Green%บ%fR%                                                                                   %fC_Green%บ%fR% 
echo %fC_Green%ฬอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออน%fR% 
echo %fC_Green%บ%fR% Creazione del File settings.json di vscode per il progetto Luna-AI...             %fC_Green%บ%fR%
echo %fC_Green%ศอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออผ%fR%  
:: Scrive il file settings.json utilizzato da Visual Studio Code (se esiste viene sovrascritto)
(
echo {
echo     "git.remote": "origin",
echo     "git.url": "https://github.com/Phobetor1999/LUNA-AI.git",
echo     "python.pythonPath": "venv\\Scripts\\python.exe",
echo     "python.envFile": "${workspaceFolder}\\.env",
echo     "python.formatting.provider": "black",
echo     "python.terminal.activateEnvInCurrentTerminal": true,
echo     "editor.formatOnSave": true,
echo     "files.exclude": {
echo        "**/__pycache__": true,
echo        "**/*.pyc": true
echo     },
echo     "python.createEnvironment.contentButton": "show",
echo     "python.linting.enabled": true,
echo     "python.linting.pylintEnabled": true,
echo     "python.linting.pylintArgs": [
echo         "--disable=C0111" 
echo     ]
echo }
) > .vscode\settings.json
echo File settings.json creato con successo nella cartella .vscode!
call :CHECK_FAIL
echo Fatto.
pause

CLS
echo %fC_Green%ษอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออป%fR% 
echo %fC_Green%บ%fR%                           %fB%%fU%LUNA-AI - Environment setup%fR%                             %fC_Green%บ%fR% 
echo %fC_Green%บ%fR%                                                                                   %fC_Green%บ%fR% 
echo %fC_Green%ฬอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออน%fR% 
echo %fC_Green%บ%fR% Creazione del File launch.json di vscode per il progetto Luna-AI...               %fC_Green%บ%fR%
echo %fC_Green%ศอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออผ%fR% 
:: Scrive il file launch.json utilizzato da Visual Studio Code (se esiste viene sovrascritto)
(
echo {
echo    "version": "0.2.0",
echo    "configurations": [
echo        {
echo            "name":          "DEV-Debug: Luna-AI console",
echo            "type":          "debugpy",
echo            "request":       "launch",
echo            "program":       "./startLuna-AI.py",
echo            "console":       "integratedTerminal",
echo            "justMyCode":    false,
echo            "preLaunchTask": "clear-terminal",
echo            "args":          ["console"]
echo        },
echo        {
echo            "name":          "DEV-Debug: Luna-AI GUI",
echo            "type":          "debugpy",
echo            "request":       "launch",
echo            "program":       "./startLuna-AI.py",
echo            "console":       "integratedTerminal",
echo            "justMyCode":    false,
echo            "preLaunchTask": "clear-terminal",
echo            "args":          ["GUI"]
echo        },
echo        {
echo            "name":          "Debug-File",
echo            "type":          "debugpy",
echo            "request":       "launch",
echo            "program":       "${file}"
echo        }
echo    ]
echo }
) > .vscode\launch.json
echo File launch.json creato con successo nella cartella .vscode!
call :CHECK_FAIL
echo Fatto.
pause

CLS
echo %fC_Green%ษอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออป%fR% 
echo %fC_Green%บ%fR%                           %fB%%fU%LUNA-AI - Environment setup%fR%                             %fC_Green%บ%fR% 
echo %fC_Green%บ%fR%                                                                                   %fC_Green%บ%fR% 
echo %fC_Green%ฬอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออน%fR% 
echo %fC_Green%บ%fR% Creazione del File tasks.json di vscode per il progetto Luna-AI...                %fC_Green%บ%fR%
echo %fC_Green%ศอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออผ%fR% 
:: Scrive il file tasks.json utilizzato da Visual Studio Code (se esiste viene sovrascritto)
(
echo {
echo    "version": "2.0.0",
echo	"tasks": [
echo        {
echo            "label":          "clear-terminal",
echo            "type":           "shell",
echo            "command":        "cls", // Per Windows usa cls, per Linux/macOS usa clear
echo            "problemMatcher": []
echo        }
echo    ]
echo }
) > .vscode\tasks.json
echo File tasks.json creato con successo nella cartella .vscode!
call :CHECK_FAIL
echo Fatto.
pause

CLS
echo %fC_Green%ษอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออป%fR% 
echo %fC_Green%บ%fR%                           %fB%%fU%LUNA-AI - Environment setup%fR%                             %fC_Green%บ%fR% 
echo %fC_Green%บ%fR%                                                                                   %fC_Green%บ%fR% 
echo %fC_Green%ฬอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออน%fR% 
echo %fC_Green%บ%fR% Installazione dei pacchetti richiesti dal progetto Luna-AI                        %fC_Green%บ%fR%
echo %fC_Green%ศอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออผ%fR%  
call ".\venv\scripts\activate.bat"
call :CHECK_FAIL
pause

python -m pip install --upgrade pip
call :CHECK_FAIL
pause

pip install -r requirements.txt
call :CHECK_FAIL
echo Fatto.
pause

CLS
echo %fC_Green%ษอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออป%fR% 
echo %fC_Green%บ%fR%                           %fB%%fU%LUNA-AI - Environment setup%fR%                             %fC_Green%บ%fR% 
echo %fC_Green%บ%fR%                                                                                   %fC_Green%บ%fR% 
echo %fC_Green%ฬอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออน%fR% 
echo %fC_Greenบ%fR% Apertura del progetto Luna-AI con Visual Studio Code.                              %fC_Green%บ%fR% 
echo %fC_Green%ศอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออผ%fR% 
start "" && code %PROJECT_DIR% :0

REM start "" && .\venv\Scripts\activate.bat && python -m pip install --upgrade pip &&  pip install -r requirements.txt && code %PROJECT_DIR% | .\venv\Scripts\activate.bat :0
goto :eof

:: /// check if the app has failed
:CHECK_FAIL
if NOT ["%errorlevel%"]==["0"] (
    pause
    exit /b %errorlevel%
)
goto :eof 


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