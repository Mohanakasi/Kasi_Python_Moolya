from abc import ABC, abstractmethod
class Car(ABC):
    def mileage(self):
        pass

    def engine(self):
        print("my secret engine")
