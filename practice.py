lst=[1,2,3,4,2]  #duplicate allowed and insertion order maintained
for i in lst:
    print(i,end='')
print()
st={1,3,4,2,2,1}  #duplicate not allowed and insertion order not maintained
for i in st:
    print(i,end='')

print()

data=[]

for i in range(10):
    data.append([i,'hello'])
x=[]
y=[]

for f,l in data:
    x.append(f)
    y.append(l)

print(x)    
print(y)