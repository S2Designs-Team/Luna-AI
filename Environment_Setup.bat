@echo off
REM Copyright 2022 S2DesignsTeam (anonimo).
REM
REM Licensed under the Creative Common Attribution-NonCommercial 4.0 
REM International (the "License");
REM you may not use this file except in compliance with the License.
REM You may obtain a copy of the License at
REM
REM      https://creativecommons.org/licenses/by/4.0/legalcode.txt
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
REM � Table draw chars                                                                                �
REM +-------------------------+----------------------+-------------------------+----------------------+
REM � Double lines            � Single line          � Double lined columns    �   Double lined rows  �
REM +-------------+-----------+----------+-----------+-------------+-----------+----------+-----------+   
REM � Example     � ANSI CHAR � Example  � ANSI CHAR � Example     � ANSI CHAR � Example  � ANSI CHAR �
REM +-------------+-----------+----------+-----------+-------------+-----------+----------+-----------+
REM � ++==++==++  � ���ͻ     � +--+--+  � ���Ŀ     � ++--++--++  � ���ķ     � +===+    � ���͸     �
REM � ��  ��  ��  � � � �     � �  �  �  � � � �     � ��  ��  ��  � � � �     � � � �    � � � �     �
REM � �+==++==+�  � ���͹     � +--+--+  � ���Ĵ     � �+--++--+�  � ���Ķ     � �=+=�    � ���͵     �
REM � ��  ��  ��  � � � �     � �  �  �  � � � �     � ��  ��  ��  � � � �     � � � �    � � � �     �
REM � ++==++==++  � ���ͼ     � +--+--+  � �����     � ++--++--++  � ���Ľ     � +===+    � ���;     �
REM +-------------+-----------+----------+-----------+-------------+-----------+----------+-----------+

SETLOCAL ENABLEDELAYEDEXPANSION

:: Initialize ANSI formatters
call :SET_TEXT_FORMATTERS

echo %fC_Green%����������������������������������������������������������������������������������ͻ%fR% 
echo %fC_Green%�%fR%                           %fB%%fU%LUNA-AI - Environment setup%fR%                            %fC_Green%�%fR% 
echo %fC_Green%�%fR%                                                                                  %fC_Green%�%fR% 
echo %fC_Green%����������������������������������������������������������������������������������͹%fR% 
echo %fC_Green%�%fR% LUNA-AI Project setup procedure                                                  %fC_Green%�%fR%
echo %fC_Green%����������������������������������������������������������������������������������ͼ%fR% 
echo The current directory is: %CD%
:: Set the project directory
set PROJECT_DIR=%CD%
pause

CLS
echo %fC_Green%����������������������������������������������������������������������������������ͻ%fR%
echo %fC_Green%�%fR%                           %fB%%fU%LUNA-AI - Environment setup%fR%                            %fC_Green%�%fR% 
echo %fC_Green%�%fR%                                                                                  %fC_Green%�%fR% 
echo %fC_Green%����������������������������������������������������������������������������������͹%fR%
echo %fC_Green%�%fR% LUNA-AI checking if Python is correctly installed....                            %fC_Green%�%fR%
echo %fC_Green%����������������������������������������������������������������������������������ͼ%fR%
:: Check if Python is installed
python --version >nul 2>&1
call :CHECK_FAIL
echo Done.
pause

CLS
echo %fC_Green%����������������������������������������������������������������������������������ͻ%fR%
echo %fC_Green%�%fR%                           %fB%%fU%LUNA-AI - Environment setup%fR%                            %fC_Green%�%fR% 
echo %fC_Green%�%fR%                                                                                  %fC_Green%�%fR% 
echo %fC_Green%����������������������������������������������������������������������������������͹%fR%
echo %fC_Green%�%fR% LUNA-AI checking if Git is correctly installed....                               %fC_Green%�%fR%
echo %fC_Green%����������������������������������������������������������������������������������ͼ%fR% 
:: Check if Git is installed
git --version >nul 2>&1
call :CHECK_FAIL
echo Done.
pause

CLS
echo %fC_Green%����������������������������������������������������������������������������������ͻ%fR%
echo %fC_Green%�%fR%                           %fB%%fU%LUNA-AI - Environment setup%fR%                            %fC_Green%�%fR% 
echo %fC_Green%�%fR%                                                                                  %fC_Green%�%fR% 
echo %fC_Green%����������������������������������������������������������������������������������͹%fR%
echo %fC_Green%�%fR% Installation or Update of pip...                                                 %fC_Green%�%fR%
echo %fC_Green%����������������������������������������������������������������������������������ͼ%fR% 
python -m pip install --upgrade pip
call :CHECK_FAIL
echo Done.
pause

CLS
echo %fC_Green%����������������������������������������������������������������������������������ͻ%fR%
echo %fC_Green%�%fR%                           %fB%%fU%LUNA-AI - Environment setup%fR%                            %fC_Green%�%fR% 
echo %fC_Green%�%fR%                                                                                  %fC_Green%�%fR% 
echo %fC_Green%����������������������������������������������������������������������������������͹%fR%
echo %fC_Green%�%fR% Installation of virtualenv...                                                    %fC_Green%�%fR%
echo %fC_Green%����������������������������������������������������������������������������������ͼ%fR% 
python -m pip install virtualenv
call :CHECK_FAIL
echo Done.
pause

CLS
echo %fC_Green%����������������������������������������������������������������������������������ͻ%fR%
echo %fC_Green%�%fR%                           %fB%%fU%LUNA-AI - Environment setup%fR%                            %fC_Green%�%fR% 
echo %fC_Green%�%fR%                                                                                  %fC_Green%�%fR% 
echo %fC_Green%����������������������������������������������������������������������������������͹%fR%
echo %fC_Green%�%fR% Creating of the virtual environment for Luna-AI...                               %fC_Green%�%fR%
echo %fC_Green%����������������������������������������������������������������������������������ͼ%fR% 
python -m venv venv
call :CHECK_FAIL
echo Done.
pause

CLS
echo %fC_Green%����������������������������������������������������������������������������������ͻ%fR%
echo %fC_Green%�%fR%                           %fB%%fU%LUNA-AI - Environment setup%fR%                            %fC_Green%�%fR%  
echo %fC_Green%�%fR%                                                                                  %fC_Green%�%fR% 
echo %fC_Green%����������������������������������������������������������������������������������͹%fR%
echo %fC_Green%�%fR% Checking if Git is initialized...                                                %fC_Green%�%fR%
echo %fC_Green%����������������������������������������������������������������������������������ͼ%fR% 
if not exist ".git" (
    echo Initializing Git repository...
    git init
	call :CHECK_FAIL
)

echo %fC_Green%����������������������������������������������������������������������������������ͻ%fR%
echo %fC_Green%�%fR%                           %fB%%fU%LUNA-AI - Environment setup%fR%                            %fC_Green%�%fR% 
echo %fC_Green%�%fR%                                                                                  %fC_Green%�%fR% 
echo %fC_Green%����������������������������������������������������������������������������������͹%fR%
echo %fC_Green%�%fR% Configuring the remote repository...                                             %fC_Green%�%fR%
echo %fC_Green%����������������������������������������������������������������������������������ͼ%fR% 
:: Remove all the alreadydefined remote gits from the .git/config file
for /f "delims=" %%i in ('git remote') do git remote remove %%i
echo Existing Git remote repositories successfully removed!
call :CHECK_FAIL

git remote add S2DesignsTeam https://github.com/S2Designs-Team/Luna-AI.git
call :CHECK_FAIL
echo Successfully added the "S2DesignsTeam Luna-AI" remote repository definition in ".git/config"!

git remote add Phobetor1999 https://github.com/Phobetor1999/Luna-AI.git
call :CHECK_FAIL
echo Successfully added the "Phobetor1999 Luna-AI" remote repository definition in ".git/config"!
echo Done.
pause

CLS
echo %fC_Green%����������������������������������������������������������������������������������ͻ%fR%
echo %fC_Green%�%fR%                           %fB%%fU%LUNA-AI - Environment setup%fR%                            %fC_Green%�%fR% 
echo %fC_Green%�%fR%                                                                                  %fC_Green%�%fR% 
echo %fC_Green%����������������������������������������������������������������������������������͹%fR%
echo %fC_Green%�%fR% Verifying the remote repository configuration...                                 %fC_Green%�%fR%
echo %fC_Green%����������������������������������������������������������������������������������ͼ%fR% 
git remote -v
call :CHECK_FAIL
echo Done.
pause

CLS
echo %fC_Green%����������������������������������������������������������������������������������ͻ%fR%
echo %fC_Green%�%fR%                           %fB%%fU%LUNA-AI - Environment setup%fR%                            %fC_Green%�%fR% 
echo %fC_Green%�%fR%                                                                                  %fC_Green%�%fR% 
echo %fC_Green%����������������������������������������������������������������������������������͹%fR%
echo %fC_Green%�%fR% Preparing the development environment settings (Visual Studio Code)...           %fC_Green%�%fR%
echo %fC_Green%����������������������������������������������������������������������������������ͼ%fR% 
:: Creates the .vscode subdirectory if it does not exists
if not exist ".vscode" (
    mkdir .vscode
	call :CHECK_FAIL
)


echo %fC_Green%����������������������������������������������������������������������������������ͻ%fR%
echo %fC_Green%�%fR%                           %fB%%fU%LUNA-AI - Environment setup%fR%                            %fC_Green%�%fR%  
echo %fC_Green%�%fR%                                                                                  %fC_Green%�%fR% 
echo %fC_Green%����������������������������������������������������������������������������������͹%fR%
echo %fC_Green%�%fR% Creating the vscode 'settings.json' file for the Luna-AI project...              %fC_Green%�%fR%
echo %fC_Green%����������������������������������������������������������������������������������ͼ%fR% 
:: Writes the settings.json file used by Visual Studio Code (if it already exists it will be overwritten)
(
echo {
echo     "git.remote": "origin",
echo     "git.url": "https://github.com/S2Designs-Team/Luna-AI.git",
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
echo Settings.json file successfully created in the .vscode folder!
call :CHECK_FAIL
echo Done.
pause

CLS
echo %fC_Green%����������������������������������������������������������������������������������ͻ%fR%
echo %fC_Green%�%fR%                           %fB%%fU%LUNA-AI - Environment setup%fR%                            %fC_Green%�%fR% 
echo %fC_Green%�%fR%                                                                                  %fC_Green%�%fR% 
echo %fC_Green%����������������������������������������������������������������������������������͹%fR%
echo %fC_Green%�%fR% Creating the vscode 'launch.json' file for the Luna-AI project...                %fC_Green%�%fR%
echo %fC_Green%����������������������������������������������������������������������������������ͼ%fR% 
:: Writes the launch.json file used by Visual Studio Code (if already existing it will be overwritten)
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
echo launch.json file successfully created in the .vscode folder!
call :CHECK_FAIL
echo Done.
pause

CLS
echo %fC_Green%����������������������������������������������������������������������������������ͻ%fR%
echo %fC_Green%�%fR%                           %fB%%fU%LUNA-AI - Environment setup%fR%                            %fC_Green%�%fR% 
echo %fC_Green%�%fR%                                                                                  %fC_Green%�%fR% 
echo %fC_Green%����������������������������������������������������������������������������������͹%fR%
echo %fC_Green%�%fR% Creating the vscode 'tasks.json' file for the Luna-AI project...                 %fC_Green%�%fR%
echo %fC_Green%����������������������������������������������������������������������������������ͼ%fR% 
:: Writes the tasks.json file used by Visual Studio Code (if already existing it will be overwritten)
(
echo {
echo    "version": "2.0.0",
echo	"tasks": [
echo        {
echo            "label":          "clear-terminal",
echo            "type":           "shell",
echo            "command":        "cls", // In Windows use cls, in Linux/macOS use clear
echo            "problemMatcher": []
echo        }
echo    ]
echo }
) > .vscode\tasks.json
echo tasks.json file successfully created in the .vscode folder!
call :CHECK_FAIL
echo Done.
pause

CLS
echo %fC_Green%����������������������������������������������������������������������������������ͻ%fR%
echo %fC_Green%�%fR%                           %fB%%fU%LUNA-AI - Environment setup%fR%                            %fC_Green%�%fR% 
echo %fC_Green%�%fR%                                                                                  %fC_Green%�%fR% 
echo %fC_Green%����������������������������������������������������������������������������������͹%fR%
echo %fC_Green%�%fR% Installing the packages required by the Luna-AI project                          %fC_Green%�%fR%
echo %fC_Green%����������������������������������������������������������������������������������ͼ%fR% 
call ".\venv\scripts\activate.bat"
call :CHECK_FAIL
pause

python -m pip install --upgrade pip
call :CHECK_FAIL
pause

pip install -r requirements.txt
call :CHECK_FAIL
echo Done.
pause

CLS
echo %fC_Green%����������������������������������������������������������������������������������ͻ%fR%
echo %fC_Green%�%fR%                           %fB%%fU%LUNA-AI - Environment setup%fR%                            %fC_Green%�%fR% 
echo %fC_Green%�%fR%                                                                                  %fC_Green%�%fR% 
echo %fC_Green%����������������������������������������������������������������������������������͹%fR%
echo %fC_Green%�%fR% Opening the Luna-AI project with Visual Studio Code.                             %fC_Green%�%fR% 
echo %fC_Green%����������������������������������������������������������������������������������ͼ%fR% 
start "" && code %PROJECT_DIR% :0

REM start "" && .\venv\Scripts\activate.bat && python -m pip install --upgrade pip &&  pip install -r requirements.txt && code %PROJECT_DIR% | .\venv\Scripts\activate.bat :0
goto :eof

:: Checks if the app has failed
:CHECK_FAIL
if NOT ["%errorlevel%"]==["0"] (
    pause
    exit /b %errorlevel%
)
goto :eof 


:SET_TEXT_FORMATTERS
  :: Manually define the ANSI escape character.
  for /F %%A in ('"prompt $E & for %%B in (1) do rem"') do set "ESC=%%A"

  :: Character formatting codes
  set "fR=%ESC%[0m"              :: Reset
  set "fB=%ESC%[1m"              :: Bold
  set "fU=%ESC%[4m"              :: Underline
  set "fI=%ESC%[7m"              :: Inverted

  :: Individual resets (optional)
  set "fB_=%ESC%[22m"            :: Bold reset
  set "fU_=%ESC%[24m"            :: Underline reset
  set "fI_=%ESC%[27m"            :: Inverted reset

  :: Font color formatting codes
  set "fC_Black=%ESC%[30m"       :: Font color Black
  set "fC_Red=%ESC%[31m"         :: Font color Red
  set "fC_Green=%ESC%[32m"       :: Font color Green
  set "fC_Yellow=%ESC%[33m"      :: Font color Yellow
  set "fC_Blue=%ESC%[34m"        :: Font color Blue
  set "fC_Magenta=%ESC%[35m"     :: Font color Magenta
  set "fC_Cyan=%ESC%[36m"        :: Font color Cyan
  set "fC_White=%ESC%[37m"       :: Font color White

  :: Light font color formatting codes
  set "fC_LBlack=%ESC%[90m"      :: Font color Light Black
  set "fC_LRed=%ESC%[91m"        :: Font color Light Red
  set "fC_LGreen=%ESC%[92m"      :: Font color Light Green
  set "fC_LYellow=%ESC%[93m"     :: Font color Light Yellow
  set "fC_LBlue=%ESC%[94m"       :: Font color Light Blue
  set "fC_LMagenta=%ESC%[95m"    :: Font color Light Magenta
  set "fC_LCyan=%ESC%[96m"       :: Font color Light Cyan
  set "fC_LWhite=%ESC%[97m"      :: Font color Light White