import numpy as np
from itertools import accumulate, islice
from functools import reduce

s=np.random.randint(1,100,size=(3,3))
sss=[]
ss=[sss.extend(i) for i in s]
# print(sss)

a=np.arange(10)
# print(any(a))
# print(list(zip(a,a)))



def max_gen(l):
    current_max=0
    for i in l:
        current_max=max(i,current_max)
        yield current_max

al=[2,3,4,2,10,7,9,5,8,10]
res=list(max_gen(al))
# print(res)

acc=accumulate(al,max)
# print(list(acc))

arr1=[1,4,5,2,7]
odd_number=filter(lambda n: n%2==1,arr1)
squared_odd_number=map(lambda n: n*n, odd_number)
total=reduce(lambda x,y:x+y,squared_odd_number)
print(total)


arr2=np.random.randint(1,100,size=(100,))

for idx, elem in islice(enumerate(arr2),0,21,4):
    print(f"{idx},{elem}",end=' ')

print()
for idx, elem in enumerate(arr2[:21:4]):
    print(f"{idx},{elem}",end=' ')

#------------------------------------------------------------------------------------------------

arr3=np.random.randint(1,100,size=(100,))
arr3=arr3.tolist()
print(arr3)
for i in arr3:
    if i%2==0:
        arr3.remove(i)
print(arr3)        