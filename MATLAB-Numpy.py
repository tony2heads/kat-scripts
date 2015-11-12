#!/usr/bin/env python
import scipy.io
from numpy import squeeze,log10,meshgrid,pi,sin,cos,conjugate,searchsorted
import pylab as plt
import sys

c=2.998e8 # speed of light
#freq=1500 #MHz
#freq=900

filename=sys.argv[1]
ff=filename.split("_")
freq=int(ff[-1][:-4])   # take last part and remove 4 chars (".mat")
#D = scipy.io.loadmat("MK_GDSatcom_%d.mat" % 900)
#D = scipy.io.loadmat("MK_GDSatcom_%d.mat" % freq)
D = scipy.io.loadmat(filename)

th = D["th"].squeeze()
ph = D["ph"].squeeze()
if  ff[0] == "MK":
    JHH = D["Jqh"].squeeze()
    JVV = D["Jpv"].squeeze()
    JHV = D["Jqv"].squeeze()
    JVH = D["Jph"].squeeze()
if ff[0] == "MeerKAT":
    JHH = D["JHH"].squeeze()
    JVV = D["JVV"].squeeze()
    JHV = D["JHV"].squeeze()
    JVH = D["JVH"].squeeze() 

JHV /= (abs(JHH).max()*abs(JVV).max())**.5
JVH /= (abs(JHH).max()*abs(JVV).max())**.5
JHH /= abs(JHH).max()
JVV /= abs(JVV).max()

phi,rho = meshgrid(ph*pi/180,sin(th*pi/180))
f = plt.figure()
for d,l in [(JHH,(2,2,1)), (JVV,(2,2,4)), (JHV,(2,2,2)), (JVH,(2,2,3))]:
    ax = f.add_subplot(*l)
    ax.set_aspect('equal')
    plt.xticks(rotation="vertical")
    plt.grid(True)
    cs = plt.contour(rho*cos(phi), rho*sin(phi), 10*log10(d*conjugate(d)), range(0, -37, -5))
    plt.clabel(cs, range(0, -37, -5))

f = plt.figure()
for B,m in [(abs(JHH[:,0])**2,'b'), (abs(JVV[:,0])**2,'r')]:
    plt.plot(th, 10*log10(B), m)
    i3dB = searchsorted(-B, -0.5, 'left')
    hbw = th[i3dB] + (th[i3dB+1]-th[i3dB])*(0.5-B[i3dB])/(B[i3dB+1]-B[i3dB])
    print(hbw, 1/2 * 1.2*(c/freq/1e6)/13.5 * 180/pi)
plt.grid(True)

plt.show()
