import csv

filename = 'database.csv'

with open(filename) as file_object:
    reader = csv.reader(file_object)
    header_row = next(reader)

    for i, v in enumerate(header_row):
        first_row = next(reader)
        print(i, v, first_row[i])

    age_sum = 0
    age_count = 0
    for row in reader:
        age_sum += int(row[12])
        age_count = age_count + 1
        
    average_age = age_sum / age_count
    print("Average age: " + str(average_age))
