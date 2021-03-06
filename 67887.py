def draw_histogram(t,dataList):
    '''draw_histogram(t,dataList) -> None
    uses turtle t to draw a histogram of dataList
    dataList must contain integers from 0-10'''
    for j in range(4):
        # draw a side of the square
        t.forward(20)
        t.left(90)

    t.penup()
    t.forward(40)
    t.pendown()
    for j in range(4):
        t.forward(20)
        t.left(90)
    t.penup()
    t.forward(40)
    t.pendown()
    for j in range(2):
        t.forward(20)
        t.left(90)
        t.forward(40)
        t.left(90)
    t.penup()
    t.forward(40)
    t.pendown()
    t.forward(20)
    t.penup()
    t.forward(40)
    t.pendown()
    for j in range(2):
        t.forward(20)
        t.left(90)
        t.forward(60)
        t.left(90)
    t.penup()
    t.forward(40)
    t.pendown()
    for j in range(2):
        t.forward(20)
        t.left(90)
        t.forward(60)
        t.left(90)
    t.penup()
    t.forward(40)
    t.pendown()
    for j in range(2):
        t.forward(20)
        t.left(90)
        t.forward(80)
        t.left(90)
    t.penup()
    t.forward(40)
    t.pendown()
    for j in range(2):
        t.forward(20)
        t.left(90)
        t.forward(100)
        t.left(90)
    t.penup()
    t.forward(40)
    t.pendown()
    for j in range(2):
        t.forward(20)
        t.left(90)
        t.forward(60)
        t.left(90)
    t.penup()
    t.forward(40)
    t.pendown()
    for j in range(2):
        t.forward(20)
        t.left(90)
        t.forward(60)
        t.left(90)
    t.penup()
    t.forward(40)
    t.pendown()
    for j in range(2):
        t.forward(20)
        t.left(90)
        t.forward(40)
        t.left(90)
    # add code here

# test suite
import turtle
turtle.setup(600,300) # Change the width of the drawing to 600px and the height to 300px.
wn = turtle.Screen()
bob = turtle.Turtle()
dataList = [6,8,0,7,7,9,2,9,10,4,8,7,6,9,1,4,6,7,5,7,2,10,4,5,5,6,8]
# move bob back a little bit so he has room
bob.penup()
bob.back(200)
bob.pendown()
# draw the histogram
draw_histogram(bob,dataList)
wn.mainloop()