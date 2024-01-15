import turtle
import math
a = turtle.Turtle()
a.color('blue','yellow')
a.speed(10)

a.begin_fill()
for i in range(10000):
    a.forward(math.sqrt(i))
    a.left(i%90)

a.end_fill()


turtle.done