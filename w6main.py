def main():
	print "Welcome to the Battle World please input the Rock,Scissor,Papaer"
	p1=raw_input("you have to only r s p:  ")
	p2=raw_input("also you have to only r s p: ")
	def subtool(p):
		if(p=='r'):
			return 4.0
		elif(p=='s'):
			return 6.0
		elif(p=='p'):
			return 9.0
		else:
			print "Input Error"        

        alpha=subtool(p1)-subtool(p2)
	if(alpha==3):
		print "p1 you win!!"
	elif(alpha==5):
		print "p1 you win!!"
	elif(alpha==0):
		print "draw :)"
	elif(alpha==-2):
		print "p2 you win!!"
	elif(alpha==-5):
		print "p2 you win!!"
	
main()
import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
t1.write("승훈이의 과제 끝!")
wn.exitonclick()