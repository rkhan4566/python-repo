#manage a to do list
#create a to do list to keep track off task

to_do_list=["buy groceries","clean house","pay bills"]
#adding task
to_do_list.append("schedule meeting")
to_do_list.append("go for run")

#remove a completed task
to_do_list.remove("clean house")

#checking if a task is in a list
if "pay bills" in to_do_list:
    print("don't forget utility bills")

print("to do list remaining")
for task in to_do_list:
    print(f"-{task}")

#organizing student grades
grades=[99,98,97,96,94,93]

#adding a new grade
grades.append(95)

#calculating the average of grade
avg_grades=sum(grades)/ len(grades)
print(f"avg_grades:{avg_grades:.2f}")

#finding a highest and lowest grades
highest_grade=max(grades)
lowest_grade=min(grades)
print(f"highest grades:{highest_grade}")
print(f"minimum_grades:{lowest_grade}")



#use a list to manage inventoty items
#managing a inventory
inventory=["apples","banana","guava","litchi"]

#adding a new item in inventory
inventory.append("strawberry")

#removing a out of stock item
inventory.remove("banana")

#check item if an is in a stock
item="apple"
if item in inventory:
    print(f"{item} are out of stock.")
else:
    print(f"{item} are in there stock.")

print("inventory list")
for item in inventory:
    print(f"-{item}")


#use a list to analyze your feedback
#collecting your feedback
feedback=["great service","full satisfied","perfect teaching","excellent work"]

#adding a new feedback
feedback.append("not happy with the services")

#counting a specific feedback
positive_feedback_count= sum(1 for comment in feedback if "great" in comment.lower() or "excellent" in comment.lower())

print(f"positive feedback count: {positive_feedback_count}")

print("user feedback:")
for comment in feedback:
    print(f"-{comment}")







