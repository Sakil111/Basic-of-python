# List comprehension
# Add n number of digit in matrix and create n number of matrix
x=int(input("Enter you number: "))
y=int(input("Enter you number: "))
z=int(input("Enter you number: "))
n=int(input("Enter you number: "))

print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k !=n])


# finding second height value
n = int(input())
arr = [2,3,6,6,5]
new_list=set(arr)
new_list.remove(max(new_list))
print(max(new_list))

# nested list
python_students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
print(python_students[1][0])
for inner in python_students:
    for value in inner:
        print(value)

# find the second largest value
python_students = [['Harry', 35.21], ['Berry', 37.2], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
minimum_score=min([x[1] for x in python_students])
python_students=[x for x in python_students if x[1]>minimum_score]
second_minimum=min([x[1] for x in python_students])
python_students=sorted([x for x in python_students if x[1]==second_minimum])
for student in python_students:
    print(student[0])


