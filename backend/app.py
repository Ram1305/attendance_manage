from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2
import numpy as np
import os
import base64
from PIL import Image
import io
import json
from datetime import datetime
import pickle

def format_time_12hour(dt):
    """Format datetime to 12-hour format"""
    return dt.strftime('%I:%M:%S %p')  # %I for 12-hour, %p for AM/PM

app = Flask(__name__)
CORS(app)

# Directory to store face encodings
FACES_DIR = 'faces'
ATTENDANCE_DIR = 'attendance'

# Ensure directories exist
os.makedirs(FACES_DIR, exist_ok=True)
os.makedirs(ATTENDANCE_DIR, exist_ok=True)

# Load face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def detect_face(image_array):
    """Detect face in image and return cropped face"""
    gray = cv2.cvtColor(image_array, cv2.COLOR_RGB2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    if len(faces) == 0:
        return None
    
    # Get the largest face
    face = max(faces, key=lambda x: x[2] * x[3])
    x, y, w, h = face
    
    # Crop and resize face
    face_roi = gray[y:y+h, x:x+w]
    face_roi = cv2.resize(face_roi, (100, 100))
    
    return face_roi

def calculate_face_features(face_image):
    """Calculate simple features from face image"""
    # Simple LBP-like feature extraction
    features = []
    for i in range(0, 100, 10):
        for j in range(0, 100, 10):
            block = face_image[i:i+10, j:j+10]
            features.append(np.mean(block))
            features.append(np.std(block))
    return np.array(features)

def compare_faces(features1, features2, threshold=0.3):
    """Compare two face feature vectors"""
    if features1 is None or features2 is None:
        return False, 1.0
    
    # Calculate normalized correlation
    correlation = np.corrcoef(features1, features2)[0, 1]
    
    if np.isnan(correlation):
        return False, 1.0
    
    distance = 1.0 - correlation
    return distance < threshold, distance

def load_all_faces():
    """Load all registered face features from disk"""
    faces = {}
    if os.path.exists(f'{FACES_DIR}/faces.pkl'):
        with open(f'{FACES_DIR}/faces.pkl', 'rb') as f:
            faces = pickle.load(f)
    return faces

def save_face_features(name, features):
    """Save face features to disk"""
    faces = load_all_faces()
    faces[name] = features
    
    with open(f'{FACES_DIR}/faces.pkl', 'wb') as f:
        pickle.dump(faces, f)

def save_attendance(name, action):
    """Save attendance record"""
    today = datetime.now().strftime('%Y-%m-%d')
    filename = f'{ATTENDANCE_DIR}/{today}.json'
    
    records = []
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            records = json.load(f)
    
    now = datetime.now()
    timestamp = now.strftime('%Y-%m-%d %H:%M:%S')
    timestamp_12hr = format_time_12hour(now)
    records.append({
        'name': name,
        'action': action,
        'timestamp': timestamp,
        'timestamp_12hr': timestamp_12hr
    })
    
    with open(filename, 'w') as f:
        json.dump(records, f, indent=2)

@app.route('/register', methods=['POST'])
def register_face():
    """Register a new face"""
    try:
        data = request.json
        name = data.get('name')
        image_base64 = data.get('image')
        
        if not name or not image_base64:
            return jsonify({'error': 'Name and image are required'}), 400
        
        # Decode base64 image
        image_data = base64.b64decode(image_base64)
        image = Image.open(io.BytesIO(image_data))
        
        # Convert to RGB if needed
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        # Convert to numpy array
        image_array = np.array(image)
        
        # Detect and extract face
        face_image = detect_face(image_array)
        
        if face_image is None:
            return jsonify({'error': 'No face detected in the image'}), 400
        
        # Calculate features
        features = calculate_face_features(face_image)
        
        # Check if name already exists
        faces = load_all_faces()
        if name in faces:
            return jsonify({'error': 'Name already registered'}), 400
        
        # Save face features
        save_face_features(name, features)
        
        return jsonify({'message': f'Face registered successfully for {name}'}), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/recognize', methods=['POST'])
def recognize_face():
    """Recognize a face from camera capture"""
    try:
        data = request.json
        image_base64 = data.get('image')
        
        if not image_base64:
            return jsonify({'error': 'Image is required'}), 400
        
        # Decode base64 image
        image_data = base64.b64decode(image_base64)
        image = Image.open(io.BytesIO(image_data))
        
        # Convert to RGB if needed
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        # Convert to numpy array
        image_array = np.array(image)
        
        # Detect and extract face
        face_image = detect_face(image_array)
        
        if face_image is None:
            return jsonify({'error': 'No face detected'}), 400
        
        # Calculate features
        features = calculate_face_features(face_image)
        
        # Load all registered faces
        registered_faces = load_all_faces()
        
        if not registered_faces:
            return jsonify({'error': 'No registered faces'}), 400
        
        # Compare with registered faces
        recognized_name = None
        best_distance = 1.0
        
        for name, registered_features in registered_faces.items():
            is_match, distance = compare_faces(registered_features, features, threshold=0.25)
            
            if is_match and distance < best_distance:
                best_distance = distance
                recognized_name = name
        
        if not recognized_name:
            return jsonify({'error': 'Face not recognized'}), 400
        
        # Determine action (checkin or checkout)
        today = datetime.now().strftime('%Y-%m-%d')
        filename = f'{ATTENDANCE_DIR}/{today}.json'
        
        last_action = None
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                records = json.load(f)
                # Find last action for this person today
                person_records = [r for r in records if r['name'] == recognized_name]
                if person_records:
                    last_action = person_records[-1]['action']
        
        # If no record or last was checkout, it's a checkin
        # If last was checkin, it's a checkout
        if last_action is None or last_action == 'checkout':
            action = 'checkin'
        else:
            action = 'checkout'
        
        # Save attendance
        save_attendance(recognized_name, action)
        
        now = datetime.now()
        return jsonify({
            'name': recognized_name,
            'action': action,
            'timestamp': now.strftime('%Y-%m-%d %H:%M:%S'),
            'timestamp_12hr': format_time_12hour(now)
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/attendance', methods=['GET'])
def get_attendance():
    """Get attendance records"""
    try:
        date = request.args.get('date', datetime.now().strftime('%Y-%m-%d'))
        filename = f'{ATTENDANCE_DIR}/{date}.json'
        
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                records = json.load(f)
            return jsonify({'records': records}), 200
        else:
            return jsonify({'records': []}), 200
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/employees', methods=['GET'])
def get_employees():
    """Get list of registered employees"""
    try:
        faces = load_all_faces()
        return jsonify({'employees': list(faces.keys())}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'ok'}), 200

# For Render deployment
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    
    print('Starting Face Recognition Attendance System Backend...')
    print('Using OpenCV face detection (no dlib/face_recognition needed)')
    print(f'Serving on http://0.0.0.0:{port}')
    
    app.run(host='0.0.0.0', port=port, debug=debug)
