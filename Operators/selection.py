

def select(ar):
    
    for i in range(len(ar)):
        minpos=i
        for j in range(i+1,len(ar)):
            if ar[j]< ar[minpos]:
                minpos=j

        temp=ar[i]
        ar[i]=arr[minpos]
        ar[minpos]=temp                

arr=[3,6,1,2,9,4,2,20]
select(arr)
print(arr)