# Requirements:
# Multithreading and Multiprocessing

# Real-World Example: Multiprocessing for CPU-bound Tasks
# Scenario: Factorial Calculation
# Factorial calculations, especially for large numbers,
# involve significant computational work. Multiprocessing
# can be used to distribute the workload across multiple
# CPU cores, improving performance.

##LAPTOP LAG KAR RHA H Q KI BIG NUMBERS KA FACTORIAL KAR RHE H ISLIYE

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

import multiprocessing
import math
import time

def computer_factorial(number):
    print(f"Computing factorial of {number}")
    result = math.factorial(number)
    return len(str(result))   # sirf digits count return

if __name__ == "__main__":
    numbers = [5000, 6000, 7000, 8000]
    start_time = time.time()

    with multiprocessing.Pool() as pool:
        results = pool.map(computer_factorial, numbers)

    end_time = time.time()
    print("Digits in factorials:", results)
    print(f"Time taken: {end_time - start_time} seconds")

## YHA SE CODE SHI H RUN KRNE LAYAK    

import multiprocessing
import math
import time

def computer_factorial(n):
    return len(str(math.factorial(n)))

if __name__ == "__main__":
    numbers = [1000, 1200, 1500]
    start = time.time()

    with multiprocessing.Pool(processes=2) as pool:
        results = pool.map(computer_factorial, numbers)

    print("Digits:", results)
    print("Time:", time.time() - start)