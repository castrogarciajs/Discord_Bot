import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

# Read variable
load_dotenv()

token = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='>', description='Bot Helper Bot')

@bot.command()
async def init(ctx):
    await ctx.send('Hola En que puedo ayudarte :) ?')

bot.run(token)

print("Hello Wordl Discord !")