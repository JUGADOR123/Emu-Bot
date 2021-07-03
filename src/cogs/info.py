from discord.ext import commands
from discord_slash import cog_ext
import discord_slash
from discord_slash.model import SlashCommandPermissionType
from discord_slash.utils.manage_components import create_button, create_actionrow
import src.messages as messages

#blacklist emurelated
blacklist = {737428668816818216: [discord_slash.utils.manage_commands.create_permission(
    737428668816818216, SlashCommandPermissionType.ROLE, False)]}
footerButtons = [
    create_button(
        style=1,
        label="Made by Jugador",
        emoji="♥",
        disabled=True),
    create_button(
        style=5,
        label="Invite Me!",
        url="https://discord.com/api/oauth2/authorize?client_id=752568871986397216&permissions=2213932102&scope=bot%20applications.commands", emoji="♥"
        ),
]
footerBar=create_actionrow(*footerButtons)

class info(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
    #profile Editor

    @cog_ext.cog_slash(name="editor", description="Skip a quest, get money, skills, etc",permissions=blacklist)
    async def editor(self,ctx):
        buttons=[
            create_button(
                style=5,
                label="Release",
                url="https://github.com/JustEmuTarkov/JET-ProfileEditor/releases"
            ),
            create_button(
                style=5,
                label="Source",
                url="https://github.com/JustEmuTarkov/JET-ProfileEditor"
            ),
        ]
        await ctx.send(embed=messages.editor(),components=[
            create_actionrow(*buttons),
            footerBar
        ])

    @cog_ext.cog_slash(name="info", description="General Information about the Jet Project",permissions=blacklist)
    async def info(self,ctx):
        buttons=[
            create_button(
                style=5,
                label="Documentation",
                url="https://docs.justemutarkov.eu/"
            ),
            create_button(
                style=5,
                label="Mods Archive",
                url="https://justemutarkov.eu/download"
            ),
            create_button(
                style=5,
                label="Jet Discord Invite",
                url="https://discord.gg/Gbn5bTV"
            )
        ]

        await ctx.send(embed=messages.info(),components=[
            create_actionrow(*buttons),
            footerBar
        ])

    @cog_ext.cog_slash(name="port", description="Solutions for port already in use error",permissions=blacklist)
    async def port(self,ctx):
        await ctx.send(embed=messages.port(),components=footerBar)


def setup(bot):
    bot.add_cog(info(bot))
