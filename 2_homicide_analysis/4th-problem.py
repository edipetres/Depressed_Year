# What is the age of the youngest victim and the oldest victim?
import csv

filename = 'database.csv'
with open(filename) as file:
    reader = csv.reader(file)
    header_row = next(reader)

# victim age index = 12, perp = 16
    victim_ages = []
    for row in reader:
        age = int(row[12])
        if age < 150:
            victim_ages.append(age)

    print(victim_ages)
    print("Min victim age: " + str(min(victim_ages)))
    print("Max victim age: " + str(max(victim_ages)))
    #print(sorted(victim_ages))

