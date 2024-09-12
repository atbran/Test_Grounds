#I do not know how to spell blud's name
# Create Screen
# Select Bounds
# Draw Triangle
# Shrink bounds
# recursively call draw triangle


import numpy as np
import turtle as t



def draw_triangle(p1,p2,p3):
    #x,y is for the center of the triangle
    # somehow convert center of triangle into places where the edges can rest.

    """
    Draws a triangle with vertices at p1, p2, p3.
    p1, p2, p3 are tuples (x, y).
    """
    t.penup()
    t.goto(p1)  # Go to the first point
    t.pendown()

    # Draw the triangle
    t.goto(p2)
    t.goto(p3)
    t.goto(p1)  # Close the triangle

def sierpinski(p1,p2,p3,depth):
    if depth == 0:
        draw_triangle(p1,p2,p3)
    else:
        mid1 = midpoint(p1, p2)
        mid2 = midpoint(p2, p3)
        mid3 = midpoint(p1, p3)

        sierpinski(p1,mid1,mid3,depth-1)
        sierpinski(mid1,p2,mid2,depth-1)
        sierpinski(mid3,mid2,p3,depth-1)
    pass

def midpoint(p1,p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)


def main():
    t.hideturtle()
    t.speed(0)
    p1 = (-400, -200)
    p2 = (0, 400)
    p3 = (400, -200)

    depth = 1
    for i in range(8):

        sierpinski(p1,p2,p3,depth)
        depth += 1

    t.update()
    t.done()

main()


