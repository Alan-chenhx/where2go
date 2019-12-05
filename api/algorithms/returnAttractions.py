from py2neo import Graph
import sys 
import json

graph = Graph(host='localhost', auth=('neo4j', 'abduabdu'))
city = sys.argv[1].replace('-',' ')

query = """
    MATCH (p:Place)-[:Near]->(c:City)
    WHERE c.name="%s"
    RETURN p
""" %(city)
res = graph.run(query).data()
attractions=[]
for attr in res:
    # print(attr['p']['name'])
    attractions.append(attr['p']['name'])
print(attractions)

