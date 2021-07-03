import json
import discord
import discord_slash
from discord.ext import commands

class Bot(commands.Bot):
    """
    Expands on the default bot class, and helps with type-hinting Thank you LordofPolls
    """
    def __init__(self,*args,**kwargs):
        self.appInfo: discord.AppInfo = None
        """A cached application info"""

        self.startTime = None
        """The time the bot started"""

        self.shouldUpdateBL = True
        """Should the bot try and update bot-lists"""
        with open("data/emoji.json","r") as emoji:
            self.emoji_list=json.load(emoji)
        """A dict of emoji the bot uses"""
        super().__init__(*args,**kwargs)
        self.slash: discord_slash=discord_slash.SlashCommand(self,sync_commands=True,delete_from_unused_guilds=True)


        
