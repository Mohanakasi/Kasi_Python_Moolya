

class acm:
    def __init__(self, name, place, age):
        self.name = name
        self._place = place
        self.__age = age

    def display(self):
        print(self.name)
        print(self.__age)
        print(self._place)

obj1 = acm('kasi', 'gnt', 26)
print(obj1.name)
obj1.display()
# print((obj1.place))
# print(obj1._place)# not proper way
# print(obj1.__age) # will not work even you use __

class acm2(acm):

    def __init__(self, date, name, place, age):
        super().__init__( name, place, age)

    def display(self):
        print(self._place)
    # def display2(self):
    #     print(self.__age)



obj2 = acm2(25, 'kasi', 'gnt', 25)
obj2.display() #protected we can not use out side the class but we can use it in inherited class
# obj2.display2() #private variables we can not access out side class even in inheritence also


"""inheritence"""
from datetime import date
class  people:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def age1_static(name, birthyear):
        return name, date.today().year-birthyear

    @classmethod
    def age2_class(cls, name, birthyear):
        return name, date.today().year - birthyear

    def display(self):
        print(self.name, self.age)

obj1 = people('kasi', '26')
obj1.display()
print(people.age1_static('kasi', 1995))
# print(people.age2_class('Mohana', 28))

# class people2()
class child(people):
    name = 'Mohana kasi'


print(child.age1_static(child.name, 1995))
print(child.age2_class('Viswa', 1996))
child_parent_obj2 = people('Mohan', 2001)
child_parent_obj2.display()
child_obj = child('Rao', 1998)
child_obj.display()


