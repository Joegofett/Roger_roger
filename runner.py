import requests
import discord
from ingestor import on_message

client = discord.Client()
client.run('')

@client.event
on_message
