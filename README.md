# Face Recognition Attendance Management System

A complete face recognition-based attendance system built with Flutter (frontend) and Python Flask (backend).

## Features

- 👤 **Employee Registration**: Register employees with face capture
- 📸 **Auto Face Recognition**: Automatic check-in/check-out based on face recognition (3 seconds detection)
- 📊 **Attendance History**: View daily attendance records with employee statistics
- 💾 **Local Storage**: All data stored locally using SQLite
- 🔄 **Automatic Check-in/Check-out**: System automatically toggles between check-in and check-out
- ⏰ **12-Hour Time Format**: Displays time in AM/PM format
- 📈 **Daily Statistics**: Shows check-in/check-out counts per employee per day

## Tech Stack

- **Frontend**: Flutter (Dart)
- **Backend**: Python Flask
- **Face Recognition**: OpenCV
- **Database**: SQLite (local), JSON files (backend)
- **Deployment**: Render (cloud hosting)

## Project Structure

```
attendance_manage/
├── backend/              # Python Flask backend
│   ├── app.py           # Main Flask application (Render compatible)
│   ├── app_simple.py    # Simple version (local development)
│   ├── app_production.py # Production server (Waitress)
│   ├── requirements.txt # Dependencies
│   ├── requirements_render.txt # Dependencies for Render
│   ├── Procfile         # Render deployment config
│   ├── runtime.txt      # Python version
│   ├── faces/           # Stored face encodings (auto-created)
│   └── attendance/      # Attendance records (auto-created)
├── lib/
│   ├── screens/         # Flutter screens
│   │   ├── attendance_home_screen.dart
│   │   ├── employee_registration_screen.dart
│   │   ├── attendance_capture_screen.dart
│   │   └── attendance_history_screen.dart
│   ├── services/        # Services
│   │   ├── api_service.dart      # Backend API communication
│   │   └── database_service.dart # Local SQLite database
│   └── main.dart        # Main app entry point
└── android/             # Android configuration
```

## Setup Instructions

### Backend Setup

#### Local Development:
```bash
cd backend
pip install -r requirements.txt
python app_simple.py
```

#### Production (Local):
```bash
cd backend
pip install -r requirements.txt
python app_production.py
```

#### Render Deployment:
1. Push code to GitHub
2. Connect to Render
3. Deploy using `requirements_render.txt`
4. Start command: `python app.py`

### Flutter Setup

1. Install dependencies:
```bash
flutter pub get
```

2. Update API URL in `lib/services/api_service.dart`:
   - For local: Set `RENDER_URL = null`
   - For Render: Set `RENDER_URL = 'https://your-app.onrender.com'`

3. Run the app:
```bash
flutter run
```

## How It Works

1. **Register Employee**: Capture face → System stores face features
2. **Mark Attendance**: Camera auto-scans → Detects face for 3 seconds → Auto-captures → Marks check-in/check-out
3. **View History**: See daily attendance with employee statistics

## API Endpoints

- `POST /register` - Register new employee face
- `POST /recognize` - Recognize face and mark attendance
- `GET /attendance?date=YYYY-MM-DD` - Get attendance records
- `GET /employees` - Get list of employees
- `GET /health` - Health check

## Configuration

- **Camera**: Front camera (selfie camera)
- **Face Detection**: 3 seconds continuous detection for auto-capture
- **Time Format**: 12-hour format (AM/PM)
- **Storage**: Local SQLite + Backend JSON files

## Deployment

### Render Deployment
See `RENDER_SETUP.md` for detailed instructions.

1. Create account on Render.com
2. Connect GitHub repository
3. Configure build and start commands
4. Deploy
5. Update Flutter app with Render URL

## License

This project is for internal use.
