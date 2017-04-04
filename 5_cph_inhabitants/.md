# Solutions

## 1. Use matplotlib to show the distribution of the following four categories over the time of 1992 - 2015

### Prerequisites

``` python
import warnings
warnings.filterwarnings('ignore')
%matplotlib inline
import csv 
import matplotlib.pyplot as plt
import collections
```

### Code

``` python
import csv 
import matplotlib.pyplot as plt
import collections

filename = "befkbhalderkoencivst.csv"

with open(filename) as file:
    reader = csv.reader(file)
    headerrow = next(reader)
    
    counter_male = 0
    counter_female = 0
    counter_male_old = 0
    counter_female_old = 0
    distribution_male = {}
    distribution_female = {}
    distribution_male_old = {}
    distribution_female_old = {}
    for row in reader:
        male = 0
        male_old = 0
        female = 0
        female_old = 0
        arr = int(row[0])
        age = int(row[2])
        
        
            
        if int(row[4]) == 1:
            male = int(row[4])
            
            counter_male += 1
            if age >= 18 and age <= 30:
                if arr not in distribution_male.keys():
                    distribution_male[arr] = 1
                else:
                    distribution_male[arr] += 1
            
        
        
        if int(row[4]) == 2:
            female = int(row[4])
            
            counter_female += 1
            if age >= 18 and age <= 30:    
                if arr not in distribution_female.keys():
                    distribution_female[arr] = 1
                else:
                    distribution_female[arr] += 1
                    
                    
        if int(row[4]) == 1:
            male_old = int(row[4])
            
            counter_male_old += 1
            if age >= 50:
                if arr not in distribution_male_old.keys():
                    distribution_male_old[arr] = 1
                else:
                    distribution_male_old[arr] += 1
            
    
    
        if int(row[4]) == 2:
            female_old = int(row[4])
            
            counter_female_old += 1
            if age >= 50:
                if arr not in distribution_female_old.keys():
                    distribution_female_old[arr] = 1
                else:
                    distribution_female_old[arr] += 1
    
    sorted_dict_male = collections.OrderedDict(sorted(distribution_male.items()))
    sorted_dict_female = collections.OrderedDict(sorted(distribution_female.items()))
    sorted_dict_male_old = collections.OrderedDict(sorted(distribution_male_old.items()))
    sorted_dict_female_old = collections.OrderedDict(sorted(distribution_female_old.items()))
    
    year_men = list((sorted_dict_male.keys()))
    total_age_men = list(sorted_dict_male.values())
    year_women = list((sorted_dict_female.keys()))
    total_age_women = list(sorted_dict_female.values())
    
    year_men_old = list((sorted_dict_male_old.keys()))
    total_age_men_old = list(sorted_dict_male_old.values())
    year_women_old = list((sorted_dict_female_old.keys()))
    total_age_women_old = list(sorted_dict_female_old.values())
    
    print(counter_male)
    print(year_men)
    print(total_age_men)
    print("----------")
    print(counter_female)
    print(year_women)
    print(total_age_women)
    print("----------")
    print(counter_male_old)
    print(year_men_old)
    print(total_age_men_old)
    print("----------")
    print(counter_female_old)
    print(year_women_old)
    print(total_age_women_old)
    
    plt.ticklabel_format(useOffset=False)
    plt.axis([1992, 2015, 0, 1500])
    title = 'Distribution of {} CPH Citizens from 1995 to 2015'
    plt.title(title, fontsize=12)
    plt.xlabel("Year", fontsize=10)
    plt.ylabel("How many of age 18 to 30", fontsize=10)
    plt.tick_params(axis='both', which='major', labelsize=10)
    
    plt.bar(year_women, total_age_women, width=0.5, linewidth=0, align='center', color='green')
    plt.show()
    
    plt.bar(year_men, total_age_men, width=0.5, linewidth=0, align='center')
    plt.ticklabel_format(useOffset=False)
    plt.axis([1992, 2015, 0, 1500])
    title = 'Distribution of {} CPH Citizens from 1995 to 2015'
    plt.title(title, fontsize=12)
    plt.xlabel("Year", fontsize=10)
    plt.ylabel("How many of age 18 to 30", fontsize=10)
    plt.tick_params(axis='both', which='major', labelsize=10)
    
    #plt.bar(year_women, total_age_women, width=0.5, linewidth=0, align='center', color='green')
    plt.show()
    
    plt.bar(year_men_old, total_age_men_old, width=0.5, linewidth=0, align='center', color='black')
    plt.ticklabel_format(useOffset=False)
    plt.axis([1992, 2015, 0, 3000])
    title = 'Distribution of {} CPH Citizens from 1995 to 2015'
    plt.title(title, fontsize=12)
    plt.xlabel("Year", fontsize=10)
    plt.ylabel("How many of age 18 to 30", fontsize=10)
    plt.tick_params(axis='both', which='major', labelsize=10)
    
    plt.show()
    
    plt.bar(year_women_old, total_age_women_old, width=0.5, linewidth=0, align='center', color='red')
    plt.ticklabel_format(useOffset=False)
    plt.axis([1992, 2015, 0, 3000])
    title = 'Distribution of {} CPH Citizens from 1995 to 2015'
    plt.title(title, fontsize=12)
    plt.xlabel("Year", fontsize=10)
    plt.ylabel("How many of age 18 to 30", fontsize=10)
    plt.tick_params(axis='both', which='major', labelsize=10)
    
    plt.show()
```

### Plot

![http://image.prntscr.com/image/e93c8c90ccf94562b525984e73467576.png](http://image.prntscr.com/image/e93c8c90ccf94562b525984e73467576.png)
![http://image.prntscr.com/image/ccb1f4dd4e1d41c3a4bbedcbaac316e5.png](http://image.prntscr.com/image/ccb1f4dd4e1d41c3a4bbedcbaac316e5.png)
![http://image.prntscr.com/image/e7f3c08fc5cf473f8f89f6ae240dd405.png](http://image.prntscr.com/image/e7f3c08fc5cf473f8f89f6ae240dd405.png)

## 2. Use matplotlib to plot a bar-char showing how many single males and females of age 18 to 30, are living in BYDEL 1, 2 and 3 over the time 1992 - 2015

### Prerequisites

``` python
import os
import requests
import csv
import matplotlib
```

### Code

``` python
import os
import requests
import csv
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pprint import pprint

url = 'http://data.kk.dk/dataset/9070067f-ab57-41cd-913e-bc37bfaf9acd/resource/9fbab4aa-1ee0-4d25-b2b4-b7b63537d2ec/download/befkbhalderkoencivst.csv'
filename = url.split('/')[-1]

# if dataset does not exist locally, download it
if not os.path.exists(filename):
    response = requests.get(url, params={'downloadformat': 'csv'})

    if response.ok:
        with open(filename, 'wb') as f:
            f.write(response.content)

single_people = {}

with open(filename, encoding='latin-1') as file:
    reader = csv.reader(file)
    next(reader)  # skip headers

    for row in reader:
        year = int(row[0])
        city_part = int(row[1])
        age = int(row[2])
        marital_status = row[3]
        gender = int(row[4])
        persons = int(row[5])

        if 1992 <= year <= 2015 and city_part in (1, 2, 3) and 18 <= age <= 30 and marital_status not in ('G', 'P'):
            single_people.setdefault(year, {})
            single_people[year].setdefault(city_part, {})
            single_people[year][city_part].setdefault(gender, {})
            single_people[year][city_part][gender].setdefault(age, 0)
            single_people[year][city_part][gender][age] += persons

plot_m_1_keys, plot_m_1_values = list(zip(*[(year, sum(single_people[year][1][1].values())) for year in single_people]))
plot_f_1_keys, plot_f_1_values = list(zip(*[(year, sum(single_people[year][1][2].values())) for year in single_people]))
plot_m_2_keys, plot_m_2_values = list(zip(*[(year, sum(single_people[year][2][1].values())) for year in single_people]))
plot_f_2_keys, plot_f_2_values = list(zip(*[(year, sum(single_people[year][2][2].values())) for year in single_people]))
plot_m_3_keys, plot_m_3_values = list(zip(*[(year, sum(single_people[year][3][1].values())) for year in single_people]))
plot_f_3_keys, plot_f_3_values = list(zip(*[(year, sum(single_people[year][3][2].values())) for year in single_people]))

# create plot 1
plt.bar(plot_m_1_keys, plot_m_1_values, width=0.5, linewidth=0, align='center', color='blue', label='Male')
plt.bar(plot_f_1_keys, plot_f_1_values, width=0.5, linewidth=0, align='center', color='red', alpha=0.8, label='Female')
plt.legend(loc='upper left', fontsize=10)
plt.ticklabel_format(useOffset=False)
plt.title('Distribution of single persons (ages 18-30) in city part 1 (years 1992-2015)', fontsize=10)
plt.xlabel('Years from 1992 to 2015', fontsize=10)
plt.ylabel('Single persons', fontsize=10)
plt.tick_params(axis='both', which='major', labelsize=10)
plt.savefig('single_people_1.png', bbox_inches='tight')
plt.clf()

# create plot 2
plt.bar(plot_m_2_keys, plot_m_2_values, width=0.5, linewidth=0, align='center', color='blue', label='Male')
plt.bar(plot_f_2_keys, plot_f_2_values, width=0.5, linewidth=0, align='center', color='red', alpha=0.8, label='Female')
plt.legend(loc='upper left', fontsize=10)
plt.ticklabel_format(useOffset=False)
plt.title('Distribution of single persons (ages 18-30) in city part 2 (years 1992-2015)', fontsize=10)
plt.xlabel('Years from 1992 to 2015', fontsize=10)
plt.ylabel('Single persons', fontsize=10)
plt.tick_params(axis='both', which='major', labelsize=10)
plt.savefig('single_people_2.png', bbox_inches='tight')
plt.clf()

# create plot 3
plt.bar(plot_m_3_keys, plot_m_3_values, width=0.5, linewidth=0, align='center', color='blue', label='Male')
plt.bar(plot_f_3_keys, plot_f_3_values, width=0.5, linewidth=0, align='center', color='red', alpha=0.8, label='Female')
plt.legend(loc='upper left', fontsize=10)
plt.ticklabel_format(useOffset=False)
plt.title('Distribution of single persons (ages 18-30) in city part 3 (years 1992-2015)', fontsize=10)
plt.xlabel('Years from 1992 to 2015', fontsize=10)
plt.ylabel('Single persons', fontsize=10)
plt.tick_params(axis='both', which='major', labelsize=10)
plt.savefig('single_people_3.png', bbox_inches='tight')
plt.clf()
```

### Plot

![https://raw.githubusercontent.com/edipetres/Depressed_Year/master/5_cph_inhabitants/single_people_1.png](https://raw.githubusercontent.com/edipetres/Depressed_Year/master/5_cph_inhabitants/single_people_1.png)
![https://raw.githubusercontent.com/edipetres/Depressed_Year/master/5_cph_inhabitants/single_people_2.png](https://raw.githubusercontent.com/edipetres/Depressed_Year/master/5_cph_inhabitants/single_people_2.png)
![https://raw.githubusercontent.com/edipetres/Depressed_Year/master/5_cph_inhabitants/single_people_3.png](https://raw.githubusercontent.com/edipetres/Depressed_Year/master/5_cph_inhabitants/single_people_3.png)

## 3. Find the three most populated city parts(BYDEL), in 1992, 2000 and 2015

### Prerequisites

``` python
import csv
import collections
```

### Code

``` python
# Support danish non-ASCII characters
# -*- coding: utf-8 -*-

import csv
import collections

filename = "befkbhalderkoencivst.csv"

with open(filename) as f:   ## encoding='latin-1'
    reader = csv.reader(f)
    header_row = next(reader)

    ppl1992 = {}
    ppl2000 = {}
    ppl2015 = {}

    for row in reader:
        year = row[0]
        citypart = row[1]
        total_people92 = 0
        total_people2k = 0
        total_people15 = 0

        if(row[0] == '1992'):
            total_people92 += int(row[5])
        if(row[0] == '2000'):
            total_people2k += int(row[5])
        if(row[0] == '2015'):
            total_people15 += int(row[5])


        if citypart not in ppl1992.keys():
            ppl1992[citypart] = total_people92
        else:
            ppl1992[citypart] += total_people92

        if citypart not in ppl2000.keys():
            ppl2000[citypart] = total_people2k
        else:
            ppl2000[citypart] += total_people2k

        if citypart not in ppl2015.keys():
            ppl2015[citypart] = total_people15
        else:
            ppl2015[citypart] += total_people15


    ppl92_sorted = sorted(ppl1992, key=ppl1992.get, reverse=True)
    ppl2k_sorted = sorted(ppl2000, key=ppl2000.get, reverse=True)
    ppl15_sorted = sorted(ppl2015, key=ppl2015.get, reverse=True)
    ##print(ppl_sorted)
    for index, citypart in enumerate(ppl92_sorted[:3]):
        print('The number {} most populated city part in 1992 is {}.'.format(index+1,citypart))
    for index, citypart in enumerate(ppl2k_sorted[:3]):
        print('The number {} most populated city part in 2000 is {}.'.format(index+1,citypart))
    for index, citypart in enumerate(ppl15_sorted[:3]):
        print('The number {} most populated city part in 2015 is {}.'.format(index+1,citypart))

    print("City parts description:")
    print(" 1=Indre By, 2=Østerbro, 3=Nørrebro, 4=Vesterbro/Kgs. Enghave, 5=Valby, 6=Vanløse, 7=Brønshøj-Husum, 8=Bispebjerg, 9=Amager Øst, 10=Amager Vest, 99=Udenfor inddeling")
```

### Plot

![http://image.prntscr.com/image/b38cdeb82dbe4913a6e9533f315277da.png](http://image.prntscr.com/image/b38cdeb82dbe4913a6e9533f315277da.png)

## 4. Create to pie-charts, showing the distribution of marital status' in bydel 1, 2 and 3 in year 2000 and 2015

### Prerequisites

``` python
from __future__ import division
import requests
import os
import csv
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np
import collections
from pylab import *
```

### Code

``` python
from __future__ import division
import requests
import os
import csv
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np
import collections
from pylab import *


def getFile(url):
    fname = url.split('/')[-1]

    if os.path.isfile(fname):
        print("File found.")
    else:
        response = requests.get(url, params={'downloadformat': 'csv'})
        if response.ok:  # status_code == 200:
            with open(fname, 'wb') as f:
                f.write(response.content)
        print('Downloaded {}'.format(fname))
    return fname

def plotPieChart(mydict, title_param='Change me..'):
    val_sum = sum(mydict.values())
    values = mydict.values()
    fractions = [] # create fractions of 100
    for val in values:
        frac = (val * 100 / val_sum)
        fractions.append(frac)
    
    # make the plot
    figure(1, figsize=(7,7))
    labels = mydict.keys()
    pie(fractions, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    title(title_param)
    figtext(.02, .1, "E=Widdow\nF=Divorced\nG=Maried\nL=Oldest living partner\nO=Dissolved partnership\nP=Registered partnership\nU=Unmarried")
    show()



# get file to work with
url = 'http://data.kk.dk/dataset/9070067f-ab57-41cd-913e-bc37bfaf9acd/resource/9fbab4aa-1ee0-4d25-b2b4-b7b63537d2ec/download/befkbhalderkoencivst.csv'
fname = getFile(url)


with open(fname) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    statuses_2000 = {}
    statuses_2015 = {}

    for row in reader:
        year = int(row[0])
        bydel = int(row[1])

        if bydel in [1, 2, 3]:
            status = row[3]

            if year == 2000:
                if status not in statuses_2000.keys():
                    statuses_2000[status] = 1
                else:
                    statuses_2000[status] += 1
            if year == 2015:
                if status not in statuses_2015.keys():
                    statuses_2015[status] = 1
                else:
                    statuses_2015[status] += 1
        

    plotPieChart(statuses_2000, 'Marital statuses in 2000')
    plotPieChart(statuses_2015, 'Marital statuses in 2015')
    
```

### Plot

![https://raw.githubusercontent.com/edipetres/Depressed_Year/master/5_cph_inhabitants/marital_status_2000.png](https://raw.githubusercontent.com/edipetres/Depressed_Year/master/5_cph_inhabitants/marital_status_2000.png)
![https://raw.githubusercontent.com/edipetres/Depressed_Year/master/5_cph_inhabitants/marital_status_2015.png](https://raw.githubusercontent.com/edipetres/Depressed_Year/master/5_cph_inhabitants/marital_status_2015.png)
