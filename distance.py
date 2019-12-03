from math import sin, cos, sqrt, atan2, radians

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

print(calc_dist(p1, p2))