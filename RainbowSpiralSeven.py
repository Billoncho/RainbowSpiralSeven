# RainbowSpiralSeven
# Billy Ridgeway
# Creates a seven sided rainbow spiral drawn by a turtle.

import turtle           # Imports the turtle library.
t = turtle.Turtle()     # Creats a new pen called t.
t.shape("turtle")       # Makes the pen look like a turtle.
turtle.bgcolor("black") # Sets the background color to black.
t.speed(0)              # Sets the pen's speed to fast.
t.width(4)              # Sets the pen's width to 4 pixels.

# A list of the colors of the rainbow.
colors = ["red", "orange", "yellow", "green", "blue",
          "indigo", "violet"]

for r in range(200):        # Sets the range of r to 200.
    t.pencolor(colors[r%7]) # Cycles repeatedly through the rainbow's colors.
    t.forward(r)            # Moves the pen forward by the value contained in r.
    t.left(360/7 + 1)       # Moves the pen left by 360 degrees divided by 7 + 1.
