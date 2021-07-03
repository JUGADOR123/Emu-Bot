import json
import src.warmup as warmup
from discord.ext import tasks, commands
import aiohttp

limits = 50


class background(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.cachegifs.start()

    @tasks.loop(hours=1)
    async def cachegifs(self):
        print("Caching Gifs")
        huggifs = []
        bonkgifs = []
        async with aiohttp.ClientSession() as session:
            async with session.get(
                "https://g.tenor.com/v1/search?q=hug&key=%s&limit=%s"
                % (warmup.tenorapi, limits)
            ) as response:
                data = json.loads(await response.text())["results"]
                for item in data:
                    huggifs.append(item["media"][0]["gif"]["url"])
                    with open("images/hug.json", "r+") as file:
                        file.seek(0)
                        json.dump(huggifs, file)
                        file.truncate()
            async with session.get(
                "https://g.tenor.com/v1/search?q=bonk&key=%s&limit=%s"
                % (warmup.tenorapi, limits)
            ) as response:
                data = json.loads(await response.text())["results"]
                for item in data:
                    bonkgifs.append(item["media"][0]["gif"]["url"])
                    with open("images/bonk.json", "r+") as file:
                        file.seek(0)
                        json.dump(bonkgifs, file)
                        file.truncate()
        await session.close()
        print("Gifs Cached")


def setup(bot):
    bot.add_cog(background(bot))
