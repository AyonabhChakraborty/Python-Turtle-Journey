import turtle

a = turtle.Turtle()

a.color('blue')
a.begin_fill()
a.forward(100)
a.left(90)
a.forward(100)
a.left(90)
a.forward(100)
a.left(90)
a.forward(100)
a.end_fill()

a.penup()
a.forward(150)
a.pendown()

a.color('red')
a.begin_fill()
a.forward(100)
a.left(90)
a.forward(100)
a.left(90)
a.forward(100)
a.left(90)
a.forward(100)
a.end_fill()


turtle.done()