## Which country has the most military-purpose satellites?

import csv

filename = "satellites.csv"

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    military_sats_count = {}

    for row in reader:
        row = next(reader)
        sat_owner = row[3]
        if(str(row[4]) == 'Military'):
            military_sats_count.setdefault(sat_owner, 0)
            military_sats_count[sat_owner] += 1



print("The country with most military-purpose satellites is: " + max(military_sats_count))
