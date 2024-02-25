import discord
from discord import option
from discord.ext import commands, tasks
import os
from dotenv import load_dotenv
import random
import json
import datetime
import traceback
from discord.ui import Button
import math

intents = discord.Intents.all()
intents.typing = False
intents.presences = False
intents.message_content = True

bot = commands.Bot(command_prefix=commands.when_mentioned_or("포노포요야 ", "포노포요 ", "포포씨 ", "ㅍ ", ), intents=intents)

#디버그 메시지 발송
#버그 있음

async def senddebug(massage):
    channel = bot.get_channel(1210730925663723600)
    channel.send(massage)