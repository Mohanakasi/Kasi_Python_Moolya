from abc import ABC, abstractmethod
class age_(ABC):
    def __init__(self, age):
        self.age = age
    @abstractmethod
    def get_age(self):
        pass

class age_get2(age_):

    def get_age(self):
        print("executing child class overided method")

obj1 = age_get2(28)
obj1.get_age()
# obj2 = age_(24)
# obj2.get_age()

