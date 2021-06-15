import json
import random
import discord
import warmup
from datetime import datetime


# Embed for Installation
def install():
    s1 = discord.Embed(
        title="Step 1", description="Download Escape From Tarkov 12.9 from [HERE](https://mega.nz/file/X8xUVZzC#I2jQWaAX6yRs94vscbsFCOU9rU7kleFmnpNZY8vMgLw) or from [HERE](https://drive.google.com/file/d/1hOJ10hiZk2EQUWKwHTPfhol5XgDpt2-U/view?usp=sharing) or [HERE](https://cdn.storeit.digital/file/JustEmuTarkov/EFT.0.12.9.2.10988.zip)", color=warmup.rmd(),timestamp=datetime.now())
    s2 = discord.Embed(
        title="Step 2", description="Download the [Server Files](https://mega.nz/folder/Fg1WCAbR#LVAylusBUPB0cJ6QQXI2QA/file/U8sWibaZ) and the [Game Binaries](https://mega.nz/folder/Fg1WCAbR#LVAylusBUPB0cJ6QQXI2QA/file/Y5tCjKZL)", color=warmup.rmd(),timestamp=datetime.now())
    s3 = discord.Embed(
        title="Step 3", description="Using [7-Zip](https://www.7-zip.org) extract the game, and then the binaries into the game folder, next extract the server elsewhere", color=warmup.rmd())
    s4 = discord.Embed(
        title="Step 4", description="Apply the [Key Already Added Fix](https://mega.nz/file/7EtxwAJK#DdsT5snvRAydwUXVw-364NUpUJBEiWspAKnlGdyoiwI) by downloading the file and extracting into server>src folder, when prompt select replace files", color=warmup.rmd(),timestamp=datetime.now())
    s5 = discord.Embed(
        title="Step 5", description="Launch the Jet launcher, it will open an error asking to locate the server, navigate to the location of the server and click ok", color=warmup.rmd(),timestamp=datetime.now())
    s6 = discord.Embed(title="Step 6", description="Click on Start Server and wait until you see the server name appear on the dropdown to the left side of the window, then hit connect, then create an account by clicking the little plus sign and you are ready to go", color=warmup.rmd(),timestamp=datetime.now())

    steps = {"1": s1, "2": s2, "3": s3, "4": s4, "5": s5, "6": s6}
    return steps


# Embed for main information


def info(context):
    info = discord.Embed(title="General information about the Jet Project", color=warmup.rmd(), timestamp=datetime.now())
    info.add_field(
        name="Update", value="We will announce when JET is updated", inline=True)
    info.add_field(name="Multiplayer?",
                   value="Planned, not in constant development", inline=True)
    info.add_field(name="Do i need official tarkov?",
                   value="Nope, all files are given", inline=True)
    info.add_field(name="How to install mods?",
                   value="drop the folders under user/mods and delete the user/cache folder", inline=True)
    info.set_thumbnail(url=str("https://imgur.com/DRNkd2a.png"))
    return info

# embed for port fix


def port():
    sol = discord.Embed(title="Port in Use Fix",
                        description="Possible Solutions for the port already in use error",color=warmup.rmd(),timestamp=datetime.now())
    sol.add_field(name="Solution 1",
                  value="Check if you have any Torrent/VM software like utorrent or VM Ware that might be interfering", inline=True)
    sol.add_field(name="Solution 2", value="Open a Command promt (Windows Key, then search cmd) as admin (right click>open as admin), then type the following command: *netstat -nabo* this command will display what ports are being used by what apps, look for port 443 and close wathever app is using it from task mananger", inline=True)
    return sol


# embed for jet editor


def editor(context):
    editor=discord.Embed(title="Profile Editor",description="Edit your ingame money, stats, complete quests and much more",color=warmup.rmd(),timestamp=datetime.now())
    return editor

# embed for bonk


def bonk(ctx, member):
    with open('images/bonk.json') as file:
        data = json.load(file)
        chosen = random.choice(data)

    bonk = discord.Embed(title="YOU HAVE BEEN BONKED", color=warmup.rmd(), timestamp=datetime.now(
    ), description=f"{member.mention} you have been bonked by{ctx.author.mention}")
    bonk.set_image(url=str(chosen))
    return bonk
# embed for key already added


def key():
    s1=discord.Embed(title="Step 1",description="Locate your Character.json (Server folder/user/profiles/AID/here)",color=warmup.rmd(),timestamp=datetime.now())
    s2=discord.Embed(title="Step 2",description="Head over to <#829464850895077406> or <#740002608424550522> and do !!clean with the profile attached",color=warmup.rmd(),timestamp=datetime.now())
    s3=discord.Embed(title="Step 3",description="Go back to where you grabbed the character.json and replace it with the output of the bot")
    s4 = discord.Embed(
        title="Step 4", description="Download [THIS FILE](https://mega.nz/file/7EtxwAJK#DdsT5snvRAydwUXVw-364NUpUJBEiWspAKnlGdyoiwI)",color=warmup.rmd(),timestamp=datetime.now())
    s5=discord.Embed(title="Step 5",description="Go to your server folder and extract the file you just downloaded into the SRC folder, when asked select replace files",color=warmup.rmd(),timestamp=datetime.now())
    s6=discord.Embed(title="Step 6",description="Go to the server folder>user and fully delete the cache folder",color=warmup.rmd(),timestamp=datetime.now())
    sol={"1":s1,"2":s2,"3":s3,"4":s4,"5":s5,"6":s6}
    return sol

# embed for hug

def hug(ctx, member):
    with open('images/hug.json') as file:
        data = json.load(file)
        chosen = random.choice(data)

    hug = discord.Embed(title="You have been hugged", timestamp=datetime.now(
    ), description=f"{member.mention} you have been hugged by{ctx.author.mention}")
    hug.set_image(url=str(chosen))
    return hug

