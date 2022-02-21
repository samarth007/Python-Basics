def test(t,*args,**kwargs):
     print(t)
     print(args)   #type of *args is tuple
     print(kwargs) #type of **kwargs is dictonary
n=123
ar=["sas",'wq',12,'klk',78]
kw={1:'one',2:'two',4:'four'}
test(n,ar,kw)

print('--------------------------------------')

l=['ABC','DEF','GHI','JKL']

for i,j in enumerate(l):   #i picks the index and j picks the value associated with the index
     if i%2==0:
          print(j)
