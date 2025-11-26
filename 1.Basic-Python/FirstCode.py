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

