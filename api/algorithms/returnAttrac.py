from py2neo import Graph
import sys 
import json

graph = Graph(host='localhost', auth=('neo4j', 'abduabdu'))
city = sys.argv[1].replace('-',' ')
attrac = sys.argv[2].replace('-',' ')
query = """
    MATCH (p:Place)-[:Near]->(c:City)
    WHERE c.name="%s" and p.name="%s"
    RETURN p
""" %(city,attrac)
# query = """
#     MATCH (p:Place)-[:Near]->(c:City)
#     WHERE c.name="Los Angeles" and p.name="Greenbar Distillery"
#     RETURN p
# """
res = graph.run(query).data()

# attractions=[]
# for attr in res:
#     # print(attr['p']['name'])
#     attractions.append(attr['p']['name'])
try:
    ans=json.dumps(res[0]['p'])
except:
    ans={}
print(ans,end='')

