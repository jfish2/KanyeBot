#kanyebot.py
import os

from discord.ext import commands
from dotenv import load_dotenv, find_dotenv
import requests
import discord

load_dotenv(find_dotenv())
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

bot = commands.Bot(command_prefix="$") #In case you want to use the bot wrapper with additional functionality

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)

    print(
        f'{client.user} is now connected to the following guild: \n'
        f'{guild.name}(id: {guild.id})'
    )
    print(client.user.name)
    print('Is this a bot? {}'.format(client.user.bot))

@client.event
async def on_message(message):
    if message.author == client.user: #Handle infinite loops so bot doesn't respond to itself
        return
    url = "https://api.kanye.rest?format=text"

    if message.content.lower() in ["kanye, what's up?", 'sup kanye', 'kanye'] :
        response = requests.get(url)
        print('Getting dope thoughts...')
        await message.channel.send(response.text)




client.run(TOKEN)
