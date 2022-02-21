class Test1():
    def __init__(self):
        pass

    def ab(self):
        print("Test1")

class Test2():
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def ab(self):
        print('Test2')


class Test3(Test2,Test1):
    def __init__(self,c,*args):
        super(Test3,self).__init__(*args)
        self.c=c


t=Test3(1,2,3)
t.ab()

#---------------------------------------------
