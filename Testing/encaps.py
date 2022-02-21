class encap:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __str__(self):
        return 'Class encap'

class impl:
    def __init__(self,c,d):
        self.d = c
        self.d = d

    def __str__(self):
        return 'Class impl'


class final():
    def __init__(self,e,i,p):
        self.encap=e
        self.impl=i
        self.__pro=p

    def __str__(self):
        return "final class"+" "+str(self.encap)+" "+str(self.impl)

en=encap(2,4)
il=impl(4,5)
f=final(en,il,8)  #encapsulation  technique
print(f)
print(f._final__pro)  #calling private variable