#Encapsulation And Abstraction
#Encapsulation and abstraction are two fundamental principles of Object-Oriented Programming (OOP) that help in designing robust, maintainable, and reusable code. Encapsulation involves bundling data and methods that operate on the data within a single unit, while abstraction involves hiding complex implementation details and exposing only the necessary features.

#Encapsulation
#Encapsulation is the concept of wrapping data (variables) and methods (functions) together as a single unit. It restricts direct access to some of the object’s components, which is a means of preventing accidental interference and misuse of the data.

#encapsulation with getter and setter methods
#public,protected,private variables
class Person:
    def __init__(self,name,age):
        self.name=name  #public variable
        self.age=age    #public variable

def get_name(person):
    return person.name

person=Person("rehan",19)
print(get_name(person))

class Person:
    def __init__(self,name,age,gender):
        self.__name=name  #private variable
        self.__age=age    #private variable
        self.gender=gender
    
def get_name(person):
    return person._Person__age

person=Person("rehan",19,"male")
print(get_name(person))


class person:
    def __init__(self,name,age,gender):
        self._name=name
        self._age=age
        self._gender=gender

class Employee(person):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)

employee=Employee("rehan",19,"male")
print(employee._gender)

#encapsulation with getter and setter method
class Person:
    def __init__(self,name,age):
        self.__name=name #private access modifier or variable
        self.__age=age   #private variable

    #getter method for name
    def get_name(self):
        return self.__name
    
    #setter method for name
    def set_name(self,name):
        self.__name=name

    #getter method for age
    def get_age(self):
        return self.__age
    
    #setter methd for age
    def set_age(self,age):
        if age >0:
            self.__age=age
        else:
            print("age cannot be negative.")

person=Person("rehan",19)

#access and modify private variable using getter and setter
print(person.get_name())
print(person.get_age())

person.set_age(20)
print(person.get_age())

person.set_age(-5)
        