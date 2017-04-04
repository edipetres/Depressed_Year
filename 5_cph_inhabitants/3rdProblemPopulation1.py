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
