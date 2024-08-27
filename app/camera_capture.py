import cv2

def capture_image():
    """OpenCVを使ってカメラから画像をキャプチャし、それをサーバーに送信する"""
    # カメラデバイスの初期化（デフォルトのカメラはID 0）
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        raise Exception("カメラデバイスにアクセスできません。")

    # 画像のキャプチャ
    ret, frame = cap.read()
    
    if not ret:
        raise Exception("画像のキャプチャに失敗しました。")
    
    # カメラを解放
    cap.release()

    # 画像データをエンコード（JPEGフォーマット）
    _, buffer = cv2.imencode('.jpg', frame)

    return buffer.tobytes()

