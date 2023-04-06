import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

# Read variable
load_dotenv()

token: str = os.getenv('TOKEN')

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='$ ', description='Bot Helper Bot',intents=intents)

@bot.command()
async def init(ctx):
    await ctx.send('Hola En que puedo ayudarte :) ?')


@bot.command()
async def sum(ctx, number_one: int, number_two: int):
    await ctx.send(number_one + number_two)

# Event

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name='Example', url='http://www.twitch.tv/accountname'))
    print('My Bot On ready')

try:
    bot.run(token)
    print("Hello World Discord !")
except discord.errors.LoginFailure as error:
    print(error)   

