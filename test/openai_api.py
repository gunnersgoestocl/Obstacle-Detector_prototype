"""画像をOPENAI_API_KEYを使って分析する 事前にexport OPNEAI_API_KEY="??????"を実行しておく"""
import base64
import requests
import os

# OpenAI API Key
api_key = os.environ["OPENAI_API_KEY"]

url = "https://api.openai.com/v1/chat/completions"
# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
image_path = "images/sample.jpg"

# Getting the base64 string
base64_image = encode_image(image_path)

headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {api_key}"
}

payload = {
  "model": "gpt-4o-mini",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "I am blind and walking. Please identify the obstacles in front of me using this picture and suggest a path to navigate through them within 20 words like 'Turn slightly right and walk forward, avoiding utility pole'. You don't need to attach 'I can't analyze the photo directly.', please answer directly."
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

response = requests.post(url=url, headers=headers, json=payload)

print(response.json())