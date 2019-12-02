import numpy as np;
import json
import pprint
from random import randint

class path:
    def __init__(self):
        self.pplist=[]
        self.uplist=[]
        self.Dprefer=[]
        self.Duprefer=[]
        self.CNRp=[]
        self.CNRup=[]
        self.Dtotal=[]
        self.data=[]
        self.Tprefer=[]
        self.Tuprefer=[]
    def read(self,city):
        with open('data copy.json') as json_file:
            tmp = json.load(json_file)
            self.data = tmp[city]
    def create(self,city,prefer):
        self.read(city) 
        for i in self.data:
            for j in i['tag']:
                if((j in prefer) or j=='Must See'):
                    self.pplist.append(i)
                    break
            else:
                self.uplist.append(i)

        for i in self.pplist:
            self.Tprefer.append(int(i['duration']))
            self.CNRp.append(i['rating']*10)
        for i in self.uplist:
            self.Tuprefer.append(int(i['duration']))
            self.CNRup.append(i['rating']*10)
        self.Dprefer=np.zeros((len(self.pplist),len(self.pplist)))
        self.Duprefer=np.zeros((len(self.uplist),len(self.uplist)))
        for i in range(0,len(self.pplist)):
            for j in range(i+1,len(self.pplist)):
                self.Dprefer[i][j]=randint(20, 100)
                self.Dprefer[j][i]=self.Dprefer[i][j]
        # print(Dprefer)
        for i in range(1,len(self.uplist)):
            for j in range(i+1,len(self.uplist)):
                self.Duprefer[i][j]=randint(20, 1000)
                self.Duprefer[j][i]=self.Duprefer[i][j]
        # return pplist,uplist,Dprefer,Duprefer,CNRp,CNRup
        # print(self.Dprefer)
    def RM(self,i,j,k,preferred=True):
        alpha1=0.3
        alpha2=0.7
        # alpha3=0.4
        sums=0
        if(preferred):
            # ccr(i)*sop(j,k)
            sums+=alpha1*(1/self.CNRp[i])*(1/len(self.pplist)*1)
            sums+=alpha2*(1/self.CNRp[i]+1/(self.CNRp[i]**2))*self.Tprefer[i]/sum(self.Dprefer[i])

        else:
            sums+=alpha1*(1/self.CNRup[i])*(1/len(self.uplist)*1)
            sums+=alpha2*(1/self.CNRup[i]+(1/(self.CNRup[i]**2)))*self.Tuprefer[i]/sum(self.Duprefer[i])
        return sums
def cal_len(city,preference):
    curPath=path()
    curPath.create(city,preference)
    n = len(curPath.pplist)
    return n

def cal(city,preference,times):
    curPath=path()
    curPath.create(city,preference)
    n = len(curPath.pplist)
    used=[]
    used.append(randint(0,n-1))
    paths=[]
    # paths.append('Day:')
    paths.append((curPath.pplist[used[0]]['name'],curPath.pplist[used[0]]['duration'],curPath.pplist[used[0]]['rating']))
    cur_time=int(curPath.pplist[used[0]]['duration'])
    # print(curPath.pplist[used[0]]['duration'])
    while(len(used)<n and cur_time<times):
        maxi=[0,0]
        for index,i in enumerate(curPath.pplist):
            # print(used)
            if(index not in used):
                RValue=curPath.RM(index,used[-1],0,True)
                if(RValue>maxi[0]):
                    maxi[0]=RValue
                    maxi[1]=index
        used.append(maxi[1])
        cur_time+=int(curPath.pplist[maxi[1]]['duration'])
        paths.append((curPath.pplist[maxi[1]]['name'],curPath.pplist[maxi[1]]['duration'],curPath.pplist[maxi[1]]['rating']))
    # print(paths)
    n = len(curPath.uplist)
    used=[]
    while(len(used)<n and cur_time<times):
        maxi=[0,0]
        for index,i in enumerate(curPath.uplist):
            # print(used)
            if(index not in used):
                RValue=curPath.RM(index,0,0,False)
                if(RValue>maxi[0]):
                    maxi[0]=RValue
                    maxi[1]=index
        used.append(maxi[1])
        cur_time+=int(curPath.uplist[maxi[1]]['duration'])
        paths.append((curPath.uplist[maxi[1]]['name'],curPath.uplist[maxi[1]]['duration'],curPath.uplist[maxi[1]]['rating']))
    # print(paths)
    return paths
    