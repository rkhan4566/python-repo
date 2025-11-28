"""print("Hello World")
print("my first code ")
print("i am rkhan10")
#syntax
a=1
b=2
sum=a+b
print(sum)
total=1+2+3+4+5+6+7+8
print(total)
a=1;b=2;x=a+b
print(x)
name="rehan"
age=19
print(type(name))
print(type(age))
##indentation
age=20
if age>19:
    print("true")
else:
    print("false")
##that is comment when we use double ## and ''''''
name="rehan"
age=19
height="5.8"
print("name:",name)
print("age:",age)
print("height:",height)
#type conversion
age=19
print(type(age))

age_str=str(age)
print(age_str)
print(type(age_str))

height=5.8
print(int(height))
print(float(height))

 #dynamic type
var=10
print(var,type(var))
var="rehan"
print(var,type(var))
var=6.0
print(var,type(var))

#input
name=str(input("what is your name"))
print(name,type(name))

age=int(input("what is your age"))
print=(age,type(age))

#simple calculaator
num1=float(input("entre your number"))
num2=float(input("entre your number"))

add=num1+num2
difference=num1-num2
product=num1*num2
quotient=num1/num2

print(add,"addition")
print(difference,"diff")
print(product,"mul")
print(quotient,"divide")

#integer data types
age=32
print(type(age))

#float value data type
height=5.8
print(type(height))

#string data types
name="rehan"
print(type(name))

#boolean data types
is_true=True
print(type(is_true))

a=10
b=10
print(type(a==b))

a=Rkhan+str(10)
print(a)

#Arithmetic operation
a=10
b=5
add_result=a+b #addition
sub_result=a-b #substraction
mul_result=a*b #multiplication
div_result=a/b #division
floor_div_result=a//b #floordivision
modulus_result=a%b #modulus
exponent_result=a**b #exponential

print(add_result)
print(sub_result)
print(mul_result)
print(div_result)
print(floor_div_result)
print(modulus_result)
print(exponent_result)


#comparison operator
a=10
b=10
result=a==b
print(result)


#not equal value
str1=("rehan")
str2=("Rehan")
result=str1!=str2
print(result)

#greater than less than and equal to
a=5
b=6
result=a>b
print(result)

a=5
b=4
result=a>b
print(result)

a=6
b=6
result=a==b
print(result)


#AND OR and NOT logic operator
a=True
b=False
result=a and b
print(result)

a=True
b=False
result=a or b
print(result)

a=True
result= not a
print(result)

#simple calculator
num1=float(input("entre your first number"))
num2=float(input("entre your second number"))

addition=num1+num2
substraction=num1-num2
multiplication=num1*num2
divide=num1/num2
floor_division=num1//num2
modulus=num1%num2
exponential=num1**num2

print("Add=",addition)
print("Sub=",substraction)
print("mul=",multiplication)
print("div=",divide)
print("fl div=",floor_division)
print("mod=",modulus)
print("exp=",exponential)


#conditonal statements
age=int(input("entre your age="))

if age<=13:
    print("you are a child")
elif age<18:
    print("you are not eligible for vote")
else:
    print("you are eligible for vote")

num=int(input("entre your number"))

if num%2==0:
    print("it is an even number")
else:
    print("it is an odd number")
   

#using nested condition
year=int(input("entre year:"))
if year%4==0:
    if year%100==0:
        if year%400==0:
           print(year,"it is a leap year")
        else:
            print(year,"it is not a leap year") 
    else:
        print(year,"it is a leap year")
else:
    print(year,"it is not a leap year")


#simple calculator
num1=int(input("entre your number"))
num2=int(input("entre your number"))
operation=input("entre operation(+,-,*,/):")

if operation == '+':
    result= num1+num2
elif operation == '-':
    result= num1-num2
elif operation == '*':
    result= num1*num2
elif operation == "/":
    result= num1/num2
    if num2 !=0:
        result=num1/num2

    else:
        result="invalid operation"
else:
    result= "error division by zero"
print(result)

# for loop

range(5)
print(range)

for i in range (5):
    print(i)

for i in range(1,10):
    print(i)

for i in range(1,10,2):
    print(i)


#while loop
count=0
while count<5:
    count=count+1
    print(count)

count=0
while count<100:
    count=count+1
    print(count)

for i in range(10):
   if i==5:
    break
   print(i)


for i in range(100):
   if i==25:
      break
   print(i)

#pass null statement
for i in range(5):
   if i==4:
    print("the null number",i)
    pass
   print( i)

#nested loop
#in loop inside a loop

for i in range(5):
  for j in range(4):
    print(f"i:{i} and j:{j}")
    
n=10
sum=0
for i in range(11):
   sum=sum+i
print(sum)

n=10
sum=0
count=1

while count<=n:
  sum=sum+count
  count=count+1
  print("sum of all natural number",sum)

#prime number of (1 , 100)

for num in range(1,101):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)
          


    print("reminder this all ")
"""
list
lst=[]
print(type(lst))

name=["rehan","rkhan",10,20,]
print(type(name))
print(name)

##mixed list
name=["rehan","alam","apple","3.14",True]
print(name)

#accesing list element
fruits=["apple","banana","kiwi","mango","pomegranate"]
print(fruits[1])
print(fruits[0:])
print(fruits[-1:])
print(fruits[1:4])

#m)odifying the list element
fruits[1]="watermelon"
print(fruits)

#append, that means add new list item in the ending of the list
fruits.append("orange")
print(fruits)

fruits.insert(1,"banana")
print(fruits)

fruits.remove("banana")
print(fruits)

#remove and return of the last element
popped_fruits=fruits.pop()
print(popped_fruits)

index=fruits.index("apple")
print(index)

fruits.insert(3,"apple")
print(fruits.count("apple"))
print(fruits)

#sort() helps to arrnage in accending order
fruits.sort()
print(fruits)

#decending order by reverse () method
fruits.reverse()
print(fruits)

#remove all item in list by clear() method
fruits.clear()
print(fruits)

#silicing method
numbers=[1,2,3,4,5,6,7,8,9,10]
print(numbers[2:5])
print(numbers[:5])
print(numbers[5:])
print(numbers[::2])
print(numbers[::-1]) 
print(numbers[::3])

#iternating over list
for number in numbers:
    print(number)

for index,number in enumerate(numbers):
    print(index,number)

#list comprehensive
lst=[]
for x in range(10):
    lst.append(x**2)
    print(lst)


#basic list comprehensive
lst = [x**2 for x in range(10)]
print(lst)

cube=[x**3 for x in range(10)]
print(cube)

#list comprehensive with condition
lst=[]
for i in range(10):
    if i%2==0:
        lst.append(i)
        print(lst)

even_list=[num for num in range(10) if num%2==0]
print(even_list)

#nested comprehension
lst1=[1,2,3,4]
lst2=['a','b','c','d']
pair=[[i,j]for i in lst1 for j in lst2]
print(pair)

#list comphensive
words=["hello","world","rehanalam","nested"]
length=[len(word) for word in words]
print(length)