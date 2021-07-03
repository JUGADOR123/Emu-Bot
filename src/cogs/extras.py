import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option
import src.messages as messages
from datetime import datetime
import src.warmup as warmup


class extras(commands.Cog):
    """Other Stuff"""
    funserver = [727670103218585693]

    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="bonk", description="bonk another member",  options=[create_option(name="member", description="Tag Member to bonk", option_type=6, required=True)])
    async def _bonk(self, ctx: SlashContext, member: discord.Member):
        """bonk another member"""
        try:
            await ctx.send(embed=messages.bonk(ctx, member))
        except discord.ext.commands.errors.MemberNotFound:
            await ctx.send(f'Hey there {ctx.author.mention}, we couldnt find that user')

    @cog_ext.cog_slash(name="hug", description="hug another member", options=[create_option(name="member", description="Tag Member to hug", option_type=6, required=True)])
    async def _hug(self, ctx: SlashContext, member: discord.Member):
        """Hug Another member"""
        await ctx.send(embed=messages.hug(ctx, member))

    @cog_ext.cog_slash(name="funfix", description="General Form to fix any issues related to the FunServer", guild_ids=funserver, options=[
        create_option(name="ingame", description="your character name inside the fun server", option_type=3, required=True), create_option(name="quest", description="name or id of the quest that you need fixed if \"key already added error\" type duplicate item", option_type=3, required=True)])
    async def funfix(self, ctx: SlashContext, ingame: str, quest: str):
        msg = discord.Embed(
            title=f" FunServer Fix: {ctx.author}", description=f"Ingame Name: {ingame} \n Quest Id or Name: {quest}", timestamp=datetime.now(), color=warmup.rmd())
        log = self.bot.get_channel(823736552341241886)  # cfgg-dev-testing
        memb = self.bot.get_user(161194728405073921)  # struan
        await log.send(f"Incoming Fix {memb.mention}", embed=msg)
        await ctx.send(f"{ctx.author.mention} Successfully notified the Fun Server team", hidden=True)


def setup(bot):
    bot.add_cog(extras(bot))
