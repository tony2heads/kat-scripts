#!/usr/bin/env python
import time
date = time.ctime()
print date			
sec70 =time.time()		#seconds since 1jan 1970
days = int(sec70/86400)		#days ,,
sec = sec70- days*86400		#seconds remaining today
hours=sec/3600                  #hours remaining today   
print ("Linux days %d seconds %f ") %(days, sec)

#Need to know days to JD
# and then use the JD formula
# 0UT on 1 jan 1970 = JD 2440587.5
jdm=days+2440587.5
print (" Julian Day last midnight was: %12.5f") %( jdm)
jd=jdm+(sec/86400)
print " jday=",jd
tu = (jdm - 2451545.0)/ 36525.0   #julian centuries since 2000
gmstm = 24110.54841 + tu*(8640184.812866 + tu*(0.093104 - tu* 6.2e-6));
gmstm = gmstm/3600.0 #from seconds back to hours
lst = gmstm + hours*1.00273790935  #from UT to sidereal hours
#lst = lst +  0.440278074  # add offset for Westerbork in sidereal hours
lst=lst+21.44389/15 #add offset for KAT in sidereal hours
days=int(lst/24)
lst=lst-24*days
print ("LST=%8.4f") %(lst)
