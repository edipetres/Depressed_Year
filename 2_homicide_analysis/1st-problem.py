# Most common ethnicity for victims and perpetrators

import csv

filename = 'database.csv'
with open(filename) as file:
    reader = csv.reader(file)
    header_row = next(reader)

#    for i, v in enumerate(header_row):
#         first_row = next(reader)
#         print(i, v, first_row[i])

    vict_ethn = {}
    perp_ethn = {}

    for row in reader:
        victim = row [14]
        perpetrator = row [18]

        if victim not in vict_ethn.keys():
            vict_ethn[victim] = 1
        else:
            vict_ethn[victim] += 1

        if perpetrator not in perp_ethn.keys():
            perp_ethn[perpetrator] = 1
        else:
            perp_ethn[perpetrator] += 1

    print("Most common ethnicity for victims: " + max(vict_ethn))
    print("Most common ethnicity for perpetrators: " + max(perp_ethn))


    
