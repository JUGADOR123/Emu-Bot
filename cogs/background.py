import json
import src.warmup as warmup
import requests
from discord.ext import tasks, commands
import aiohttp


limits = 50
hellolimit=10


class background(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.cachegifs.start()

    @tasks.loop(hours=12)
    async def cachegifs(self):
        huggifs = []
        bonkgifs = []
        hellogifs = []
        async with aiohttp.ClientSession() as session:
            async with session.get("https://g.tenor.com/v1/search?q=hug&key=%s&limit=%s" % (warmup.tenorapi, limits)) as response:
                data = json.loads(await response.text())['results']
                for item in data:
                    huggifs.append(item['media'][0]['gif']['url'])
                    with open('images/hug.json', 'r+') as file:
                        file.seek(0)
                        json.dump(huggifs, file)
                        file.truncate()
            async with session.get("https://g.tenor.com/v1/search?q=bonk&key=%s&limit=%s" % (warmup.tenorapi, limits)) as response:
                data = json.loads(await response.text())['results']
                for item in data:
                    bonkgifs.append(item['media'][0]['gif']['url'])
                    with open('images/bonk.json', 'r+') as file:
                        file.seek(0)
                        json.dump(bonkgifs, file)
                        file.truncate()
            async with session.get("https://g.tenor.com/v1/search?q=hi&key=%s&limit=%s" % (warmup.tenorapi, hellolimit)) as response:
                data = json.loads(await response.text())['results']
                for item in data:
                    hellogifs.append(item['media'][0]['gif']['url'])
                    with open('images/hello.json', 'r+') as file:
                        file.seek(0)
                        json.dump(hellogifs, file)
                        file.truncate()
        await session.close()            
    print("Gifs Cached")


def setup(bot):
    bot.add_cog(background(bot))
