from src.Paginator import Paginator
import discord_slash
import src.messages as messages
from discord.ext import commands
from discord_slash import cog_ext
from discord_slash.model import SlashCommandPermissionType
from discord_slash.utils.manage_components import create_actionrow, create_button

ids=[842947049489563700]
class test(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
    @cog_ext.cog_slash(name="test",description="test",guild_ids=ids)
    async def test(self,ctx):
        await Paginator(bot=self.bot,ctx=ctx,pages=messages.install())
def setup(bot):
    bot.add_cog(test(bot))
