#sets:-sets are a build in data type in python used to store in unique colletion of items.
#  sets are unorderd elements that meaans do not follow a specific order and do not allow duplicate element

my_sets={1,2,3,4}
print(type(my_sets))
print(my_sets)

my_empty_sets=set()
print(my_empty_sets)
print(type(my_empty_sets))

my_empty_sets=set([1,2,3,4,5,6])
print(my_empty_sets)

#basic sets operations
#adding and removing elements
my_sets.add(7)
print(my_sets)

my_sets.remove(7)
print(my_sets)

#diacard is a method to remove to set item if it is present else not present it doesnot get any error
# thats means discard helps to check the element will present or not
my_sets.discard(3)
print(my_sets)

##pop method:-thats method helps to remove first element and also show specific removing element
removed_element=my_sets.pop()
print(removed_element)
print(my_sets)

#clear all element
my_sets.clear()
print(my_sets)

#set membership test
my_sets={1,2,3,4,5,6}
print(3 in my_sets)
print(8 in my_sets)

##mathematical operation
set1={1,2,3,4,5,6}
set2={3,4,5,6,7,8}

#union:-means add to each other without common element in same row
union_set=set1.union(set2)
print(union_set)

#intersection set:- means shows commom element thst show in different row
intersection_set=set1.intersection(set2)
print(intersection_set)

##intersection update
set1.intersection_update(set2)
print(set1)

#difference 
set1={1,2,3,4,5,6}
set2={3,4,5,6,7,8}
print(set1.difference(set2))

#symmertric difference
set1.symmetric_difference(set2)
print(set1)

set2.symmetric_difference(set1)
print(set2)

#issubset and issuperset:-means all elements of set1 are present in set2 that show true either false
print(set1.issubset(set2))
print(set1.issuperset(set2))

#how to convert from any to sets
lst_element=[1,2,3,4,4,5,6,6,7,7,7,7]
set_element=set(lst_element)
print(set_element)

##convert list of word to set to get unique word
text="this is the property of rkhan"
words=text.split()

unique_word=set(words)
print(unique_word)
print(len(unique_word))


