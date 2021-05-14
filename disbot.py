import discord
import asyncio
from google_trans_new import google_translator
import os

TOKEN = os.environ.get('BOT_TOKEN')

class DiscordBot(discord.Client):
    async def on_message(self, message):
        if self.user != message.author:
            if message.content.startswith('!translate'):
                context = message.content[11:]
                print(context)
                translator = google_translator()
                translated_one = translator.translate(context, lang_src="en", lang_tgt='ru')
                print(translated_one)
                await message.channel.send(translated_one)


client = DiscordBot()
client.run(TOKEN)