class dash:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def m(self):
        print("dash class")

class comma:
    def __init__(self,c):
        self.c=c

    def n(self):
        print('comma class')

class done:
    def __init__(self,d,e):
        self.d=d
        self.e=e
    def __str__(self):
      return str(self.d)+" "+" "+str(self.e)

d=dash(12,12)
c=comma(10)
mak=done(d,c)
print(mak)