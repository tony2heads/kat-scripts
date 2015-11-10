#!/usr/bin/env python
from math import *

lat=radians(-30.71317) #latitude MeerKAT

def elev(ha,dec):    #elevation and azimuth
    elev=asin((sin(dec)*sin(lat)+cos(dec)*cos(ha)*cos(lat)))                    #el
    azim=atan2((cos(dec)*sin(ha)),(cos(dec)*cos(ha)*sin(lat)-sin(dec)*cos(lat)))#az    
    return (azim,elev)
   
def hadec(az,el):
    dec=asin(sin(el)*sin(lat)-cos(el)*cos(az)*cos(lat))  #declination
    ha=atan2((cos(el)*sin(az)),(sin(el)*cos(lat)+cos(el)*cos(az)*sin(lat))) #hour angle
    return (ha,dec)

#ha=radians(90.0)   # for this case I am interested in extreme HA

#print "# El    Az   HA  Dec"
#for declin in range(-37,90,1):  # declination limit about 88.7deg
#    dec=radians(declin)
#    azel=elev(ha,dec)
#    el=azel[1]
#    az=azel[0]
#    if az<0:
#        az=az+radians(360)      # just a convention 
#    if el > 0 :                 # not interest in ranges where the telescope limits are negative elevations
#       print "%4.1f  %5.1f %3.1f %3.1f" % (degrees(el),degrees(az),degrees(ha),degrees(dec))

#el=0
#for azim in range(-90,90,1):
#    az=radians(azim)
#    hadc=hadec(az,el)
#    print degrees(hadc[0]), degrees(hadc[1])

coord=raw_input("What do you want to input, HADC or AZEL:  ")
# VLBI and KAT frame has north =0, east=90, south=180, west=270 azimuth
# WSRT frame has north=-180, east=-90, south=0, west=90 azimuth
# so for VLBI or KAT subtract 180 for azimuth input, add 180 for output
if "h" in coord or "H" in coord:
    ha=radians(float(input("Hour angle in degrees: ")))
    dec=radians(float(input("Declination in degrees:")))
    azel=elev(ha,dec)
    print "Az: %8.3f El %8.3f" % ((degrees(azel[0])+180), degrees(azel[1]))
    
elif "z" in coord or "Z" in coord:
    az=radians(float(input("Azimuth in degrees: ")))
    el=radians(float(input("Elevation in degrees:")))
    az=az-radians(180)
    hadc=hadec(az,el)
    print "HA: %8.3f Dec %8.3f" % (degrees(hadc[0]), degrees(hadc[1])) 
else:
    print "Sorry, I dont understabd"

    
