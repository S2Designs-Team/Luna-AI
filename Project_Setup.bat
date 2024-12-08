@echo off
REM Copyright 2022 S2DesignsTeam (??anonimo??).
REM
REM Licensed under the Apache License, Version 2.0 (the "License");
REM you may not use this file except in compliance with the License.
REM You may obtain a copy of the License at
REM
REM      http://www.apache.org/licenses/LICENSE-2.0
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
REM 
REM +---------------------------------------------------------------------------------------------------------------+
REM ฆ TEXT COLORS                                                                                                   ฆ
REM ฆ---------------------------------------------------------------------------------------------------------------ฆ
REM ฆ FORE COLORS                                           ฆ BACKGROUND COLORS                                     ฆ
REM ฆ-------------------------------------------------------+-------------------------------------------------------ฆ   
REM ฆ           DARKER          ฆ           LIGHTER         ฆ           DARKER          ฆ           LIGHTER         ฆ
REM ฆ---------------------------+---------------------------+---------------------------+---------------------------ฆ
REM ฆ COLOR NAME  ฆ  ANSI CODE  ฆ COLOR NAME  ฆ  ANSI CODE  ฆ COLOR NAME  ฆ  ANSI CODE  ฆ COLOR NAME  ฆ  ANSI CODE  ฆ
REM ฆ-------------+-------------+-------------+-------------+-------------+-------------+-------------+-------------ฆ
REM ฆ BLACK       ฆ [30m       ฆ BLACK       ฆ [90m       ฆ             ฆ             ฆ             ฆ             ฆ
REM ฆ RED         ฆ [31m       ฆ RED         ฆ [91m       ฆ             ฆ             ฆ             ฆ             ฆ
REM ฆ GREEN       ฆ [32m       ฆ GREEN       ฆ [92m       ฆ             ฆ             ฆ             ฆ             ฆ
REM ฆ YELLOW      ฆ [33m       ฆ YELLOW      ฆ [93m       ฆ             ฆ             ฆ             ฆ             ฆ
REM ฆ BLUE        ฆ [34m       ฆ BLUE        ฆ [94m       ฆ             ฆ             ฆ             ฆ             ฆ
REM ฆ MAGENTA     ฆ [35m       ฆ MAGENTA     ฆ [95m       ฆ             ฆ             ฆ             ฆ             ฆ
REM ฆ CYAN        ฆ [36m       ฆ CYAN        ฆ [96m       ฆ             ฆ             ฆ             ฆ             ฆ
REM ฆ WHITE       ฆ [37m       ฆ WHITE       ฆ [97m       ฆ             ฆ             ฆ             ฆ             ฆ
REM +---------------------------------------------------------------------------------------------------------------+

echo ษอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออป
echo บ LUNA-AI Project setup procedure                                             บ
echo ศอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออผ
echo La directory corrente e': %CD%
:: Imposta la directory del progetto
set PROJECT_DIR=%CD%
pause

CLS
echo ษอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออป
echo บ Installazione o Aggiornamento di pip...                                     บ
echo ศอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออผ
python -m pip install --upgrade pip
call :CHECK_FAIL
pause

CLS
echo ษอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออป
echo บ Installazione virtualenv...                                                 บ
echo ศอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออผ
echo Installazione virtualenv
python -m pip install virtualenv
call :CHECK_FAIL
pause

CLS
echo ษอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออป
echo บ Creazione dell'environment virtuale per Luna-AI...                          บ
echo ศอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออผ
python -m venv venv
call :CHECK_FAIL
pause

CLS
echo ษอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออป
echo บ Verifico se Git e' inizializzato...                                         บ
echo ศอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออผ
:: Verifica se Git   inizializzato
if not exist ".git" (
    echo Inizializzo il repository Git...
    git init
	call :CHECK_FAIL
)

echo ษอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออป
echo บ Configuro il repository remoto...                                           บ
echo ศอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออผ
:: Configura il repository remoto
git remote remove origin 2>nul
call :CHECK_FAIL

git remote add origin https://github.com/Phobetor1999/LUNA-AI.git
call :CHECK_FAIL

echo ษอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออป
echo บ Verifico la configurazione del repository remoto...                         บ
echo ศอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออผ
:: Verifica la configurazione del repository
git remote -v
call :CHECK_FAIL

:: Crea la directory .vscode se non esiste
echo ษอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออป
echo บ Creazione del File settings.json di vscode per il progetto Luna-AI...       บ
echo ศอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออผ
if not exist ".vscode" (
    mkdir .vscode
	call :CHECK_FAIL
)
:: Scrive il file settings.json utilizzato da Visual Studio Code
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
pause

CLS
echo ษอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออป
echo บ Installazione dei pacchetti richiesti dal progetto Luna-AI e avvio di       บ
echo บ Visual Studio Code.                                                         บ
echo ศอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออผ
call ".\venv\scripts\activate.bat"
call :CHECK_FAIL
pause

python -m pip install --upgrade pip
call :CHECK_FAIL
pause

pip install -r requirements.txt
call :CHECK_FAIL
pause

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