# # Printing the individual character's
# print("Hello"[1])
#
# # adding string and intiger value in a sentence
# name=input("what is your name: ")
# new_char=str(len(name))
# print("Your name has "+new_char+" characters")
#
# # write a program that adds the digits in a 2 digits number
# number=input("Enter a two digit number: ")
# first_digit=int(number[0])
# second_digit=int(number[1])
# result=first_digit+second_digit
# print(result)
#
# # BMI Calculator
# height=float(input("enter your height in m: "))
# weight=float(input("enter your weiht in kg: "))
#
# bmi=weight/height**2
# print(bmi)
result=4/2
result /=2
print(result)

score=0
score +=2
print(score)

# using f-string
print(f"your score is {score}, your result is {result}")

# creat a program and tell how many days,weeks,months you have left if we life until 90 years old
your_age=int(input("What is you current age: "))
years_remaining=90-your_age
days=years_remaining*365
weeks=years_remaining*52
months=years_remaining*12

print(f"You have {days} days,{weeks} weeks and {months} months left")