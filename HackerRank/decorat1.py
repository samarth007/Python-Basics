


def main_wel(func):

    def sub_func():
      print('Inside Function')
      func()
      print('Inside done')
    return sub_func

@main_wel
def child():
    print('Child function')

child()
# -------------------------------------------------------------------------------------
class Test:
  def __init__(self,a):
    self.a=a
  

  def __add__(self,b):
    return self.a + b.a
  
  def __mul__(self,b):
    return self.a * b.a


t=Test(2)
s=Test(3)
print(t*s)
