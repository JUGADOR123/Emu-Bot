
from asyncio.exceptions import TimeoutError
import src.slash_patch
from discord.ext import commands
from discord_components.button import ButtonStyle
from discord_slash import cog_ext, SlashContext
from discord_components import Button
import src.messages as messages
import src.warmup as warmup

auth = Button(style=1, label="Made by Jug", emoji="♥", disabled=True)
invite = Button(style=5, label="Invite Me!",
                url="https://discord.com/api/oauth2/authorize?client_id=752568871986397216&permissions=2201873472&scope=bot%20applications.commands", emoji="♥")


class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # common information(updates,installation,etc,multiplayer)

    @cog_ext.cog_slash(name="info", description="General Information about the Jet Project")
    async def info(self, ctx: SlashContext):
        await ctx.send(embed=messages.info(ctx), components=[[Button(style=ButtonStyle.URL, label="Documentation", url="https://docs.justemutarkov.eu/"), Button(style=ButtonStyle.URL, label="Mods Archive", url="https://justemutarkov.eu/download"), Button(style=ButtonStyle.URL, label="Jet Discord Invite", url="https://discord.gg/Gbn5bTV")], [auth, invite]])

    # profile editor

    @cog_ext.cog_slash(name="editor", description="Skip a quest, get money, skills, etc")
    async def editor(self, ctx: SlashContext):
        rel = Button(style=5, label="Release",
                     url="https://github.com/JustEmuTarkov/JET-ProfileEditor/releases")
        src = Button(style=5, label="Source Code",
                     url="https://github.com/JustEmuTarkov/JET-ProfileEditor")
        comps = [[rel, src], [auth, invite]]
        await ctx.send(embed=messages.editor(ctx), components=comps)
# general install

    @cog_ext.cog_slash(name="install", description="How to install Jet 12.9")
    async def install(self, ctx: SlashContext):
        steps = messages.install()
        index = 1
        b1 = Button(style=3, label="Previous", id="prev0", disabled=True)
        b2 = Button(style=1, label=f"Step 1/6", disabled=True)
        b3 = Button(style=3, label="Next", id="next0")

        comps = [[b1, b2, b3], [auth, invite]]
        msg = await ctx.send(embed=steps["1"], components=comps)
        while True:
            try:
                inte = await self.bot.wait_for("button_click", timeout=120, check=lambda i: i.message.id == msg.id)
            except TimeoutError:
                return
            else:
                if inte.component.id == "next0" and index < 6:
                    index = index+1
                    comps[0][1].label = f"Step {index}/6"
                    comps[0][0].disabled = False
                    await msg.edit(embed=steps[f"{index}"], components=comps)
                    await inte.respond(type=6)
                if inte.component.id == "prev0" and index > 1:
                    index = index-1
                    comps[0][1].label = f"Step {index}/6"
                    await msg.edit(embed=steps[f"{index}"], components=comps)
                    await inte.respond(type=6)
                if index == 1:
                    comps[0][0].disabled = True
                    await msg.edit(embed=steps[f"{index}"], components=comps)

                if index == 6:
                    comps[0][2].disabled = True
                    await msg.edit(embed=steps[f"{index}"], components=comps)
    # key already added fix

    @cog_ext.cog_slash(name="key", description="A key has already been added fix")
    async def key(self, ctx: SlashContext):
        b1 = Button(style=3, label="Previous", id="prev1", disabled=True)
        b2 = Button(style=1, label=f"Step 1/6", disabled=True)
        b3 = Button(style=3, label="Next", id="next1")
        comps = [[b1, b2, b3], [auth, invite]]
        steps = messages.key()
        index = 1
        msg = await ctx.send(embed=steps[f"{index}"], components=comps)
        while True:
            try:
                inte = await self.bot.wait_for("button_click", timeout=120, check=lambda i: i.message.id == msg.id)
            except TimeoutError:
                return
            else:
                if inte.component.id == "next1" and index < 6:
                    index = index+1
                    comps[0][1].label = f"Step {index}/6"
                    comps[0][0].disabled = False
                    await msg.edit(embed=steps[f"{index}"], components=comps)
                    await inte.respond(type=6)
                if inte.component.id == "prev1" and index > 1:
                    index = index-1
                    comps[0][1].label = f"Step {index}/6"
                    await msg.edit(embed=steps[f"{index}"], components=comps)
                    await inte.respond(type=6)
                if index == 1:
                    comps[0][0].disabled = True
                    await msg.edit(embed=steps[f"{index}"], components=comps)

                if index == 6:
                    comps[0][2].disabled = True
                    await msg.edit(embed=steps[f"{index}"], components=comps)

    @cog_ext.cog_slash(name="port", description="Solutions for port already in use error")
    async def port(self, ctx: SlashContext):
        comps = [[auth, invite]]
        await ctx.send(embed=messages.port(), components=comps)


def setup(bot):
    bot.add_cog(Info(bot))
