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
            // サーバーからの応答メッセージを音声で読み上げ
            const msg = new SpeechSynthesisUtterance(data.message);
            window.speechSynthesis.speak(msg);
        }
    })
    .catch(error => console.error('Error:', error));
});
