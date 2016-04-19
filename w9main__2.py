import turtle

wn=turtle.Screen()

t1=turtle.Turtle()

t1.shape("turtle")

c=dict()

c=({0:(0,0),1:(200,0),2:(200,200),3:(0,200),4:(0,0)})

def lab7():
    for i in range(1,5):
        t1.goto(c[i])
    for k in range(1,5):
        print c[k]

def main():
    lab7()

if __name__=="__main__":
    main()

wn.exitonclick()