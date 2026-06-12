import os
import logging
import requests
from telethon import TelegramClient, events

logging.getLogger('telethon').setLevel(logging.ERROR)

API_ID = int(os.environ.get('API_ID'))
API_HASH = os.environ.get('API_HASH')
PHONE = os.environ.get('PHONE')
N8N_WEBHOOK = os.environ.get('N8N_WEBHOOK')
CHANNEL = os.environ.get('CHANNEL', 'worldcupGoals2026')

async def main():
    client = TelegramClient('session', API_ID, API_HASH)
    await client.start(phone=PHONE)
    print("✅ Authenticated & Connected!")

    @client.on(events.NewMessage(chats=CHANNEL))
    async def handler(event):
        if event.message.video:
            print("📹 New video detected! Downloading...")
            path = await event.message.download_media(file='/tmp/goal.mp4')
            print("⬆️ Sending to n8n...")
            with open(path, 'rb') as f:
                r = requests.post(N8N_WEBHOOK, files={
                    'video': ('goal.mp4', f, 'video/mp4')
                }, data={
                    'caption': event.message.text or '⚽ World Cup 2026 Goal!'
                })
            print(f"✅ Done! Status: {r.status_code}")
            os.remove(path)

    print(f"👂 Listening to {CHANNEL}...")
    await client.run_until_disconnected()

import asyncio
asyncio.run(main())
