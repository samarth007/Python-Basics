
class over:
    def a(self,a,b):
        return a-b
    def a(self,a,b):
        return  a+b

o=over()
print(o.a(2,3))  #Method overloading is not supported in python
                 # it will pick the latest method


s='add'
print(eval(s))                 