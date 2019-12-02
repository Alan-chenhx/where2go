import create_graph
import find
import sys
import re
import pprint
def main():
    
    cities = sys.argv[1].replace('-',' ').split(',')
    preference = sys.argv[2]
    if(preference=='None'):
        preference=''
    days = int(sys.argv[3])
    ans={}
    city_len=[]
    for city in cities:
        city_len.append(create_graph.cal_len(city,preference))
    sums=sum(city_len)
    day=[]
    for i in city_len:
        day.append(days*i/sums)


    for index,city in enumerate(cities):
        ans.setdefault(city,[])
        # print(find.generate(city,preference,int(day[index])))
        ans[city]=find.generate(city,preference,int(day[index]))
    # pprint.pprint(ans)
    return ans





if __name__ == "__main__":
    main()
