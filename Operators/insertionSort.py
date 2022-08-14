
def insertSort(ar):
  
  for i in range(1,len(ar)):
    key=ar[i]
    j=i-1
    while j>=0 and key < ar[j]:
        ar[j+1]=ar[j]
        j=j-1
    ar[j+1]=key

arr=[4,2,3,7,1,10]
insertSort(arr)
print('Ascending order',arr)

