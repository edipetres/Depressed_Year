import csv

best_countries = ['Norway', 'Australia',
                  'Switzerland', 'Denmark', 'Netherlands']
best_countries_purpose = {}

last_countries = ['Niger', 'Central African Republic', 'Eritrea', 'Chad', 'Burundi']
last_countries_purpose = {}

filename = "satellite_dataset.csv"

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for row in reader:
        purpose = row[5]
        country = row[3]
        
        if country in best_countries:    
            best_countries_purpose[country] = purpose
        
        if country in last_countries:
            last_countries_purpose[country] = purpose
    
    print("The purpose of the satellites for the top 5 countries \n" + str(best_countries_purpose))
    print("The purpose of the satellites for the lowest 5 countries \n" + str(last_countries_purpose))

