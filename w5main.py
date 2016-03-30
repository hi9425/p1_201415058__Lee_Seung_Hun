import turtle

wn=turtle.Screen()

t1=turtle.Turtle()

marks = raw_input("input 0~100 :")
def Convermarksgrade(marks):
    if 90<=float(marks)<=100:
        grade="A 매우 잘하시네용"
    elif 80<=float(marks)<90:
        grade="B 잘하시네용"
    elif 70<=float(marks)<80:
        grade="C 애매하네용"
    elif 60<=float(marks)<70:
        grade="D 재수강 어떠세용"
    else:
        grade="재수강 하세용 "
    return t1.write(grade)
result=Convermarksgrade(marks)
print "your grade  %s " %result

wn.exitonclick()