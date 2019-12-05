import sys
import json
from py2neo import Graph
import math

graph = Graph(host='localhost', auth=('neo4j', 'abduabdu'))

city = sys.argv[1]
oldname = sys.argv[2]
name = sys.argv[3].replace('\\', '')
duration = sys.argv[4]
planId = sys.argv[5]

query = """
    MATCH (p:Place)-[:Near]->(c:City)
    WHERE p.name = "%s" AND c.name = "%s"
    RETURN ID(p)
""" %(name, city)
ref_id = graph.run(query).data()[0]['ID(p)']
query = """
    MATCH (i:Itinerary)
    WHERE i.name = "%s" AND i.city = "%s" AND i.plan_id = %s
    RETURN i.timetonext
""" %(oldname, city, planId)
timetonext = graph.run(query).data()[0]['i.timetonext']
nextiter = ''
newtime = 0
if timetonext != 0:
    query = """
        MATCH (i:Itinerary)-[:Next]->(j:Itinerary)
        WHERE i.name = "%s" AND i.city = "%s" AND i.plan_id = %s
        RETURN j.name
    """ %(oldname, city, planId)
    nextiter = graph.run(query).data()[0]['j.name']
    with open('distance.json', 'r') as f:
        dat = json.load(f)
    newtime = math.ceil(float(dat[city][name][nextiter]) * 1.6)

query = """
    MATCH (i:Itinerary)
    WHERE i.name = "%s" AND i.city = "%s" AND i.plan_id = %s
    SET i.name = "%s", i.duration = %s, i.ref_id = %s, i.timetonext = %s
    RETURN i
""" %(oldname, city, planId, name, duration, ref_id, newtime)
graph.run(query)


query = """
    MATCH (i:Itinerary)-[:Next]->(j:Itinerary)
    WHERE j.name = "%s" AND j.plan_id = %s
    RETURN i.name
""" %(name, planId)
prev = graph.run(query).data()
if prev != []:
    prev = prev[0]['i.name']
    newtime = math.ceil(float(dat[city][prev][name]))
    query = """
        MATCH (i:Itinerary)
        WHERE i.name = "%s" AND i.plan_id = %s
        SET i.timetonext = %s
        RETURN i
    """ %(prev, planId, newtime)
    graph.run(query)
