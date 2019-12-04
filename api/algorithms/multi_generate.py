import create_graph
import find
import sys
import re
import pprint
import json
import demjson
import math
dic={
    "culture": [
        "Architectural Building", "Art Gallery", "Brewery", "Cemetery",
        "Character Experience", "Church", "Distillery", "Educational Site",
        "Farm", "Forest", "Ghost Town", "Government Building", "Historic Site",
        "Historic Museum", "Landmark", "Library", "Monument", "National Park",
        "Religious Site", "University / School"
    ],
    "outdoors": [
        "Auto Race Track", "Balloon Ride", "Beach", "Biking Trail", "Bridge",
        "Canyon", "Cave", "Cross-country Ski Area", "Dam", "Desert",
        "Disney Park / Activity", "Equestrian Trail", "Farm", "Forest",
        "Geologic Formation", "Ghost Town", "Golf Course", "Hiking Trail",
        "Historic Walking Area", "Island", "Lighthouse", "Marina", "Mountain",
        "National Park", "Outdoor Activity", "Playground", "Ski Area", "Valley"
    ],
    "relaxing": [
        "Aquarium", "Bowling Alley", "Casino", "Civic Center",
        "Cross-country Ski Area", "Dolphin / Whale Watching",
        "Entertainment Center", "Flea Market", "Fountain", "Fun & Games",
        "Garden", "Golf Course", "Island", "Marina", "National Park", "Park",
        "Pier / Boardwalk", "Playground"
    ],
    "romatic": [
        "Balloon Ride", "Beach", "Civic Center", "Dolphin / Whale Watching",
        "Entertainment Center", "Fountain", "Fun & Games", "Garden",
        "Ghost / Vampire Tour", "Lighthouse", "Marina", "Theme Park"
    ],
    "beaches": ["Beach"],
    "historic sites": [
        "Canyon", "Castle", "Cave", "Forest", "Geologic Formation",
        "Historic Site", "Historic Walking Area"
    ],
    "museums": [
        "Architectural Building", "Art Gallery", "Art Museum",
        "Children's Museum", "History Museum", "Military Museum",
        "Science Museum", "Shopping Mall", "Specialty Museum"
    ],
    "shopping": [
        "Antique Store", "Casino", "Department Store", "Factory Outlet",
        "Farmers Market", "Flea Market", "Gift & Specialty Shop", "Shopping"
    ],
    "wildlife": ["Wildlife Area", "Zoo"]
}


def algorithm1(cities, preference, days, pace='medium'):
    with open('distance.json') as json_file:
        distance = json.load(json_file)
    with open('data.json') as json_file:
        data = json.load(json_file)
    # cities = sys.argv[1].replace('-',' ').split(',')
    # preference = sys.argv[2]
    prefer=[]
    if (preference == 'None'):
        preference = ''
    else:
        for  pr in preference:
            for tag in dic[pr]:
                prefer.append(tag)
    preference=prefer
    # days = int(sys.argv[3])
    # pace = sys.argv[4]
    ans = {}
    city_len = []
    for city in cities:
        city_len.append(create_graph.cal_len(city, preference, distance, data))
    sums = sum(city_len)
    day = []
    for i in city_len[:-1]:
        day.append(int(days * i / sums+0.5))
    day.append(days-sum(day))
    

    for index, city in enumerate(cities):
        ans.setdefault(city, [])
        # print(find.generate(city,preference,int(day[index])))
        ans[city] = find.generate(city, preference,
                                  day[index], pace,
                                  distance, data)
    # print(ans)
    for i in ans:
        days = ans[i]
        for day_in, day in enumerate(days):
            day = list(day)
            day.pop(-1)
            for index, ele in enumerate(day[0]):
                # print(ele)
                if isinstance(ele, tuple):
                    tmp = {}
                    tmp['name'] = ele[0]
                    tmp['duration'] = ele[1]
                    tmp['rating'] = ele[2]
                    # print(tmp)
                    try:
                        tmp['timetonext'] = day[0][index + 1]
                    except:
                        tmp['timetonext'] = 0
                    # print(day[0][index])
                    day[0][index] = tmp.copy()
            for index, ele in enumerate(day[0]):
                # print(ele)
                if isinstance(ele, float):
                    day[0].pop(index)

            days[day_in] = day[0]

    # json_ans=demjson.encode(ans)
    # print(json)
    return ans


print(algorithm1(['Los Angeles',"Mountain View"],"None", 5, "medium"))
