import cv2
import time
from flask_socketio import emit
from .openai_api import analyze_image

def camera_worker(socketio, capture_event):
    latest_frame = None
    cap = cv2.VideoCapture(0)
    while not capture_event.is_set():
        ret, frame = cap.read()
        if ret:
            latest_frame = frame
            if latest_frame is not None:
                # 画像をエンコードしてOpenAI APIで解析
                result = analyze_image(cv2.imencode('.jpg', latest_frame)[1].tobytes())
                
                # OpenAIの結果をSocketIOでフロントエンドに送信
                socketio.emit('update', {'message': result})
        time.sleep(10)  # 10秒ごとに画像を取得
    cap.release()
