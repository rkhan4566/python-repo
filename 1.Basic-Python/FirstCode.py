#generators:-
#Generators are a simpler way to create iterators. They use the yield keyword to produce a series of values lazily, which means they generate values on the fly and do not store them in memory.

def square(n):
    for i in range(3):
        yield i**2
        
print(square(3))

for i in square(3):
    print(i)

def my_generator():
    yield 1
    yield 2
    yield 3

gen=my_generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

for val in gen:
    print(val)

#practicle example:-reading large file
def read_large_file(file_path):
    with open(file_path,'r') as file:
        for line in file:
            yield line

file_path='sample.txt'
for line in read_large_file(file_path):
    print(line.strip())

