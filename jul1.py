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
# Sky and telescope  algorithm
f=-0.5+frac
j=-1*int(7*(int((month+9)/12)+year)/4)
#this is simplified for dates after gregorian calendar in 1582
j1=0 #I guess
#g=1
a=abs(month-9)
if (month !=9 ):
   s=(month-9)/a  # for sign value
else:
   s=0
j1=int(year+s*int(a/7))
j1=-1*int((int(j1/100)+1)*3/4)
j=j+int(275*month/9)+day+j1
j=j + 1721027 + 2 + 367*year
f=f+1
j=j-1
julianday=j+f
#
print "Julian Day is ", julianday
#print weekdays[weekday]
print "Day of year ",ti[7]
#print "Check 25 Dec 1981 is 2444963.5"



