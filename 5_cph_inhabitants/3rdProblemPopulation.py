import csv

filename = "befkbhalderkoencivst.csv"

with open(filename, encoding='latin-1') as f:
    reader = csv.reader(f)
    header_row = next(reader)

    ppl1992 = {}


    for row in reader:
        year = int(row[0])
        citypart = row[1]
        people = int(row[5])
        total_people = 0

        if(row[0] == 1992):
            total_people += people


        if citypart not in ppl1992.keys():
            ppl1992[citypart] = total_people
        else:
            ppl1992[citypart] += total_people


            ppl_sorted = sorted(ppl1992, key=ppl1992.get, reverse=True)
            ## for year, citypart in enumerate(ppl_sorted[:5]):
                ##print('The most populated city part in {} is {}.'.format(year,citypart))
            ##print(ppl_sorted)
            print(ppl1992)
