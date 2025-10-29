# Setup and Run Script for Face Recognition Attendance System

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Face Recognition Attendance System Setup" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check Python
Write-Host "Checking Python installation..." -ForegroundColor Yellow
$pythonCmd = $null

# Try different Python commands
$pythonCommands = @("python", "python3", "py")
foreach ($cmd in $pythonCommands) {
    try {
        $version = & $cmd --version 2>&1
        if ($LASTEXITCODE -eq 0) {
            $pythonCmd = $cmd
            Write-Host "✓ Found Python: $version" -ForegroundColor Green
            break
        }
    } catch {
        continue
    }
}

if (-not $pythonCmd) {
    Write-Host "✗ Python not found!" -ForegroundColor Red
    Write-Host ""
    Write-Host "Please install Python 3.8+ from:" -ForegroundColor Yellow
    Write-Host "  https://www.python.org/downloads/" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Make sure to check 'Add Python to PATH' during installation." -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Press any key to exit..."
    $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
    exit 1
}

# Check if backend directory exists
if (-not (Test-Path "backend")) {
    Write-Host "✗ Backend directory not found!" -ForegroundColor Red
    exit 1
}

# Navigate to backend
Set-Location backend

# Check if requirements.txt exists
if (-not (Test-Path "requirements.txt")) {
    Write-Host "✗ requirements.txt not found!" -ForegroundColor Red
    exit 1
}

# Check if dependencies are installed
Write-Host ""
Write-Host "Checking Python dependencies..." -ForegroundColor Yellow
try {
    & $pythonCmd -c "import flask" 2>$null
    $flaskInstalled = $LASTEXITCODE -eq 0
} catch {
    $flaskInstalled = $false
}

if (-not $flaskInstalled) {
    Write-Host "Installing Python dependencies..." -ForegroundColor Yellow
    & $pythonCmd -m pip install -r requirements.txt
    if ($LASTEXITCODE -ne 0) {
        Write-Host "✗ Failed to install dependencies!" -ForegroundColor Red
        Write-Host "Try running manually: pip install -r requirements.txt" -ForegroundColor Yellow
        exit 1
    }
    Write-Host "✓ Dependencies installed successfully" -ForegroundColor Green
} else {
    Write-Host "✓ Dependencies already installed" -ForegroundColor Green
}

# Start the server
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Starting Backend Server..." -ForegroundColor Cyan
Write-Host "Server will run on http://localhost:5000" -ForegroundColor Green
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

& $pythonCmd app.py

