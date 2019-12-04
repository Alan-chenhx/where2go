import numpy as np;
import json
import demjson
import pprint
from random import randint
with open('data.json') as json_file:
    data = json.load(json_file)
for i in data["Mountain View"]:
    if(i["name"]=="Monterey Bay National Marine Sanctuary"):
        print(i)