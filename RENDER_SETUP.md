# Render Deployment Configuration

## Quick Start:

1. **Sign up at Render**: https://render.com

2. **Create New Web Service**:
   - Click "New +" → "Web Service"
   - Connect your GitHub repo OR upload files manually
   - Settings:
     - **Name**: face-attendance-backend
     - **Environment**: Python 3
     - **Root Directory**: `backend`
     - **Build Command**: `pip install -r requirements_render.txt`
     - **Start Command**: `python app.py`

3. **Deploy**:
   - Click "Create Web Service"
   - Wait for build (5-10 minutes)

4. **Get Your URL**:
   - After deployment, Render gives you a URL like: `https://your-app-name.onrender.com`
   - Copy this URL

5. **Update Flutter App**:
   - Open `lib/services/api_service.dart`
   - Find line: `static const String? RENDER_URL = null;`
   - Change to: `static const String? RENDER_URL = 'https://your-app-name.onrender.com';`
   - Save and rebuild your Flutter app

## Files Created for Render:
- ✅ `backend/app.py` - Main app (uses PORT env var)
- ✅ `backend/Procfile` - Tells Render how to start
- ✅ `backend/requirements_render.txt` - Dependencies (no dlib)

## Testing:
After deployment, test: `https://your-app-name.onrender.com/health`

Should return: `{"status":"ok"}`

## Important Notes:
⚠️ **Free Tier Limitations**:
- Spins down after 15 min inactivity
- First request after spin-down takes 30-60 seconds
- Files stored in `faces/` and `attendance/` may reset on restart

💡 **For Production**:
- Consider Render Disk for persistent storage
- Or use external database (PostgreSQL, MongoDB)
- Upgrade to paid tier for always-on service

## Environment Variables (Optional):
- `PORT`: Auto-set by Render (don't override)
- `FLASK_ENV`: Set to `production` for production mode

## Troubleshooting:
- Build fails? Check `requirements_render.txt` has all dependencies
- App crashes? Check Render logs
- Connection timeout? Free tier spin-down delay

