class M():
  def __init__(self,b):
      self.__s=100
      self.r=b

m=M(10)
print(m._M__s)

class N(M):
    def __init__(self,q,w):
        super().__init__(q)
        self.t=w

n=N(20,30)
print(n.r,n.t,) # since __s is private we have access only to variable r and t
print(n._M__s)   # To access parent class private 