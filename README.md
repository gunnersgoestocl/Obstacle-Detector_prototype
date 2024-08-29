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
  (env) yuri1@Yuri-no-MacBook-Air prototype % python3 app.py
  * Serving Flask app 'app'
  * Debug mode: on
  WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
  * Running on all addresses (0.0.0.0)
  * Running on http://127.0.0.1:8080
  * Running on http://192.168.3.46:8080
  Press CTRL+C to quit
  * Restarting with stat
  * Debugger is active!
  * Debugger PIN: 137-461-120
  127.0.0.1 - - [30/Aug/2024 00:44:40] "GET /socket.io/?EIO=4&transport=polling&t=P6Ups_i HTTP/1.1" 200 -
  Client connected
  127.0.0.1 - - [30/Aug/2024 00:44:40] "POST /socket.io/?EIO=4&transport=polling&t=P6Ups_s&sid=kqRe1xJ1x-CoC312AAAA HTTP/1.1" 200 -
  127.0.0.1 - - [30/Aug/2024 00:44:40] "GET /socket.io/?EIO=4&transport=polling&t=P6Ups_u&sid=kqRe1xJ1x-CoC312AAAA HTTP/1.1" 200 -
  127.0.0.1 - - [30/Aug/2024 00:44:40] "GET /socket.io/?EIO=4&transport=polling&t=P6Ups__&sid=kqRe1xJ1x-CoC312AAAA HTTP/1.1" 200 -
  127.0.0.1 - - [30/Aug/2024 00:44:42] "GET / HTTP/1.1" 200 -
  Client disconnected
  127.0.0.1 - - [30/Aug/2024 00:44:42] "GET /socket.io/?EIO=4&transport=websocket&sid=kqRe1xJ1x-CoC312AAAA HTTP/1.1" 200 -
  127.0.0.1 - - [30/Aug/2024 00:44:42] "GET /static/css/styles.css HTTP/1.1" 304 -
  127.0.0.1 - - [30/Aug/2024 00:44:42] "GET /static/js/scripts.js HTTP/1.1" 304 -
  127.0.0.1 - - [30/Aug/2024 00:44:42] "GET /socket.io/?EIO=4&transport=polling&t=P6UptV- HTTP/1.1" 200 -
  127.0.0.1 - - [30/Aug/2024 00:44:42] "GET /static/images/favicon.ico HTTP/1.1" 304 -
  Client connected
  127.0.0.1 - - [30/Aug/2024 00:44:42] "POST /socket.io/?EIO=4&transport=polling&t=P6UptX4&sid=gDOPw9oywUWYYjo8AAAC HTTP/1.1" 200 -
  127.0.0.1 - - [30/Aug/2024 00:44:42] "GET /socket.io/?EIO=4&transport=polling&t=P6UptX5&sid=gDOPw9oywUWYYjo8AAAC HTTP/1.1" 200 -
  2024-08-30 00:44:47.108 Python[97473:4196581] WARNING: AVCaptureDeviceTypeExternal is deprecated for Continuity Cameras. Please use AVCaptureDeviceTypeContinuityCamera and add NSCameraUseContinuityCameraDeviceType to your Info.plist.
  Exception in thread Thread-24 (camera_worker):
  Traceback (most recent call last):
    File "/opt/homebrew/Cellar/python@3.12/3.12.4/Frameworks/Python.framework/Versions/3.12/lib/python3.12/threading.py", line 1073, in _bootstrap_inner
      self.run()
    File "/opt/homebrew/Cellar/python@3.12/3.12.4/Frameworks/Python.framework/Versions/3.12/lib/python3.12/threading.py", line 1010, in run
      self._target(*self._args, **self._kwargs)
    File "/Users/yuri1/Documents/23_LLM_Hackathon/prototype/app/camera_capture.py", line 15, in camera_worker
      result = analyze_image(cv2.imencode('.jpg', latest_frame)[1].tobytes())
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "/Users/yuri1/Documents/23_LLM_Hackathon/prototype/app/openai_api.py", line 13, in analyze_image
      response = openai.ChatCompletion.create(
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "/Users/yuri1/Documents/23_LLM_Hackathon/prototype/env/lib/python3.12/site-packages/openai/lib/_old_api.py", line 39, in __call__
      raise APIRemovedInV1(symbol=self._symbol)
  openai.lib._old_api.APIRemovedInV1: 

  You tried to access openai.ChatCompletion, but this is no longer supported in openai>=1.0.0 - see the README at https://github.com/openai/openai-python for the API.

  You can run `openai migrate` to automatically upgrade your codebase to use the 1.0.0 interface. 

  Alternatively, you can pin your installation to the old version, e.g. `pip install openai==0.28`

  A detailed migration guide is available here: https://github.com/openai/openai-python/discussions/742

  ^C%                                          

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
  export OPENAI_API_KEY='your-api-key-here'
  ```
  
- **Windows:**
  ```cmd
  set OPENAI_API_KEY='your-api-key-here'
  ```

または、`config.py`に以下のように直接APIキーを設定しても良いです。

```python
class Config:
    OPENAI_API_KEY = 'your-api-key-here'
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

ブラウザを開き、`http://127.0.0.1:5000/` にアクセスすると、アプリケーションが表示されます。

### 5. **操作方法**
- アプリケーションが表示されたら、画面上の「Capture and Analyze」ボタンをクリックします。
- サーバー側でカメラが起動し、画像がキャプチャされて、障害物が認識されると、その結果が音声で読み上げられます。

### 6. **終了方法**
アプリケーションの実行を終了する場合は、ターミナルで`CTRL+C`を押してください。

---

以上がアプリケーションを起動するための手順です。もし途中でエラーが発生したり、何か問題があれば、その内容を教えてください。対応策を考えます。
## 3. Appendix