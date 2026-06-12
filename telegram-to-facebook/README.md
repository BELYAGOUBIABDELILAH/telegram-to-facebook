# Telegram → Facebook Goal Videos Bot

Watches a Telegram channel for football goal videos and automatically posts them to a Facebook page via n8n.

## Setup

### 1. Environment Variables
Set these in Railway dashboard:

| Variable | Value |
|---|---|
| `API_ID` | From https://my.telegram.org |
| `API_HASH` | From https://my.telegram.org |
| `PHONE` | Your Telegram phone number |
| `N8N_WEBHOOK` | Your n8n webhook URL |
| `CHANNEL` | Telegram channel username |

### 2. Deploy to Railway
1. Push this repo to GitHub
2. Go to railway.app → New Project → Deploy from GitHub
3. Add environment variables in Railway dashboard
4. Deploy

## Files
- `main.py` — Telethon listener script
- `session.session` — Telegram session (never delete)
- `railway.toml` — Railway config
- `requirements.txt` — Python dependencies
