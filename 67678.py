def draw_square(t, size):
    '''draws a square of side length size'''
    for i in range(4):
        t.forward(size)
        t.left(90)


# test suite
import turtle

wn = turtle.Screen()
alex = turtle.Turtle()
draw_square(alex, 100)

alex.forward(10)
alex.left(90)
alex.penup()
alex.forward(10)
alex.right(90)
alex.pendown()
draw_square(alex, 80)

alex.forward(10)
alex.left(90)
alex.penup()
alex.forward(10)
alex.right(90)
alex.pendown()
draw_square(alex,60)

alex.forward(10)
alex.left(90)
alex.penup()
alex.forward(10)
alex.right(90)
alex.pendown()
draw_square(alex,40)

alex.forward(10)
alex.left(90)
alex.penup()
alex.forward(10)
alex.right(90)
alex.pendown()
draw_square(alex,20)



wn.mainloop()
