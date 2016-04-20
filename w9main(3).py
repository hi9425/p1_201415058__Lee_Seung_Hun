def st():
    import turtle
    wn=turtle.Screen()
    t1=turtle.Turtle() 
    t1.speed(3)
    t1.penup()
    mytracks=list()
    t1.goto(-400,400)
    t1.pendown()
    t1.setheading(0)
    t1.fd(100)
    mytracks.append(t1.pos())
    t1.right(90)
    t1.fd(100)
    mytracks.append(t1.pos())
    t1.left(90)
    t1.fd(100)
    mytracks.append(t1.pos())
    t1.right(90)
    t1.fd(300)
    mytracks.append(t1.pos())
    t1.left(90)
    t1.fd(300)
    mytracks.append(t1.pos())
    t1.left(90)
    t1.fd(100)
    mytracks.append(t1.pos())
    t1.right(90) 
    t1.fd(100)
    mytracks.append(t1.pos())
    t1.right(90)
    t1.fd(350)
    mytracks.append(t1.pos())
    return mytracks


def replayTracks(mytracks):
    for i in mytracks:
        print i
        

def lab7():
    mytracks=st()
    replayTracks(mytracks)
    

def main():
    lab7()
if __name__=="__main__":
    main()