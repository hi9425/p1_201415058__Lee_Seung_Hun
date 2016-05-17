import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
coord=[(100,100),(200,200)]
curpos=(0,0)
def Rectangle():
    
    t1.setpos(0,-400)
    t1.clear()
    t1.fd(100)
    t1.left(90)
    t1.fd(100)
    t1.left(90)
    t1.fd(100)
    t1.left(90)
    t1.fd(100)
def isInRectangle(curpos,coord):
    if coord[0][0]<curpos[0]<coord[1][0] and coord[0][1]<curpos[1]<coord[1][1]:
        print "In"
    else:   
	print " Out"

def keyup():
    t1.fd(30)
    tp=t1.pos()
    isInRectangle(tp,coord)

def keydown():
    t1.back(30)
    tp=t1.pos()
    isInRectangle(tp,coord)

def keyleft():
    t1.left(30)
def keyright():
    t1.right(30)
def mousegoto(x,y):
    t1.setpos(x,y)
    tp=t1.pos()
    isInRectangle(tp,coord)

def addmouse():
    wn.onclick(mousegoto)

def addkeys():
    wn.onkey(keyup,"Up")
    wn.onkey(keydown,"Down")
    wn.onkey(keyleft,"Left")
    wn.onkey(keyright,"Right")

def game():
    Rectangle()
    addkeys()
    addmouse()
    wn.listen()
    turtle.mainloop()
game()