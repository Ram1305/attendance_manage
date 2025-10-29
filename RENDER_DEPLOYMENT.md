# Render Deployment Guide

## Step 1: Create Render Account
1. Go to https://render.com
2. Sign up for a free account

## Step 2: Create New Web Service
1. Click "New +" → "Web Service"
2. Connect your GitHub repository (or use Render's Git)
3. Configure:
   - **Name**: face-attendance-backend (or your preferred name)
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements_render.txt`
   - **Start Command**: `python app.py`
   - **Root Directory**: `backend`

## Step 3: Environment Variables (Optional)
- `PORT`: Automatically set by Render (default: 5000)
- `FLASK_ENV`: Set to `production` for production mode

## Step 4: Deploy
1. Click "Create Web Service"
2. Render will automatically build and deploy
3. Wait for deployment to complete (~5-10 minutes)

## Step 5: Update Flutter App
After deployment, update `lib/services/api_service.dart`:

```dart
static String get baseUrl {
  if (kIsWeb) {
    return 'https://your-app-name.onrender.com';
  }
  
  if (Platform.isAndroid) {
    return 'https://your-app-name.onrender.com';
  }
  
  // ... rest of code
}
```

Replace `your-app-name` with your Render service name.

## Important Notes:
- Render free tier spins down after 15 minutes of inactivity
- First request after spin-down may take 30-60 seconds
- For production, consider upgrading to paid tier
- Data stored in `faces/` and `attendance/` directories will persist
- For persistent storage, consider using Render Disk or external database

## Render URL Format:
Your app will be available at: `https://your-app-name.onrender.com`

## Build & Deploy Commands:
- Build: `pip install -r requirements_render.txt`
- Start: `python app.py`

## File Structure for Render:
```
backend/
├── app.py                    # Main application (uses PORT env var)
├── requirements_render.txt    # Dependencies (no dlib needed)
├── Procfile                  # Tells Render how to start
└── (faces/ and attendance/ will be created automatically)
```

## Troubleshooting:
- If build fails: Check that all dependencies are in requirements_render.txt
- If app crashes: Check Render logs for errors
- Port issues: Render automatically sets PORT, don't hardcode it

