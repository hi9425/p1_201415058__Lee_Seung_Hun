import turtle
import math
import time
wn=turtle.Screen()
t1=turtle.Turtle()
t2=turtle.Turtle()
t2.shape("turtle")
t2.color("lightpink")
t2.penup()
t2.goto(0,-220)
t2.setheading(90)
t1.speed(5)
wn.bgcolor("green")
wn.setup(650,480)
result=0

def OpenCoords():
    filehome=open('position.txt')
    coords=list()
    for line in filehome:
        cirpos=line.split(',')
        coords.append([cirpos[0],cirpos[1], cirpos[2],cirpos[3], cirpos[4],cirpos[5].strip()])
    filehome.close()
    return coords
coords=OpenCoords()


  
	

def square():
    for coord in coords:
        x1=int(coords[0][0])
        x2=int(coords[0][1])
        y1=int(coords[0][2])
        y2=int(coords[0][3])
        x3=int(coords[0][4])
        y3=int(coords[0][5])

    t1.penup()
    t1.goto(x1,y2)
    t1.pendown()
    t1.fillcolor("lightblue")
    t1.begin_fill()
    for i in range(0,4):
        t1.fd(100)
        t1.right(90)

    t1.end_fill()



def Triangle2():
    t1.penup()
    t1.goto(50,0)
    t1.pendown()
    
    t1.fillcolor("red")
    t1.begin_fill()
    for i in range(0,3):
        t1.right(120)
        t1.fd(100)

    t1.end_fill()
        
        
def circle():
    t1.penup()
    t1.goto(240,-200)
    t1.fillcolor("Brown")
    t1.begin_fill()
    t1.pendown()
    t1.circle(50)
    t1.pendown()
    
   
    t1.end_fill()
        
def do():
    square()
    Triangle2()
    circle()

def sq():
    (x,y)=t2.pos()
    global result
    if -300<=x<-200 and 100<=y<=200:
        result=result+1
        print(" point total %d !" % result)
        t2.goto(0,-200)

def tr():
    (x,y)=t2.pos()
    global result
    if 0<=x<150 and 0<=y<=200:
        result=result+3
        print(" point %d !" % result)
        t2.goto(0,-220)
    if 0<=x<150 and -100<=y<=0:
        result=result+3
        print(" point %d !" % result)
        t2.goto(0,-220)



def ci():
    (x,y)=t2.pos()
    global result
    if 150<=x<100 and -150<=y<=-250:
        result=result+2
        print(" point %d !" % result)
        t2.goto(0,-200)
    

    
do()
  

    

    
    
    
def h1():
    t2.forward(10)
    sq()
    tr()
    po()
   
    
   

def h2():
    t2.left(45)

def h3():
    t2.right(45)

def h4():
    t2.back(30)  
 
wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(h4, "Down")
wn.listen()

turtle.mainloop()