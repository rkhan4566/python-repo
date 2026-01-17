#multithreading with thread pool executor
from concurrent.futures import ThreadPoolExecutor
import time
def print_number(numbers):
    time.sleep(1)
    return f"number :{numbers}"

numbers=[1,2,3,4,5,6,7,8,9,10]

with ThreadPoolExecutor(max_workers=1) as executor:
    results=executor.map(print_number,numbers)
    for result in results:
        print(result)

##multiprocessing with processpoolexecutor
from concurrent.futures import ProcessPoolExecutor
import time

def square_number(number):
    time.sleep(1)
    return f"square: {number*number}"

numbers=[1,2,3,4,5,6,7,8,9]
if __name__=="__main__":
    with ProcessPoolExecutor(max_workers=3) as executor:
        results=executor.map(square_number,numbers)

    for result in results:
        print(result)
