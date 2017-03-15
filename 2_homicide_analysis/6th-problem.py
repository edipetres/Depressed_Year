import csv

filename = 'database.csv'

with open(filename) as file:
    reader = csv.reader(file)
    next(reader)  # skip headers

    perp_gender_count = {}

    for row in reader:
        row = next(reader)
        gender_name = row[15]
        perp_gender_count.setdefault(gender_name, 0)
        perp_gender_count[gender_name] += 1

    total_perp_count = sum(perp_gender_count.values())

    for gender_name, gender_count in perp_gender_count.items():
        gender_percentage = float(gender_count / total_perp_count) * 100
        print('There are {}% ({}) {} perpetrators.'.format(round(gender_percentage, 2), gender_count, gender_name.lower()))
