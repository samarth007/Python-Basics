
def even(a):
    if a%2==0:
        return True
    else:
        return False

l=[1,2,3,4,5,6,7,8,0]

print(list(filter(even,l))) #filter functions return True values

#OR
#using lamba function

print(list(filter(lambda num:num%2==0,l)))