import time

import discord
from discord import option
from discord.ext import commands, tasks
import os
from dotenv import load_dotenv
from module.ponopoyo_debug import senddebug
import random
import json
import datetime
import traceback
from discord.ui import Button
import math

# 관리 권한
intents = discord.Intents.all()
intents.typing = False
intents.presences = False
intents.message_content = True

# 봇 설정
bot = commands.Bot(command_prefix=commands.when_mentioned_or("포노포요야 ", "포노포요 ", "포포씨 ", "ㅍ ", ), intents=intents)


# 시작되었을때 봇 설정
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="PonopoyoAlpha"))
    await debug_send(f"{bot.user} online, {time.time()}")


# 명령어 status
@bot.command(name="status")
async def status(ctx):
    await ctx.send(f"online, {ctx}")


# 명령어 action
@bot.command(name="action")
async def action(ctx):
    # 현재 버그 있음 여기서 메시지를 받고 공백으로 분할해서 맨 끝에 있는 명령어를 가지고 와야 함
    try:
        await print(eval(command))

    except Exception as e:
        error_traceback = traceback.format_exc()
        embed = discord.Embed(title="에러났잖아... 책임져", description=f"{error_traceback} in error: {command}",
                              color=0xFF0000)
        await ctx.respond(embed=embed)


# 디버그 보내기
async def debug_send(massage):
    channel = bot.get_channel(1210730925663723600)
    await channel.send(massage)
    print(massage)


# 실행
load_dotenv()
bot.run(os.getenv('TOKEN'))
