data='23,12,32,45,214,214'

l=data.split(',')  #converting to list
t=tuple(l)  # converting to tuple
print(l)
print(t)

print('--------------------------------------')


#if str has Is at begining then print as is else concat Is at front of str
str='Isempty'

if str[:2]=='Is':
  print(str)
else:
    print('Is'+str)


#count of given number
df=[23,4,32,4,21,22,5,4,21,4,8,45,4]
n=4
count=0
for i in range(len(df)):
    if df[i]==n:
       count=count+1
print(count)

print('-------------------------------------')


#Check
a=[2,4,5,7,3,1]
check=7

def checking(a):
 for i in range(len(a)):
    if a[i]==check:
        return True

 return False

print(checking(a))

print('--------------------------------')