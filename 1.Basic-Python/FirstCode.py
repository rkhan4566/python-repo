#functions
# A functions is a block of code that soecific task. help in organising code reuse code and impeove readability

def function_name(parameter):
    """docstring"""
    #function body"
    return expression

#why function is essential
num=24
if num%2==0:
    print("this is even number")
else:
    print("this is odd number")

def even_or_odd(num):
    if num%2==0:
        print("this is evens number")
    else:
        print("this is odds number")
#call this function
even_or_odd(23)
even_or_odd(32)

#function with multiple parameters
def add(a,b):
    return a+b
result=add(2,4)
print(result)

result=add(3,5)
print(result)

#substaction
def sub(a,b):
    return a-b
result=sub(4,1)
print(result)

#defult parameters
def greet(name):
    print(f"hello {name} welcome to the paradise")
greet("rehan")
def greet(name):
    print(f"hello {name} you are professional player")
greet("Rkhan10")

#variable length arguments
#positional and keywords arguments

#positional statement
def print_numbers(*args):
    for number in args:
        print(number)
print_numbers(1,2,3,4,5,6,7,8,9,"rakib")       

###keywords arguments
def print_details(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
print_details(name="rehan",age="19",country="india")

def print_details(*args,**kwargs):
    for val in args:
        print(f"posotional arguments : {val}")
    for key,value in kwargs.items():
            print(f"{key}:{value}")
print_details(1,2,3,4,"rehan",name="rehan",age="19",country="india")           

def multiply(a,b):
    return a*b

multiply=(2*3)
print(multiply)
