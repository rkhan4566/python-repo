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

#writing a list of a line    
lines=('firstline\n','secondline\n','thirdline\n')
with open('sample.txt','a')as file:
    file.writelines(lines)

#writing to a binary file
data=b'\x00\x01\x02\x03\x04'
with open('example.bin','wb')as file:
    file.write(data)

#reading a binary file
with open ('example.bin','rb')as file:
    content=file.read()
    print(content) 

#read the content from a source text file and write to a destination file 

with open('sample.txt','r') as source_file:
    content=source_file.read()

with open('destination.txt','w')as destination_file:
    destination_file.write(content)

#read a text file and count the number of lines words and characters.
def count_text_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        line_count = len(lines)
        word_count = sum(len(line.split()) for line in lines)
        char_count = sum(len(line) for line in lines)
    return line_count, word_count, char_count


file_path = 'sample.txt'
lines, words, characters = count_text_file(file_path)
print(f'Lines: {lines}, Words: {words}, Characters: {characters}')
   
#writing and then reading a file
with open ('sample.txt','w+')as file:
    file.write('hello world\n')
    file.write('this is my new line\n')

    """#move the file cursor to the begining
    file.seek(0)"""

    #read the content of the file 
    content.file.read()
    print(content)
