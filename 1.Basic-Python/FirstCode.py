#iterators:- 

#iterators are advanced python concepts that allows for efficient looping and memory management.
# iterators provide a way to access elements of a collections sequentially without exposing the underlying structure.

my_list=[1,2,3,4,5,6]
for i in my_list:
    print(i)

print(type(my_list))
print(my_list)

iterator=iter(my_list)
print(type(my_list))
iterator
 
print(next(iterator))

try:
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
except StopIteration:
    print("there will be not iterate")
