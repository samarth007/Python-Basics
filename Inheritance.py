
class A:
    def __init__(self):
        print("In A")

    def m1(self):
        print("m1 in a")

    def m2(self):
        print("m2 in a")


class B(A):
    def __init__(self):
        print("In B")

    def m1(self):
        print("m1 in b")

class C (B,A): #if we rite (A,B) it will give error bcz B is already inherting A
    def __init__(self):
        super().__init__()
        print("In C")

    def m3(self):
        print("m3 in c")

c=C()
c.m3()
c.m1()
c.m2()