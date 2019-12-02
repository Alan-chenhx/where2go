import json
import googlemaps
import numpy as np

gmaps = googlemaps.Client(key = 'AIzaSyDcDPRv_BJpXbEscdAN4lsTngNNcmJnTFc')

with open('data.json') as f:
    json_dat = json.load(f)

distance_mat = {}

for city in json_dat:
# city = 'Ontario'
    print('==============='+city+'===============')
    distance_mat[city] = {}
    for i in range(len(json_dat[city])):
        place = json_dat[city][i]['name']
        otherplaces = [json_dat[city][j]['name'] for j in range(len(json_dat[city])) if j != i]
        distance_mat[city][place] = {}
        origin = place + ', ' + city
        for j in range(len(otherplaces)):
            mat = gmaps.distance_matrix(origin, otherplaces[j])
            if 'distance' not in mat['rows'][0]['elements'][0]:
                continue
            distance_mat[city][place][otherplaces[j]] = float(mat['rows'][0]['elements'][0]['distance']['text'][:-3].replace(',', ''))
        print('==='+place+'===')
        print(distance_mat[city][place])
# for i in range(len(origins)):
#     for j in range(i+1, len(destinations)):
#         distance_mat[i, j] = float(gmaps.distance_matrix(origins, destinations)['rows'][0]['elements'][0]['distance']['text'][:-3].replace(',', ''))
# # distances = gmaps.distance_matrix(origins, destinations, mode='driving')
# print(distance_mat)