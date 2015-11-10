#!/usr/bin/env python
import katfile
import sys
#
filename=sys.argv[1]
#
h5=katfile.open(filename,refant='ant1')
x=h5.sensor.get('DBE/auto-delay')
print "number of autodelays",x.events[1]
print "min",min(x),"max",max(x)
print "targets",h5.catalogue.targets
print "antennas",h5.inputs
print "min elevation",h5.el.min()
print "max elevation",h5.el.max()
print "dump period",h5.dump_period
print "band",h5.channel_freqs.min()/1e9,"to",h5.channel_freqs.max()/1e9,"GHz"
print "start",h5.start_time.local(),"end",h5.end_time.local(),\
"duration",(h5.end_time-h5.start_time)/3600,"hrs"
