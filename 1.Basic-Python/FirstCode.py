####  Understanding Exceptions  ###
#Exception handling in Python allows you to handle errors gracefully and take corrective actions without stopping the execution of the program. This lesson will cover the basics of exceptions, including how to use try, except, else, and finally blocks.

#What Are Exceptions?
#Exceptions are events that disrupt the normal flow of a program. They occur when an error is encountered during program execution. Common exceptions include:

#  1.  ZeroDivisionError: Dividing by zero.

#  2.  FileNotFoundError: File not found.

#  3. ValueError: Invalid value.

#  4. TypeError: Invalid type.

#try and except block
try:
    a=b
except:
    print("the variable has not be assigned")

try:
    a=b
except NameError as ex:
    print(ex)

try:
    result=1/0
except ZeroDivisionError as ex:
    print(ex)
    print('entre the denominator is greater than zero')
    
try:
    result=1/2
    a=b
except ZeroDivisionError as ex:
    print(ex)
except Exception as ex1:
    print(ex1)
    print('main exception get caught here')
     
#input method by try,except,else 
try:
    num=int(input("enter a number "))
    result=10/num
except ValueError:
    print("this is not a valid error")
except ZeroDivisionError:
    print("entre denominator greater than zero")
except Exception as ex:
    print(ex)
else:
    print(f"the result is {result}")

#try,except,else and finally blocks
try:
    num=int(input("enter a number "))
    result=10/num
except ValueError:
    print("this is not a valid error")     
except ZeroDivisionError:
    print("you can't divided by zero")
except Exception as ex:                     #except block is work when error will get found
    print(ex)
else:                                       #else is work when no error will be found
    print(f"the result is {result}")  
finally:
    print("execution complete.")             #finally block works both in except and else 

#file handling and exception handling
try:
    file=open('example.txt','r')
    content=file.read()
    a=b
    print(content)
except FileNotFoundError:
    print("the file doesnot get exists")
except Exception as ex:
    print(ex)
finally:
    if 'file' in locals() and not file.closed():
        file.close()
        print('file close')
