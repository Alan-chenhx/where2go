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
                WHERE p1.name = {place}, p2.name = {otherplace}
                CREATE (p1)-[:WEIGHT {{weight: {weight}}}]->(p2)
            """
            graph.run(query, place=place, weight=json_dat[city][place][otherplace], otherplace=otherplace)