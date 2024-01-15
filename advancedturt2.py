import turtle


a = turtle.Turtle()
a.getscreen().bgcolor('#994444')

a.penup()
a.goto(c)

a.forward(200)
a.left(216)
a.forward(200)
a.left(216)
a.forward(200)
a.left(216)
a.forward(200)
a.left(216)
a.forward(200)
a.left(216)

for i in range(25):
    a.forward(100)
    a.left(216)

#def star(a, size):
# if size <= 10:
# return
# 
# else:
# for i in range(100):
# a.forward(size)
# star(a, size)
# a.left(216)3  



turtle.done()