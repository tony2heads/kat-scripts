#!/usr/bin/env python

import matplotlib.pyplot as plt
import astropy.units as u
from astropy.coordinates import EarthLocation, SkyCoord
from pytz import timezone
from astropy.time import Time

from astroplan import Observer
from astroplan import FixedTarget
from astroplan.plots import plot_sky

# Set up Observer, Target and observation time objects for KAT-7
longitude = '21d23m16.8s'
latitude = '-30d42m53.28s'
elevation = 1038* u.m
location = EarthLocation.from_geodetic(longitude, latitude, elevation)

observer = Observer(name='KAT-7',
               location=location,
               pressure=0.91* u.bar,
               relative_humidity=0.22,
               temperature=32 * u.deg_C,
               timezone=timezone('Africa/Johannesburg'),
               description="KAT-7 array in the Karoo")

coordinates = SkyCoord('19h39m25.03s', '-63d42m45.63s', frame='icrs')
pks1934= FixedTarget(name='PKS1934-638', coord=coordinates)
pks1934_style= {'color': 'k'}

coordinates= SkyCoord('13h31m08.29s','30d30m33.0s', frame='icrs')
x3C286= FixedTarget(name='3C286', coord=coordinates)
x3C286_style={'color':'red'}

coords="J052109.90+163822.1"
coordinates= SkyCoord(coords,frame='icrs',unit=(u.hour, u.deg))
x3C138=FixedTarget(name='3C138',coord=coordinates)
x3C138_style={'color':'blue'}

coords="17:45:40.0383-29:00:28.069"
coordinates= SkyCoord(coords,frame='icrs',unit=(u.hour, u.deg))
pks1742=FixedTarget(name='PKS1742-289',coord=coordinates)
pks1742_style={'color':'green'}

import numpy as np

observe_time = Time('2015-03-15 17:00:00')
observe_time = observe_time + np.linspace(-12, 12, 24)*u.hour

plot_sky(pks1934, observer, observe_time,style_kwargs=pks1934_style)
plot_sky(x3C286,observer, observe_time,style_kwargs=x3C286_style)
plot_sky(x3C138,observer, observe_time,style_kwargs=x3C138_style)
plot_sky(pks1742, observer, observe_time,style_kwargs=pks1742_style)


# Note that you don't need this code block to produce the plot.
# It reduces the plot size for the documentation.
ax = plt.gca()
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.75, box.height * 0.75])

plt.legend(loc='center left', bbox_to_anchor=(1.25, 0.5))
plt.show()
