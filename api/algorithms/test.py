import numpy as np;
import json
import demjson
import pprint
from random import randint
with open('data.json') as json_file:
    data = json.load(json_file)
ans_tags={}
for city in data:
    for attracks in data[city]:
        # print(attracks)
        for tag in attracks['tag']:
            ans_tags.setdefault(tag,0)
            ans_tags[tag]+=1
json=demjson.encode(ans_tags)
fo = open("tags.json", "w")
fo.write(json)
fo.close()