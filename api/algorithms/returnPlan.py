from py2neo import Graph
import sys 
import json

graph = Graph(host='localhost', auth=('neo4j', 'abduabdu'))
uniq_id = sys.argv[1]

query = """
    MATCH (i) WHERE ID(i) = %s
    WITH (i)
    MATCH (p:Place) WHERE ID(p) = i.ref_id
    RETURN p
""" %(uniq_id)
place_list = graph.run(query).data()
query = """
    MATCH (i) WHERE ID(i) = %s
    WITH (i)
    MATCH (i)-[:Next*]->(n)
    WITH n
    MATCH (p:Place) WHERE ID(p) = n.ref_id
    RETURN p
""" %(uniq_id)
place_list += graph.run(query).data()
#print(json.dumps(place_list))
out_list = []
for i in place_list:
    out_list.append(i['p'])

print(json.dumps(out_list))
