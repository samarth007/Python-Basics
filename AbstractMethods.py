from abc import ABC, abstractmethod

class shape(ABC):

    def __init__(self):
        print("hi")

    @abstractmethod
    def area(self):
        print("abstract method")


class square(shape):   #if we are inherting abstract method then we need to override it in sub class
    # def __init__(self,a,b):
    #     self.a=a
    #     self.b=b

    def area(self):
        print("square class")

s=square()
s.area()