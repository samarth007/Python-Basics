
fname='test'

for i in fname[::-1]:
    print(i,end='')
print()

print('--------------------------')


a=[7,2,3,1]
p=' * '

for i in a:
    print(p*i)

print('----------------------------')


#print even  and stop at 237
numbers = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958,743, 527
    ]

even=[]
check=237
for i in numbers:
    if i==check:
        break
    if i%2==0:
        even.append(i)

print(even)

print('----------------------------')

color_list1=set(['RED','BLACK','BLUE'])
color_list2=set(['WHITE','RED','GREEN'])


print(color_list1.difference(color_list2))