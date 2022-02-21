class M():
  def __init__(self,a,b):
      self.__s=a
      self.r=b

m=M(1,2)
print(m._M__s)

class N (M):
    def __init__(self,a,b,d):
        super().__init__(a,b)
        self.t=d

n=N(12,13,14)
print(n.r,n.t) # since __s is private we have access only to variable r and t