
n= int(input("Enter the number of rows: "))
pattern=bool(int(input("Enter the number 1 or 0")))

if pattern==True:
 for i in range(1,n+1):
     print(i*'*')
else:
 row=n+1
 for i in range(1,n+1):
    print((row-i)*'*')
