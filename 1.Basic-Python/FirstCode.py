"""#functions
# A functions is a block of code that soecific task. help in organising code reuse code and impeove readability

def function_name(parameter):
    ###docstring###
    #function body"
    return "expression"

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

#check if a string is palindrome
def is_palindrome(s):
    s=s.lower().replace(" "," ")
    return s==s[::-1]

print(is_palindrome("A man a plan a canal panama"))
print(is_palindrome("sos"))

#calculate the factorial of a number using recursion
def factorial(n):
    if n==0:
        return 1
    else:
        return n* factorial(n-1)
    
print(factorial(5))
print(factorial(25))
      
# A function to read a file and count the frequency of each word
def count_word_frequency(file_path):
    word_count={}
    with open(file_path,'r')as file:
        for line in file:
            words=line.split()
            for word in words:
                word=word.lower().sprit(',.!!;:"')
                word_count[word]=word_count.get(word,0)+1
    return word_count

filepath='sample.txt'
word_frequency=count_word_frequency(filepath)
print(word_frequency)  

#lamda functions in python
# lamda functions are small anonynus function define using lamda function keyword.they can have any number of arguments but only one expressions.
#they are commonly used for short operations or as arguments to higher order function

#THIS IS SIMPLE DEFINITION FUNCTION
def addition(a,b):
    return a+b
print(addition(2,5))

#THIS IS LAMBDA FUNCTION
addition= lambda a,b:a+b
print(addition(2,5))


#def
def even(num):
    if num%2==0:
        return True
    else:
        False
print(even(44))    
print(even(45))
#lambda
even1=lambda num:num%2==0
print(even1(12))


#def
def addition (x,y,z):
    return x+y+z
print(addition(4,5,6))
#lambda
addition1=lambda x,y,z:x+y+z
print(addition(4,5,6))

#square of list of items
numbers=[1,2,3,4,5,6]
def square(numbers):
    return numbers**2
print(square(6))
#using lambda
result=list(map(lambda x:x**2,numbers))
print(result)

#map:- the map() functions applies a given function to all items in an input list(or any other iterable)
#and returns a map object (an iterator).this is particularly useful for transforming data in a list comprehensively

def square(num):
    return num*num
print(square(10))

numbers=[1,2,3,4,5,6,7,8]
result=list(map(square,numbers))
print(result)

#lambda functions with map
numbers=[1,2,3,4,5,6,7,8]
result=list(map(lambda x:x*x,numbers))
print(result)

#map multiple iterables
numbers1=[1,2,3]
numbers2=[4,5,6]
added_numbers=list(map(lambda x,y:x+y,numbers1,numbers2))
print(added_numbers)

#map() to convert a list of string to integers
#use map to convert string to integer
str_numbers=['1','2','3','4','5','6']
int_numbers=list(map(int,str_numbers))
print(int_numbers)

words=['apple','banana','orange',]
upper_word=list(map(str.upper,words))
print(upper_word)

def get_person(person):
    return person['name']
people=[
    {'name':'rehan','age':'19'},
    {'name':'rkhan','age':'22'}
]
result=list(map(get_person,people))
print(result)
"""
#filter:-the filter() function constructs an iterior from elements of an iterable for which a function return true.
# it is used to filter out items from a list(or any other iterable)based on a condition

def even(num):
    if num%2==0:
        return True
    else:
        return False
print(even(45))

lst=[1,2,3,4,5,6,7,8,9]
result=list(filter(even,lst))
print(result)

#filter with lambda function
num=[1,2,3,4,5,6,7,8,9,10,11]
greater_than_five=list(filter(lambda x:x>5,num))
print(greater_than_five)

#filter with a lambda function and multiple function conditions
number=[1,2,3,4,5,6,7,8,9,10,11]
even_and_greater_than_five=list(filter(lambda x:x>5 and x%2==0,number))
print(even_and_greater_than_five)

#filter() to check if the age is greater than 25 in dictionaries
people=[
    {'name':'rehan','age':19},
    {'name':'rkhan','age':29}
]

def age_greater_than_25(person):
    return person['age']>25

result=list(filter(age_greater_than_25,people))
print(result)