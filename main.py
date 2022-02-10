import turtle as t
import random
from turtle import Turtle, Screen
from random import choice



from random import randint

timmy = Turtle()
timmy.pensize(3)
timmy.speed(0)

t.colormode(255)

# for shape_sides in range(3, 11):
#     shapes(shape_sides)
#     sides +=
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    chosen_color = (r, g, b)
    return chosen_color




def direction(directionchoice):
    if directionchoice == 0:
        timmy.forward(20)
    elif directionchoice == 1:
        timmy.right(90)
        timmy.forward(20)
    elif directionchoice == 2:
        timmy.right(180)
        timmy.forward(20)
    elif directionchoice == 3:
        timmy.right(270)
        timmy.forward(20)


for _ in range(10000):
    directionchoice = randint(0, 4)
    direction(directionchoice)
    timmy.color(random_color())



screen = Screen()
screen.exitonclick()

######## Challenge 1 - Draw a Square ############