from abc import ABC,abstractmethod

class test(ABC):
    @abstractmethod
    def work(self):
        pass
    def dele(self):
        print("cool")

class test1(test):
    def m(self):
        print("hi")

    def work(self):
        print("abstract")

class test2():
    def n(self,a):
        print("test2")
        a.dele()

t=test1()
t2=test2()
t2.n(t)