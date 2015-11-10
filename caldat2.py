#!/usr/bin/env python
import sys
if len (sys.argv) >1:
    julian=float(sys.argv[1])
else:
    julian=input("Julian Day number: ")
jd=int(julian)
l=jd+68569
n=4*int(l/146097)
l=l-int((146097*n+3)/4)
i=int(4000*(l+1)/1461001)
l=l-int(1461*i/4)+31
j=int(80*l/2447)
k=l-int(2447*j/80)
l=int(j/11)
j=j+2-12*l
i=100*(n-49)+i+l
#
year=i
month=j
day=k
print "Date is: %04i/%02i/%02i" %( year , month ,  day)
#algorithm from USNO
