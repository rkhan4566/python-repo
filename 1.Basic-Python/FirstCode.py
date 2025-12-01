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