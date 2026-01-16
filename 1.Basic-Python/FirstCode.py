# Multithreading and Multiprocessing

# Processes that run in parallel
# CPU-bound tasks - tasks that are heavy on CPU usage (e.g., mathematical computations, data processing)
# Parallel execution - Multiple cores of the CPU

import multiprocessing
import time

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"sqare: {i*i}")

def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"cube: {i*i*i}")

if __name__=="__main__":
        
    #create 2 processes
    p1=multiprocessing.Process(target=square_numbers)
    p2=multiprocessing.Process(target=cube_numbers)
    t=time.time()

    #start the process
    p1.start()
    p2.start()

    #wait for the process to complete
    p1.join()
    p2.join()

    finished_time=time.time()-t
    print(finished_time)


from multiprocessing import Process, Queue
import time

def square(q):
    for i in range(4):
        q.put(i)
        time.sleep(1)

def cube(q):
    for _ in range(4):
        i = q.get()
        print(f"square: {i*i}")
        print(f"cube: {i*i*i}")

if __name__ == "__main__":
    q = Queue()
    p1 = Process(target=square, args=(q,))
    p2 = Process(target=cube, args=(q,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
