"""Flaskアプリケーションを起動するためのエントリーポイントがある"""

from app import create_app,socketio

# Flaskアプリケーションのインスタンスを作成
app = create_app()

if __name__ == "__main__":
    # Flaskアプリケーションを実行
    socketio.run(app, host='0.0.0.0', port=8080, debug=True)



"""
from flask import Flask
from app.routes import init_routes

def create_app():
    app = Flask(__name__, template_folder='app/templates', static_folder='app/static')
    init_routes(app)
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
"""
