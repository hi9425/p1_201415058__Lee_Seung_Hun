x1=list()
def sumlist(alist):
	sum=0
	for i in range(0,1000):
		if i%4==0 and i%5!=0:
			alist.append(i)
	for i in range(0,len(alist)):
		sum=sum+alist[i]
	return sum
print sumlist(x1)

raw_input("finish")