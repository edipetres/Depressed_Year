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
