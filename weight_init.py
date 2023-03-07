import numpy as np

param={}

def wt_bs(ls):

    l=len(ls)

    for i in range(1,l):
        param['W'+str(i)]=np.ones((ls[i-1],ls[i]))*0.1
        param['B'+str(i)]=np.zeros((ls[i],1))
l=[3,2,3,1]
wt_bs(l)
# print(param)

