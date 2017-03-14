import csv

filename = 'database.csv'

with open(filename) as f:
    reader = csv.reader(f)
    next(reader)  # skip headers

    state_count = {}

    for row in reader:
        row = next(reader)
        state_name = row[5]
        state_count.setdefault(state_name, 0)
        state_count[state_name] += 1

    state_sorted_keys = sorted(state_count, key=state_count.get, reverse=True)

    for index, state_name in enumerate(state_sorted_keys[:10]):
        print('Rank {}\t{} with {} homicides'.format(index + 1, state_name, state_count[state_name]))
