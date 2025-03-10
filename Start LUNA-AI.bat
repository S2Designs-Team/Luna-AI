@ECHO OFF
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

:: Initialize ANSI formatters
CALL :SET_TEXT_FORMATTERS
ECHO %fC_Green%ษอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออป%fR% 
ECHO %fC_Green%บ%fR%                              %fB%%fU%START LUNA-AI%fR%                                        %fC_Green%บ%fR% 
ECHO %fC_Green%บ%fR%                                                                                   %fC_Green%บ%fR% 
ECHO %fC_Green%ฬอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออน%fR%
ECHO %fC_Green%บ%fR% Initializing....%fR%                                                                  %fC_Green%บ%fR% 
ECHO %fC_Green%ศอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออผ%fR%
ECHO.
:: Set the project directory
SET PROJECT_DIR=%CD%
CD /d "%~dp0"
ECHO The current directory is: %CD%
PAUSE

CLS
ECHO %fC_Green%ษอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออป%fR% 
ECHO %fC_Green%บ%fR%                              %fB%%fU%START LUNA-AI%fR%                                        %fC_Green%บ%fR% 
ECHO %fC_Green%บ%fR%                                                                                   %fC_Green%บ%fR% 
ECHO %fC_Green%ฬอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออน%fR%
ECHO %fC_Green%บ%fR% Checking if Python is correctly installed....%fR%                                     %fC_Green%บ%fR% 
ECHO %fC_Green%ศอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออผ%fR%
ECHO.
:: Check if Python is installed
CALL :TRY_OR_FAIL "python --version >nul 2>&1" "Python is not installed. Provide a python installation before trying to start LUNA-AI."
PAUSE

CLS
ECHO %fC_Green%ษอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออป%fR% 
ECHO %fC_Green%บ%fR%                              %fB%%fU%START LUNA-AI%fR%                                        %fC_Green%บ%fR% 
ECHO %fC_Green%บ%fR%                                                                                   %fC_Green%บ%fR% 
ECHO %fC_Green%ฬอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออน%fR%
ECHO %fC_Green%บ%fR% Activating LUNA-AI virtual environment....%fR%                                    %fC_Green%บ%fR% 
ECHO %fC_Green%ศอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออผ%fR%
ECHO.
REM CALL :TRY_OR_FAIL "venv\Scripts\activateactivate.bat >>EXECUTE.LOG 2>&1

CLS
ECHO %fC_Green%ษอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออป%fR% 
ECHO %fC_Green%บ%fR%                              %fB%%fU%START LUNA-AI%fR%                                        %fC_Green%บ%fR% 
ECHO %fC_Green%บ%fR%                                                                                   %fC_Green%บ%fR% 
ECHO %fC_Green%ฬอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออน%fR%
ECHO %fC_Green%บ%fR% Launching LUNA-AI....%fR%                                                             %fC_Green%บ%fR% 
ECHO %fC_Green%ศอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออผ%fR%
ECHO.
:: Start the python application entry point
CD /d "%~dp0\Source\"
CALL :TRY_OR_FAIL "python startLuna-AI.py 'console' >>EXECUTE.LOG 2>&1" "Some error occurred trying to start LUNA-AI. Check the log file."
PAUSE

:: Termites this program
EXIT /b


::-------------------------------------------------------------------------------------------------
:: [FUNCTION] -------------------------------------------------------------------------------------
:: Tries to execute the command if it fails prints the relative error message ---------------------
::-------------------------------------------------------------------------------------------------
:TRY_OR_FAIL
    SET "command=%~1"
    SET "errorMsg=%~2"
    SET "maxLen=40"
    SET "offset=0"
    :: Execute the command passed as 1st parameter
    %command%
    IF %ERRORLEVEL% EQU 0 (
       ECHO Done. 
       EXIT /b
    )

    :: Execution failed. Show the error message
    CALL :SHOW_ERROR "%errorMsg%"
EXIT /b

::-------------------------------------------------------------------------------------------------
:: [FUNCTION] -------------------------------------------------------------------------------------
:: Function used to shows the error message -------------------------------------------------------
::-------------------------------------------------------------------------------------------------
:SHOW_ERROR
    SET "msg=%~1"
    SET "maxLen=81"
    SET "offset=0"
    ECHO.
    ECHO.
    ECHO %fC_Red%ษอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออป%fR%
    ECHO %fC_Red%บ ERROR: %fR%                                                                           %fC_Red%บ%fR% 
    ECHO %fC_Red%ฬอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออน%fR%

    :LOOP
        SET "pad=                                                                                   "
  
        REM Estrae una sottostringa di maxLen caratteri usando delayed expansion
        CALL SET "line=%%msg:~%offset%,%maxLen%%%"
        IF "%line%"=="" GOTO EXIT_LOOP
    
        REM Crea la stringa "padded" concatenando il pezzo estratto con il padding e troncandolo a maxLen caratteri
        SET "padded=!line!!pad!"
        SET "padded=!padded:~0,%maxLen%!"
    
        ECHO %fC_Red%บ !padded! %fC_Red%บ%fR%
        SET /A offset+=maxLen
        GOTO LOOP
    :EXIT_LOOP

    ECHO %fC_Red%ศอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออผ%fR%
    ECHO.
EXIT /b

::-------------------------------------------------------------------------------------------------
:: [FUNCTION] -------------------------------------------------------------------------------------
:: Function used to set the text color palette and formatter keywords -----------------------------
::-------------------------------------------------------------------------------------------------
:SET_TEXT_FORMATTERS
  :: Manually define the ANSI escape character.
  for /F %%A in ('"prompt $E & for %%B in (1) do rem"') do set "ESC=%%A"

  :: Character formatting codes
  SET "fR=%ESC%[0m"              :: Reset
  SET "fB=%ESC%[1m"              :: Bold
  SET "fU=%ESC%[4m"              :: Underline
  SET "fI=%ESC%[7m"              :: Inverted

  :: Individual resets (optional)
  SET "fB_=%ESC%[22m"            :: Bold reset
  SET "fU_=%ESC%[24m"            :: Underline reset
  SET "fI_=%ESC%[27m"            :: Inverted reset

  :: Font color formatting codes
  SET "fC_Black=%ESC%[30m"       :: Font color Black
  SET "fC_Red=%ESC%[31m"         :: Font color Red
  SET "fC_Green=%ESC%[32m"       :: Font color Green
  SET "fC_Yellow=%ESC%[33m"      :: Font color Yellow
  SET "fC_Blue=%ESC%[34m"        :: Font color Blue
  SET "fC_Magenta=%ESC%[35m"     :: Font color Magenta
  SET "fC_Cyan=%ESC%[36m"        :: Font color Cyan
  SET "fC_White=%ESC%[37m"       :: Font color White

  :: Light font color formatting codes
  SET "fC_LBlack=%ESC%[90m"      :: Font color Light Black
  SET "fC_LRed=%ESC%[91m"        :: Font color Light Red
  SET "fC_LGreen=%ESC%[92m"      :: Font color Light Green
  SET "fC_LYellow=%ESC%[93m"     :: Font color Light Yellow
  SET "fC_LBlue=%ESC%[94m"       :: Font color Light Blue
  SET "fC_LMagenta=%ESC%[95m"    :: Font color Light Magenta
  SET "fC_LCyan=%ESC%[96m"       :: Font color Light Cyan
  SET "fC_LWhite=%ESC%[97m"      :: Font color Light White
EXIT /b