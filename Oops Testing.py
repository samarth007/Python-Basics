
class Computer:
    def __init__(self):
        self.name='Test'
        self.age=26

    def compare(self,other):

        if self.age==other.age:
            return True
        else:
            return False

    def update(self):
        self.age=30


c1=Computer()
c2=Computer()

c1.update()
if c1.compare(c2):
    print("same")
else:
    print("different")

print('-----------------------------------------')

class Cars:
    wheel=4             #class variable or static variable
    def __init__(self,f,c):
        self.fuel=f    #instance variable
        self.colr=c

c3=Cars('petrol','white')
c4=Cars('Diesel','silver')
Cars.wheel=5
print(c3.fuel,c3.colr,c3.wheel)
print(c4.fuel,c4.colr,c4.wheel)

print('--------------------------------------------')

class StaticAndClass:
    m4=8727
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    @classmethod
    def clsMethod(cls):
        cls.m4=8778

    @staticmethod
    def statMethod(): #static method is related to class or object
        print("This is static method")

s1=StaticAndClass(23,12,43)
s2=StaticAndClass(67,45,23)
print(s1.avg())
StaticAndClass.clsMethod()
#s1.clsMethod() we can call class method using object and class name
print(StaticAndClass.m4)
s1.statMethod()