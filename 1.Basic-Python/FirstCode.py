#dictionaries
#dictionaries are unorderd collection item they store data in key value pairs.
# keys must be unique and immutable(eg:-string number or tuples)while value can be on any type

#creating a empty dictionaries
empty_dict={}
print(type(empty_dict))

#single key always used
student={"name":"rehan","age":"19","height":"5.8"}
print(student)

#accesing dictionary element
print(student["age"])
print(student["name"])
print(student["height"])

#also accessing using get()
print(student.get("name"))
print(student.get("rehan")) ##none value

#dictionaries are modifying element
#dictionaries are mutable item so i you can add and update or delete elements

student["age"]=19 #it helps to update value
print(student)
student["address"]="ranchi" # it can used to add value
print(student)

#del - it helps to delete keys and pair value
del student["name"]
print(student)

#dictionaries method
keys=student.keys()
print(keys)

values=student.values()
print(values)

items=student.items()
print(items)

#shallow copy
student_copy=student
print(student)
print(student_copy)

student["name"]="rehan1"
print(student)
print(student_copy)

student["name"]="rehan2"
print(student)
print(student_copy)

student_copy1=student.copy()
print(student_copy1)
print(student)

student["name"]="rehan3"
print(student)
print(student_copy1)

#itersting over dictionaries
#you can use to loop to iterate over dictionaries,keys ,values or items

#iterating over keys
for keys in student.keys():
    print(keys)

#iterate over values
for value in student.keys():
    print(values)

#iterating over key value pairs
for keys,values in student.items():
    print(f"{keys}:{values}")

#nested dictionaries
students={
    "student1":{"name":"rehan","age":19,"height":5.8},
    "student2":{"name":"sohail","age":19,"height":5.7}
}
print(students)

#access nested dictionaries elements
print(students["student2"]["age"])
print(students["student2"]["height"])

#iterating over nested dictionaries
for student_id,student_info in students.items():
    print(f"{student_id}:{student_info}")
    for keys,values in student_info.items():
        print(f"{keys}:{values}")

#dictionaries comprehension
student={x:x**2 for x in range(6)}
print(student)

#conditon dictionaries comprehension
even={x:x**2 for x in range(10) if x%2==0}
print(even)

### SOME PRACTICAL EXAMPLES
#use a dictionaries to count it frrequency of element in list

numbers=[1,2,2,3,3,3,4,4,4,4]
frequency={}

for number in numbers:
    if number in frequency:
        frequency[number]+1
    else:
        frequency[number]=1
print(frequency)

#merge two dictionaries into one
dict1={"a":1,"b":2}
dict2={"a":3,"c":4}
merge_dict={**dict1,**dict2}
print(merge_dict)