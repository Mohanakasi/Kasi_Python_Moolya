from oops import Maths
class child_inher(Maths):
    num2 = 200
    def __init__(self):
        Maths.__init__(self,4,5)
    
    def add2(self):
        return self.num2+self.addition()
    
obj1 = child_inher()
print(obj1.add2())