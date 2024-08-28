"""クライアントからのリクエストに応じて、カメラから画像をキャプチャし、その画像を処理するエンドポイントを定義"""
from flask import render_template, request, jsonify
from .openai_api import analyze_image
from .camera_capture import capture_image
# from . import create_app

from flask import current_app as app

print("Setting up app...")
# app = create_app()
"""
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

        # 画像をOpenAI APIで分析（例として使用）
        result = analyze_image(image)
        
        return jsonify({'message': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
"""
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