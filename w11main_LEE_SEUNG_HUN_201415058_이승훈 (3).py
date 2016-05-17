import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

wn.bgpic("bg.GIF")

t1.goto(-211,120)
t1.clear()
def mousegoto(x,y):
	t1.penup()
	t1.write(t1.pos())
	t1.setpos(x,y)


def addMouse():
	wn.onclick(mousegoto)


addMouse()

wn.listen()
turtle.mainloop()