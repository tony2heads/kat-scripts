#!/usr/bin/env python
from math import *
import sys
if len(sys.argv) > 1:
    JD=float(sys.argv[1])
else:
    JD=float(raw_input("JD:"))

#JD=2451588.5	#Julian Day 14feb2000 AT MIDNIGHT
hours= (JD-int(JD)-0.5)*24  #UT hours since last midnight*24
t=(JD-2451545.0)/36525.0	#julian centuries since 1Jan2000 12UT

gmst=24100.54841+8640184.812866*t+0.093104*t*t+6.2e-6*t*t*t #SECONDS
gmsth=gmst/3600   #hours
gmst=gmsth+ hours*1.00273790935
#lst=gmst+0.440278074   #Westerbork oddset from GMST
lst= gmst+21.44389/15 # KAT offset from GMST
lst=lst%24   #modulo 24hrs
gmst=gmst%24
print ("LST %7.3f GMST %7.3f") %(lst,gmst)

