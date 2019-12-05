from py2neo import Graph
import sys 
import json

graph = Graph(host='localhost', auth=('neo4j', 'abduabdu'))
uniq_id = sys.argv[1]

query = """
    MATCH (d:Day)
    WHERE d.plan_id = %s
    RETURN d
""" %(uniq_id)
res = graph.run(query).data()

days = []

for entry in res:
    plan_id = entry['d']['plan_id']
    uu = entry['d']['uu']
    days.append((plan_id, uu))

for day in days:
    query = """
        MATCH (i)-[:Next*]->(j)
        WHERE j.plan_id = %s
        RETURN (j)
    """ %(day[0])
    print(graph.run(query).data())

print(days)
