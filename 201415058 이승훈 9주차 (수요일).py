﻿Locations=tuple()
Locations=((37.571616,126.976584),(37.565596,126.966542),(37.576385,126.985676),(37.576385,126.985676))
import math
distanceex=math.sqrt((1-3)**2+ (2-4)**2)
print Locations[0][0]
for i in Locations:
        print "x={0},y={1}".format(i[0],i[1]) 
name='LSH'
where='home'
gbloc=(37.575723,126.973526)
dist=list()
for t in Locations:
        distance=math.sqrt((gbloc[0]-t[0])**2+(gbloc[1]-t[1])**2)
        dist.append(distance)
print "the minimum distance is %s" %min(dist)
input()
