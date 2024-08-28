import cv2

# カメラデバイスの初期化
cap = cv2.VideoCapture(0)

# カメラが正しく開かれたかを確認
if not cap.isOpened():
    print("Error: Could not open video device.")
else:
    while True:
        # フレームを読み込む
        ret, frame = cap.read()
        
        # 正しくフレームが取得できているか確認
        if not ret:
            print("Failed to grab frame")
            break
        
        # フレームを表示
        cv2.imshow('frame', frame)
        
        # 'q'キーを押すと終了
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# リソースを解放
cap.release()
cv2.destroyAllWindows()
