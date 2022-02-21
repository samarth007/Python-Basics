class A2B:
    def __init__(self,m,n):
        self.m=m
        self.n=n
    def update(self):
        print(self.m)


class B2C(A2B):
    def __init__(self,m,n,q):
       super().__init__(m,n)
       self.q=q

    def up(self):
        print(self.m+self.n+self.q)

b=B2C(1,3,4)
b.up()
b.update()