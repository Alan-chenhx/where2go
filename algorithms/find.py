import sys
import create_graph
from random import randint
import heapq
import numpy as np

paths = create_graph.cal('Santa Monica','',1890)
n=len(paths)
print(paths)
graph = np.zeros((n,n)) 
for i in range(0,n):
    for j in range(i+1,n):
        graph[i][j]=randint(20, 100)
        graph[j][i]=graph[i][j]
# print(graph)
p=[]
p.append(randint(0,n-1))
while(len(p)!=n):
    cur=p[-1]
    mini=[999,999]
    for i in range(n):
       
        if(i not in p):
            # print(i,cur,graph[i][cur])
            if(graph[i][cur]<mini[1]):
                # print(i,cur)
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
        if(daytime>300):
            days.append((day,daytime))
            daytime=0
            day=[paths[tmp[-1]]]
            tmp=[tmp[-1]]
        else:
            day.append(graph[ tmp[-1] ][ tmp[-2] ])
    day.append( paths[tmp[-1]] )
    # print(paths[tmp[-1]])
    daytime+=int(paths[tmp[-1]][1])
    if(daytime>300):
        days.append((day,daytime))
        daytime=0
        day=[]
        tmp=[]
result=days[:5]
for i in result:
    print(i)
    # pass