
def MaxKeyValue(t):
    print("Original Values :",t)
    key='age'
    max=0
    res=None
    for i in t:
        if(t[i][key]>max):
            max=t[i][key]
            res=i

    print(res)

t={'jk':{'age':26,'branch':'civil'},'kgf':{'branch':'CS','age':28},'k3':{'branch':'3K','age':25}}
MaxKeyValue(t)

print('---------------------------------------------------------------')

def AvgDict(a):
    print('Original Dict :',a)
    avg=0
    for i in a.values():
       avg=avg+i
    print(avg/len(a))

a={'s':4,'r':2,'w':1}
AvgDict(a)

print('-----------------------------------------')

def fib(n):
    n1,n2=0,1
    n3=0
    if n<=0:
        print("enter +ve number")
        return 0
    while n3<n:
        print(n1, end=' ')
        n4=n1+n2
        n1=n2
        n2=n4
        n3=n3+1
    print()
fib(4)

print('--------------------------------------')

#['This', 'is', 'python', 'programming']

l=[1,2,3,4,5,6,7,8,9]
print(l[::-1])

str='This is python programming'
l=(str.split(' '))
print(l)


def rec(n):
    c=1
    d=1
    if n==1:
        return n
    while c<n:
       d=d*c
       c=c