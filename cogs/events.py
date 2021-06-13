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
    async def on_member_join(self, member):
        guild = member.guild
        print(f'{member} Has joined {guild}')
        if guild.system_channel is not None:
            await guild.system_channel.send(embed=messages.welcome(member))

    @commands.Cog.listener()
    async def on_ready(self):
        DiscordComponents(self.bot)
        for guild in self.bot.guilds:
            with open('guilds.json','r+') as file:
                data=json.load(file)
                if guild.id not in data:
                    data.append(guild.id)
                    file.seek(0)
                    json.dump(data,file)
                    file.truncate()
                    print(f'Added Guild: '+guild.name+' to the list')
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
                time = datetime.now()

                stuff = f'[{time.strftime("%b %d %Y %H:%M:%S")}] [{message.guild} @ {message.channel}] [{message.author}] : {message.content}'
                print(stuff)
    #@commands.Cog.listener()
    #async def on_button_click(self,res):
    #    await res.respond(type=InteractionType.ChannelMessageWithSource,content=f"{res.component.label} pressed")

def setup(bot):
    bot.add_cog(events(bot))
