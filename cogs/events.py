import re
from difflib import SequenceMatcher
from urllib.parse import urlparse
import discord
from datetime import datetime
from discord_components.client import DiscordComponents
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

    #@commands.Cog.listener()
    #async def on_button_click(self,res):
    #    await res.respond(type=InteractionType.ChannelMessageWithSource,content=f"{res.component.label} pressed")
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if message.author == message.author.bot:
            return
        modChannel = self.bot.get_channel(740048843575525437)

        regex = re.compile(
            r'((https)|(http)):\/\/st.*((\.ru)|(\.com))')
        
        content = message.content
        match = re.findall(regex,content)
        if(match):
            foundLinks = re.search(
                "(?P<url>https?://[^\s]+)", content).group('url')
            parsed = urlparse(url=foundLinks)
            likeness = SequenceMatcher(
                None, 'steamcommunity.com', parsed.hostname).ratio()
            matches = re.findall(regex, foundLinks)
            if matches and likeness < 1:
                result = "{:.3f}.format(likeness)"
                print(
                    f'Message sent by: {message.author} \n Possible Scam link: {parsed.hostname} with a match of: {result}')
                await message.delete()
                
                await modChannel.send(f"Message sent by: {message.author.mention} \n Possible Scam link: {parsed.hostname} with a match of: {result}")
                await message.author.send(f"you were token logged due to a malicious file you have opened, your account is currently being used as a phishing bot in servers. please change your password as your account security is critical")


        

def setup(bot):
    bot.add_cog(events(bot))
