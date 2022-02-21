# Average and sum of list
def avgSum(lis):
    summ=0
    for i in lis:
        summ=summ+i
    print("Average is " + str(summ/len(lis)))
    return  summ

print("Sum is "+ str(avgSum([10,20,10,20])))

print("-------------------------------------")
# Finding smallest number in list
def smallest(lis):
    min=lis[0]
    for i in range(len(lis)):
        if lis[i]<min:
            min=lis[i]

    print("Min value is "+ str(min))
smallest([-5,2,3,-1,4])

print("--------------------------------------")

#Largest number in list
def Largest(lis):
    max=lis[0]
    for i in range(len(lis)):
        if lis[i]>max:
            max=lis[i]
    print("Largest Value is "+ str(max))
Largest([4,-1,2,-5,7])

print("--------------------------------------")

#Reversing each letter of string in list
test_list = ["geeks", "for", "geeks", "is", "best"]

# printing original list
print("The original list is : " + str(test_list))

# using list comprehension
# Reverse All Strings in String List
res = [i[::-1] for i in test_list]

# printing result
print("The reversed string list is : " + str(res))

