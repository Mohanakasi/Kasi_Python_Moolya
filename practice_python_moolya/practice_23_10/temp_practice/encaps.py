class prime:
    def __init__(self):
        self.name = 'kasi'
        self._desig = 'sdet'
        self.__company = 'moolya'

p1 = prime()
print(dir(prime))
# print(p1._desig)
print(dir(p1))
# p1.__company()
class emp(prime):

    def __init__(self):
        prime.__init__(self)
        print(self.__company)

emp = prime()
print(emp.name)
# print(emp.__company)#we can not use

class type1:
    def __init__(self):
        pass

    def method1(self):
        print('my self mohana')
class type2(type1):
    def __init__(self):
        pass

    def method1(self):
        super().method1()
        print("I am also kasi")

obj1 = type1()
obj2 = type2()
obj1.method1()
obj2.method1()


"example2"
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")


cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()

