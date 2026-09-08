import os
import random
import requests

# =========================
# 設定
# =========================

TOKEN = os.environ["DISCORD_TOKEN"]

# テスト用チャンネル
CHANNEL_ID = "1523123948613795974"

# 投稿する言葉
MESSAGES = [
    "いいよ!来いよ!",
    "イキスギィ！",
    "これもうわかんねぇな",
    "ぬわああん疲れたもおおおおおおん",
    "やりますねぇ！",
    "(≧Д≦)ンアーッ！",
    "あぁ＾～いいっすねぇ＾～",
    "まずいですよ！",
    "いいゾ〜これ",
]

# =========================
# 投稿時刻
# GitHub Actionsから渡す
# =========================

POST_PREFIX = os.environ.get("POST_PREFIX", "テスト")

# =========================
# 前回の言葉を読み込む
# =========================

LAST_FILE = "last_message.txt"

try:
    with open(LAST_FILE, "r", encoding="utf-8") as f:
        last_message = f.read().strip()
except FileNotFoundError:
    last_message = ""

# =========================
# 前回と同じ言葉を除外
# =========================

choices = [
    message
    for message in MESSAGES
    if message != last_message
]

message = random.choice(choices)

# =========================
# 投稿内容を作る
# =========================

content = f"{POST_PREFIX} {message}"

# =========================
# Discordへ投稿
# =========================

url = f"https://discord.com/api/v10/channels/{CHANNEL_ID}/messages"

headers = {
    "Authorization": f"Bot {TOKEN}",
    "Content-Type": "application/json"
}

data = {
    "content": content
}

response = requests.post(
    url,
    headers=headers,
    json=data
)

# =========================
# 結果確認
# =========================

if response.status_code == 200:
    print("投稿成功！")
    print(f"投稿内容: {content}")

    # 今回選んだ言葉を保存
    with open(LAST_FILE, "w", encoding="utf-8") as f:
        f.write(message)

else:
    print("投稿失敗！")
    print("ステータスコード:", response.status_code)
    print(response.text)
    exit(1)
