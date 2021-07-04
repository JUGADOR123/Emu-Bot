import json
import os
from time import sleep

from src import bot, warmup

art = """\
███████ ███    ███ ██    ██     ██████   ██████  ████████     
██      ████  ████ ██    ██     ██   ██ ██    ██    ██        
█████   ██ ████ ██ ██    ██     ██████  ██    ██    ██        
██      ██  ██  ██ ██    ██     ██   ██ ██    ██    ██        
███████ ██      ██  ██████      ██████   ██████     ██        """


def startup() -> bool:
    try:
        if not os.path.exists("images"):
            print("Creating Directories...")
            os.makedirs("images")
            empty = []
            data = json.dumps(empty)
            with open(os.path.join("images", "bonk.json"), "x") as temp:
                temp.write(data)
            with open(os.path.join("images", "hug.json"), "x") as temp:
                temp.write(data)
            print("Directories Created")
    except Exception as e:
        print(e)
        return False
    warmup.init()
    return True


def main():
    bot.start()


if __name__ == "__main__":
    print(art)
    sleep(5)
    print("Loading Startup")
    startup()
    print("Startup Loaded")
    print("Starting Discord Bot....")
    main()
