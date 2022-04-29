import turtle
turtle.speed(0)
turtle.bgcolor("black")
for i in range(15):
    for colors in("red", "magenta", "blue", "cyan", "green", "yellow"):
        turtle.color(colors)
        turtle.pensize(3)
        turtle.right(4)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
