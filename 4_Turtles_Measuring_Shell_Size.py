#Name: Thomas Marr Date:09/06/2020 Brief Description: 4 turtles measuring shell size

import turtle, random #uses turtle and random library
wn = turtle.Screen() #creates graphics window
wn.bgcolor("lightgreen") #Unit 3 New Function: changes background color to light green

side_one = 60 #variable used several times
side_two = 150 #variable used twice
leonardo = turtle.Turtle()#creates turtle named leonardo
leonardo.color("blue") #creates leonardo's color (blue) 
leonardo.pensize(random.randrange(0,11)) #Unit 3 New Function: changes leonardo's pen size to random number between 0 and 10
for size in range(2): #for loop creates leonardo's diamond
    leonardo.left(side_one)
    leonardo.forward(side_one) 
    leonardo.left(side_one)
    leonardo.forward(side_one)
    leonardo.left(side_one)

michaelangelo = turtle.Turtle() #creates turtle named michaelangelo
michaelangelo.color("orange") #creates michaelangelo's color (orange)
michaelangelo.pensize(random.randrange(0,11)) #Unit 3 New Function: changes michaelangelo's pen size to random number between 0 and 10
for size in range(2): #for loop creates michaelangelo's diamond
    michaelangelo.right(side_one)
    michaelangelo.forward(side_one) 
    michaelangelo.right(side_one)
    michaelangelo.forward(side_one)
    michaelangelo.right(side_one)
    
raphael = turtle.Turtle() #creates turtle named raphael
raphael.color("red") #creates raphael's color (red) 
raphael.pensize(random.randrange(0,11)) #Unit 3 New Function: changes raphael's pen size to random number between 0 and 10
for size in range(1): #for loop creates raphael's diamond
    raphael.right(side_two)
    raphael.forward(side_one) 
    raphael.right(side_one)
    raphael.forward(side_one)
    raphael.right(120)
    raphael.forward(side_one)
    raphael.right(side_one)
    raphael.forward(side_one)
    
donatello = turtle.Turtle() #creates turtle named donatello
donatello.color("purple") #creates donatello's color (purple)
donatello.pensize(random.randrange(0,11)) #Unit 3 New Function: changes donatello's pen size to random number between 0 and 10
for size in range(2): #creates donatello's diamond
    donatello.left(30)
    donatello.forward(side_one) 
    donatello.right(side_one)
    donatello.forward(side_one)
    donatello.right(side_two)