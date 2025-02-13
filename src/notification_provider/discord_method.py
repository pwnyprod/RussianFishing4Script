import os

from discord import Client
from discord.abc import Snowflake
from dotenv import load_dotenv

from notification_provider.abstract_messaging_method import MessagingMethod
import discord

class DiscordMethod(MessagingMethod):
    recipient: str | Snowflake
    client: Client

    def __init__(self, recipient: str):
        load_dotenv()
        intents = discord.Intents.default()
        intents.message_content = True

        self.client = discord.Client(intents=intents, token=os.getenv("DISCORD_TOKEN"))
        self.recipient = recipient

    def send_message(self, message: str):
        dm_channel = self.client.create_dm(self.recipient)
        dm_channel.send(message)
