import os
import json
import random
import requests


def init():
    global guilds
    with open('guilds.json', 'r+') as file:
        guilds = json.load(file)
    global tenorapi
    tenorapi = os.getenv('tenor')
   
def rmd():
    r = random.randint(0, 0xFFFFFF)
    return r

def cachegifs():
    limits = 50
    hellolimit = 10
    # caching 50 hugs
    r = requests.get(
        "https://g.tenor.com/v1/search?q=hug&key=%s&limit=%s" % (tenorapi, limits))
    if r.status_code == 200:
        huggifs = []
        data = json.loads(r.content)['results']
        for item in data:
            huggifs.append(item['media'][0]['gif']['url'])
        with open('images/hug.json', 'r+') as file:
            file.seek(0)
            json.dump(huggifs, file)
            file.truncate()
   # caching 50 bonks
    r = requests.get(
        "https://g.tenor.com/v1/search?q=bonk&key=%s&limit=%s" % (tenorapi, limits))
    if r.status_code == 200:
        bonkgis = []
        data = json.loads(r.content)['results']
        for item in data:
            bonkgis.append(item['media'][0]['gif']['url'])
        with open('images/bonk.json', 'r+') as file:
            file.seek(0)
            json.dump(bonkgis, file)
            file.truncate()
   # caching 10 hi's
    r = requests.get(
        "https://g.tenor.com/v1/search?q=hi&key=%s&limit=%s" % (tenorapi, hellolimit))
    if r.status_code == 200:
        hellogifs = []
        data = json.loads(r.content)['results']
        for item in data:
            hellogifs.append(item['media'][0]['gif']['url'])
        with open('images/hello.json', 'r+') as file:
            file.seek(0)
            json.dump(hellogifs, file)
            file.truncate()
