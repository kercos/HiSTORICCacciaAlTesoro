from bot import bot_telegram, settings
from bot.bot_telegram import BOT

def get_ngrok_base():
    import requests
    r = requests.get('http://localhost:4040/api/tunnels')
    remote_base = next(t['public_url'] for t in r.json()['tunnels'] if t["proto"]=="https")
    return remote_base


def set_webhook():
    s = BOT.setWebhook(settings.WEBHOOK_TELEGRAM_BASE, allowed_updates=['message','callback_query'])
    if s:
        print("webhook setup ok: {}".format(settings.WEBHOOK_TELEGRAM_BASE))
    else:
        print("webhook setup failed")


def delete_webhook():
    BOT.deleteWebhook()


def get_webhook_info():
    print(BOT.get_webhook_info())


if __name__ == "__main__":    
    set_webhook()