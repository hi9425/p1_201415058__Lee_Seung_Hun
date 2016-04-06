def main():
	sum=0
	for i in range(1,1001):
		if(i%3==0 or i%5==0):
			sum=sum+i
	print sum
main()
import turtle
wn=turtle.Screen()
wn.exitonclick()
