import os
from datetime import datetime

import discord
import discord_slash
from dotenv import load_dotenv

from . import dataclass

intents = discord.Intents.all()
bot = dataclass.Bot(command_prefix="--", description="Emutarkov Bot",
                    case_insensitive=True, intents=intents, help_command=None)
slash = bot.slash
load_dotenv()
token = os.getenv('key')


def start():
    # Load Cogs
    print("Loading Cogs")
    for filename in os.listdir('src/cogs'):
        if filename.endswith('.py'):
            bot.load_extension(f'src.cogs.{filename[:-3]}')
            print(f"Loaded {filename}")
    print("Cogs Loaded")
    bot.run(token, bot=True, reconnect=True)


async def startupTasks():
    """All the tasks the bot needs to run when it starts up"""
    bot.appInfo = await bot.application_info()
    bot.startTime = datetime.now()


@bot.event
async def on_ready():
    """Called when the bot is ready"""
    if not bot.startTime:
        await startupTasks()
        output =f"""
"Logged in as         : {bot.user.name} #{bot.user.discriminator}"
"User ID              : {bot.user.id}"
"Start Time           : {bot.startTime.ctime()}"
"Server Count         : {len(bot.guilds)}"
"Cog Count            : {len(bot.cogs)}"
"Command Count        : {len(slash.commands)}"
"Discord.py Version   : {discord.__version__}"
"DiscordSlash Version : {discord_slash.__version__}"""
        print(f"{output}")
        await bot.change_presence(
            status=discord.Status.online,
            activity=discord.Activity(
                type=discord.ActivityType.watching, name="over your server"),
        )
