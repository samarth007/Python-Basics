#Swaping first and last item of list
def swap(lis):
    size=len(lis)

    temp=lis[size-1]
    lis[size - 1] = lis[0]
    lis[0]=temp

    return lis

print(swap([20,30,11,15]))

#-------------------------------------------
# swapping elements is list
def swap2(lis):
    size=len(lis)
    lis1=[]
    for i in range(size-1,-1,-1):
      lis1.append(lis[i])

    print(*lis1)

swap2([10,20,30,40])

#--------------------------------------------
#Counting number of element in list
def length(lis):
    counter = 0
    for i in lis:
      counter=counter+1
    print((counter))

length([10,20,30,40])

#-----------------------------------------------
#Check the element present in list
def check(lis,num):

 if (num in lis):
   print("Element present")
 else:
     print("Element Absent")

check([30,80,42,18],30)


#------------------------------------------
#Reversing the element in list

def Reverse(lis):
    #new =lis[:-2]
    new=lis[::-1]
    return new

print(Reverse([23,24,34,90]))