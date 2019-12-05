from multi_generate import *
from py2neo import Graph
import json
def getcover(city,attrac):
    graph = Graph(host='localhost', auth=('neo4j', 'abduabdu'))
    # city = sys.argv[1].replace('-',' ')
    # attrac = sys.argv[2].replace('-',' ')
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
        ans=res[0]['p']['photo']
    except:
        ans={}
    return ans

graph = Graph(host='localhost', auth=('neo4j', 'abduabdu'))

cities = sys.argv[1].replace('-',' ').split(',')
preference = sys.argv[2].replace('-', ' ').split(',')
days = int(sys.argv[3])
pace = sys.argv[4]
itinerary = algorithm1(cities, preference, days, pace)

cover_city=''
for keyp in itinerary:
    cover_city=keyp
# cover_city = itinerary[key]
# print()
# print(itinerary[cover_city])
try:
    cover_attra = itinerary[cover_city][0][0]['name']
    # print(cover_attra)
except:
    pass
# print(cover_city)
it_list = []

d = 0

query = """
    CREATE (p:Plan)
    RETURN ID(p)
"""
plan_id = graph.run(query).data()[0]['ID(p)']

for city in itinerary:
    for day in itinerary[city]:
        oneday = []
        query = """
            CREATE (d:Day {uu: %s, plan_id: %s})
            RETURN d
        """ %(d, plan_id)
        graph.run(query)
        for place in day:
            step = {}
            duration = place['duration']
            name = place['name']
            timetonext = place['timetonext']
            query = """
                MATCH (p:Place)-[:Near]->(c:City)
                WHERE p.name = "%s" AND c.name = "%s"
                WITH p
                CREATE (i:Itinerary {city: "%s", duration: %s, name: "%s", timetonext: %s, ref_id: ID(p), plan_id: %s, uu: %s})
                RETURN i
            """ %(name, city, city, duration, name, timetonext, plan_id, d) 
            graph.run(query)
            query = """
                MATCH (i:Itinerary), (d:Day)
                WHERE i.name = "%s" AND d.uu = %s AND d.plan_id = %s AND i.plan_id = %s
                CREATE (i)-[:In]->(d)
            """ %(name, d, plan_id, plan_id)
            graph.run(query)
            step['city'] = city
            step['duration'] = duration
            step['name'] = name
            step['timetonext'] = timetonext
            oneday.append(step)
        d += 1
        it_list.append(oneday)
its = []
for day in it_list:
    for entry in day:
        its.append(entry)
for i in range(len(its) - 1):
    head = its[i]
    nxt = its[i + 1]
    query = """
        MATCH (i:Itinerary), (j:Itinerary)
        WHERE i.name = "%s" AND j.name = "%s" AND i.plan_id = %s AND j.plan_id = %s
        CREATE (i)-[:Next]->(j)
        RETURN i, j
    """ %(head['name'], nxt['name'], plan_id, plan_id)
    graph.run(query)
head = its[0]
query = """
    MATCH (i:Itinerary), (p:Plan)
    WHERE i.name = "%s" AND i.plan_id = %s AND ID(p) = %s
    CREATE (p)-[:Next]->(i)
    RETURN p, i
""" %(head['name'], plan_id, plan_id)
graph.run(query)
try:
    cover=getcover(cover_city,cover_attra)
    cover=cover.replace("background-image: url('",'')
    cover=cover.replace("')'",'')
    # print(cover)
    print( json.dumps([plan_id,cover]),end='' )
except:
    print(json.dumps([plan_id,"https:\/\/s.inspirockcdn.com\/ds10\/photos\/United States\/1\/town-and-country-village-1255533322.jpg"]),end='')