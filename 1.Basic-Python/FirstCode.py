#magic method:-Magic Methods
#Magic methods in Python, also known as dunder methods (double underscore methods), are special methods that start and end with double underscores. These methods enable you to define the behavior of objects for built-in operations, such as arithmetic operations, comparisons, and more.
#Magic Methods:-
#Magic methods are predefined methods in Python that you can override to change the behavior of your objects. Some common magic methods include:
#__init__: Initializes a new instance of a class.
#__str__: Returns a string representation of an object.
#__repr__: Returns an official string representation of an object.

class Person:
     pass

person=Person
print(dir(person))

#basic methods
class Person:
     def __init__(self,name,age):
         self.name=name
         self.age=age
         
person=Person("rehan",19)
print(person)

#
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name}, {self.age} years old"
    def __repr__(self):
        return f"person(name={self.name},age={self.age}"
    
person=Person("rehan",19)
print(person)
print(repr(person))