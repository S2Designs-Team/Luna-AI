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
REM ฆ Table draw chars                                                                                ฆ
REM +-------------------------+----------------------+-------------------------+----------------------+
REM ฆ Double lines            ฆ Single line          ฆ Double lined columns    ฆ   Double lined rows  ฆ
REM +-------------+-----------+----------+-----------+-------------+-----------+----------+-----------+   
REM ฆ Example     ฆ ANSI CHAR ฆ Example  ฆ ANSI CHAR ฆ Example     ฆ ANSI CHAR ฆ Example  ฆ ANSI CHAR ฆ
REM +-------------+-----------+----------+-----------+-------------+-----------+----------+-----------+
REM ฆ ++==++==++  ฆ ษอหอป     ฆ +--+--+  ฆ ฺฤยฤฟ     ฆ ++--++--++  ฆ ึฤาฤท     ฆ +===+    ฆ ีอัอธ     ฆ
REM ฆ ฆฆ  ฆฆ  ฆฆ  ฆ บ บ บ     ฆ ฆ  ฆ  ฆ  ฆ ณ ณ ณ     ฆ ฆฆ  ฆฆ  ฆฆ  ฆ บ บ บ     ฆ ฆ ฆ ฆ    ฆ ณ ณ ณ     ฆ
REM ฆ ฆ+==++==+ฆ  ฆ ฬอฮอน     ฆ +--+--+  ฆ รฤลฤด     ฆ ฆ+--++--+ฆ  ฆ วฤืฤถ     ฆ ฆ=+=ฆ    ฆ ฦอุอต     ฆ
REM ฆ ฆฆ  ฆฆ  ฆฆ  ฆ บ บ บ     ฆ ฆ  ฆ  ฆ  ฆ ณ ณ ณ     ฆ ฆฆ  ฆฆ  ฆฆ  ฆ บ บ บ     ฆ ฆ ฆ ฆ    ฆ ณ ณ ณ     ฆ
REM ฆ ++==++==++  ฆ ศอสอผ     ฆ +--+--+  ฆ ภฤมฤู     ฆ ++--++--++  ฆ ำฤะฤฝ     ฆ +===+    ฆ ิอฯอพ     ฆ
REM +-------------+-----------+----------+-----------+-------------+-----------+----------+-----------+

SETLOCAL ENABLEDELAYEDEXPANSION
SET "EXECUTION_DIR=%~dp0"

:: Inizializza i formattatori ANSI
call :SET_TEXT_FORMATTERS

:START
cls
echo %fC_Green%ษอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออป
echo %fC_Green%บ%fR%                        %fB%%fU%PROJECT LUNA-AI - BUILDER TOOL%fR%                             %fC_Green%บ
echo %fC_Green%บ%fR%                                                                                   %fC_Green%บ
echo %fC_Green%ฬอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออน
echo %fC_Green%บ%fR% Please choose one of the following procedures:                                    %fC_Green%บ
echo %fC_Green%บ%fR%                                                                                   %fC_Green%บ
echo %fC_Green%ฬอออออยอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออยอออออออน
echo %fC_Green%บ%fR% OPT %fC_Green%ณ%fR% PROCEDURE SHORT DESCRIPTION                                         %fC_Green%ณ%fR%    ?  %fC_Green%บ 
echo %fC_Green%ฬอออออลอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออลอออออออน
echo %fC_Green%บ%fR%   1 %fC_Green%ณ%fR% Package installation                                                %fC_Green%ณ%fR%   H1  %fC_Green%บ
echo %fC_Green%บ%fR%   2 %fC_Green%ณ%fR% Create an archive to distribute (sdist)                             %fC_Green%ณ%fR%   H2  %fC_Green%บ
echo %fC_Green%บ%fR%   3 %fC_Green%ณ%fR% Create a binary package (wheel)                                     %fC_Green%ณ%fR%   H3  %fC_Green%บ
echo %fC_Green%บ%fR%   4 %fC_Green%ณ%fR% Clean all previous build files                                      %fC_Green%ณ%fR%   H4  %fC_Green%บ
echo %fC_Green%บ%fR%   5 %fC_Green%ณ%fR% List all other available commands                                   %fC_Green%ณ%fR%   H5  %fC_Green%บ
echo %fC_Green%บ%fR%   6 %fC_Green%ณ%fR% QUIT                                                                %fC_Green%ณ%fR%       %fC_Green%บ
echo %fC_Green%ฬอออออมอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออมอออออออน
echo %fC_Green%บ CURRENT EXECUTION DIRECTORY: %EXECUTION_DIR%              %fC_Green%บ
echo %fC_Green%ศอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออออผ%fR%
set /p choice=Choose an option(1-6):

if "%choice%"=="1" (
    echo Executing: python .\Scripts\setup.py install
    python .\Scripts\setup.py install
    pause
    goto START
)

if "%choice%"=="2" (
    echo Executing: python .\Scripts\setup.py sdist
    python .\Scripts\setup.py sdist
    pause
    goto START
)

if "%choice%"=="3" (
    echo Executing: python .\Scripts\setup.py bdist_wheel
    python .\Scripts\setup.py bdist_wheel
    pause
    goto START
)

if "%choice%"=="4" (
    echo Executing: python .\Scripts\setup.py clean --all
    python .\Scripts\setup.py clean --all
    pause
    goto START
)

if "%choice%"=="5" (
    echo Executing: python .\Scripts\setup.py --help-commands
    python .\Scripts\setup.py --help-commands
    pause
    goto START
)

if "%choice%"== "6" ( goto end )
if "%choice%"=="H1" ( goto help_h1 )
if "%choice%"=="H2" ( goto help_h2 )
if "%choice%"=="H3" ( goto help_h3 )
if "%choice%"=="H4" ( goto help_h4 )
if "%choice%"=="H5" ( goto help_h5 )

echo Option not valid! Please retry.
pause
goto start

:help_h1
  echo This option will install the package in your Python environment.
  pause
  goto start

:help_h2
  echo This option will create a .tar.gz package file containing the source code of the project (useful for distribution).
  pause
  goto start

:help_h3
  echo This option will generate a .whl file (the standard file format used to distribute Python packages).
  echo This option will also install the 'wheel' package in your python environment if not already installed.
  pause
  goto start

:help_h4
  echo This option will remove all the prevously generated build files.
  pause
  goto start

:help_h5
  echo This option will show all the builder available commands.
  pause
  goto start

:end
  echo Exiting from menu...
  ENDLOCAL 
  exit


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