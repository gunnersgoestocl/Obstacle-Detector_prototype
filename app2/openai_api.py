"""キャプチャされた画像をOpenAI APIまたは他の分析APIで処理"""
# import openai
from openai import AzureOpenAI
import base64
from config import Config

# openai.api_key = Config.OPENAI_API_KEY
AzureOpenAI.api_key = Config.AZURE_OPENAI_API_KEY
AzureOpenAI.azure_endpoint = Config.AZURE_OPENAI_ENDPOINT

def analyze_image(image_data):
    # 画像データをBase64にエンコード
    base64_image = base64.b64encode(image_data).decode('utf-8')
    
    # OpenAI APIにリクエストを送信
    # response = openai.chat.completions.create(
    response = AzureOpenAI.chat.completions.create(
        # model="gpt-4o-mini",
        model = "aoai-gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "I am blind and walking. Please identify the obstacles in front of me using this picture and suggest a path to navigate through them within 20 words like 'Turn slightly right and walk forward, avoiding utility pole'. You don't need to to attach 'I can't analyze the photo directly.', please answer directly."
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        max_tokens=25
    )
    
    # 応答から生成されたテキストを取得
    result = response.choices[0].message.content
    return result

"""
prompt = "Identify obstacles in the image and suggest a path to navigate through them within 20 words."

def analyze_image(encoded_image, prompt=prompt):
    # ここでは、画像をAPIに送信して分析を行う処理
    # 現実的な実装として、画像のエンコードやAPIの呼び出しが含まれます
    # 例: OpenAIのAPIや他の画像分析APIを利用
    print("Analyzing image...")
    response = openai.Image.create(file=encoded_image, prompt=prompt)
    print(response['choices'][0]['text'].strip())
    return response['choices'][0]['text'].strip()
"""

"""
import requests

def analyze_image(image_data):
    # 画像データをBase64にエンコード
    base64_image = base64.b64encode(image_data).decode('utf-8')
    
    # OpenAI APIのエンドポイント
    url = "https://api.openai.com/v1/chat/completions"
    
    # リクエストヘッダ
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    # リクエストペイロード
    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "I am blind and walking. Please identify the obstacles in front of me using this picture and suggest a path to navigate through them within 20 words like 'Turn slightly right and walk forward, avoiding utility pole'."
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        "max_tokens": 25
    }
    
    # API呼び出し
    response = requests.post(url=url, headers=headers, json=payload)
    
    # APIの応答からテキストを取得
    result = response.json()
    return result["choices"][0]["message"]["content"]
"""