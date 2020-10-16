import discord
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

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

client.run("NzY2MjY2MTcwNzQ3Mzg3OTQ1.X4g2-w.r7dOd9_VibQ2D0GWA8T_BcNZBDw")