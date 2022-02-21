
def EvenOrOdd(a):
    if a%2==0:
        print('Number {} is even'.format(a))
    else:
        print('Number {} is odd'.format(a))

l=[23,12,45,10,44,65,18,20,72,77]

print(list(map(EvenOrOdd,l)))

#OR using Lambda Function

print(list(map(lambda num:num%2==0, l)))