import json
from py2neo import Graph

graph = Graph(host='localhost', auth=('neo4j', 'abduabdu'))

with open('algorithms/data.json') as f:
    json_dat = json.load(f)

for city in json_dat:
    query = """
        CREATE (c:City)
        SET c.name = {city}
        RETURN c
    """
    graph.run(query, city=city)
    for place in json_dat[city]:
        if 'address' not in place.keys():
            query = """
            MATCH (c:City)
            WHERE c.name = {city}
            CREATE (p:Place), (c)<-[:Near]-(p)
            SET p.name = {name}, p.duration = {duration}, p.url = {url}, p.rating = {rating}, p.tag = {tag}, p.address = {address}
            RETURN p
            """
            graph.run(query, city=city, name=place['name'], duration=place['duration'], url=place['url'], rating=place['rating'], tag=place['tag'], address='')
            print(place['name'])
            continue
        query = """
        MATCH (c:City)
        WHERE c.name = {city}
        CREATE (p:Place), (c)<-[:Near]-(p)
        SET p.name = {name}, p.duration = {duration}, p.url = {url}, p.rating = {rating}, p.tag = {tag}, p.address = {address}
        RETURN p
        """
        graph.run(query, city=city, name=place['name'], duration=place['duration'], url=place['url'], rating=place['rating'], tag=place['tag'], address=place['address'])
        if 'photo' in place.keys():
            query = """
            MATCH (p:Place)
            WHERE p.name = {name}
            SET p.photo = {photo}
            RETURN p
            """
        graph.run(query, name = place['name'], photo = place['photo'])
        if 'description' in place.keys():
            query = """
            MATCH (p:Place)
            WHERE p.name = {name}
            SET p.description = {description}
            RETURN p
            """
        graph.run(query, name = place['name'], description = place['description'])
