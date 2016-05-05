import math
l=tuple()
l=[(74425,76326),(61164,61636),(109688,115744),(144796,146776),(174996,181676),(177841,177434),(204630,205980),(223373,232245),(161055,166130),(171576,176735),(279169,293772),(239450,251066),(148690,156510),(182977,196992),(237792,242641),(283869,296762),(209344,210282),(118965,114441),(186503,186856),(195734,203014),(254381,249472),(212401,229111),(271654,295354),(319197,335045),(229829,231671)]
len(l)
sum=0
sum1=0
sum2=0
people=list()
for q in l:
    sum=sum+q[0]
    sum1=sum1+q[1]
    sum2=q[0]+q[1]
    people.append(sum2)
print sum
male= sum/len(l)
print "average seoul is %s"%male
print sum1
female=sum1/len(l)
print "average seoul is %s"%female
import matplotlib
import matplotlib.pyplot as plt
print people
lsh=dict()
plt.bar(range(len(people)),people,align='center')
plt.show()