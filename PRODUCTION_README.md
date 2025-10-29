# Production Server Instructions

## To Start Production Server:

### Option 1: Double-click START_PRODUCTION.bat
- This will install dependencies and start the production server

### Option 2: Manual Start
```bash
cd backend
python app_production.py
```

## Production Server Features:
- Uses Waitress WSGI Server (production-ready)
- Handles multiple concurrent requests
- More stable than development server
- No debug mode (better performance)
- Auto-restarts on crashes

## Differences from Development:
- Development: `python app_simple.py` (Flask debug server)
- Production: `python app_production.py` (Waitress WSGI server)

## Server URLs:
- Local: http://localhost:5000
- Network: http://192.168.29.61:5000

## Note:
Production server runs without debug output, making it faster and more stable for real-world use.

