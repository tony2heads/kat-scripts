#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt


lat=np.radians(-30.7148) #latitude of KAT7
coslat=np.cos(lat)
sinlat=np.sin(lat)


def elev(ha,dec):    #elevation and azimuth
    """
    ha,dec => az,el
    All values are in radians
    az 0 is SOUTH
    """
    elev=np.arcsin((np.sin(dec)*sinlat +np.cos(dec)*np.cos(ha)*coslat))                    #el
    azim=np.arctan2((np.cos(dec)*np.sin(ha)), (np.cos(dec)*np.cos(ha)*sinlat-np.sin(dec)*coslat))#az    
    return (azim,elev)
   
def hadec(az,el):
    """
    az,el => ha,dec
    All values are in radians
    az 0 is SOUTH
    """
    dec=np.arcsin(np.sin(el)*sinlat -np.cos(el)*np.cos(az)*coslat)  #declination
    ha=np.arctan2((np.cos(el)*np.sin(az)), (np.sin(el)*coslat+np.cos(el)*np.cos(az)*sinlat)) #hour angle
    return (ha,dec)

#ax = plt.subplot(111, polar=True)
#ax.set_theta_offset(np.pi/2)
#ax.set_rmax(2.0)

hadeg=np.linspace(0,360,304) # lots of steps entries 
ha=np.radians(hadeg)
for decdeg in np.arange(-80,40,20):  # hadeg is HA in degrees, decdeg is Dec in degrees
    dec=np.radians(decdeg)
    azel=elev(ha,dec)
    az=azel[0]
    el=azel[1]
    za=np.pi/2.0 - azel[1]
    t2=np.tan(za/2.0) # tan/2 zenith angle
    s=np.sin(za)
    #print ha,dec,az,el,t2,s
    plt.plot(np.degrees(az),np.degrees(el),label="Dec "+str(decdeg),linestyle="--")
#
decdeg=np.linspace(-90,60,300)
dec=np.radians(decdeg)
for hadeg in np.arange(0,360,30):
    ha=np.radians(hadeg)
    azel=elev(ha,dec)
    az=azel[0]
    el=azel[1]
    za=np.pi/2.0 - azel[1]
    t2=np.tan(za/2.0) # tan/2 zenith angle
    s=np.sin(za)
    #print ha,dec,az,el,t2,s
    plt.plot(np.degrees(az),np.degrees(el),label="HA "+str(hadeg),linestyle=":") 
plt.xlabel("Az")
plt.ylabel("El")
plt.ylim(0,90)
plt.xlim(-180,180)
plt.legend( loc=2,ncol=6) # upper left
plt.show()


