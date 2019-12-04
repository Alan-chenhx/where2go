import numpy as np;
import json
import pprint
from random import randint
with open('distance.json') as json_file:
    dis = json.load(json_file)
    dist = dis['Los Angeles']
print(dist['Studio Tour']['Guinness World Records Museum'])

