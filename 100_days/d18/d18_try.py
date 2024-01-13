######## Challenge 1 - Draw a Square ############
import turtle as t

timmy_the_turtle = t.Turtle()

for _ in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(90)

tim1 = t.Turtle()

########### Challenge 2 - Draw a Dashed Line ########

timmy_the_turtle.right(90)

for _ in range(15):
    tim1.forward(10)
    tim1.penup()
    tim1.forward(10)
    tim1.pendown()

import random

########### Challenge 3 - Draw Shapes ########
tim = t.Turtle()
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3, 10):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)


########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
tim1.pensize(15)
tim1.speed("fastest")

for _ in range(200):
    tim1.color(random.choice(colours))
    tim1.forward(30)
    tim1.setheading(random.choice(directions))

t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

########### Challenge 5 - Spirograph ########

tim.right(180)
tim.forward(300)
tim.right(90)
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)


