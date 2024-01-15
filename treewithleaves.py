import turtle


screen = turtle.Screen()


tree = turtle.Turtle()


tree.penup()
tree.setpos(0,-200)
tree.pendom()
tree.left(30)




def draw_branch(branch_length):
    if branch_length < 5:
        return
    else:
        tree.forward(branch_length)


        tree.right(25)
        draw_branch(branch_length - 15)


        tree.left(25)
        