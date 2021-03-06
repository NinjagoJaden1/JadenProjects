# Python Class 2231
# Lesson 9 Problem 6
# Author: pokemonJJ (471438)

import turtle

turtle.setup(800,600) # Change the width of the drawing to 800px and the height to 600px.
wn = turtle.Screen()
sammy = turtle.Turtle()
inFile = open('mystery.txt','r')
for aline in inFile:
    items = aline.split()
    if items[0] == "UP":
        sammy.up()
    else:
        if items[0] == "DOWN":
            sammy.down()
        else:
            #must be coords
            sammy.goto(int(items[0]),int(items[1]))


# you need to fill in the code
inFile.close()
