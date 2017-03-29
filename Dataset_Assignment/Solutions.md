# Solutions

## 1. How do the flight phases (ex. take off, cruise, landing..) contribute to fatalities? Chart!

### Prerequisites

``` python
import requests
import os
import csv
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np
import collections
```

### Code

``` python
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
```

http://prntscr.com/eprulg

## 2. Which 5 locations saw the most injuries in the US? Show it on a barchart!

### Prerequisites

``` python
import os
import requests
import csv
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
```

### Code

``` python
import os
import requests
import csv
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/edipetres/Depressed_Year/master/Dataset_Assignment/AviationDataset.csv'
filename = url.split('/')[-1]

# if dataset does not exist locally, download it
if not os.path.exists(filename):
    response = requests.get(url, params={'downloadformat': 'csv'})

    if response.ok:
        with open(filename, 'wb') as f:
            f.write(response.content)

location_injuries = {}

with open(filename, encoding='latin-1') as file:
    reader = csv.reader(file)
    next(reader)  # skip headers

    for row in reader:
        # row[4]    => Location
        # row[5]    => Country
        # row[24]   => Total.Serious.Injuries
        # row[25]   => Total.Minor.Injuries

        if row[5] == 'United States':
            total_injuries = 0

            if row[24]:
                total_injuries += int(row[24])

            if row[25]:
                total_injuries += int(row[25])

            location_injuries.setdefault(row[4], 0)
            location_injuries[row[4]] += total_injuries

location_injuries_sorted = [(location, location_injuries[location]) for location in
                            sorted(location_injuries, key=location_injuries.get, reverse=True)]
top5_most_injuries = list(zip(*location_injuries_sorted[:5]))
locations = top5_most_injuries[0]
injuries = top5_most_injuries[1]

# create plot from processed data
plt.bar(range(len(locations)), injuries, width=0.5, linewidth=0, align='center')
plt.xticks(range(len(injuries)), locations, size='small')
plt.title('Top 5 locations with most injuries in the United States', fontsize=20)
plt.xlabel('Locations in the United States', fontsize=12)
plt.ylabel('Injuries', fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=7)
plt.savefig('top5_most_injuries_plot.png', bbox_inches='tight')
```

http://prnt.sc/eprvpn

## 3. Which 5 aircraft models had the most injuries (fatal, serious, minor)? Show them on a piechart!

### Prerequisites

``` python
import csv
import matplotlib.pyplot as plt
```

### Code

``` python
import csv
import matplotlib.pyplot as plt

filename = "AviationDataEnd2016UP.csv"

with open(filename, encoding='latin-1') as f:
    reader = csv.reader(f)
    header_row = next(reader)

## amc = aicraft model chart
    amc = {}

    for row in reader:
## according row numbers of injuries - 23,24,25
        aircraft_model = row[15]
        total_injuries = 0
        if(row[23].isdigit()):
            total_injuries += int(row[23])
        if(row[24].isdigit()):
            total_injuries += int(row[24])
        if(row[25].isdigit()):
            total_injuries += int(row[25])
        if aircraft_model not in amc.keys():
            amc[aircraft_model] = total_injuries
        else:
            amc[aircraft_model] += total_injuries


## Test print top5
    amc_sorted = sorted(amc, key=amc.get, reverse=True)
    for index, aircraft_model in enumerate(amc_ordered[:5]):
        print('Number {} aircraft model regarding injuries is {}.'.format(index+1,aircraft_model))

## Baking a pie chart
    amc_ordered = collections.OrderedDict(sorted(amc.items(), key=lambda t: t[1], reverse = True))

    models = list(amc.keys())
    ##print(models)
    injuries = list(amc.values())
    ##print(injuries)

    plt.title("The top five aircraft models regarding injuries")
```

No Pie Chart

## 4. What was the distribution of fatal injuries during the last 20 years? Show it on a barchart!

### Prerequisites

``` python
import warnings
import csv 
import matplotlib.pyplot as plt
```

### Code

``` python
import warnings
warnings.filterwarnings('ignore')

# the following line is jupyter notebook specific 
%matplotlib inline

import csv 
import matplotlib.pyplot as plt

filename = "AviationDataset.csv"

with open(filename, encoding='latin-1') as f:
    reader = csv.reader(f)
    headerrow = next(reader)

    distribution = {}
    for row in reader:
        fatal_injuries = 0
        year = 0
        year = int((row[3].split('-')[0]))
        
        
        if(row[23].isdigit()):
            fatal_injuries = int(row[23])
            
        if(year >= 1997):    
            if year not in distribution.keys():
                distribution[year] = fatal_injuries            
            else:
                distribution[year] += fatal_injuries
        #print(year)
        #print(distribution)
        #print("Hello")
        #list1 = [distribution]
        
        #distribution = list(map(int, distribution))
        
        print(int(distribution))
        
       
plt.bar(year, fatal_injuries, width=0.5, linewidth=0, align='center')
plt.ticklabel_format(useOffset=False)
title = 'Fatalities from 1997 to 2017'
plt.title(title, fontsize=12)
plt.ylabel("Fatalities", fontsize=10)
plt.xlabel("Year", fontsize=10)
plt.tick_params(axis='both', which='major', labelsize=10)
plt.show()
```

http://prntscr.com/eprxam
