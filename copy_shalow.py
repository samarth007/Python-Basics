import copy

#Copy
l=[2,3,4,5]
l1=l
l1[2]=76
print('L',l)
print('L1',l1)


#Shallow Copy
lst=[1,2,3,4]
lst1=lst.copy()
lst1[2]=7
print('Lst',lst)
print('Lst',lst1)


#In case of multi-dimensional list if we change elements of the list in that case changes are reflected in both the list object
ll=[[2,3,4,5,],[4,5,6,7]]
ll1=ll.copy()
ll1.insert(2,[6,3,8,9])
ll1[1][0]=70
print('LL',ll)
print('LL1',ll1)


#To avoid above scenario we go for Deep Copy
a=[[4,5,6,7],[6,8,9,1]]
b=copy.deepcopy(a)
a[1][1]=89
print('a',a)
print('b',b)
