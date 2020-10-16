import discord
import os
import asyncio
from discord.ext import commands
from discord.ext.commands import bot

client = commands.Bot(command_prefix='!')

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

@client.event
async def on_massage(message):
    await client.process_commands(message)
    if message.author.bot:
        return None

    if message.content.startswitch("!say"): 
        await message.channel.send("why") 

    if message.content.startswith("!안녕"):
        await message.channel.send('안녕하세요')

    if message.content.startswith("!계산"):
        global calcResult
        param = message.content.split()
        try:
            if param[1].startswith("더하기"):
                calcResult = int(param[2])+int(param[3])
                await message.channel.send("Result : "+str(calcResult))
            if param[1].startswith("빼기"):
                calcResult = int(param[2])-int(param[3])
                await message.channel.send("Result : "+str(calcResult))
            if param[1].startswith("곱하기"):
                calcResult = int(param[2])*int(param[3])
                await message.channel.send("Result : "+str(calcResult))
            if param[1].startswith("나누기"):
                calcResult = int(param[2])/int(param[3])
                await message.channel.send("Result : "+str(calcResult))
        except IndexError:
            await message.channel.send("무슨 숫자를 계산할지 알려주세요.")
        except ValueError:
            await message.channel.send("숫자로 넣어주세요.")
        except ZeroDivisionError:
            await message.channel.send("You can't divide with 0.")
 
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
