
def closest(arr,l):
   arr.sort()
   close=arr[0]
   target=0
   for i in range(1,l):
      currDiff=abs(arr[i]-target)
      prevdiff=abs(close-target)

      if currDiff < prevdiff:
          close=arr[i]

      else:
          if currDiff==prevdiff:
              return arr[l]

   return close


def fartest(arr,l):
    arr.sort()
    f=arr[l]
    target=0
    for i in range(0,l-1):
        currDiff=abs(arr[i]-target)
        prevDiff=abs(f-target)
        if currDiff > prevDiff:
            f=arr[i]
    return f

arr=[-2,-2,8,5,5,10,5,6]
l=len(arr)-1
print(closest(arr,l))
