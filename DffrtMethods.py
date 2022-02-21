
class Students:
    school='telusko'
    def __init__(self,m1,m2,m3):
         self.m1=m1
         self.m2=m2
         self.m3=m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    @classmethod
    def info(cls):
        return cls.school

    @staticmethod
    def info_class():
        print("Static method")
s=Students(12,34,45)
print(s.avg())
print(Students.info())
Students.info_class()