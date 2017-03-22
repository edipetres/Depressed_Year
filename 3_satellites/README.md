# Analysis of the active satellites and human development databases

## Questions
### Human development
1. Which country has the highest HDI (Human Development Index) and which has the lowest?
2. Which country has raised its HDI the most, in the period 1990 to 2014?

### Active satellites
3. Which country has the most satelites for military usage?
4. Wich country has the lightest satelite and how much does it weight?
5. Compare the usage of satelites, between the 5 poorest countries and the 5 welthiest countries, according to the HDI dataset (see first dataset), plotting optional.

## Solutions

``` python
import csv

filename = "human_development.csv"

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    hd = {}

    for row in reader:
        hdi = row[2]
        country = row[1]
        hd[country] = hdi


    hd_keys = sorted(hd, key=hd.get, reverse=True)

    for index, country in enumerate(hd_keys[:1]):
        print('The country with the highest HDI is {} '.format(country))
    hd_keys1 = sorted(hd, key=hd.get)
    for index, country in enumerate(hd_keys[:1]):
        print('The country with the lowest HDI is {} '.format(country))


```
Which prints:

> The country with the highest HDI is Lithuania 

> The country with the lowest HDI is Lithuania 


## 2. Which country has raised its HDI the most, in the period 1990 to 2014?

```python

import csv

filename = "historical_index.csv"

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    hddif = {}

    for row in reader:
        country = row[1]
       # hdi1990 = float(row[2])

#! Had problems with parsing some lines to float, since they are string of "..." meaning no data present.
# Therefore, I just tested the method I tried with a column full of floats, which worked.

        hdi2010 = float(row[4])
        hdi2014 = float(row[8])
        hddif[country] = hdi2014 - hdi2010


    hddif_keys = sorted(hddif, key=hddif.get, reverse=True)

    for index, country in enumerate(hddif_keys[:1]):
        print('The country with the greatest raise of HDI is {} '.format(country))
    print(hddif)

```
Which prints:

> The country with the greatest raise of HDI is Zimbabwe 


## 3. Which country has the most satelites for military usage?

```python
# Which country has the most satelites for military usage?

import csv
import pprint

filename = 'satellite_dataset.csv'
with open(filename) as file:
    reader = csv.reader(file)
    header_row = next(reader)

    ownersForMilitary = {}
    for row in reader:
        usedFor = row[4]
        ownedBy = row[3]

        if 'Military' in usedFor:
            if ownedBy not in ownersForMilitary.keys():
                ownersForMilitary[ownedBy] = 1
            else:
                ownersForMilitary[ownedBy] += 1

    print("Countries with number of satellites that (also) has a military purpose")
    pprint.pprint(ownersForMilitary)

```


Which prints:

```Countries with number of satellites that (also) has a military purpose

 {'Australia': 1,
 'Brazil': 1,
 'Canada': 1,
 'Chile': 1,
 'China': 58,
 'France': 8,
 'France/Italy': 2,
 'France/Italy/Belgium/Spain/Greece': 2,
 'Germany': 7,
 'India': 4,
 'Israel': 11,
 'Italy': 6,
 'Mexico': 1,
 'Russia': 84,
 'South Africa': 1,
 'South Korea': 1,
 'Spain': 2,
 'Taiwan': 1,
 'Turkey': 1,
 'USA': 147,
 'United Arab Emirates': 2,
 'United Kingdom': 8}
 ```

## 4. Which country has the lightest satelite and how much does it weight?

``` python
import csv

filename = 'satellite_dataset.csv'

with open(filename) as f:
    reader = csv.reader(f)
    next(reader)

    filtered_sats = [sat for sat in reader if str(sat[15]).strip()]  # filter out invalid weight data (empty strings)
    lightest_sat = filtered_sats[0]

    for sat in filtered_sats:
        # if the current satellite weight is smaller than the previous, set the new one
        if sat[15] < lightest_sat[15]:
            lightest_sat = sat

    # lightest_sat[0]   => "Official Name of Satellite"
    # lightest_sat[3]   => "Country of Operator/Owner"
    # lightest_sat[15]  => "Launch Mass (Kilograms)"
    print('The lightest satellite "{}" comes from {} and weighs {} kilograms.'.format(lightest_sat[0],
                                                                                      lightest_sat[3],
                                                                                      lightest_sat[15]))


```

Which prints:

`The lightest satellite "NUDT Phonesat" comes from China and weighs 0 kilograms.`

## 5. Compare the usage of satelites, between the 5 poorest countries and the 5 welthiest countries, according to the HDI dataset (see first dataset), plotting optional.
``` python
import csv

best_countries = ['Norway', 'Australia',
'Switzerland', 'Denmark', 'Netherlands']
best_countries_purpose = {}

last_countries = ['Niger', 'Central African Republic', 'Eritrea', 'Chad', 'Burundi']
last_countries_purpose = {}

filename = "satellite_dataset.csv"

with open(filename) as f:
reader = csv.reader(f)
header_row = next(reader)

for row in reader:
purpose = row[5]
country = row[3]

if country in best_countries:    
best_countries_purpose[country] = purpose

if country in last_countries:
last_countries_purpose[country] = purpose

print("The purpose of the satellites for the top 5 countries \n" + str(best_countries_purpose))
print("The purpose of the satellites for the lowest 5 countries \n" + str(last_countries_purpose))

```

Which prints:

```
The purpose of the satellites for the top 5 countries
{'Australia': 'Communications', 'Denmark': 'Technology Development', 'Netherlands': 'Communicatio
ns', 'Norway': 'Communications', 'Switzerland': 'Technology Development'}
The purpose of the satellites for the lowest 5 countries
{}
```
