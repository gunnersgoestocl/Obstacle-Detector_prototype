import openai
from config import Config

openai.api_key = Config.OPENAI_API_KEY

def analyze_image(image):
    # ここでは、画像をAPIに送信して分析を行う処理
    # 現実的な実装として、画像のエンコードやAPIの呼び出しが含まれます
    # 例: OpenAIのAPIや他の画像分析APIを利用

    response = openai.Image.create(file=image, prompt="Identify obstacles.")
    return response['choices'][0]['text'].strip()
