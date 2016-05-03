home=list()
friend=list()
home=['tv','dslr','camera','phone','2gphone','audio','audiomixer','light','mouse','raptop','gobo']
friend=['HDtv','radiohead','camera','tungsten','ramp','light','raptop','gobo']
print home
print friend
k=friend
k1=set(home)&set(friend)
x1=list()
print k1
for c in friend:
    if c in k and c not in k1:
        x1.append(c)
print "not exist " , x1 
input()