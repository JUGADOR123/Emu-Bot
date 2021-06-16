import re
from difflib import SequenceMatcher
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
        regex = re.compile(r'(s(?!:).{10,17}y)')
        content = message.content
        match = re.findall(regex, content)
        for entry in match:
            likeness = SequenceMatcher(None, 'steamcommunity', entry).ratio()
            scam_match = re.search(
                rf'(https?://)?{re.escape(entry)}(\.(ru|com))', content)
            if scam_match and 0.76 <= likeness < 1:
                print(
                    f'{str(datetime.now().time())}| Message Deleted from: {message.author}')
                await message.delete()
                await message.author.send(f"you were token logged due to a malicious file you have opened, your account is currently being used as a phishing bot in servers. please change your password as your account security is critical")

def setup(bot):
    bot.add_cog(events(bot))
