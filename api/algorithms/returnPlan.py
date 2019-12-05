from py2neo import Graph
import sys 
import json

graph = Graph(host='localhost', auth=('neo4j', 'abduabdu'))
uniq_id = sys.argv[1]

query = """
    MATCH (p:Plan)-[:Next*]->(i)
    WHERE ID(p) = %s
    RETURN i
""" %(uniq_id)
res = graph.run(query).data()

days = set()

curr = 0
for entry in res:
    uu = entry['i']['uu']
    days.add(uu)
days = list(days)
i = 0
place = []
places = []
for entry in res:
    if entry['i']['uu'] == days[i]:
        place.append(entry['i']['name'])
    else:
        places.append(place)
        i += 1
        place = []
        place.append(entry['i']['name'])
places.append(place)

frontfinal = []
for day in places:
    frontday = []
    for p in day:
        query = """
            MATCH (p:Place)
            WHERE p.name = "%s"
            RETURN DISTINCT p
        """ %(p)
        frontday.append(graph.run(query).data()[0]['p'])
    frontfinal.append(frontday)
print(frontfinal)
fname = 'test_' + str(uniq_id) + '.json'
with open(fname, 'w+') as f:
    f.write(json.dumps(frontfinal))
