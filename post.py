import os
import requests

TOKEN = os.environ["DISCORD_TOKEN"]
CHANNEL_ID = "1523123948613795974"

url = f"https://discord.com/api/v10/channels/{CHANNEL_ID}/messages"

headers = {
    "Authorization": f"Bot {TOKEN}",
    "Content-Type": "application/json"
}

data = {
    "content": "時報Botのテスト投稿です！"
}

response = requests.post(
    url,
    headers=headers,
    json=data
)

if response.status_code == 200:
    print("投稿成功！")
else:
    print("投稿失敗:", response.status_code)
    print(response.text)
