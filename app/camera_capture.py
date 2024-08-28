import cv2

def capture_image():
    """OpenCVを使ってカメラから画像をキャプチャし、それをサーバーに送信する"""
    print("Now capturing image...")
    # カメラデバイスの初期化（デフォルトのカメラはID 0）
    cap = cv2.VideoCapture(0)   # 0: my iPhone
    
    if not cap.isOpened():
        print("Device not found")
        raise Exception("カメラデバイスにアクセスできません。")

    # 画像のキャプチャ
    ret, frame = cap.read()
    print("Successfully captured image1.")
    
    if not ret:
        print("Failed to capture image")
        print(ret, frame)
        raise Exception("画像のキャプチャに失敗しました。")
    
    # カメラを解放
    cap.release()

    # 画像データをエンコード（JPEGフォーマット）
    _, buffer = cv2.imencode('.jpg', frame)

    return buffer.tobytes()

