import os
import discord

from dotenv import load_dotenv
from unidecode import unidecode

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise

@client.event
async def on_message(message):
    # Don't respond to ourselves
    if message.author == client.user:
        return

    if 'zacina noc' in unidecode(message.content.lower()):
        await message.channel.send('Drz hubu')

client.run(token)