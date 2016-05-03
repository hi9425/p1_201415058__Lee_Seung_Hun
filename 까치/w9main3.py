word='kor2aAnimatiom2highSchool2lL'
words=word.split()
d=dict()
wcount=0
ncount=0
for c in word:
        if c not in d:
            d[c]=1
            print d
        else:
            d[c]=d[c]+1
for i in d:
    if i.isdigit()and d[c]==1:
        ncount=ncount+1
    elif i.isdigit()and d[c]==2:
        ncount=ncount+2    
    elif i.isalpha()and d[c]==1:
        wcount=wcount+1
    elif i.isalpha()and d[c]==2:
        wcount=wcount+2
    elif i.isalpha()and d[c]==3:
        wcount=wcount+3
    else:
        wcount=wcount
        ncount=ncount
print wcount
print ncount
input()