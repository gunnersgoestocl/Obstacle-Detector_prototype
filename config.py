"""環境変数からAPIキーを読み込む基本的な設定クラスがある"""
import os

class Config:
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
