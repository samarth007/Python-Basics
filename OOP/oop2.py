
from oop import Test

class Refer():

    var=10
    def __init__(self,a,b):
        self.a=a
        self.b=b

def refer(obj):
    print(obj.var,obj.a,obj.b)

r=Refer(2,4)
refer(r)

# t=Test(10,10)
# t1=Test(10,10)
# t.method()
# t1.method()