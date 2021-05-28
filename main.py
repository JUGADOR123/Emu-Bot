
import os
import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from discord_slash import SlashCommand
from datetime import datetime
from dotenv import load_dotenv
import settings

settings.init()
load_dotenv()
token = os.getenv('key')
# construct bot
bot = commands.Bot(command_prefix='*')
slash = SlashCommand(bot, override_type=True, sync_commands=True)


# get boot date and time
time = datetime.now()
uptime = time.strftime("%d/%m/%Y %H:%M:%S")

# Load Cogs
for filename in os.listdir('cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
# bot.load_extension(f'cogs.Others')


# Handle common errors
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send(f'{ctx.author.mention} Command not found')
        print(f'{datetime.now()} {ctx.author} has sent a bad command')
        return
    if isinstance(error, commands.MemberNotFound):
        await ctx.send(f'{ctx.author.mention} User not found')
        print(f'{datetime.now()} {ctx.author} has sent a bad argument')
        return
    raise error


@bot.event
async def on_ready():
    print('Bot {0.user}'.format(bot))
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Slash commands!! 🎂🎂"))
bot.run(token)
