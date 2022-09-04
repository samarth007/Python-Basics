import numpy as np


# n= int(input("Enter the number of rows: "))
# pattern=bool(int(input("Enter the number 1 or 0")))

# if pattern==True:
#  for i in range(1,n+1):
#      print(i*'*')
# else:
#  row=n+1
#  for i in range(1,n+1):
#     print((row-i)*'*')


# a,_,b=[1,2,3]
# print(a,b)
# print(_+2)

l=[2,1,4,6,3,1,2,1,4]
a,s=np.unique(l,return_counts=True,axis=0)
print(s)

np.random.randint()