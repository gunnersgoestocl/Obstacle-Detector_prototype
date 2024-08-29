from flask import Flask
from flask_socketio import SocketIO
import os
from config import Config


# websocket用のsocketioを初期化
socketio = SocketIO()

def create_app():
    """Flaskアプリケーションのインスタンスを作成"""
    app = Flask(__name__)
    app.config['SECRET_KEY'] = Config.APP_KEY
    socketio.init_app(app)
    
    with app.app_context():
        from .routes import init_routes
        init_routes(app)
    return app

