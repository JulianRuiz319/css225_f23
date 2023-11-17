#Julian Ruiz
#10/27/23

#creating a polygon

import turtle

num_sides = int(input("Enter the number of sides: "))
side_length = int(input("Enter the length of each side: "))
line_color = input("Enter the line color: ")
fill_color = input("Enter the fill color: ")

screen = turtle.Screen()
screen.bgcolor("white")  # Set the background color

polygon = turtle.Turtle()
polygon.color(line_color)
polygon.fillcolor(fill_color)
polygon.begin_fill()

for _ in range(num_sides):
    polygon.forward(side_length)
    polygon.left(360 / num_sides)

polygon.end_fill()

screen.exitonclick()