class new_1:
    var_1 = 'Kasi'
    def __init__(self, place):
        self.place = place
        
    
    def display_var():
        return new_1.var_1
    
    def name_place(self):
        return self.var_1+self.place

obj1 = new_1('HSR')
print(obj1.name_place())
print(new_1.display_var())

class Maths:
    sim_var = 100
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print('Iam the constructor of parent')
    @staticmethod
    def data():
        print("temp")

    def addition(self):
        return self.a+self.b+Maths.sim_var
    
# obj1 = Maths(4, 5)
# print(obj1.data())
# print(obj1.addition())


