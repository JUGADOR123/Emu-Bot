import json
import os
import discord
from datetime import datetime
from discord_components.client import DiscordComponents
from discord_components.interaction import InteractionType
import messages
from discord.ext import commands


class events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    @commands.Cog.listener()
    async def on_ready(self):
        DiscordComponents(self.bot)
        print("<-------------------->")
        print(str(datetime.now().time()) +
              ' Bot has logged in as: {0.user}'.format(self.bot))
        print("<-------------------->")
        print("Active Guilds: ")
        for guild in self.bot.guilds:
            print(guild.name)
        print("<-------------------->")
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Slash commands!! 🎂🎂"))


    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        print(f'Bot has joined {guild}')

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        print(f'Bot has left the guild: {guild}')

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author is not self.bot:
            if message.author is not message.author.bot:
                time = datetime.now()

                stuff = f'[{time.strftime("%b %d %Y %H:%M:%S")}] [{message.guild} @ {message.channel}] [{message.author}] : {message.content}'
                print(stuff)
    #@commands.Cog.listener()
    #async def on_button_click(self,res):
    #    await res.respond(type=InteractionType.ChannelMessageWithSource,content=f"{res.component.label} pressed")

def setup(bot):
    bot.add_cog(events(bot))
