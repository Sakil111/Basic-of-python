# # find out the average height using for loop
# student_height=input("Input the list of student height: ").split()
# for n in range(0,len(student_height)):
#     student_height[n]=int(student_height[n])
# print(student_height)
# total_height=0
# for n in student_height:
#     n+=total_height
#     total_height=n
# number_of_items=0
# for item in student_height:
#     number_of_items+=1
#
# average=total_height/number_of_items
# print(average)

# # find out the height score in a list
# student_score=input("Input the list of students score: ").split()
#
# for n in range (0,len(student_score)):
#     student_score[n]=int(student_score[n])
# print(student_score)
# height_score=0
# for score in student_score:
#     if score>height_score:
#         height_score=score
# print(height_score)

# # adding 1-100
# total=0
# for number in range(1,101):
#     total+=number
#
# print(total)
# # adding all the even number
# total=0
# for number in range(2,101,2):
#     total+=number
# print(total)
#
# total1=0
# for number in range(1,101):
#     if number%2==0:
#         total1+=number
# print(total1)

# Creating Fizz buzz problem

for number in range(1,101):
    if number%3==0 and number%5==0:
        print("Fizz Buzz")
    elif number%5==0:
        print("Buzz")
    elif number%3==0:
        print("Fizz")
    else:
        print(number)


