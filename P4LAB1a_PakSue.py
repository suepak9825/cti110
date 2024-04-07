import turtle

t = turtle.Turtle()
t.speed(0)

for _ in range(4):
    t.forward(100)
    t.left(90)

t.penup()
t.goto(-50, -100)
t.pendown()

for _ in range(3):
    t.forward(100)
    t.left(120)

turtle.done()
