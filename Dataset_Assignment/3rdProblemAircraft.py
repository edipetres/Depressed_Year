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
