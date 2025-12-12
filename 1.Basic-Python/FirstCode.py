########file operation- read and write lines#######
# ** file handling is a crucial part of programming language.python provied built in functions and method
#   and methods to read from and write to files,both text and binary.this lesson will cover thr basics of file handling,
#    incluiding reading and writing text files and binary files.


#read a whole file
"""with open('sample.txt','r')as file:
    content=file.read
    print(content)"""

with open(r"D:\AI-ML-FOLDER\1.Basic-Python\sample.txt", "r") as file:
    print(file.read())

#read a file with line by line
with open (r"D:\AI-ML-FOLDER\1.Basic-Python\sample.txt", "r")as file:
    for line in file:
        print(line.strip()) #strip remove the new line characteristics

#write a file with overwriting
with open(r"D:\AI-ML-FOLDER\1.Basic-Python\sample.txt", "w")as file:
    file.write('hello world\n')
    file.write('hello brother')

#write a file without overwriting
with open (r"D:\AI-ML-FOLDER\1.Basic-Python\sample.txt", "a")as file:
    file.write("append a new sentences!/n")

    