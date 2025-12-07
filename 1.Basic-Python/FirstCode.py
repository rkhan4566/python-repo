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