import sys
import create_graph
from random import randint
import heapq
import math
import numpy as np
import math
def generate(city,preference,day_s,pace,maps,data):
    if(pace=='Slow-easy'):
        para=300
    elif(pace=='Medium'):
        para=450
    else:
        para=600

    time=day_s*para
    paths,distance = create_graph.cal(city,preference,time,maps,data)
    # print(distance)
    n=len(paths)
    # print(paths)
    graph = np.zeros((n,n)) 
    # print(distance)
    
    for i in range(0,n):
        for j in range(i+1,n):
            try:
                graph[i][j] = math.ceil(distance[paths[i][0]][paths[j][0]]*1.6)
                graph[j][i] = graph[i][j]
                
               
            except:
                graph[i][j]=60
    # print(graph)    
    p=[]
    p.append(randint(0,n-1))
    while(len(p)!=n):
        cur=p[-1]
        mini=[9999,9999]
        for i in range(n):
            if(i not in p):
                # print(i,cur)
                if(graph[i][cur]<mini[1]):
                    mini[0]=i
                    mini[1]=graph[i][cur]
        p.append(mini[0])     
    days=[]
    daytime=0
    day=[]
    tmp=[]
 
    while(len(p)!=0):
        
        tmp.append(p.pop(0))
        if(len(tmp)!=1):
            
            daytime+=graph[ tmp[-1] ][ tmp[-2] ]
            if(graph[ tmp[-1] ][ tmp[-2] ]==0.0):
                # print(tmp[-1],tmp[-2])
                pass
            day.append(graph[ tmp[-1] ][ tmp[-2] ])
        day.append( paths[tmp[-1]] )

        daytime+=int(paths[tmp[-1]][1])
        store=[]
        while(daytime> para and len(p)!=0):
            
            daytime-=int(paths[tmp[-1]][1])
            day.pop(-1)
            # store.append(day.pop(-1))
            daytime-=graph[ tmp[-1] ][ tmp[-2] ]
            store.append(tmp.pop(-1))
            tmp.append(p.pop(0))            
            daytime+=graph[ tmp[-1] ][ tmp[-2] ]
            day.append( paths[tmp[-1]] )
            # print(paths[tmp[-1]])
            daytime+=int(paths[tmp[-1]][1])
        
        for i in store[::-1]:
            p.append(i)

        if(daytime>=0.8*para):
            days.append((day,daytime))
            daytime=0
            day=[]
            tmp=[]
    result=days[:day_s]
    return result
    # pass