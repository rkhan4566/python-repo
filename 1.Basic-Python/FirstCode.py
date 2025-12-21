##polymorphism

# polymorphism is a core concept in object oriented programming (oops) that allows objects of different classes 
# to be treated as object of a common superclass it provode a way to perform a single action in diffeerent form.
# polymorphism is typically achieved through method overriding and interfaces 

#base class 
class animal:
    def speak (self):
        return "sound of animals"
#derived class
class dog(animal):
    def speak(self):
        return "woof"
    
class cat(animal): 
    def speak(self):
        return "meow"
    
#function that demonstrate polymorphism 
def animal_speak(animal):
    print(animal.speak(dog))

dog1=dog()
cat1=cat()
print(dog1.speak())
print(cat1.speak())
animal_speak(dog)

#polymorphism with function and methods
# base class  
class shape:
    def area(self):
        return "area of the figure"
    
#derived class
class Rectangle(shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def area(self):
        return self.width*self.height
    
class Circle(shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14*self.radius*self.radius
    
#functions that demonstrate polymorphism

def print_area(shape):
    print(f"the area is {shape.area()}")

rectangle=Rectangle(4,5)
circle=Circle(3)

print_area(rectangle)
print_area(circle)

#Polymorphism with Abstract Base Classes
#Abstract Base Classes (ABCs) are used to define common methods for a group of related objects. They can enforce that derived classes implement particular methods, promoting consistency across different implementations.
from abc import ABC,abstractmethod

#define a abstact class
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

#derive class 1
class Car(Vehicle):
    def start_engine(self):
        return "car engine started"
    
#derived class 2
class Motorcycle(Vehicle):
    def start_engine(self):
        return "motorcycle engine started"
    
#function that demonstrate polymorphism
def start_vehicle(vehicle):
    print(vehicle.start_engine())
    
#create an object of car and motorcycle
car=Car()
motorcycle=Motorcycle()

start_vehicle(car)


