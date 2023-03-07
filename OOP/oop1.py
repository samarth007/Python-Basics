

class Decorat():

    cs=12

    def __gen(func):
        def wrapper(self,val):
            func(self,val)
            print(self.cs)
        return wrapper
    
    @__gen
    def m(self,val):
      print('hello'*val)
    
    @__gen
    def n(self,val):
      print('hi'*val)
    
    @staticmethod
    def check():
      print('static method')  

d=Decorat()
d.m(2)
d.n(3)
