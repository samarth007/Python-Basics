 
#program to print a list of tuple in that first element is number and second is the cube of first one

def cube(lis):
    ntl=[]
    for i in lis:
        tl=(i,pow(i,3))
        ntl.append(tl)
    return ntl

print(cube([2,4,6,8]))
print('--------------------------------------')
#Alternate method
def cube1(lis):
   res= [(i,pow(i,3)) for i in lis]
   print(res)

cube1([2,4,6,8])

#updating element of list of tuple
def update(lis):
    updateNum=4
    print('Original list of tuple : '+ str(lis))
    newUpdateList=[]
    for i in lis:
       for j in i:
          s=(j+updateNum)
          newUpdateList.append(s)
    print(newUpdateList)


update([(2,3),(3,4),(4,5)])