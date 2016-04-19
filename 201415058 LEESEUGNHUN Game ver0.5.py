import turtle
wn=turtle.Screen()
d1=turtle.Turtle()
wn.bgcolor("Lightpink")
size=100

def Triangle():
 d1.penup()
 d1.goto(0,0)
 d1.pendown()
 for i in range(0,3):
  d1.fd(100)
  d1.right(120)
  d1.write("게임 타이틀")

def Triangle2():
 d1.penup()
 d1.goto(-200,0)
 d1.pendown()
 d1.write("방1")
 for i in range(0,3):
  d1.fd(100)
  d1.right(120)
  

Triangle()
Triangle2()

d1.penup()




from turtle import *

move = Turtle()
move.shape("turtle")
showturtle()
move.penup()

def k1():
    move.forward(45)

def k2():
    move.left(45)

def k3():
    move.right(45)

def k4():
    move.back(45)


onkey(k1, "Up")
onkey(k2, "Left")
onkey(k3, "Right")
onkey(k4, "Down")

listen()
mainloop()