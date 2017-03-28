# 1. How do the flight phases (ex. take off, cruise, landing..) contribute to fatalities? Chart!

import requests
import os
import csv
from pprint import pprint
import matplotlib.pyplot as plt

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

    for row in reader: 
        year = row[3]
        isinstanceyear = isinstance(year, str)
        if not isinstance:
            print(isinstance)
        #print(year)
        

