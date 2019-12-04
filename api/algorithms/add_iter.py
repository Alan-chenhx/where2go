from multi_generate import *
from py2neo import Graph

graph = Graph(host='localhost', auth=('neo4j', 'abduabdu'))

cities = sys.argv[1].replace('-',' ').split(',')
preference = sys.argv[2]
days = int(sys.argv[3])
pace = sys.argv[4]
itinerary = algorithm1(cities, preference, days, pace)
print(itinerary)
it_list = []

for city in itinerary:
    d = 0
    for day in itinerary[city]:
        oneday = []
        query = """
            CREATE (d:Day {uu: %s})
            RETURN d
        """ %(d)
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
                CREATE (i:Itinerary {city: "%s", duration: %s, name: "%s", timetonext: %s, ref_id: ID(p)})
                RETURN i
            """ %(name, city, city, duration, name, timetonext) 
            graph.run(query)
            query = """
                MATCH (i:Itinerary), (d:Day)
                WHERE i.city = "%s" AND i.name = "%s" AND d.uu = %s
                CREATE (i)-[:In]->(d)
            """ %(city, name, d)
            graph.run(query)
            step['city'] = city
            step['duration'] = duration
            step['name'] = name
            step['timetonext'] = timetonext
            oneday.append(step)
        d += 1
        it_list.append(oneday)
print(it_list)
for day in it_list:
    for i in range(len(day) - 1):
        head = day[i]
        nxt = day[i + 1]
        query = """
            MATCH (i:Itinerary), (j:Itinerary)
            WHERE i.city = '%s' AND i.name = "%s" AND j.city = '%s' AND j.name = "%s"
            CREATE (i)-[:Next]->(j)
            RETURN i, j
        """ %(head['city'], head['name'], nxt['city'], nxt['name'])
        graph.run(query)
