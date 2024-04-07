import turtle

t = turtle.Turtle()
t.speed(0)
t.penup()

t.color("pink")
t.pensize(3)

t.goto(-100,0)
t.pendown()

t.forward(40)
t.circle(50, 180)
t.circle(-50, 180)
t.forward(40)
t.penup()

t.goto(50,0)
t.pendown()

t.left(90)
t.forward(200)
t.right(90)
t.circle(-50, 180)
t.penup()

t.hideturtle()

turtle.done()
