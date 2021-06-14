
from asyncio.exceptions import TimeoutError
import slash_patch
from discord.ext import commands
from discord_components.button import ButtonStyle
from discord_slash import cog_ext, SlashContext
from discord_components import Button
import messages
import warmup

auth = Button(style=4, label="Made by Jug", disabled=True)

class Info(commands.Cog):
    """Information Related commands"""
    
    def __init__(self, bot):
        self.bot = bot

    # common information(updates,installation,etc,multiplayer)

    @cog_ext.cog_slash(name="info", guild_ids=warmup.guilds, description="General Information about the Jet Project")
    async def info(self, ctx: SlashContext):
        """General Information about the Jet Project"""
        await ctx.send(embed=messages.info(ctx), components=[[Button(style=ButtonStyle.URL, label="Documentation", url="https://docs.justemutarkov.eu/"), Button(style=ButtonStyle.URL, label="Mods Archive", url="https://justemutarkov.eu/download"), Button(style=ButtonStyle.URL, label="Jet Discord Invite", url="https://discord.gg/Gbn5bTV")],[auth]])

    # harder bots

    @cog_ext.cog_slash(name="difficulty", guild_ids=warmup.guilds, description="Make the game harder")
    async def difficulty(self, ctx: SlashContext):
        """Make the game harder"""
        await ctx.send(embed=messages.difficulty(ctx))

    # profile editor

    @cog_ext.cog_slash(name="editor", guild_ids=warmup.guilds, description="Skip a quest, get money, skills, etc")
    async def editor(self, ctx: SlashContext):
        """Skip a quest, get money, skills, etc"""
        await ctx.send(embed=messages.editor(ctx))
    # all in one

    @cog_ext.cog_slash(name="aio", guild_ids=warmup.guilds, description="How to shorten hideout craftings, longer raids,no weight, etc.")
    async def aio(self, ctx: SlashContext):
        """How to shorten hideout craftings, longer raids,no weight, etc."""
        await ctx.send(embed=messages.hideout(ctx))
    # server closes instantly

    @cog_ext.cog_slash(name="server", guild_ids=warmup.guilds, description="Fix for Server Closes Instantly")
    async def server(self, ctx: SlashContext):
        """Server Closes Instantly"""
        await ctx.send(embed=messages.server(ctx))
# general install

    @cog_ext.cog_slash(name="install", guild_ids=warmup.guilds, description="How to install Jet 12.9")
    async def install(self, ctx: SlashContext):
        """How to install Jet 12.9"""
        steps = messages.install()
        index = 1
        b1=Button(style=3, label="Previous", id="prev", disabled=True)
        b2=Button(style=1, label=f"Step 1/6", disabled=True)
        b3=Button(style=3, label="Next", id="next")
        
        comps=[[b1,b2,b3],[auth]]
        msg = await ctx.send(embed=steps["1"], components=comps)
        while True:
            try:
                inte = await self.bot.wait_for("button_click", timeout=120, check=lambda i: i.message.id == msg.id)
            except TimeoutError:
               return
            else:
                if inte.component.id == "next" and index < 6:
                    index=index+1
                    comps[0][1].label=f"Step {index}/6"
                    comps[0][0].disabled=False
                    await msg.edit(embed=steps[f"{index}"],components=comps)
                    await inte.respond(type=6)
                if inte.component.id=="prev" and index > 1:
                    index=index-1
                    comps[0][1].label = f"Step {index}/6"
                    await msg.edit(embed=steps[f"{index}"], components=comps)
                    await inte.respond(type=6)
                if index==1:
                    comps[0][0].disabled=True
                    await msg.edit(embed=steps[f"{index}"], components=comps)
                    
                if index==6:
                    comps[0][2].disabled=True
                    await msg.edit(embed=steps[f"{index}"], components=comps)
                   

# send noobs to kovac's discord

    @cog_ext.cog_slash(name="kovacs", guild_ids=warmup.guilds, description="Kovacs related help")
    async def kovacs(self, ctx: SlashContext):
        """Kovacs related help"""
        await ctx.send(embed=messages.kovacs(ctx))

    @cog_ext.cog_slash(name="key", guild_ids=warmup.guilds, description="A key has already been added fix")
    async def key(self, ctx: SlashContext):
        """A key has already been added fix"""
        await ctx.send(embed=messages.key(ctx))


def setup(bot):
    bot.add_cog(Info(bot))
