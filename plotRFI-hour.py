#!/usr/bin/env python
import h5py
import pylab as pl
import numpy as np
import urllib
import sys
import os
"""
get h5 file from server
02 SAST every time
read in spectra and mode
plot with information
"""

#defaults
yr="2015"
mon="11"
day="17"
hr="02"


if  len(sys.argv[1:]) !=2:
    print "Give Date and hour yyyy/mm/dd hh"
    date=raw_input("Date in format yyyy/mm/dd :")
    hour=raw_input("Hour:")
    hr=int(hour)
else:
    date=sys.argv[1]
    hr=int(sys.argv[2])

ymd=date.split("/")
yr=int(ymd[0])
mon=int(ymd[1])
day=int(ymd[2])

#print("%d/%02d/%02d %02d:00") %(yr,mon,day,hr)

tstr=("%d/%02d/%02d/%02d.h5")  %(yr,mon,day,hr)
filename=("%d_%02d_%02d_%02d.h5") %(yr,mon,day,hr)


url="http://rfimonitor.kat.ac.za/rfi_data/"+tstr
urllib.urlretrieve(url,filename)
print "retrieved:",filename

h5=h5py.File(filename,'r')
#h5.keys()
l=h5['spectra']
m=h5['mode']



def freq(chans,mode):
    if mode==4:
        freq=1800000000.0 +chans*27465.8203125
    if mode ==3:
        freq = 855000000.0 +chans*26092.529296875
    if mode ==2:
        freq= 600000000.0 + chans*18310.546875
    if mode ==1:
        freq=0+chans*27465.8203125
    return freq/1e6

fchans=np.array(range(l.shape[1]))
times=l.shape[0]
pl.grid(True)

tf=np.bool()  # boolean array
marr=np.array(m) # array for modes
ll=np.array(l) # array for spectra
tf=marr > 0 # true if value >0
mode=max(marr)
sp=ll[tf]
f=freq(fchans,mode)


"""
sp has dimensions of [time,channel]
time is in 2second dumps
so 1 minute is 30 dumps

"""

#tenmin=sp[0:300]
start=float(hr)
sec2=sp.shape[0] # number of 2seconds dumps
end=start+sec2/1800.

"""
This dump rate works for mode3, but seems wrong for mode1, which looks like one dump per 16 seconds or so

"""

# for  mode 3 it runs from 855 to 1710
if mode==3:
    pl.imshow(sp,aspect='auto',cmap='rainbow',vmin=-125,vmax=-120,extent=(f[0],f[-1],end,start))
else:
    up=sp.mean()+10
    down=sp.mean()-10
    # check this end time
    if mode ==1:
        end=start+(sec2*8)/1800.
    pl.imshow(sp,aspect='auto',cmap='rainbow',vmin=down,vmax=up,extent=(f[0],f[-1],end,start))
pl.title("Date "+tstr[0:10]+"  mode"+str(mode))
pl.xlabel("Freq/MHz")
pl.ylabel("Time/hr")
pl.colorbar()
pl.show()




os.remove(filename)

