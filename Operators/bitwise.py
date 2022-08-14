a=10
b=3
print(a & b)
print(a|b)
# print(a>>5)
# print(a>>3)
# print(a<<3)   #refer bookmark addition using bitwise operator

def bitwise_add(x,y):
    while y!=0:
        carry=x&y
        print('carry : ',carry)
        x=x^y
        print('sum : ',x)
        y=carry<<1
        print('y :',y)
    return x

# print(bitwise_add(100,200))        

# a=False
# b=True
# print(b<<1)
# print(a&b)
# print(a|b)

