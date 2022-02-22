import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

bot.run('OTQ1NTM0MzQ3MTQ5MTk3Mzcy.YhRjew.hXChyh1CVO-jfWs8MlCRFayTqw4')