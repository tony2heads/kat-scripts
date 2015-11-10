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
weekday=ti[6]
weekdays="Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"
#
frac=(ti[3]+  (ti[4] +ti[5]/60.0)/60.0)/24.0
#
#
if (year < 1583):
    print "Dont do years before 1583"
    Exception("Bad Year")
# Meeus algorithm
if  (month < 3 ):
   month=month+12
   year = year-1
century = int(year/100)
b = 2 - century + int(century/4)
c = int(365.25*year) -694025
d = int(30.6001*(month+1))
julianday = b + c + d + day + 2415019.5 +frac
print "Julian Day is ", julianday
print weekdays[weekday]
print "Day of year ",ti[7]
#print "Check 25 Dec 1981 is 2444963.5"



