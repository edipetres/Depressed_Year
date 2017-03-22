# Greatest difference between 1990 and 2014 HDI

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
