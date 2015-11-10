#!/usr/bin/env python
#
from time import *
#
datein = raw_input("Date in yyyy/mm/dd format - empty for today: ")
if (datein ==""):
   ti=gmtime()
else:
   timein = raw_input("UT time in   hh:mm:ss format : ")
   ti=strptime(datein+" "+timein,"%Y/%m/%d %H:%M:%S")
#  
year=ti[0]
month=ti[1]
day=ti[2]
#
frac=(ti[3]+  (ti[4] +ti[5]/60.0)/60.0)/24.0
# USNO algorithm

i=year
j=month
k=day
n=(j-14)/12
l=i+4800+n
julianday=k-32075+1461*l/4 \
           +367*(j-2-12*n)/12 \
           -3*((l+100)/100)/4
#
print "Julian Day is ", julianday-2.5+frac
print "FUDGED by 2.5 days -BUT STILL WRONG"
#print weekdays[weekday]
print "Day of year ",ti[7]
#print "Check 25 Dec 1981 is 2444963.5"



