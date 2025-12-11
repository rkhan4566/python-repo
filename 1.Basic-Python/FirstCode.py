# STANDARD LIBRARY OVERVIEW:-
"""python library is vast collection of modules and packages that comes bundled with python,
   providing a wide range of functionalities out of the box. here's an overview of the sum of the most commonly
   used modules and packages in the python standard libraries."""


import array 
arr=array.array('i',[1,2,3,4,5,6])
print(arr)

import random
print(random.randint(1,20))
print(random.choice(['apple','banana','cherry']))

import os
print(os.getcwd())

###  os.mkdir('test_dir')
"""
high level operations on files and collection on files

import shutil
shutil.copyfile('sample.txt','desination.txt')
"""
#datetime
from datetime import datetime,timedelta
now=datetime.now()
print(now)

yesterday=now-timedelta(days=1)
print(yesterday)

#time
import time
print(time.time())

time.sleep(2)
print(time.time())

#regular expression
import re
pattern=r'\d+'
text='there are 123 apples are present in there'
match=re.search(pattern,text)
print(match.group())

#data seialization
import json
data={'name':'rehan','age':19}
json_str=json.dumps(data)
print(json_str)
print(type(json_str))

paresed_data=json.loads(json_str)
print(paresed_data)
print(type(paresed_data))

#csv 
import csv
with open('example.csv',mode='w',newline='')as file:
    writer=csv.writer(file)
    writer.writerow(['name','age'])
    writer.writerow(['rehan',19])

with open('example.csv',mode='r')as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)    

#Conclusion

#Python’s Standard Library is very powerful and provides tools for almost any task—from file handling and web services to data serialization and concurrent execution.
# By understanding and using the available modules and packages, you can greatly improve your ability to write efficient and effective Python programs.