## PYTHON MEMORY MANAGEMENT

## Memory management in Python involves a combination of automatic garbage collection,
# reference counting, and various internal optimizations to efficiently manage memory allocation and deallocation. Understanding these mechanisms can help developers write more efficient and robust applications.
# 1.Key Concepts in Python Memory Management
# 2.Memory Allocation and Deallocation
# 3.Reference Counting
# 4.Garbage Collection
# 5.The gc Module
# 6.Memory Management Best Practices

## REFERENCE COUNTING
# reference counting is the primary method python uses to manage memory.
# Each object in python maintain a count of reference pointing to it.
# when the reference pointing to it when the reference output drops to zero.
# the memory occupied by the object is dealloated.

import sys
a=[]
## 2 (one reference from 'a' and one from getrecount())
print(sys.getrefcount(a))

b=a
print(sys.getrefcount(b))

del b
print(sys.getrefcount(b))

#GARBAGE COLLECTION

#Python includes a cyclic garbage collector to handle reference cycles.
#Reference cycles occur when objects reference each other, preventing
#their reference counts from reaching zero. 

import gc
## enable garbage collection
gc.enable()

gc.disable()

gc.collect()

print(gc.get_stats())

print(gc.garbage)

##Memory Management Best Practices
#Use Local Variables:
#Local variables have a shorter lifespan and are freed sooner than global variables.
#Avoid Circular References:
#Circular references can lead to memory leaks if not properly managed.
#Use Generators:
#Generators produce items one at a time and only keep one item in memory at a time, making them memory efficient.
#Explicitly Delete Objects:
#Use the del statement to delete variables and objects explicitly.
#Profile Memory Usage:
#Use memory profiling tools like tracemalloc and memory_profiler to identify memory leaks and optimize memory usage

import gc
class myObject:
    def __init__(self,name):
        self.name=name
        print(f"object {self.name} created")

    def __del__(self):
        print(f"object {self.name} deleted")

#create circular reference
obj1=myObject("obj1")
obj2=myObject("obj2")
obj1.ref=obj2
obj2.ref=obj1

del obj1
del obj2

##manually trigger garbage collection
gc.collect()

#print collected objects
print(f"garbage collected objects: {gc.garbage}")

#generators for memory efficiency
#generators allow you to produce items one at a times one at a time,using memory efficiently by only keeping one item

def generate_numbers(n):
    for i in range (n):
        yield i

#using generators 
for num in generate_numbers(100000):
    print(num)
    if num>10:
        break

#rofiling memory usage with tracemalloc
import tracemalloc

def create_list():
    return [i for i in range(10000)]

def main():
    tracemalloc.start()

    create_list()

    snapsshot = tracemalloc.take_snapshot()
    top_stats = snapsshot.statistics('lineno') 

    print("[top 10]")
    for stat in top_stats[::]:
        print(stat) 

main()









