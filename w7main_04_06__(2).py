"""
@author 이승훈
@since 04_06
"""
def hun():

    year=input("input the year")


    if(year%4==0) and (year%100!=0 or year%400==0):
        print"leap year"
    else:
        print"not leap year"
hun()
import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
t1.write("윤년")
wn.exitonclick()

"""
repeat

start
:input year;
if(year%4==0)and(year%100!=0 or year%400==0)
:print leap year;
else(fales)
:print not leap lear;
endif
stop


 

"""

def main():
     hun()
