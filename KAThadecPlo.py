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

azdeg=np.linspace(0,360,304) # lots of steps entries 
az=np.radians(azdeg)
for eldeg in np.arange(15,80,15):  # azdeg is AZ in degrees, eldeg is El in degrees
    el=np.radians(eldeg)
    hd=hadec(az,el)
    ha=hd[0]
    dec=hd[1]
    plt.plot(np.degrees(ha),np.degrees(dec),label="El "+str(eldeg),linestyle="--")
#
eldeg=np.linspace(10,90,300)
el=np.radians(eldeg)
for azdeg in np.arange(0,360,30):
    az=np.radians(azdeg)
    hd=hadec(az,el)
    ha=hd[0]
    dec=hd[1]
    plt.plot(np.degrees(ha),np.degrees(dec),label="AZ "+str(azdeg),linestyle=":") 
plt.xlabel("HA")
plt.xlim(-180,180)
plt.ylabel("Dec")
plt.ylim(-90,50)
plt.legend( loc=2,ncol=2 ) # left side
plt.show()


