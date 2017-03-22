# Highest and lowest HDI 

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
