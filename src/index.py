import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

# Read variable
load_dotenv()

token = os.getenv('TOKEN')

intents = discord.Intents.default()

# Intents
intents.members = True
intents.messages = True
intents.dm_messages = True
intents.guilds = True
intents.guild_messages = True

bot = commands.Bot(command_prefix='>', description='Bot Helper Bot',intents=intents)

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

bot.run(token)

print("Hello World Discord !")