#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 13:13:21 2022

@author: somrawee
"""

import csv

from plotly.graph_objs import Layout
from plotly import offline

filename = '/Users/somrawee/PythonClass2/Data/world_fires_1_day.csv'
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)
    lats, lons, brightnesses=[], [], []
    
    for row in reader:
        lat = row[0]
        lon = row[1]
        brightness= float(row[2])
        
        lats.append(lat)
        lons.append(lon)
        brightnesses.append(brightness)
        
#data = [Scattergeo(lon=lons, lat=lats)]
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'size': [bn/30 for bn in brightnesses],
        'color': brightnesses,
        'colorscale': 'Hot',
        'reversescale': True,
        'colorbar': {'title': 'Brightness'},
        },
    }]
my_layout = Layout(title='World Fires')

fig={'data':data, 'layout':my_layout}
offline.plot(fig, filename='world_fires.html')

#print(lons[:5])
#print(lats[:5])
#print(brightnesses[:5])