from abc import ABC, abstractmethod

class shape(ABC):

    def __init__(self):
        print("hi")

    @abstractmethod
    def area(self):
        pass

    def length(self):
        print('length_shape')


class square(shape):   #if we are inherting abstract class then we need to override it's abstract mth
    def __init__(self):
        print('square class')

    def area(self):
        print("square class")

    def length(self):
        print('length_square')

s=square()
s.area()
s.length()