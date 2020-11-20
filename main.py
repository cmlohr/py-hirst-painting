from turtle import Turtle, Screen
import random
import turtle as t

t.setworldcoordinates(-1, -1, 10, 10)
tom = t.Turtle()
tom.shape("circle")
tom.speed("fast")
t.colormode(255)
tom.pensize(20)
tom.hideturtle()


picked_colors = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123),
                 (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35),
                 (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
                 (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102),
                 (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]


def color_changer():
    choice = random.choice(picked_colors)
    tom.fillcolor(choice)
    tom.pencolor(choice)
    return choice


def dots(tom, num_dots, dot_length):
    for i in range(num_dots):
        tom.penup()
        tom.color(color_changer())
        tom.dot(20)
        tom.forward(dot_length)


row = 0
while row != 10:
    row += 1
    dots(tom, 10, 1)
    tom.setpos(0, row)









screen = Screen()
screen.exitonclick()
