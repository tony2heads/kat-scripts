#!/usr/bin/env python
import sys
if len (sys.argv) >1:
    julian=float(sys.argv[1])
else:
    julian=input("Julian Day number: ")
f=0.5
julian=julian-1
f=f+1
#assumer gregorian ; g=1
a1=int((julian/36524.25)-51.12264)
a=julian+1+a1-int(a1/4)
b=a+1524
c=int((b/365.25)-0.3343)
d=int(365.25*c)
e=int((b-d)/30.61)
day=b-d-int(30.61*e)+f
month=e-1
year=c-4716
if(e>13.5):
    month=month-12
if(month<2.5):
    year=year+1
print "Date is: %04i/%02i/%02i" %( year , month ,  day)
#algorithm from Sky and Telescop
