import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time


Client = discord.Client() #Initialise Client 
client = commands.Bot(command_prefix = ".") #Initialise client bot

@client.event 
async def on_ready():
    print("Der Bot ist online und bereit sich zu verbinden mit Discord")

@client.event
async def on_message(message):
    if message.content.upper().startswith('.PING'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Pong!" % (userID))
        
client.run("NDc1MzU4OTQ1OTA1NDc1NjA1.DkfBJQ.SEBQqoaeISrBuklQv6Xx2XL3wVM")
