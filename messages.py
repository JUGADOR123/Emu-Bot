import json
import random
import discord
import warmup
from datetime import datetime


def shortMsg():
    shortMsg = discord.Embed(
        title="Need Help?", description=r"Do you need help? Cant find the solution for your problem? type / and see all the available commands! Keep in mind, this is JET not AKI", color=0xF5D713, timestamp=datetime.now())
    shortMsg.set_thumbnail(
        url=str("https://cdn.discordapp.com/emojis/354149510252986378.png"))
    return shortMsg
# Embed for Installation


def install(context):
    install = discord.Embed(title="How to get JET 12.9", timestamp=datetime.now(
    ), description=f"We have multiple ways of getting JET, choose the one you desire")

    install.add_field(name="Option 1 ",
                      value="Go to [this message](https://discord.com/channels/739984913599692881/739985161973792839/777963115198545940) and follow the instructions ", inline=False)
    install.add_field(
        name="Step 2", value="It is also recommended to follow [this](https://discord.com/channels/739984913599692881/739985161973792839/818148664472109066), it will prevent \"Key Already Added \" from happening")
    return install
# Embed for Population


def popu(context):
    popu = discord.Embed(title="Population", color=0xF5D713,
                         timestamp=datetime.now(), description=f"Hey there {context.author.mention} You are part of the {context.guild.member_count} members of this server!")
    popu.set_thumbnail(url=str("https://i.imgur.com/lDGYw7D.png"))
    return popu
# Embed for main information


def info(context):
    info = discord.Embed(title="General Information", color=0xF5D713, timestamp=datetime.now(
    ), description=f"Hey {context.author.mention} you looking for some general information? This is the right place!")
    info.add_field(
        name="Update", value="We will announce when JET is updated", inline=True)
    info.add_field(name="Multiplayer?",
                   value="Planned, not in constant development", inline=True)
    info.add_field(name="Do i need official tarkov?",
                   value="Nope, all files are given", inline=True)
    info.add_field(name="How to install?",
                   value="Check the [install](https://discord.com/channels/739984913599692881/739985161973792839/816229421186940958) OR use *install", inline=True)
    info.add_field(name="How to install mods?",
                   value="drop the folders under user/mods and delete the user/cache folder", inline=True)
    info.add_field(name="Documentation",
                   value="You can find how to mod, make edits and general info [HERE](https://docs.kiobu.dev/)", inline=True)
    info.set_thumbnail(url=str("https://imgur.com/DRNkd2a.png"))
    return info

# embed for port fix


def port(context):
    port = discord.Embed(title="Port Permission Denied Fix",
                         color=0xF5D713, timestamp=datetime.now(), description=f"Hey {context.author.mention} Go to user/config/server.json and change the port to something else, then go to you game client, open the launcher.config.json and change the port so its the same one as the file earlier")
    port.set_image(url=str("https://imgur.com/QjmUklX.png"))
    return port

# embed for difficulty


def difficulty(context):
    difficulty = discord.Embed(title="Want a real challenge huh?",
                               color=0xF5D713, timestamp=datetime.now(), description=f"I see, so u believe u can do better {context.author.mention}? Well prove it")
    difficulty.add_field(
        name="Step 1", value="You can use Altered Escape Mod to get harder gameplay, you can find it [here](https://discord.gg/AwvGSFHucw)", inline=False)
    return difficulty

# embed for jet editor


def editor(context):
    editor = discord.Embed(title="Jet Profile Editor", color=0xF5D713, timestamp=datetime.now(
    ), description=f"{context.author.mention} you cheeky bastard you want to skip a quest or give youself money, dont you? Anyways here is how:")
    editor.add_field(name="Where to Get?",
                     value="[Here](https://github.com/JustEmuTarkov/JET-ProfileEditor/releases)", inline=False)
    return editor
# embed for all in one mod


def hideout(context):
    hideout = discord.Embed(title="Short Crafting timers, Remove Weight, more stamina,etc",
                            color=0xF5D713, timestamp=datetime.now(), description=f"Hey {context.author.mention} here is how you fix the bug plus more goodies")
    hideout.add_field(
        name="Step 1", value="Download [All in One Mod](https://github.com/JUGADOR123/All-in-One/releases)", inline=False)
    hideout.add_field(
        name="Step 2", value="Extract it on user/mods", inline=False)
    hideout.add_field(
        name="Step 3", value="Chose your settings on config.json ", inline=False)
    hideout.add_field(name="Step 4", value="Delete user/cache", inline=False)
    return hideout
# embed for general server fix


def server(context):
    server = discord.Embed(title="Fix server closing instantly upon booting", color=0xF5D713, timestamp=datetime.now(
    ), description=f"Lmao look at this dude {context.author.mention} he broke his server lmaooo, get a load of this guy. Anyways, there is no fix for that you have to reinstall")
    server.set_image(url=str(
        "https://media.tenor.com/images/8c23b964645e1e7de2b958964efb5328/tenor.gif"))
    return server
# embed for kovacs help


def kovacs(context):
    kovacs = discord.Embed(title="Kovacs Related Help",  color=0xF5D713,
                           timestamp=datetime.now(), description=f"Hey there {context.author.mention} you need help with altered escape install? or any of the kovacs mods? PLEASE refer to that under [Kovac's Discord](https://discord.gg/AwvGSFHucw) ")
    return kovacs
# embed for bonk


def bonk(ctx, member):
    with open('images/bonk.json') as file:
        data = json.load(file)
        chosen = random.choice(data)

    bonk = discord.Embed(title="YOU HAVE BEEN BONKED", color=0xF5D713, timestamp=datetime.now(
    ), description=f"{member.mention} you have been bonked by{ctx.author.mention}")
    bonk.set_image(url=str(chosen))
    return bonk
# embed for key already added


def key(ctx):
    key = discord.Embed(title="A key has already been added fix",
                        timestamp=datetime.now(), description=f"How to fix this issue")
    key.add_field(
        name="Step 1", value="Locate your character.json (user/profiles/AID/here)", inline=False)
    key.add_field(
        name="Step 2", value="Go to <#740002608424550522> or <#829464850895077406> and do !!clean with your character.json attached", inline=False)
    key.add_field(
        name="Step 3", value="Replace your current character.json with the new clean one", inline=False)
    key.add_field(name="Step 4 (Optional but recommended)",
                  value="follow [this instructions](https://discord.com/channels/739984913599692881/739985161973792839/818148664472109066), they will prevent this bug from happening again")
    return key


def hug(ctx, member):
    with open('images/hug.json') as file:
        data=json.load(file)
        chosen=random.choice(data)

    hug = discord.Embed(title="You have been hugged", timestamp=datetime.now(
    ), description=f"{member.mention} you have been hugged by{ctx.author.mention}")
    hug.set_image(url=str(chosen))
    return hug


def welcome(member):
    with open('images/hello.json', 'r+') as file:
        data = json.load(file)
        chosen = random.choice(data)

    welcome = discord.Embed(
        title='\u200b', color=warmup.r, timestamp=datetime.now())
    welcome.add_field(
        name='\u200b', value=f'Welcome {member.mention} to the server!')
    welcome.set_image(url=str(chosen))
    return welcome
