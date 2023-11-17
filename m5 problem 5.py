#Julian Ruiz
#10/27/23

#Program that creates a smiling face

import turtle

# Create a turtle screen
screen = turtle.Screen()
screen.bgcolor("lightblue")  # Set the background color

# Create a turtle object
smiley = turtle.Turtle()
smiley.speed(1)  # Set the drawing speed (1 is slowest)

# Draw the head (a yellow circle)
smiley.color("yellow")
smiley.begin_fill()
smiley.circle(100)
smiley.end_fill()

# Draw the left eye (a white circle)
smiley.penup()
smiley.goto(-40, 120)
smiley.pendown()
smiley.color("white")
smiley.begin_fill()
smiley.circle(20)
smiley.end_fill()

# Draw the right eye (a white circle)
smiley.penup()
smiley.goto(40, 120)
smiley.pendown()
smiley.color("white")
smiley.begin_fill()
smiley.circle(20)
smiley.end_fill()

# Draw the left eye (a black dot)
smiley.penup()
smiley.goto(-20, 130)
smiley.pendown()
smiley.color("black")
smiley.begin_fill()
smiley.circle(10)
smiley.end_fill()

# Draw the right eye (a black dot)
smiley.penup()
smiley.goto(20, 130)
smiley.pendown()
smiley.color("black")
smiley.begin_fill()
smiley.circle(10)
smiley.end_fill()

# Draw the mouth (a semi-circle)
smiley.penup()
smiley.goto(-50, 80)
smiley.pendown()
smiley.setheading(-60)
smiley.color("black")
smiley.pensize(3)
smiley.circle(60, 120)

# Close the window when clicked
screen.exitonclick()