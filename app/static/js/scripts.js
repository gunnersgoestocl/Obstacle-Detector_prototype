const socket = io(); // サーバーとの WebSocket 接続を確立

/* Startボタンの処理 (サーバーに start イベントを送信) */
document.getElementById('start-button').addEventListener('click', () => {
    socket.emit('start');
});

/* Stopボタンの処理 */
document.getElementById('stop-button').addEventListener('click', () => {
    socket.emit('stop');
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

/*
document.getElementById('captureButton').addEventListener('click', function() {
    // カメラ画像のキャプチャリクエストをサーバーに送信
    fetch('/capture', {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            console.error('Error:', data.error);
        } else {
            const message = data.message;
            // サーバーからの応答メッセージを画面に表示
            document.getElementById('message').innerText = message;

            // サーバーからの応答メッセージを SpeechSynthesis API で音声読み上げ
            const speech = new SpeechSynthesisUtterance(message);
            window.speechSynthesis.speak(speech);
        }
    })
    .catch(error => console.error('Error:', error));
});
*/