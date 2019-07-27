# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 19:05:04 2019

@author: motec
"""

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('phila_poverty_density_clean_sheet.csv')

#increase figure size and resolution
fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 12
fig_size[1] = 9.5
plt.rcParams["figure.figsize"] = fig_size
plt.rcParams["figure.dpi"] = 150

array_x = data['Density_sqmi']
array_y = data['Poverty_rate']
zip_label = data['ZCTA']

plt.plot(array_x, array_y, 'b.')

#annotate data points in figure with ZCTAs
for i in range(0,len(data)):
    plt.annotate(zip_label[i], (array_x[i],array_y[i]), fontsize=6)

plt.xlabel('Population density per square mile')
plt.ylabel('Poverty rate')
plt.title('Philadelphia population density vs. poverty by ZIP code')

plt.savefig('graph.png')
plt.show()
