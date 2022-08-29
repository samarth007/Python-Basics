

x=True
y=False
z=False

if not x or y:
    print ('1')
elif not x or not y and z:
    print('2')
elif not x or y or not y and x:
    print('3')
else:
    print('4')            



l=[1,3,45,5]
l1=[1,2,3]
print(l1+l)
print(not x or y or not y and x)