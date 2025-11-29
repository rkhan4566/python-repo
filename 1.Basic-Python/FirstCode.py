#tuples
#create a empty tuples
numbers=1,2,3,4,5,6
empty_tuple=()
print(empty_tuple)
print(type(empty_tuple))

lst=list()
print(type(lst))
tpl=tuple()
print(type(tpl))

mixed_tuple=(1,2,"rehan",3.14)
print(mixed_tuple)

#silicing and accessing index are similar as list 
#operation of tuples
concatenation_tuples=numbers+mixed_tuple
print(concatenation_tuples)

mixed_tuple * 3
print(mixed_tuple)

#tuples are immutable
numbers=1,2,3,4,5,6
numbers=[2]="krish"
print(numbers)

#tuples method
numbers=1,2,3,4,5,6
print(numbers.count(1))
print(numbers.index(4))

#packing and unpcking tuples
#packing
packed_tuple=(1,2,"rehan",4,3.14)
print(packed_tuple)


#unpacked tuples
packed_tuple=(1,2,"rehan",4,3.14)
a,b,c,d,e=packed_tuple
print(a)
print(b)
print(c)
print(d)
print(e)

#unpacked tuples with *
numbers=(1,2,3,4,5,6)
first,*middle,last=numbers
print(first)
print(*middle)
print(last)

#nested tuple
#nested list
lst=[[1,2,3],[4,5,6],[7,"rehan",3.14]]
lst[0:1]
print(lst)

#access the elements inside a tuple
nested_tuple=[[1,2,3],[4,5,6],[3.14,"rehan","c"]]
print(nested_tuple[0])
print(nested_tuple[2][2])

#iterate over nested tuple
nested_tuple=[[1,2,3],[4,5,6],[3.14,"rehan","c"]]
for sub_tuple in nested_tuple:
    for item in sub_tuple:
        print(item," ")
        print()

