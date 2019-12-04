import googlemaps
gmaps = googlemaps.Client(key='AIzaSyD8QJce47OrLwngF4qHtlPfvO9LID53lSQ')

import json
with open('data/data.json') as f:
    json_dat = json.load(f)

def get_cord(address):
    geocode_result = gmaps.geocode(address)
    latitude = geocode_result[0]['geometry']['location']['lat']
    longitude = geocode_result[0]['geometry']['location']['lng']
    return latitude, longitude

geoinfo = {}
# city = 'Los Angeles'
for city in json_dat:
    places = json_dat[city]
    geoinfo[city] = {}
    for place in places:
        attraction = place['name']
        geoinfo[city][attraction] = {}
        address = attraction + ',' + city
        try:
            lat, lng = get_cord(address)
        except:
            continue
        geoinfo[city][attraction]['lat'] = lat
        geoinfo[city][attraction]['lng'] = lng

print(geoinfo)