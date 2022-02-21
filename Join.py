
tup=('east','north','south')
ex='-west'
s=ex.join(tup)
print(s)
print('---------------------------')

dit={"one":"1","four":"4","six":"6","seven":"7","nine":"9"}
wordString="seven four one"

#res=''.join(dit[i] for i in wordString.split())
#print(res)

for i in wordString.split():
    res="".join(dit[i])
    print(res,end='')