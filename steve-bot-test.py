import discord
import os
import asyncio
from discord.ext import commands
from discord.ext.commands import bot

client = commands.Bot(command_prefix="/")

calcResult = 0

@client.event
async def on_ready():
    print("로그인")
    print(client.user.name)
    print(client.user.id)
    print('------')
    game = discord.Game("steve bot 실행")
    await client.change_presence(status=discord.Status.online, activity=game)
    
@client.command(name="청소", pass_context=True)
async def _clear(ctx, *, amount=5):
    await ctx.channel.purge(limit=amount)
    pass    

@client.command(name="list")
async def _list(ctx, arg):
    pass

@client.event
async def on_massage(message):
    await client.process_commands(message)
    if message.content.startswitch("/say"): 
        await message.channel.send("why") 
    if message.content.startswith("/안녕"):
        await message.channel.send("안녕하세요")
    if message.author.bot:
        return None
   
    access_token = os.environ["BOT_TOKEN"]
    client.run(access_token)
