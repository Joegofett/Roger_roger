import requests
import discord

client = discord.Client()

@client.event
async def on_message(message):
    if message.author ==client.user:
        return

    if message.content.startswith('$help'):
        await message.channel.send("""Roger_roger \n 
        What do I do?
        Currently I make Polls\n
        How do I do this?
        $poll [Question]\n [Option1], [Option2], [Option3]\n
        Where is my code?
        https://github.com/Joegofett/Roger_roger/tree/master
        """)

    if message.content.startswith('$poll %s '.):
        await message.channel.send(""" Test""")

client.run('')
