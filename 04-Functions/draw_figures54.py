import turtle
from figures54 import draw_square

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Side length
side_length = 100

# Draw a square
draw_square(side_length)

window.mainloop()