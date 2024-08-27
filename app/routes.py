from flask import render_template, request, jsonify
from .openai_api import analyze_image
from .camera_capture import capture_image
from . import create_app

app = create_app()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/capture', methods=['POST'])
def capture():
    try:
        # カメラから画像をキャプチャ
        image = capture_image()

        # 画像をOpenAI APIで分析（例として使用）
        result = analyze_image(image)
        
        return jsonify({'message': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
