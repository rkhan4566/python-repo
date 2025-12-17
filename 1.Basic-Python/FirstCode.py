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

#polymorphism with functions and methods
