
def fib(n):
    n1,n2=0,1
    n3=0
    if n<0:
        print("enter valid number")
        return
    while n3<n:
        print(n1,end=' ')
        n4=n1+n2
        n1=n2
        n2=n4
        n3=n3+1
fib(5)
print()
print("----------------------------------------")
#Prints string with even length
def EvenLength(s):
    s=s.split(" ")
    for i in s:
     if len(i)%2==0:
        print(i, end=' ')

EvenLength("Hi there i'm using whatsapp")

print()
print("----------------------------------------")
#print if string has at least one letter and one number
def StrNum(s):
    s=s.split(" ")
    flag_l=False
    flag_n=False
    for i in s:
        if i.isalpha():
            flag_l=True
        if i.isdigit():
            flag_n=True

    return flag_n and flag_l

print("Is Text is AlphaNumeric :" + str(StrNum("hi5")))

print("-------------------------------------------")

def natural(n):
    i=0
    c=0
    while c <=n:
        i=i+pow(c,3)
        c=c+1
    return i
print(natural(10))