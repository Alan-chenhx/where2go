from math import sin, cos, sqrt, atan2, radians
from tqdm import tqdm
import json

def calc_dist(p1, p2):
    lat1 = radians(p1[0])
    lon1 = radians(p1[1]) 
    lat2 = radians(p2[0])
    lon2 = radians(p2[1]) 
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    R = 6373.0
    return R * c

with open('geo.json') as f:
    json_dat = json.load(f)

distance_dict = {}

for city in json_dat:
    distance_dict[city] = {}
    places = json_dat[city]
    for place in tqdm(places):
        distance_dict[city][place] = {}
        for otherplace in places:
            if place == otherplace:
                continue
            else:
                if 'lat' not in json_dat[city][place].keys() or 'lat' not in json_dat[city][otherplace].keys():
                    continue
                p1 = (json_dat[city][place]['lat'], json_dat[city][place]['lng'])
                p2 = (json_dat[city][otherplace]['lat'], json_dat[city][otherplace]['lng'])
                distance_dict[city][place][otherplace] = calc_dist(p1, p2)

distance_json = json.dumps(distance_dict)
print(distance_json)