# Which platform is the most popular in the regions NA, EU and Japan?

import csv
import pprint

filename = "vgsales.csv"

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    platforms = {}

    for row in reader:
        this_platform = row[2]
        if(this_platform not in platforms.keys()):
            platforms[this_platform] = 1
        else:
            platforms[this_platform] = platforms[this_platform] + 1

    print("Platforms: ")
    pprint.pprint(platforms)
    print("Max: "+max(platforms))

    maxvalue = 0
    maxkey = ''
    for key, value in platforms.items():
        
        if value > maxvalue:
            maxvalue = value
            maxkey = key
    
    print("maxvalue: " + str(maxvalue))
    print("maxkey: " + maxkey)
