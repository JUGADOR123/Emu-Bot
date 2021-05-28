import json
import os
import discord
from datetime import datetime
import messages
from discord.ext import commands


class events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild = member.guild
        print(f'{member} Has joined {guild}')
        if guild.system_channel is not None:
            await guild.system_channel.send(embed=messages.welcome(member))

    @commands.Cog.listener()
    async def on_ready(self):
        print(str(datetime.now().time()) +
              ' Bot has logged in as: {0.user}'.format(self.bot))

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        print(f'Bot has joined {guild}')
        with open('guilds.json', 'r+') as file:
            data = json.load(file)
            data.append(guild.id)
            file.seek(0)
            json.dump(data, file)
            file.truncate()
        # reload the cogs
        for filename in os.listdir('cogs'):
            if filename.endswith('.py'):
                self.bot.reload_extension(f'cogs.{filename[:-3]}')

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        print(f'Bot has left the guild: {guild}')
        with open('guilds.json', 'r+') as file:
            data = json.load(file)
            if guild.id in data:
                data.remove(guild.id)
                file.seek(0)
                json.dump(data, file)
                file.truncate()
                # reload the cogs
        for filename in os.listdir('cogs'):
            if filename.endswith('.py'):
                self.bot.reload_extension(f'cogs.{filename[:-3]}')
        print(str(datetime.now())+' Cogs have been reloaded')

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author is not self.bot:
            if message.author is not message.author.bot:
                stuff = f'[{datetime.now()}] [{message.guild} @ {message.channel}] [{message.author}] : {message.content}'
                print(stuff)


def setup(bot):
    bot.add_cog(events(bot))
