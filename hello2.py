import turtle
myPen = turtle.Turtle()
myPen.speed(0)
myPen.color("black")
side=200
for i in range (1,20):
   myPen.forward(side)
   myPen.left(90)
   side=side-10
