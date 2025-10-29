# Face Recognition Attendance System

A complete face recognition-based attendance system built with Flutter (frontend) and Python (backend).

## Features

- 👤 **Employee Registration**: Register employees with face capture
- 📸 **Face Recognition**: Automatic check-in/check-out based on face recognition
- 📊 **Attendance History**: View daily attendance records
- 💾 **Local Storage**: All data stored locally using SQLite
- 🔄 **Automatic Check-in/Check-out**: System automatically toggles between check-in and check-out

## Project Structure

```
maya/
├── backend/              # Python Flask backend
│   ├── app.py           # Main Flask application
│   ├── requirements.txt  # Python dependencies
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
└── pubspec.yaml         # Flutter dependencies
```

## Setup Instructions

### 1. Backend Setup

```bash
cd backend
pip install -r requirements.txt
python app.py
```

The backend will run on `http://localhost:5000`

### 2. Flutter Setup

1. Install Flutter dependencies:
```bash
flutter pub get
```

2. Update API URL (if needed):
   - Edit `lib/services/api_service.dart`
   - For Android Emulator: Use `http://10.0.2.2:5000`
   - For iOS Simulator: Use `http://localhost:5000`
   - For Physical Device: Use your computer's local IP (e.g., `http://192.168.1.100:5000`)

3. Run the app:
```bash
flutter run
```

### 3. Camera Permissions

Make sure to grant camera permissions:
- **Android**: Permissions are automatically requested
- **iOS**: Add camera permission in `ios/Runner/Info.plist`:
  ```xml
  <key>NSCameraUsageDescription</key>
  <string>This app needs camera access for face recognition</string>
  ```

## How to Use

### Register Employee
1. Navigate to "Attendance" tab
2. Tap "Register Employee"
3. Enter employee name
4. Capture face photo
5. Tap "Register"

### Mark Attendance
1. Navigate to "Attendance" tab
2. Tap "Mark Attendance"
3. Position face in the camera frame
4. Tap "Mark Attendance"
5. System will recognize the face and automatically mark check-in or check-out

### View History
1. Navigate to "Attendance" tab
2. Tap "View History"
3. Select date to view attendance records
4. See all check-ins and check-outs for that date

## Technical Details

### Backend (Python)
- **Flask**: Web framework
- **face_recognition**: Face detection and recognition library
- **OpenCV**: Image processing
- **JSON**: Local data storage

### Frontend (Flutter)
- **camera**: Camera access
- **sqflite**: Local SQLite database
- **http**: API communication
- **path_provider**: File system access

### Data Storage
- **Face Encodings**: Stored in `backend/faces/encodings.json`
- **Attendance Records**: 
  - Backend: `backend/attendance/YYYY-MM-DD.json`
  - Frontend: SQLite database (`attendance.db`)

## Troubleshooting

### Backend Connection Issues
- Ensure Python backend is running
- Check firewall settings
- Verify IP address in `api_service.dart`
- Check backend health: `http://localhost:5000/health`

### Face Recognition Issues
- Ensure good lighting
- Face should be clearly visible
- Try registering with multiple angles
- Check face detection threshold (currently 0.6)

### Camera Issues
- Grant camera permissions
- Restart the app
- Check device camera availability

## License

This project is for internal use.

