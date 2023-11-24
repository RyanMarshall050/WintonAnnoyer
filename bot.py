import os
from discord_webhook import DiscordWebhook
from dotenv import load_dotenv

load_dotenv()

webhook = DiscordWebhook(url=os.getenv("webhook"), content = os.getenv("content"))
response = webhook.execute()