import matplotlib
# Force matplotlib to not use any Xwindows backend.
matplotlib.use('Agg')
import csv
from collections import defaultdict
import matplotlib.pyplot as plt

movies = defaultdict(list)
filename = "movies.csv"

##movies = {}
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for row in reader:
        length = int(row[3])
        year = int(row[2])
        movies[year].append(length)

##print(movies)
x = movies.keys()
y = movies.values()
##print(x)
##print(y)

plt.scatter(x, y, s=50)
plt.title("Year to Length Connection", fontsize=14)
plt.xlabel("Year", fontsize=10)
plt.ylabel("Length", fontsize=10)
plt.show()
