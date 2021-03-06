x=int(input("Enter any positive integer from 1 to 12: "))
n=int(input("Enter any positive integer from 0 to 59: "))
import turtle
myPen = turtle.Turtle()
wn = turtle.Screen()
myPen.speed(0)
myPen.left(90)
myPen.penup()
for i in range(1,13):
    myPen.right(30)
    myPen.forward(100)
    myPen.stamp()
    myPen.back(100)
angle=6*n
myPen.right(angle)
myPen.pendown()
myPen.forward(75)
myPen.stamp()
myPen.back(75)
myPen.left(angle)
smallAngle=30*x+n/2
myPen.right(smallAngle)
myPen.forward(50)


wn.mainloop()

