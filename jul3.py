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
# Very rough
#Use reference epoch
ref=mktime((1995,10,9,12,0,0,0,0,0))   #Use reference 9oct1995 12UT
#
t=mktime(ti)
j=(t-ref)/(24*3600.0)
julianday=j+2450000.0                   #Julian day at ref=2450000
#
print "Julian Day is ", julianday
#print weekdays[weekday]
print "Day of year ",ti[7]
#print "Check 25 Dec 1981 is 2444963.5"



