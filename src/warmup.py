import os
import random
def init():
    global tenorapi
    tenorapi = os.getenv('tenor')
def rmd():
    r = random.randint(0, 0xFFFFFF)
    return r
