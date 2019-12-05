import sys
import json
from py2neo import Graph
import math

graph = Graph(host='localhost', auth=('neo4j', 'abduabdu'))
city = sys.argv[1]
name = sys.argv[2]
planId = sys.argv[3]
query = """
    MATCH (i:Itinerary)-[:Next]->(j:Itinerary)
    WHERE j.name = "%s" AND j.plan_id = %s
    RETURN i.name
""" %(name, planId)
res = graph.run(query).data()
prev = ''
if res != []:
    prev = res[0]['i.name']
query = """
    MATCH (i:Itinerary)-[:Next]->(j:Itinerary)
    WHERE i.name = "%s" AND i.plan_id = %s
    RETURN j.name
""" %(name, planId)
res = graph.run(query).data()
nextname = ''
if res != []:
    nextname = res[0]['j.name']
query = """
    MATCH (i:Itinerary)
    WHERE i.name = "%s" AND i.plan_id = %s
    DETACH DELETE i
    RETURN i
""" %(name, planId)
print(query)
graph.run(query)
if prev != '' and nextname != '':
    with open('distance.json', 'r') as f:
        dat = json.load(f)
        dis = dat[city][prev][nextname]
        dis = math.ceil(dis * 1.6)
        query = """
            MATCH (i:Itinerary), (j:Itinerary)
            WHERE i.name = "%s" AND i.plan_id = %s AND j.name = "%s" AND j.plan_id = %s
            CREATE (i)-[:Next]->(j)
            SET i.timetonext = %s
            RETURN i, j
        """ %(prev, planId, nextname, planId, dis)
elif prev != '' and nextname == '':
    query = """
        MATCH (i:Itinerary)
        WHERE i.name = "%s" AND i.plan_id = %s
        SET i.timetonext = 0
        RETURN i
    """ %(prev, planId)
elif prev == '' and nextname != '':
    query = """
        MATCH (p), (i:Itinerary)
        WHERE ID(p) = %s AND i.name = "%s" AND i.plan_id = %s
        CREATE (p)-[:Next]->(i)
        RETURN p, i
    """ %(planId, nextname, planId)
else:
    query = """"""
graph.run(query)
