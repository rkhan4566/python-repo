#classes and object in python
#Object-Oriented Programming (OOP) is a programming paradigm that uses "objects" to design applications and computer programs. 
#OOP allows for modeling real-world scenarios using classes and objects. This lesson covers the basics of creating classes and objects, including instance variables and methods.

###A class is a blueprint for creating objects.
# It defines attributes (data) and methods (functions) that the objects will have.

"""class car:
    pass
audi=car()
bmw=car()
print(type(audi))
print(audi)

audi.windows=4
print(audi.windows)

class car:
    pass
tata=car()
print(tata)

tata.windows=5
print(tata.windows)
dir(tata)

#insatnce variable and methods
class dog:
    #constructor
    def __init__(self,name,age):
        self.name=name
        self.age=age
    #create object
dog1 = dog("buddy",3)
print(dog1)
print(dog1.name)
print(dog1.age)

dog2=dog("lucy",4)
print(dog2.name)
print(dog2.age)"""

#define a class with instance methods
class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def bark(self):
        print(f"{self.name} says woof")
    
dog=Dog("lucy",3)
dog.bark()

#modelling a bank account

#define a class of bank account
class bankaccount:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print(f"{amount}is deposited.new balance is{self.balance}")

    def withdraw(self,amount):
        if amount>self.balance:
            print("insufficient balance")
        else:
            self.balance-=amount
            print(f"{amount}is withdrawn.new balance is {self.balance}")

    def get_balance(self):
        return self.balance
    

#create an account
account=bankaccount("rehan",15000)
print(account.balance)

account.deposit(1000)
account.withdraw(10000)

     