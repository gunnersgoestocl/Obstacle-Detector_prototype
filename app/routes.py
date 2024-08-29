"""クライアントからのリクエストに応じて、カメラから画像をキャプチャし、その画像を処理するエンドポイントを定義"""
from flask import render_template
from flask_socketio import emit
from . import socketio
from threading import Thread, Event
from .camera_capture import camera_worker

# グローバル変数
capture_event = Event()
camera_thread = None

@socketio.on('connect')
def handle_connect():
    print("Client connected")

@socketio.on('disconnect')
def handle_disconnect():
    print("Client disconnected")
    
@socketio.on('start')
def start_camera():
    global camera_thread
    if camera_thread is None or not camera_thread.is_alive():
        capture_event.clear()
        camera_thread = Thread(target=camera_worker, args=(socketio, capture_event))
        camera_thread.start()
    emit('status', {'status': 'Camera started'})

@socketio.on('stop')
def stop_camera():
    capture_event.set()
    if camera_thread:
        camera_thread.join()
    emit('status', {'status': 'Camera stopped'})
    
@socketio.on('get_status')
def get_status():
    emit('status', {'status': 'Camera is running' if camera_thread and camera_thread.is_alive() else 'Camera is stopped'})

# Flaskルート
def init_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')

"""
from flask import jsonify, request, render_template
from flask import current_app as app

print("Setting up app...")
# app = create_app()

def init_routes(app):
    @app.route('/')
    def index():
        print("Rendering index.html...")
        return render_template('index.html')

    @app.route('/capture', methods=['POST'])
    def capture():
        print("Capturing image...")
        try:
            # カメラから画像をキャプチャ
            image = capture_image()
            print("Successfully captured image2.")
            # 画像をOpenAI APIで分析（例として使用）
            result = analyze_image(image)
            print("result: ", result)
            return jsonify({'message': result})
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    return app
"""