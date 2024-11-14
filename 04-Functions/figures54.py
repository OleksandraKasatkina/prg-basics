###
# Draw a square
#

import turtle

def draw_square(length):
    pen = turtle.Turtle()
    pen.speed(5)
    
    for i in range(4):
        pen.forward(length)
        pen.right(90)
    
    pen.hideturtle()  
