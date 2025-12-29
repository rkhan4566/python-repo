"""#Decorators:-
#Decorators are a powerful and flexible feature in Python that allows you to modify the behavior of a function or class method.
# They are commonly used to add functionality to functions or methods without modifying their actual code.
# This lesson covers the basics of decorators, including how to create and use them.

#Python
## function copy
## closures
## decorators

#function copy:-
def welcome():
    return "welcome to advanced python course"

print(welcome())

wel=welcome()
print(wel)

del welcome
print(wel)

#closers:-
def main_welcome():
    msg='welcome'
    def sub_welcome_method():
        print("welcome to the advanced python course")
        print(msg)
        print("please learn these concepts properly")
    return sub_welcome_method()

print(main_welcome())

#closers function
def main_welcome(msg):
   
    def sub_welcome_method():
        print("welcome to the advanced python course")
        print(msg)
        print("please learn these concepts properly")
    return sub_welcome_method()

print(main_welcome("welcome everyone"))

def main_welcome(func):
    def sub_welcome_method():
        print("welcome to the advanced python course")
        func("welcome everyone to this tutorial")
        print("please learn these concepts properly")
    return sub_welcome_method()

main_welcome(print)

def main_welcome(func,lst):
    def sub_welcome_method():
        print("welcome to the advanced python course")
        print(func(lst))
        print("please learn these concepts properly")
    return sub_welcome_method()

print(main_welcome(len,[1,2,3,4,5]))
"""
#decorators:-
def my_decorator(func):
    def wrapper():
        print("something is happening before the function is called.")
        func()
        print("something is happening before the function is called.")
    return wrapper 

@my_decorator
def say_hello():
    print("hello")

say_hello()

#decorators with positional arguments:-
def repeat(n):
    def decorator(func):
        def wrapper(*args,**kwargs):
            for _ in range(n):
                func(*args,**kwargs)
        return wrapper
    return decorator

@repeat(5)
def say_hello():
    print("hello")

say_hello()
