class school:
    school_name='SVM'
    school_add="Mumbai"

class college:
    college_name='SV'
    college_add="Kdpr"

class candidate(school,college):
    def __init__(self,name):
        self.name=name

    def col_name(self):
        print(self.name,self.college_name,self.college_add)

    def schl_name(self):
        print(self.name,self.school_name,self.school_add)

c=candidate('test')
c.col_name()
c.schl_name()