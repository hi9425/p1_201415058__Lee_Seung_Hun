import turtle

wn=turtle.Screen()

t1=turtle.Turtle()


def BMI():
    weight=raw_input("input your weight : ")
    height=raw_input("input your Height : ")
    weight=float(weight)
    height=float(height)
    bheight=height/100
    bmi=weight/(bheight*bheight)
    if(bmi<18.5):
        print "low weight"
    elif(18.5<=bmi<25):
        print"nomal"
    elif(25<=bmi<30):
        print "middle obesity"
    elif(30<=bmi):
        print "high obesity"
    else:
        print "Error"

    t1.write("승훈 과제 끝")


BMI()
def main():
	BMI()


wn.exitonclick()

