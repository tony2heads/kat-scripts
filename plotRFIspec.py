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

date=sys.argv[1]
hr=sys.argv[2]

if  len(sys.argv[1:]) !=2:
    print "Give Date and hour yyyy/mm/dd hh"

ymd=date.split("/")
yr=ymd[0]
mon=ymd[1]
day=ymd[2]

print yr,mon,day,hr



tstr=yr+"/"+mon+"/"+day+"/"+hr+".h5"
filename=yr+"_"+mon+"_"+day+"_"+hr+".h5"


url="http://rfimonitor.kat.ac.za/rfi_data/"+tstr
urllib.urlretrieve(url,filename)

x=h5py.File(filename,'r')
#x.keys()
l=x['spectra']
m=x['mode']



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

mod=np.median(sp,axis=0)
maxim=np.max(sp,axis=0)
minim=np.min(sp,axis=0)
pk=np.max(maxim[500:-500]) # peak
chpk=np.argmax(maxim[500:-500]) # channel with peakf
fpk=freq(chpk,mode) # freq of channel with peak

aver=np.average(mod[500:-500])

pl.plot(f[500:-500],mod[500:-500],label="Median",color='c')
pl.plot(f[500:-500],maxim[500:-500],label="Max", color='g')
pl.plot(f[500:-500],minim[500:-500],label="Min",color='r')

pl.ylim(-130,-90)
pl.title(filename+" Mode:"+str(mode))
pl.xlabel("Freq/MHz")
pl.ylabel("Power/dB")
pl.text(fpk,pk,"peak "+str(pk))
pl.text(1200,aver,"average "+str(aver),fontsize=10,color='k', weight='bold')
pl.legend()
pl.grid(True)
figname=yr+"_"+mon+"_"+day+":"+hr+".png"
pl.savefig(figname)
pl.show()

os.remove(filename)

