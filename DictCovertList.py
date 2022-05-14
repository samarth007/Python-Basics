#dictonary to map conversion
def DicConverLis(t):
 print("Original Values : ",t)
 r=[]
 for i,j in t.items():
     r.append([i]+j)
 print(r)


t={'gfg':[1,2,3],'is':[3,4,1],'best':[2,3]}
DicConverLis(t)
print('---------------------------------------')

#converting list to list of dictonary
def Mapping(m):
 print('Original values : ',m)
 map=['alpha','numeric']
 r=[]
 n=len(m)
 for i in range(0,n,2):
  r.append({map[0]:m[i],map[1]:m[i+1]})
 print(r)

m=['test',4,'java',2,'python',7,'falsk',6]
Mapping(m)

print('------------------------------------------------')

#Coverting list of dictonary to list of list
def ConvertList(l):
 print("Original Values : ",l)
 r=[]
 for i in l:
  print(i)
  r.append(list(i.keys()))
  r.append(list(i.values()))
 print(r)

l=[{'test':1,'java':2},{'python':7,'flask':6}]
ConvertList(l)