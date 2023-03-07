

class Test():
 
    __clspriv='clspriv'    #private static variable
    _clsproc='clsproc'     #protected static variables
    val=5                  #static variable

    def __init__(self,a,b):
        self.__objpriv=a
        self.b=b
        print('construtor')
        
    def method(self):
        self.__clspriv='updatd'
        # print(self.__objpriv)
        print(self.__clspriv)
        print(self._clsproc)
        # self.val+=10
        Test.val+=10
        print(self.val)
    
    @staticmethod
    def statmethod(q):  #static method will nevr have acess to cls and object var directly, by passing object we can acs
       print(q.b)

    @staticmethod
    def default():
        print('defaut')   

    def check(self):
        print(Test.val)    

    @classmethod
    def clsmethod(cls):
       print(cls.__clspriv)
    #    print(cls.b)                    #we cant access instance variable using class 


if __name__=='__main__':        
    t=Test(3,4)
    t.statmethod(t)
    Test.clsmethod()   
    t.method()     #  or   t.clsmethod
    t.check()
    s=Test(3,4)
    s.check()