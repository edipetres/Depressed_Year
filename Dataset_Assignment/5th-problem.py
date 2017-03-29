# What was the survival rate (how many died / how many survived) 
# for substantially damaged AND destroyed aircrafts since 1993, 
# showing data for each year. Show results on a stacked bar plot. 
# (see more in notebook 14 - Intro to plotting / example 62.) \**

import requests
import os
import csv
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np
import collections

url = 'https://raw.githubusercontent.com/edipetres/Depressed_Year/master/Dataset_Assignment/AviationDataset.csv'
fname = url.split('/')[-1]


if os.path.isfile(fname):
    print("File found.")
else:
    response = requests.get(url, params={'downloadformat': 'csv'})
    if response.ok:  # status_code == 200:
        with open(fname, 'wb') as f:
            f.write(response.content)   
    print('Downloaded {}'.format(fname))

with open(fname) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    aircraft_damage_substantial = {}
    aircraft_damage_destroyed = {}

    distribution = {}
    damages = []
    for row in reader:
        if row[23].isdigit(): 
            deaths = int(row[23]) 
        else:
            deaths = 0
        if row[24].isdigit() and row[25].isdigit() and row[26].isdigit():
            surviors = int(row[24]) + int(row[25]) + int(row[26])
        else:
            surviors = 0

        event_date = row[3]
        year = event_date.split('-')[0]

        try:            
            survival_rate = (100 * surviors) / (deaths + surviors)
        except Exception:
            survival_rate = 100

        damage = row[11]
        if 'Substantial' in damage:
            aircraft_damage_substantial[year] = survival_rate

        if 'Destroyed' in damage:
            aircraft_damage_destroyed[year] = survival_rate

    print(aircraft_damage_substantial, aircraft_damage_destroyed)
 