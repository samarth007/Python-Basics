
#Here lis is iterable, As soon we initialise the lis it will get saved in the memory location.
lis=[1,2,3,4,5]
for i in lis:
    print(i,end=' ')

print()
print('---------------------------------')
lis1=iter(lis)     #Converting Iterable lis to Iterator lis1 using iter method.
print(next(lis1))                   # And the memory is not initialised for this lis1.
                   #Memory is initialised when we call the next() method

print('-------------------------------------------')

s='Ind vs Pak WCT20'
print(s)
print(s[::-1])
print(s[::-2])
print(s.upper())
print('-------------------------------------------')

num=[23,12,19,43,21]
#print(num.extend([12,23,42])) #extends method takes list as an argument and append it to the list
# print(num.append(78)) # append method takes single object as an argument and append it to the list

d={"one":1,"two":2,"three":3}
print(d)
d['seven']={7,27,47}  #adding set to dictonary
d["four"]=4
d["five"]=5
print(d)
del d['three'] #deleting key three
print(d)
print('---------------------------------------')

dt={"lap":"Dell","Mob":"OnePlus","Car":"Brezza","Sim":"airtel"}
dt1=dt                #By assigning dt to new variable dt1 is not recommended
dt1["lap"] = "Hp"     # bcoz changing the element of dt1 will also reflect in dt
print("dt : ", dt)
print("dt1 : ", dt1)
print('---------------------------------------')

td={"org":"sapient","role":"QA","type":"manual"}
td1=td.copy()            #By using .copy method we make a separate copy for td1
td1["type"]="automation" # so that if we change the value of td1, td is not impacted.
print("td1 : ",td1)
print("td : ",td)