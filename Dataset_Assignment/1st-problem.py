# 1. How do the flight phases (ex. take off, cruise, landing..) contribute to fatalities? Chart!

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

    distribution = {}
    for row in reader:
        total_fatal = 0
        flight_phase = row[28].title()
        if(row[23].isdigit()):
            total_fatal = int(row[23])

        if flight_phase not in distribution.keys():
            distribution[flight_phase] = total_fatal
        else:
            distribution[flight_phase] += total_fatal
    
    # rename empty key to Unknown
    distribution['Unknown'] = distribution.pop('')
    
    # sort the dictionary
    sorted_dict = collections.OrderedDict(sorted(distribution.items(), key=lambda t: t[1]))

    # make lists for plotting
    phases = range(len(sorted_dict.keys()))
    no_fatalities = list(sorted_dict.values())

    title = 'Distribution of fatalities during different flight phases'
    plt.title(title, fontsize=12)
    plt.xlabel("Phases", fontsize=10)
    plt.ylabel("Fatalities", fontsize=10)
    plt.bar(phases, no_fatalities, width=0.8, linewidth=0.5, align='center')
    myxticks = sorted_dict.keys()
    plt.xticks(phases, myxticks)
    plt.tick_params(axis='both', which='major', labelsize=10)
    plt.show()

