const socket = io(); // サーバーとの WebSocket 接続を確立
let videoStream = null;
let captureInterval = null;

/* カメラを起動してvideo要素に表示する */
async function startCamera() {
    try {
        const stream = await navigator.mediaDevices.getUserMedia({ video: true });
        videoStream = stream;
        const videoElement = document.getElementById('video');
        videoElement.srcObject = stream;

        // 10秒ごとに画像をキャプチャしてサーバーに送信
        captureInterval = setInterval(() => {
            captureImageAndSend();
        }, 10000);
    } catch (error) {
        console.error("Error accessing camera: ", error);
    }
}

/* カメラを停止する */
function stopCamera() {
    if (videoStream) {
        videoStream.getTracks().forEach(track => track.stop());
    }
    if (captureInterval) {
        clearInterval(captureInterval);
    }
}

/* 画像をキャプチャしてサーバーに送信する */
function captureImageAndSend() {
    const videoElement = document.getElementById('video');
    const canvas = document.getElementById('canvas');
    const context = canvas.getContext('2d');
    canvas.width = videoElement.videoWidth;
    canvas.height = videoElement.videoHeight;
    context.drawImage(videoElement, 0, 0, canvas.width, canvas.height);
    const imageData = canvas.toDataURL('image/jpeg');

    // サーバーに画像を送信
    socket.emit('image_data', { image: imageData });
}


/* Startボタンの処理 (サーバーに start イベントを送信) */
document.getElementById('start-button').addEventListener('click', () => {
    startCamera();
    // socket.emit('start');
});

/* Stopボタンの処理 */
document.getElementById('stop-button').addEventListener('click', () => {
    stopCamera();
    // socket.emit('stop');
});

/* サーバーからのメッセージを受信する処理 */
socket.on('update', function(data) {
    if (data.message) {
        const message = data.message;
        // サーバーからの応答メッセージを画面に表示
        document.getElementById('message').innerText = message;

        // サーバーからの応答メッセージを SpeechSynthesis API で音声読み上げ
        const speech = new SpeechSynthesisUtterance(message);
        window.speechSynthesis.speak(speech);
    }
});

/* サーバーからのステータス更新を受け取る処理 */
socket.on('status', function(data) {
    console.log(data.status);
});