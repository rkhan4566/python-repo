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