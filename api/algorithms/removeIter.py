import sys
import json
from py2neo import Graph
import math

graph = Graph(host='localhost', auth=('neo4j', 'abduabdu'))

name = sys.argv[1]
planId = sys.argv[2]
query = """
    MATCH (k:Itinerary)-[:Next]->(i:Itinerary), (i)-[:Next]->(j:Itinerary)
    WHERE i.name = "%s" AND i.plan_id = %s
    RETURN j.name, k
""" %(name, planId)
print(graph.run(query).data())
