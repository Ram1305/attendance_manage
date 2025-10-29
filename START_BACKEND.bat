@echo off
echo ========================================
echo Face Recognition Attendance - Backend
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
    echo Make sure to check "Add Python to PATH" during installation.
    echo.
    pause
    exit /b 1
)

echo Python found!
cd backend

echo.
echo Installing dependencies...
python -m pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo ERROR: Failed to install dependencies
    echo Try running manually: pip install -r requirements.txt
    pause
    exit /b 1
)

echo.
echo ========================================
echo Starting Backend Server...
echo Server will run on http://localhost:5000
echo Press Ctrl+C to stop the server
echo ========================================
echo.

python app.py

pause

