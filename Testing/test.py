class Test1():
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.d=c

    def ab(self):
        print("Test1")

class Test2():
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def ab(self):
        print('Test2')


class Test3(Test1,Test2):
    def __init__(self,c,*args):
        super().__init__(*args)
        self.c=c


t=Test3(1,2,3,4)
t.ab()
print(t.a,t.b,t.c,t.d)

#---------------------------------------------
