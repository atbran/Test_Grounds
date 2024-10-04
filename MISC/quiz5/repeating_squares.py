import turtle as t
t.speed(0)
t.hideturtle()
size = 10
for i in range(100):
    t.penup()
    #for my screen size, I had to use these weird values to get the squares to fit
    #if I had more time, I would calculate the screen size and use that instead
    t.goto(415, -390)
    t.pendown()

    for j in range(4):
        t.left(90)
        t.forward(size)
    size += 10

t.done()