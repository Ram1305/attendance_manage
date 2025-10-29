# Production Server Startup Script

from waitress import serve
from app_simple import app

if __name__ == '__main__':
    print('=' * 60)
    print('Starting Face Recognition Attendance System Backend')
    print('PRODUCTION MODE - Using Waitress WSGI Server')
    print('=' * 60)
    print('Server will run on http://0.0.0.0:5000')
    print('Press Ctrl+C to stop the server')
    print('=' * 60)
    print()
    
    # Run with Waitress (production WSGI server)
    # threads=4: Handle 4 concurrent requests
    # channel_timeout=120: Timeout for keep-alive connections
    serve(app, host='0.0.0.0', port=5000, threads=4, channel_timeout=120)
