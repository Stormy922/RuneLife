import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Eingeloggt als')
    print(client.user.name)
    print(client.user.id)
    print('-----------')


@client.event
async def on_message(message):
    if message.content.lower().startswith('?test'):
        await client.send_message(message.channel, "Test bestanden")


client.run('NDc1MzU4OTQ1OTA1NDc1NjA1.DkfBJQ.SEBQqoaeISrBuklQv6Xx2XL3wVM')
