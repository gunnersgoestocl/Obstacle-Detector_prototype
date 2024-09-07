"""環境変数からAPIキーを読み込む基本的な設定クラスがある"""
import os

class Config:
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    # export AZURE_OPENAI_API_KEY='e25f7e82bb2440e49e183908c3324e8a'
    # export OPENAI_API_VERSION='2024-07-01-preview' 
    # export AZURE_OPENAI_ENDPOINT='https://aoai-ump-just-eastus.openai.azure.com/'
    APP_KEY = os.getenv('APP_KEY')
