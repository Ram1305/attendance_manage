@echo off
echo ========================================
echo Starting Backend in PRODUCTION Mode
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found!
    echo.
    echo Please install Python 3.8+ from:
    echo https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

cd backend

echo Installing/Updating dependencies...
python -m pip install -r requirements.txt --quiet

if errorlevel 1 (
    echo.
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo ========================================
echo Starting Production Server...
echo Server: http://localhost:5000
echo Network: http://192.168.29.61:5000
echo ========================================
echo.

python app_production.py

pause

