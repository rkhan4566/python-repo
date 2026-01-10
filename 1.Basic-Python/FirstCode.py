#program:- A program is a sequence a instruction return in programming language
              #eg:- python,c++,java

              #eg:-Google chrome:-exe-> program -> browser should work 

#process:- A process is a simply an instance of a program that is being executed

#Threads:- A thread is a unit of execution within a process

### Multithreading
### when to use multi Threading
### I/O- bound tasks: Tasks that spend more time waiting for I/O operations (eg:- file operation,network,request).
### concurrent execution: When you want to improve the thoughtut of the application by performing multiple operation cuncurrently.

import threading
import time
def print_numbers():
    for i in range(5):
        print(f"numbers:{i}")

def print_latter():
    for latter in "abcde":
        print(f"Latter:{latter}")

t=time.time()
print_numbers()
print_latter() 
finished_time=time.time()-t
print(finished_time)      


