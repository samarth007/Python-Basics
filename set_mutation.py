
def operate():
    order=input().split()
    o=order[0]
    update=set(map(int,input().split()))
    if o == 'Intersection_update':
        a.intersection_update(update)
    elif o == 'difference_update':
        a.difference_update(update)
    elif o == 'update':
        a.update(update)
    elif o =='symmetric_difference_update':
        a.symmetric_difference_update(update)
    return a


a=set(map(int,input().split()))
c=int(input())
for i in range(c):
    print(operate())