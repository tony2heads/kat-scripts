#!/usr/bin/env python
import sys

if len(sys.argv)>1:
    julian= float(sys.argv[1])
else:
    julian=input("Julian Day number: ")
j=int(julian)
f=julian-j
d=j-2451545    # 1jan2000 12:00:00
t=d/36525
t1=int(t)
j0=t1*36525 + 2451545    # 1jan2000 12:00:00
t2=(j-j0+0.5)/36525
s=24110.54841 + 184.812866*t1
s=s + 8640184.812866*t2
s=s + 0.093104*t*t
s=s - 0.0000062*t*t*t
s=s/86400
s=s-int(s) # down to fractional days
s=24*(s + (f - 0.5)*1.002737790935)   #GMST hours
#offset=6.604171/15 #Westerbork offset in hours
offset=21.44389/15 # MeerKAT offset in hours
s=s+offset
if(s<0):
    s=s+24
if(s>24):
    s=s-24
hours=int(s)
m1=60*(s-hours)
minutes=int(m1)
seconds=60*(m1-minutes)
print "KAT LST %02i:%02i:%02i" %(hours,minutes,seconds)
#Algorithm from Sky and Telescope
