"""クライアントからのリクエストに応じて、カメラから画像をキャプチャし、その画像を処理するエンドポイントを定義"""
from flask import render_template
from flask_socketio import emit
from . import socketio
import base64
from .openai_api import analyze_image

@socketio.on('connect')
def handle_connect():
    print("Client connected")

@socketio.on('disconnect')
def handle_disconnect():
    print("Client disconnected")
    
@socketio.on('image_data')
def handle_image(data):
    print("Received image data")
    # クライアントから受け取った画像データをデコードして解析
    image_data = base64.b64decode(data['image_data'])
    
    # OpenAI APIを使用して解析
    result = analyze_image(image_data)
    
    # クライアントに結果を送信
    socketio.emit('update', {'message': result})

# Flaskルート
def init_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')