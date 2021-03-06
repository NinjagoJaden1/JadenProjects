import turtle
wn = turtle.Screen()
alex = turtle.Turtle()
n=int(input("Enter any odd number: "))
for i in range (0,n):
    alex.forward(100)
    angle= 180-(180/n)
    alex.left(angle)


wn.mainloop()