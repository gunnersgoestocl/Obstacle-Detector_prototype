# Obstacle-Detector_prototype

## 1. [Overview](#overview)
### 1. Idea from Chat-GPT
    project_root/
      │
      ├── app/
      │   ├── static/
      │   │   ├── css/
      │   │   │   └── styles.css
      │   │   ├── js/
      │   │   │   └── scripts.js
      │   │   └── images/
      │   ├── templates/
      │   │   └── index.html
      │   ├── __init__.py
      │   ├── routes.py
      │   └── openai_api.py
      │   └── camera_capture.py
      │
      ├── models/
      │   └── obstacle_detection_model.py
      │
      ├── config.py
      ├── app.py
      ├── requirements.txt
      └── README.md
### 2. API Documentation
  https://platform.openai.com/docs/guides/vision
  https://qiita.com/kurata04/items/a10bdc44cc0d1e62dad3
### 3. Note
    

## 2. How to run the project

### 1. **依存パッケージのインストール**
まず、プロジェクトのディレクトリに移動して、`requirements.txt`に記載されている依存パッケージをインストールします。

```bash
cd /path/to/your/project_root
pip install -r requirements.txt
```

### 2. **OpenAI APIキーの設定**
OpenAI APIを利用するために、APIキーを環境変数として設定します。環境変数に設定する方法は、OSに依存します。

- **Linux/MacOS:**
  ```bash
  export OPENAI_API_KEY='sk-proj-xxxxxxxxxxxxxxxxxxxxxxxx'
  ```
  
- **Windows:**
  ```cmd
  set OPENAI_API_KEY='your-api-key-here'
  ```

または、`config.py`に以下のように直接APIキーを設定しても良いです。

```python
class Config:
    OPENAI_API_KEY = 'sk-proj-xxxxxxxxxxxxxxxxxxxxxxxx'
```

### 3. **アプリケーションの起動**
次に、Flaskアプリケーションを起動します。`app.py`を実行することでアプリケーションを立ち上げることができます。

```bash
python app.py
```

### 4. **アプリケーションへのアクセス**
アプリケーションが正常に起動したら、以下のようなメッセージがターミナルに表示されるはずです。

```
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

ブラウザを開き、`http://127.0.0.1:5000/` にアクセスすると、アプリケーションが表示されます。5000番ポートが使用中の場合は、8080番ポートなど他のポートを指定して起動してください。

### 5. **操作方法**
- アプリケーションが表示されたら、画面上の「Start Camera and Analyze」ボタンをクリックします。
- サーバー側でカメラが起動し、10秒おきに画像がキャプチャされて、障害物が認識されると、その結果が音声で読み上げられます。
- 画面上の「Stop Camera」ボタンをクリックすると、カメラが停止します。

僕の場合は、0番デバイスがiPhoneのカメラになっていて、あらかじめiPhoneのロックを解除しておかないと、Start Cameraボタンを押してもカメラが起動しませんでした。
スマホのブラウザで、http://192.168.3.48:8080 を打ち込んでも、同じ操作は行えたので、きちんとサーバーさえ立ててしまえば、質はさておいてサービスとしては動きます。

### 6. **終了方法**
アプリケーションの実行を終了する場合は、ターミナルで`CTRL+C`を押してください。

---

以上がアプリケーションを起動するための手順です。もし途中でエラーが発生したり、何か問題があれば、その内容を教えてください。対応策を考えます。
## 3. Appendix