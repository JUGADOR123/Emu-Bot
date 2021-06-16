import os
import json
import random


def init():
    global guilds
    with open('guilds.json', 'r+') as file:
        guilds = json.load(file)
    global tenorapi
    tenorapi = os.getenv('tenor')
   
def rmd():
    r = random.randint(0, 0xFFFFFF)
    return r