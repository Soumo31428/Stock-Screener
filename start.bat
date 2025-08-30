@echo off
REM Windows batch file to start the Indian Stock Analysis Dashboard

echo Starting Indian Stock Analysis Dashboard...

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.11 or higher from https://python.org
    pause
    exit /b 1
)

REM Run setup if first time
if not exist "requirements.txt" (
    echo First time setup...
    python setup.py
)

REM Start the dashboard
echo Starting dashboard...
python run.py

pause