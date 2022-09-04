

def SelectionSort(arr):
    n=len(arr)
    for i in range(0,n):
        min_idx=i
        for j in range(i+1,n):
            if arr[j] < arr[min_idx]:
                min_idx=j
        
        #Swapping
        arr[i],arr[min_idx]=arr[min_idx],arr[i]
    return arr            

l=[23,42,41,7,12,44,11,4,5,1,19]
result= SelectionSort(l)
print(l)