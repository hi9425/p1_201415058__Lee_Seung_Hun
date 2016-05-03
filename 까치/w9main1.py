word='sangmyung'

mydict=dict()

import matplotlib.pyplot as plt
def lab9():	
	for c in word:
    		if c not in mydict:
        		mydict[c]=1
        		print mydict
    		else:
        		mydict[c]=mydict[c]+1
	print len(mydict)
	print mydict.keys()
	print mydict.values()
	plt.bar(range(len(mydict)), mydict.values() ,)
	plt.xticks(range(len(mydict)),list(mydict.keys()))
	plt.show()
lab8()
