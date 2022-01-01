# def greet():
#     print("Hello")
#     print("welcome")
#     print("Goodby")
# greet()

# # Parameter is the name of the argument in a function
# # function with input
# def greeting_with_name(name):
#     print(f"Hello {name}")
#     print(f"Welcome {name}")
#
# greeting_with_name("sakil")

# # function with multiple aurgument
# def greet_with(name,location):
#     print(f"Hello {name}")
#     print(f"What is like in {location}")
# greet_with(location="sakil",name="America")

# # calculate the number of cans need in a given area
# wall_height=int(input("What is the wall height: "))
# wall_width=int(input("What is the wall width: "))
# coverage=int(input("What is the wall coverage: "))
# def elements(height,width,coverage):
#     number_of_cans=round((wall_height*wall_width)/coverage)
#     print(f"you will need {number_of_cans} cans for painting")
# elements(height=wall_height,width=wall_width,coverage=coverage)

# Prime number checker
n=int(input("Check the number: "))
def prime_checker(number):
    is_prime=True
    for i in range(2,number-1):
        if number %i ==0:
            is_prime=False
    if is_prime:
        print("It is a prime number")
    else:
        print("It is not a prime number")
prime_checker(number=n)