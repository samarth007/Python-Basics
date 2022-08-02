
class MainTest:
  def m1(self):
      print("m1")

  def m2(self):
      print("m2")

  def mainMethod(self):
     self.m1()
     self.m2()

  def m3(self):
    print('m3')

if __name__ == '__main__':
  m=MainTest()
  m.mainMethod()   #Since it only has both m1() and m2() so it wont print m3()
