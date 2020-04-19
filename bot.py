import discord
from discord.ext import commands

creds = open('./creds', 'r').read()

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('Ready!')

client.run(creds)