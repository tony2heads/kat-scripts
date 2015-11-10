#!/usr/bin/env python
import katfile
import sys
#
filename=sys.argv[1]
#
h5=katfile.open(filename,refant='ant1')
for ant in h5.ants:
    ecef=ant.position_ecef
    wgs =ant.ref_position_wgs84
    enu =ant.position_enu
    #print "ECEF values", ecef
    #print "WGS84 values",wgs
    print "ENU values %6.3f, %6.3f, %6.3f" %(enu)
