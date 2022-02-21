class Test:
    a=0
    def __init__(self,b,c,d):
        self.b=b
        self.c=c
        self.d=d
    @classmethod
    def from_dash(cls,s):
        return cls(*s.split('-'))

    @staticmethod
    def stats(s):
        print("Hi {}".format(s))

t=Test(10,20,30)
print(t.b,t.c,t.d,t.a)
t1=Test.from_dash("sam-007-DS")
print(t1.c)
Test.stats("Calling from Class")
t.stats("Calling from Object")