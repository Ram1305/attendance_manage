# Face Recognition Attendance System - Backend

## Setup Instructions

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Run the Flask server:
```bash
python app.py
```

The server will start on `http://localhost:5000`

## API Endpoints

### Health Check
- `GET /health` - Check if server is running

### Employee Registration
- `POST /register` - Register a new employee face
  - Body: `{"name": "Employee Name", "image": "base64_encoded_image"}`

### Face Recognition
- `POST /recognize` - Recognize face and mark attendance
  - Body: `{"image": "base64_encoded_image"}`
  - Returns: `{"name": "Employee Name", "action": "checkin/checkout", "timestamp": "..."}`

### Attendance Records
- `GET /attendance?date=YYYY-MM-DD` - Get attendance for a specific date
- `GET /attendance` - Get today's attendance

### Employees List
- `GET /employees` - Get list of all registered employees

## Data Storage

- Face encodings are stored in `faces/encodings.json`
- Attendance records are stored in `attendance/YYYY-MM-DD.json` files

## Note

For Flutter app connectivity:
- Android Emulator: Use `http://10.0.2.2:5000`
- iOS Simulator: Use `http://localhost:5000`
- Physical Device: Use your computer's local IP (e.g., `http://192.168.1.100:5000`)

Update the `baseUrl` in `lib/services/api_service.dart` accordingly.

