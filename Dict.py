
def SumOfDict(d):
    sum=0
    for i in d:
      s=d[i]
      sum=sum+s
    print(sum)
    print(len(d))

SumOfDict({'2':200,'1':100,'3':320})

print('------------------------------------------')

def MaxKeyValue(t):
 print("Original value : ",t)
 key='age'
 res_max=0
 res=None
 for i in t:
     if t[i][key]>res_max:
         res_max=t[i][key]
         res=i

 print(res)

test_dict={'gfg':{'test':3,'age':20},
           'is':{'fgh':4,'age':27},
           'python':{'loi':4,'age':26}}
MaxKeyValue(test_dict)


print('--------------------------------------------')

#Print the average of the Values
def extract(l):
    print("Original values : ",l)
    sum=0
    for i in l.values():
        sum=sum+i
    avg=sum//len(l)
    print("Average of the values : ",avg)
extract({'gfg':4,'is':5,'best':7})




