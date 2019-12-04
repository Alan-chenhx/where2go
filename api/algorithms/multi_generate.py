import create_graph
import find
import sys
import re
import pprint
import json
import demjson
import math
def algorithm1(cities,preference,days,pace='medium'):
    with open('distance.json') as json_file:
        distance = json.load(json_file)
    # cities = sys.argv[1].replace('-',' ').split(',')
    # preference = sys.argv[2]
    
    if(preference=='None'):
        preference=''
    # days = int(sys.argv[3])
    # pace = sys.argv[4]
    ans={}
    city_len=[]
    for city in cities:
        city_len.append(create_graph.cal_len(city,preference,distance))
    sums=sum(city_len)
    day=[]
    for i in city_len:
        day.append(days*i/sums)


    for index,city in enumerate(cities):
        ans.setdefault(city,[])
        # print(find.generate(city,preference,int(day[index])))
        ans[city]=find.generate(city,preference,int(math.floor(day[index]+0.5)),pace,distance)
    # print(ans)
    for i in ans:
        days=ans[i]
        for day_in,day in enumerate(days):
            day=list(day)
            day.pop(-1)
            for index,ele in enumerate(day[0]):
                # print(ele)
                if isinstance(ele,tuple):
                    tmp={}
                    tmp['name']=ele[0]
                    tmp['duration']=ele[1]
                    tmp['rating']=ele[2]
                    # print(tmp)
                    try:
                        tmp['timetonext']=day[0][index+1]
                    except:
                        tmp['timetonext']=0
                    # print(day[0][index])
                    day[0][index]=tmp.copy()
            for index,ele in enumerate(day[0]):
                # print(ele)
                if isinstance(ele,float):
                    day[0].pop(index)
                
            days[day_in]=day[0]

    # json_ans=demjson.encode(ans)
    # print(json)
    return ans




print(algorithm1(['Los Angeles','San Diego','Santa Monica'],['Water Park','Park'],10,"high"))