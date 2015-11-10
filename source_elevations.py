#!/usr/bin/env python
import katpoint
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
import optparse
import time
import sys
from datetime import datetime
from matplotlib.ticker import MaxNLocator
from matplotlib.dates import DateFormatter
from matplotlib.font_manager import FontProperties
parser = optparse.OptionParser(usage="%prog [opts] <directories or files>",
                               description="Create a plot of elevations of sources in a catalogue for KAT-7")
parser.add_option('-t', '--start_time', dest='start_time', type="string", default='',
   help="Date and time (UTC) from which to start calculation in YYYY-MM-DD HH:MM:SS. Leave blank to start from current time")
(opts, args) = parser.parse_args()

if len(args) ==0:
    print 'Please specify a catalogue file'
    sys.exit(1)

cat_filename = args[0]
if len(opts.start_time) == 0:
   opts.start_time = time.strftime('%Y-%m-%d %H:%M',time.gmtime())

#create a variety of coloured markers.  After a while the plots get really crowded,
#but you can add on to this if you like.
markers = []
colors = ['b','g','r','c','m','y','k']
pointtypes = ['o','*','x','^','s','p','h','+','D','d','v','H','d','v']
for point in  pointtypes:
    for color in colors:
        markers.append(str(color+point))

cat = katpoint.Catalogue(file(cat_filename),add_specials=False)
#cat.add('Sun, special') # except maybe the sun


cat.antenna = katpoint.Antenna('ant1, -30:43:17.3, 21:24:38.5, 1038.0, 12.0, 18.4 -8.7 0.0, -0:05:30.6 0 -0:00:03.3 0:02:14.2 0:00:01.6 -0:01:30.6 0:08:42.1, 1.22')
target = cat.targets[0]

t = katpoint.Timestamp().secs + np.arange(0, 24. * 60. * 60., 360.)
lst = katpoint.rad2deg(target.antenna.local_sidereal_time(t)) / 15

fig = plt.figure(1)
plt.clf()
fig.set_size_inches(12, 4)
plt.subplots_adjust(right=0.8)
lines = list()
labels = list()
count = 0
fontP = FontProperties()
fontP.set_size('small')


for target in cat.targets:
   count = count + 1
   elev = katpoint.rad2deg(target.azel(t)[1])
   lines.append(plt.plot(lst,elev, markers[count-1], linewidth = 0, label=target.name))
   labels.append(target.name)
plt.legend(lines,labels, bbox_to_anchor = (1, 1), loc = 'best',ncol=2,prop = fontP, fancybox=True)

plt.ylim(0.90)
plt.xlim(0,24)
plt.ylabel('Elevation (deg)')
plt.xlabel ('Local Sidereal Time (hours)')
plt.legend()
plt.title('Elevations of targets')
plt.savefig('elevation_lst.png',dpi=160)
plt.show()

#Calculate the corresponding times in UTC
t = katpoint.Timestamp(opts.start_time).secs + np.arange(0, 24. * 60. * 60., 360)
date_times =  mdates.date2num(datetime.strptime(opts.start_time,'%Y-%m-%d %H:%M')) + np.arange(0, 24. * 60. * 60., 360)/(3600*24)
fig = plt.figure(2)
plt.clf()
fig.set_size_inches(12, 4)
ax = plt.subplot(111)
plt.subplots_adjust(right=0.8)
lines = list()
labels = list()
count = 0


for target in cat.targets :
   count = count + 1
   elev = katpoint.rad2deg(target.azel(t)[1])
   lines.append(plt.plot_date(date_times,elev, markers[count-1], linewidth = 0, label=target.name))
   labels.append(target.name)
hours = mdates.HourLocator()
#minutes = mdates.MinuteLocator()
#hoursFmt = mdates.DateFormatter('%H')
#ax.xaxis.set_major_formatter(hoursFmt)
#ax.xaxis.set_major_locator(MaxNLocator(24))
#ax.xaxis.set_minor_locator(MaxNLocator(3))
#ax.xaxis.set_major_formatter(hours)
ax.yaxis.grid(color='gray', linestyle='dashed')
fig.autofmt_xdate()
plt.legend(lines,labels, bbox_to_anchor = (1, 1), loc = 'center',ncol=1,prop = fontP, fancybox=True)
plt.legend()
plt.ylim(0.90)
plt.ylabel('Elevation (deg)')
plt.xlabel ('Time starting from %s'%opts.start_time)
plt.title('Elevations of targets')
plt.savefig('elevation_UTC.png',dpi=300)
plt.show()


