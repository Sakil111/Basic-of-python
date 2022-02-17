# import main
# print(main.another_variable)
from turtle import Turtle,Screen
timmy=Turtle()
timmy.shape("turtle")
timmy.color("red")
timmy.forward(100)

# using attributes of a module
screen=Screen()
print(screen.canvheight)


# using methods of a module
screen.exitonclick()