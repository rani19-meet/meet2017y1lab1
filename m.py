import turtle


#Everything that comes after the # is a comment.
#It is a note to yje person reading the code.
#the computer ignores it.
#Write  your code below here...



#...and end it before the next line.
turtle.penup() #Pick up the pen so it doesn't draw
turtle.goto(-200,-100) #Move the turtle to the
#position, -200, -100,
#on
#the screen
turtle.pendown() #Put the pen down to start
#drawing
#Draw the M:
turtle.goto(-200,-100+200)
turtle.goto(-200+50,-100)
turtle.goto(-200+100,-100+200)
turtle.goto(-200+100,-100)
#Draw the E:
turtle.penup()
turtle.goto(-50,-100)
turtle.pendown()
turtle.goto(-50,100)
turtle.goto(+50,+100)






turtle.mainloop()
