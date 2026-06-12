import os
import logging
import requests
import asyncio
from telethon import TelegramClient, events

logging.getLogger('telethon').setLevel(logging.ERROR)

API_ID = int(os.environ.get('API_ID'))
API_HASH = os.environ.get('API_HASH')
N8N_WEBHOOK = os.environ.get('N8N_WEBHOOK')
CHANNEL = os.environ.get('CHANNEL', 'worldcupGoals2026')

async def main():
    # Use connect() not start() — session file handles auth
    client = TelegramClient('session', API_ID, API_HASH)
    await client.connect()

    if not await client.is_user_authorized():
        print("❌ Session not authorized!")
        return

    print("✅ Connected!")

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

asyncio.run(main())
