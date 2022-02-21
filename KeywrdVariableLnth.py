def employee(name, **data):
    print(name)
    print(data)
    for i, j in data.items():
        print(i, j)


employee("test", age=28, city='bnglr', mob=98765432)

print('-------------------------------------------')


# remove duplicate from tuple
def convert(lis):
    print("Original tuple : ", lis)
    res = tuple(set(lis))
    print("Removed duplicate : ", res)


convert((1, 3, 4, 3, 1, 7, 5, 2, 7))

print('------------------------------------------')


def removeSub(s):
    print("Original String is : ",s)
    remove = ['best', 'all']
    for i in remove:
        s = s.replace(i, '')
    print('After removing : ',s)

(removeSub("gfg is best for all geeks"))

print('----------------------------------------------')


# Truncate the string from substring
def removeAll(s):
    sub = 'for'
    for i in s.split(' '):
        if i == sub:
            s = s[:s.index(sub)]
    print(s)


removeAll('geeks is the best for all geeks')

print('-----------------------------------------------')


def Largest(lis):
    max = lis[0]
    for i in lis:
        if i > max:
            max = i
    return max


print(Largest([3, 2, 32, 70, 43, 53, 23]))
# print(Largest(['test','abc','hji']))
