# initializing list
list=[]

# sum of values from the list
list=[1,2,3,4,5]
print(list[0])
total=(list[0]+list[1]+list[3])
print(total)

# adding single elements to the end of the list using "append"

list.append(10)
print(list)

# margin another list to the end using "extend"
l=[15,20]
list.extend(l)
print(list)

# inserting elements x in i position using "insert"
list.insert(5,3)
print(list)

# remove the first occurrence of the elements using "remove"
list.remove(3)
print(list)

# remove the last elements from the list using "pop"
list.pop()
print(list)

# give the index value from a list "index"
t=list.index(4)
print(t)

# count the number of occurrence in the list "count"
count=list.count(2)
print(count)

# sort the list "sort"
list.sort()
print(list)
# reversing the list "reverse"
list.reverse()
print(list)
