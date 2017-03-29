import os
import requests
import csv
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/edipetres/Depressed_Year/master/Dataset_Assignment/AviationDataset.csv'
filename = url.split('/')[-1]

# if dataset does not exist locally, download it
if not os.path.exists(filename):
    response = requests.get(url, params={'downloadformat': 'csv'})

    if response.ok:
        with open(filename, 'wb') as f:
            f.write(response.content)

location_injuries = {}

with open(filename, encoding='latin-1') as file:
    reader = csv.reader(file)
    next(reader)  # skip headers

    for row in reader:
        # row[4]    => Location
        # row[5]    => Country
        # row[24]   => Total.Serious.Injuries
        # row[25]   => Total.Minor.Injuries

        if row[5] == 'United States':
            total_injuries = 0

            if row[24]:
                total_injuries += int(row[24])

            if row[25]:
                total_injuries += int(row[25])

            location_injuries.setdefault(row[4], 0)
            location_injuries[row[4]] += total_injuries

location_injuries_sorted = [(location, location_injuries[location]) for location in
                            sorted(location_injuries, key=location_injuries.get, reverse=True)]
top5_most_injuries = list(zip(*location_injuries_sorted[:5]))
locations = top5_most_injuries[0]
injuries = top5_most_injuries[1]

# create plot from processed data
plt.bar(range(len(locations)), injuries, width=0.5, linewidth=0, align='center')
plt.xticks(range(len(injuries)), locations, size='small')
plt.title('Top 5 locations with most injuries in the United States', fontsize=20)
plt.xlabel('Locations in the United States', fontsize=12)
plt.ylabel('Injuries', fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=7)
plt.savefig('top5_most_injuries_plot.png', bbox_inches='tight')
