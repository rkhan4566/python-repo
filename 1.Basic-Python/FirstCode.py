#abstraction:-abstraction is the concept of hiding the complex implementation details and showing only the necessary features of the object. 
#this helps in reducing programing complexity and effort

from abc import ABC,abstractmethod
#abstract base class
class Vehicle(ABC):
    def drive(self):
        print("the vehicle is used for driving")

    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("car engine start")

def operate_vehicle(vehicle):
        vehicle.start_engine()
        vehicle.drive()
car=Car()
operate_vehicle(car)


