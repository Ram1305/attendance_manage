# Quick Start Guide - Face Recognition Attendance System

## 🚀 Setup in 3 Steps

### Step 1: Install Backend Dependencies
```bash
cd backend
pip install -r requirements.txt
```

### Step 2: Start Backend Server
```bash
# Windows
python app.py
# OR double-click start_server.bat

# Linux/Mac
python app.py
# OR ./start_server.sh
```

Server will run on `http://localhost:5000`

### Step 3: Run Flutter App
```bash
flutter pub get
flutter run
```

## 📱 Using the App

1. **Navigate to Attendance Tab** (bottom navigation)
2. **Register Employee**: Tap "Register Employee" → Enter name → Capture face → Register
3. **Mark Attendance**: Tap "Mark Attendance" → Position face → Tap button → Done!
4. **View History**: Tap "View History" → Select date → See records

## ⚙️ Configuration

### For Physical Device
Edit `lib/services/api_service.dart` and change:
```dart
static const String baseUrl = 'http://YOUR_COMPUTER_IP:5000';
```

Find your computer's IP:
- **Windows**: `ipconfig` → Look for IPv4 Address
- **Mac/Linux**: `ifconfig` → Look for inet address

### For Emulator/Simulator
- **Android Emulator**: Use `http://10.0.2.2:5000`
- **iOS Simulator**: Use `http://localhost:5000`

## ✅ Features

- ✅ Face Recognition
- ✅ Automatic Check-in/Check-out
- ✅ Local Data Storage
- ✅ Attendance History
- ✅ Employee Registration

## 🐛 Troubleshooting

**Backend not connecting?**
- Check if Python server is running
- Verify firewall isn't blocking port 5000
- Update IP address in `api_service.dart`

**Camera not working?**
- Grant camera permissions in device settings
- Restart the app

**Face not recognized?**
- Ensure good lighting
- Face should be clear and centered
- Re-register with better image

## 📂 Project Structure

```
backend/          # Python Flask server
lib/
  screens/        # Flutter UI screens
  services/       # API & Database services
```

For detailed documentation, see `README_ATTENDANCE.md`

