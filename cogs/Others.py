import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option
import messages
import warmup


class Others(commands.Cog):
    """Other Stuff"""

    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="bonk", description="bonk another member", guild_ids=warmup.guilds, options=[create_option(name="member", description="Tag Member to bonk", option_type=6, required=True)])
    async def _bonk(self, ctx: SlashContext, member: discord.Member):
        """bonk another member"""
        try:
            await ctx.send(embed=messages.bonk(ctx, member))
        except discord.ext.commands.errors.MemberNotFound:
            await ctx.send(f'Hey there {ctx.author.mention}, we couldnt find that user')

    @cog_ext.cog_slash(name="hug", description="hug another member", guild_ids=warmup.guilds, options=[create_option(name="member", description="Tag Member to hug", option_type=6, required=True)])
    async def _hug(self, ctx: SlashContext, member: discord.Member):
        """Hug Another member"""
        await ctx.send(embed=messages.hug(ctx, member))


def setup(bot):
    bot.add_cog(Others(bot))
