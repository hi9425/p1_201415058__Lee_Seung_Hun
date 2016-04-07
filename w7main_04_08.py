"""
@author LeeSeungHUn
@since 201415058
"""


def UpDown():
	import random
	ai = input("choice  range  ")
	r1 = random.randrange(1,ai+1)
	global pl
	print "Start!"


	def game():
	    pl = input("choice number")
	    if (r1>pl):
	        result = "Up"
	        print result
	        game()
	    elif (r1<pl):
	        result = "Down"
	        print result
	        game()
	    else :
	        result = "Correct"
	        print result
        	if (result=="Correct"):
	            wn = raw_input("congratulation ")
	game()

"""

@startuml
title Up n Down Game
start
:Player : 범위선택;
:Computer AI : 범위 안의 숫자 선택;
:시작;
:숫자 입력; 
while(플레이)
if (숫자 비교) then (Plater N < AI N)
:Up;
else (Player N > AI B)
:Down;
endif
endwhile
:Player N = AI N;
:"축하";
:끝;
stop
@enduml

"""

	
def main():
    UpDown()

if __name__=="__main__":
    main()