import os
import requests

TOKEN = os.getenv("BOT_TOKEN")
API = f"https://api.telegram.org/bot{TOKEN}"

offset = 0

while True:
    response = requests.get(
        f"{API}/getUpdates",
        params={"offset": offset, "timeout": 30}
    ).json()

    for update in response.get("result", []):
        offset = update["update_id"] + 1

        message = update.get("message")
        if not message:
            continue

        chat_id = message["chat"]["id"]
        text = message.get("text", "")

        requests.post(
            f"{API}/sendMessage",
            data={
                "chat_id": chat_id,
                "text": "Mesajın alındı. Bot üzerinden iletişim kuruluyor."
            }
        )
