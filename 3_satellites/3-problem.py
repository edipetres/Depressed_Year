# Which country has the most satelites for military usage?

import csv
import pprint

filename = 'satellite_dataset.csv'
with open(filename) as file:
    reader = csv.reader(file)
    header_row = next(reader)

    for i, v in enumerate(header_row):
         first_row = next(reader)
         #print(i, v, first_row[i])

    ownersForMilitary = {}
    for row in reader:
        usedFor = row[4]
        ownedBy = row[3]

        if 'Military' in usedFor:
            if ownedBy not in ownersForMilitary.keys():
                ownersForMilitary[ownedBy] = 1
            else:
                ownersForMilitary[ownedBy] += 1
            

    
    pprint.pprint(ownersForMilitary)