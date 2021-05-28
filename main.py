
import os
import logging
import discord
from discord.ext import commands
from discord_slash import SlashCommand
from dotenv import load_dotenv
import warmup

# Setup Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(
    filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter(
    '%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
# Warmup and global variables
load_dotenv()
warmup.init()
warmup.cachegifs()
token = os.getenv('key')
# Start Setting up the bot
intent = discord.Intents.default()
intent.members = True
intent.guilds = True
bot = commands.Bot(command_prefix='-', help_command=None,
                   description='Just a Discord Bot', intents=intent)
slash = SlashCommand(bot, sync_commands=True,
                     sync_on_cog_reload=True, override_type=True)
# Load Cogs
for filename in os.listdir('cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
# bot.load_extension(f'cogs.Others')
bot.run(token)
