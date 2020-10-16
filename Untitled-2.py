import discord
import os
import asyncio
from discord.ext import commands

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print(client.user.id)
    print("로그인")
    game = discord.Game("steve bot 실행")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_massage(message):
    if message.content.startswitch("!안녕"):
        await message.channel.send("안녕하세요")

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
#[출처] 디스코드 봇 만들기 6 - 리팩터링하기 (1)|작성자 곰사냥 https://blog.naver.com/huntingbear21/221795947053

@client.command(name="청소", pass_context=True)
async def _clear(ctx, *, amount=5):
    await ctx.channel.purge(limit=amount)    

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
