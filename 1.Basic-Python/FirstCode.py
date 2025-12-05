#functions
# A functions is a block of code that soecific task. help in organising code reuse code and impeove readability

def function_name(parameter):
    ###docstring###
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

##temperature conversion
def convert_temperature(temp,unit):
    if unit=='c':
        return temp *9/5 + 32
    elif unit=='f':
        return (temp-32)*5/9
    else:
        return None

print(convert_temperature(25 ,'c'))     
print(convert_temperature(77, 'f'))

##password strong checker
##this function have to check the password is strong or not##
def is_strong_password(password):
    if len(password)<8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char in '!@#$%&' for char in password):
        return False
    return True

print(is_strong_password("Rehanr0#"))

##calculate the total cost of item in a shopping cart

def calculate_total_cost(cart):
    total_cost=0
    for item in cart:
        total_cost+=item['price']* item['quantity']
    return total_cost

cart=[
        {'name':'apple','price':20,'quantity':10},
        {'name':'banana','price':5,'quantity':6},
        {'name':'orange','price':40,'quantity':4}
    ]
print("total_cost:",calculate_total_cost(cart))

