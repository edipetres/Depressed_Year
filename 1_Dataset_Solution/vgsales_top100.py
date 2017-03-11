import csv

filename = 'vgsales.csv'  # download file from url instead

with open(filename) as f:
    reader = csv.reader(f)
    next(reader)

    publishers = {}

    for i in range(100):
        row = next(reader)
        publisher = row[5]
        publishers.setdefault(publisher, 0)
        publishers[publisher] += 1

    pub_sorted_keys = sorted(publishers, key=publishers.get, reverse=True)

    for publisher in pub_sorted_keys:
        print('{} has {} game(s) in the top 100'.format(publisher, publishers[publisher]))

    print('\n{} has the most games in the top 100'.format(pub_sorted_keys[0]))
