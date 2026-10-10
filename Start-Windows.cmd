@echo off
setlocal
cd /d "%~dp0"
title GNT Order Converter

if exist ".venv\Scripts\python.exe" goto checkdeps
py -3 -c "import sys; sys.exit(0 if sys.version_info >= (3, 10) else 1)" >nul 2>&1
if not errorlevel 1 (
    py -3 -m venv .venv
    if errorlevel 1 goto failed
    goto checkdeps
)
python -c "import sys; sys.exit(0 if sys.version_info >= (3, 10) else 1)" >nul 2>&1
if not errorlevel 1 (
    python -m venv .venv
    if errorlevel 1 goto failed
    goto checkdeps
)
echo Python 3.10 or newer is required.
echo Install Python from https://www.python.org/downloads/windows/
echo Select "Add python.exe to PATH", then run this file again.
pause
exit /b 1

:checkdeps
fc /b requirements.txt .venv\installed-requirements.txt >nul 2>&1
if not errorlevel 1 goto run
echo Preparing dependencies. Internet access is required on first use.
".venv\Scripts\python.exe" -m pip install -r requirements.txt
if errorlevel 1 goto failed
copy /y requirements.txt .venv\installed-requirements.txt >nul

:run
echo Opening GNT Order Converter in your browser.
echo Keep this window open while using the tool. Close it to stop.
".venv\Scripts\python.exe" app.py --open-browser
if errorlevel 1 goto failed
exit /b 0

:failed
echo Setup or startup failed. Please share the error message above.
pause
exit /b 1
