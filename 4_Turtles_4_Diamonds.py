#Name: Thomas Marr Date:08/25/2020 Brief Description: 4 turtles, 4 diamonds

import turtle #uses turtle library
wn = turtle.Screen() #creates graphics window
side_one = 60 #variable used several times
side_two = 150 #variable used twice
leonardo = turtle.Turtle()#creates turtle named leonardo
leonardo.color("blue") #creates leonardo's color (blue) 
for size in range(2): #for loop creates leonardo's diamond
    leonardo.left(side_one)
    leonardo.forward(side_one) 
    leonardo.left(side_one)
    leonardo.forward(side_one)
    leonardo.left(side_one)

michaelangelo = turtle.Turtle() #creates turtle named michaelangelo
michaelangelo.color("orange") #creates michaelangelo's color (orange) 
for size in range(2): #for loop creates michaelangelo's diamond
    michaelangelo.right(side_one)
    michaelangelo.forward(side_one) 
    michaelangelo.right(side_one)
    michaelangelo.forward(side_one)
    michaelangelo.right(side_one)
    
raphael = turtle.Turtle() #creates turtle named raphael
raphael.color("red") #creates raphael's color (red) 
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
for size in range(2): #creates donatello's diamond
    donatello.left(30)
    donatello.forward(side_one) 
    donatello.right(side_one)
    donatello.forward(side_one)
    donatello.right(side_two)