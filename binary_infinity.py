import math

def binary_infy(arr,i,j,n):

    while i<=j:
        mid=i+(j-i)//2

        if arr[mid]!=n:
            binary_infy(arr,mid+1,j,n)
        else:
            val=mid-1
            if type(arr[val])==int:
                return mid
            else:
                binary_infy(arr,i,mid-1,n)
    return -1               


l=[23,42,0,32,13,41,52,78,67,math.inf,math.inf,math.inf]
first_index=0
last_index=len(l)-1
num=math.inf
result=binary_infy(l,first_index,last_index,num)
print(l)