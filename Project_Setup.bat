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

REM table draw chars 
REM +---+    ษอหอป
REM ฆ + ฆ    ฬ ฮ น
REM +---+    ศอสอผ
REM - ฆ    อ บ

echo ษออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออป
echo บ LUNA-AI Project setup procedure                                            บ
echo ศออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออผ
echo La directory corrente e': %CD%
:: Imposta la directory del progetto
set PROJECT_DIR=%CD%
pause

CLS
echo ษออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออป
echo บ Installazione o Aggiornamento di pip...                                    บ
echo ศออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออผ
python -m pip install --upgrade pip
pause

CLS
echo ษออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออป
echo บ Installazione virtualenv...                                                บ
echo ศออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออผ
echo Installazione virtualenv
python -m pip install virtualenv
pause

CLS
echo ษออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออป
echo บ Creazione dell'environment virtuale per Luna-AI...                         บ
echo ศออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออผ
python -m venv venv
pause

CLS
echo ษออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออป
echo บ Verifico se Git e' inizializzato...                                        บ
echo ศออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออผ
:: Verifica se Git ่ inizializzato
if not exist ".git" (
    echo Inizializzo il repository Git...
    git init
)


echo ษออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออป
echo บ Configuro il repository remoto...                                          บ
echo ศออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออผ
:: Configura il repository remoto
git remote remove origin 2>nul
git remote add origin https://github.com/Phobetor1999/LUNA-AI.git

echo ษออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออป
echo บ Verifico la configurazione del repository remoto...                        บ
echo ศออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออผ
:: Verifica la configurazione del repository
git remote -v

echo 
:: Crea la directory .vscode se non esiste
echo ษออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออป
echo บ Creazione del File settings.json di vscode per il progetto Luna-AI...      บ
echo ศออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออผ
if not exist ".vscode" (
    mkdir .vscode
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
pause

CLS
echo Installazione dei pacchetti richiesti dal progetto Luna-AI e avvio di Visual Studio Code
@Call .\venv\Scripts\activate.bat
pause
python -m pip install --upgrade pip
pause
pip install -r requirements.txt
pause
start "" && code %PROJECT_DIR% :0

REM start "" && .\venv\Scripts\activate.bat && python -m pip install --upgrade pip &&  pip install -r requirements.txt && code %PROJECT_DIR% | .\venv\Scripts\activate.bat :0

GOTO EOF

:: /// check if the app has failed
:CHECK_FAIL
[AT]echo off
if NOT ["%errorlevel%"]==["0"] (
    pause
    exit /b %errorlevel%
)