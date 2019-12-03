import json
from py2neo import Graph

graph = Graph(host='localhost', auth=('neo4j', 'abduabdu'))

with open('distance.json') as f:
    json_dat = json.load(f)

for city in json_dat:
    for place in json_dat[city]:
        for otherplace in json_dat[city][place]:
            query = """
                MATCH (p1:Place), (p2:Place)
                WHERE p1.name = '%s', p2.name = '%s'
                CREATE (p1)-[:WEIGHT {weight: %s} ]->(p2)
            """ %(place, otherplace, json_dat[city][place][otherplace])
            graph.run(query)