# Requirements:
# Multithreading and Multiprocessing

# Real-World Example: Multiprocessing for CPU-bound Tasks
# Scenario: Factorial Calculation
# Factorial calculations, especially for large numbers,
# involve significant computational work. Multiprocessing
# can be used to distribute the workload across multiple
# CPU cores, improving performance.

import multiprocessing
import math
import sys
import time


#increase the maxium number of digits for integer conversion
sys.set_int_max_str_digits(10000)

##function to compute factorial of a given numbers
def computer_factorial(number):
    print(f"computing factorial {number}")
    result=math.factorial(number)
    print(f"factorial of {number} is {result}")

if __name__=="__main__":
    numbers=[5000,6000,7000,8000]
    start_time=time.time()

#create a pool of worker processes
with multiprocessing.Pool() as pool:
    results=pool.map(computer_factorial,numbers)

end_time=time.time()
print(f"results:{results}")
print(f"time taken:{end_time - start_time} seconds")
