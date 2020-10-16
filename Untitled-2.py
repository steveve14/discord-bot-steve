import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("gogo")
    game = discord.Game("steve bot on")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_massage(message):
    if message.content.startswitch("안녕"):
        await message.channel.send("안녕하세요")
        
        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
