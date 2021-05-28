
import json
import messages
import discord
from discord_slash import cog_ext, SlashContext
from discord.ext import commands, tasks
from discord_slash.utils.manage_commands import create_option
import settings


def addchannel(tmp):

    # handle repetitive commands
    with open('channels.json', 'r+') as file:
        data = json.load(file)
        if tmp in data:
            return False
        else:
            data.append(tmp)
            file.seek(0)
            json.dump(data, file)
            file.truncate()
            return data


def rmchannel(tmp):
    with open('channels.json', 'r+') as file:
        data = json.load(file)
        if tmp in data:
            data.remove(tmp)
            file.seek(0)
            json.dump(data, file)
            file.truncate()
            return data
        else:
            return False


class Admin(commands.Cog):
    """Admin Tools"""

    def __init__(self, bot):
        self.bot = bot
    @tasks.loop(hours=1)
    async def timedMessages(self):
        with open('channels.json', 'r') as file:
            data=json.load(file)
            for id in data:
                channel=self.bot.get_channel(id)
                await channel.send(embed=messages.shortMsg())

    @cog_ext.cog_slash(name="add_channel", description="Adds Channel to the Timed Message Whitelist", guild_ids=settings.guilds)
    @commands.is_owner()
    async def add_channel(self, ctx: SlashContext, channel: discord.TextChannel):
        """Adds Channel to the Timed Message Whitelist"""
        tmp = addchannel(channel.id)
        if(tmp != False):
            await ctx.send(f"{ctx.author.mention} Succesfully added {channel.mention} to the whitelist \n Current Channel List: {tmp}")
        elif(tmp == False):
            await ctx.send(f"{ctx.author.mention} Channel not added to the whitelist: Key Already Exists")

    @cog_ext.cog_slash(name="rm_channel", description="Removes Channel from whitelist", guild_ids=settings.guilds)
    @commands.is_owner()
    async def rm_channel(self, ctx: SlashContext, channel: discord.TextChannel):
        """Removes Channel from whitelist"""
        tmp = rmchannel(channel.id)
        if(tmp != False):
            await ctx.send(f"{ctx.author.mention} Succesfully removed {channel.mention} from the whitelist")
        elif(tmp == False):
            await ctx.send(f"{ctx.author.mention} Couldn't remove channel from whitelist: Key does not exist.")

    @cog_ext.cog_slash(name="init_messages", description="Start/Stop repetitive messages", guild_ids=settings.guilds, options=[create_option(name="value", description="Enable or disable", option_type=5, required=True), create_option(name="time", description="Minutes", option_type=4, required=False)])
    @commands.is_owner()
    async def init_Messages(self, ctx: SlashContext, value: bool, time: int):
        if value is True:
            self.timedMessages.change_interval(minutes =time)
            self.timedMessages.start()
            await ctx.send(f'{ctx.author.mention} Started loop with a time of {time} minutes')
        else:
            self.timedMessages.stop()
            await ctx.send(f'{ctx.author.mention}Stopped the loop')


    


def setup(bot):
    bot.add_cog(Admin(bot))
