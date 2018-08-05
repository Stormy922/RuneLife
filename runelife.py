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
    
async def ex(args, message, client, invoke):

    try:
        ammount = int(args[0]) + 1 if len(args) > 0 else 2
    except:
        await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), descrition="Please enter a valid value for message ammount!"))
        return

    cleared = 0
    failed = 0

    async for m in client.logs_from(message.channel, limit=ammount):
        try:
            await client.delete_message(m)
            cleared += 1
        except:
            failed += 1
            pass

    failed_str = "\n\nFailed to clear %s message(s)." % failed if failed > 0 else ""
    returnmsg = await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.blue(), description="Cleared %s message(s).%s" % (cleared, failed_str)))
    await asyncio.sleep(4)
    await client.delete_message(returnmsg)

    # SCHNELLERE ALTERNATIVE:
    # messages = []
    # async for m in client.logs_from(message.channel, limit=ammount):
    #     messages.append(m)

    # await client.delete_messages(messages)

    # return_msg = await client.send_message(message.channel, "Deleted %s messages." % ammount)
    # await asyncio.sleep(4)
    # await client.delete_message(return_msg)
    
client.run("NDc1MzU4OTQ1OTA1NDc1NjA1.DkfBJQ.SEBQqoaeISrBuklQv6Xx2XL3wVM")
