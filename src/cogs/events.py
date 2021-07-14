import re
from difflib import SequenceMatcher
from urllib.parse import urlparse

from discord.ext import commands


class events(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        print(f"Bot has joined {guild}")

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        print(f"Bot has left the guild: {guild}")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if message.author == message.author.bot:
            return
        log1 = self.bot.get_channel(858971025174036540)  # Emutarkov logs
        log2 = self.bot.get_channel(826592098702721065)  # emu related

        regex = re.compile(r"((https)|(http)):\/\/st.*((\.ru)|(\.com))")

        content = message.content
        match = re.findall(regex, content)
        if match:
            foundLinks = re.search("(?P<url>https?://[^\s]+)", content).group("url")
            parsed = urlparse(url=foundLinks)
            likeness = SequenceMatcher(
                None, "steamcommunity.com", parsed.hostname
            ).ratio()
            matches = re.findall(regex, foundLinks)
            for match in matches:
                if match and likeness < 1 and likeness > 0.65:
                    result = "{:.3f}".format(likeness)
                    print(
                        f"Message sent by: {message.author} \n Possible Scam link: {parsed.hostname} with a match of: {result}"
                    )
                    await message.delete()
                    if message.guild.id == 826592098702721065:  # post in emu related
                        await log2.send(
                            f"Message sent by: {message.author.mention} \n Possible Scam link: {parsed.hostname} with a match of: {result}"
                        )
                    else:  # post in emutarkov
                        await log1.send(
                            f"Message sent by: {message.author.mention} \n Possible Scam link: {parsed.hostname} with a match of: {result}"
                        )
                    await message.author.send(
                        f"you were token logged due to a malicious file you have opened, your account is currently being used as a phishing bot in servers. please change your password as your account security is critical"
                    )


def setup(bot):
    bot.add_cog(events(bot))
