import turtle as t

def draw_triangle(x,y,color):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for i in range(3):
        t.forward(50)
        t.right(120)
    t.end_fill()
    t.done()

draw_triangle(100,200,"red")