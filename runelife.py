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
    
   Client = Bot('!')

@Client.command(pass_context = True)
async def clear(ctx, number):
    number = int(number) #Converting the amount of messages to delete to an integer
    counter = 0
    async for x in Client.logs_from(ctx.message.channel, limit = number):
        if counter < number:
            await Client.delete_message(x)
            counter += 1
            await asyncio.sleep(1.2) #1.2 second timer so the deleting process can be even
 
    
client.run("NDc1MzU4OTQ1OTA1NDc1NjA1.DkfBJQ.SEBQqoaeISrBuklQv6Xx2XL3wVM")
