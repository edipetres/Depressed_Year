import csv
import os
import requests
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np

def getFile(url):
    fname = url.split('/')[-1]

    if os.path.isfile(fname):
        print("File found.")
    else:
        response = requests.get(url, params={'downloadformat': 'csv'})
        if response.ok:  # status_code == 200:
            with open(fname, 'wb') as f:
                f.write(response.content)
        print('Downloaded {}'.format(fname))
    return fname


url = 'http://vincentarelbundock.github.io/Rdatasets/csv/ggplot2/movies.csv'
filename = getFile(url)

ratings_dict = {}
lengths_dict = {}
title_lengths = {}
years_dict = {}
scatter_years = []
scatter_length = []
lengths_per_year_dict = {}
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    for row in reader:
        year = int(row[2])
        length = int(row[3])
        rating = float(row[5])
        title_length = len(row[1])

        if rating not in ratings_dict.keys():
            ratings_dict[rating] = 1
        else:
            ratings_dict[rating] += 1

        # To be able to show the majority on one graph, 
        # we ignore the few moves longer than 200 mins
        if length not in lengths_dict.keys():
            lengths_dict[length] = 1
        else:
            lengths_dict[length] += 1

        if title_length not in title_lengths.keys() and title_length < 70:
            title_lengths[title_length] = 1
        elif title_length < 70:
            title_lengths[title_length] += 1

        if year not in years_dict.keys():
            years_dict[year] = 1
        else:
            years_dict[year] += 1

        scatter_length.append(length)
        scatter_years.append(year)

        # Question 3: create median line for year and length of movies
        if year not in lengths_per_year_dict.keys():
            lengths_per_year_dict[year] = [length]
        else:
            lengths_per_year_dict[year].append(length)


# Calculate average length per year for median line
avg_length_per_year_dict = {}
for year, lengths_arr in lengths_per_year_dict.items():
    avg_length = sum(lengths_arr) / len(lengths_arr)
    avg_length_per_year_dict[year] = avg_length


plt.scatter(scatter_years, scatter_length, c='b', alpha=0.3, s=3)
plt.plot(avg_length_per_year_dict.keys(), avg_length_per_year_dict.values(), linewidth=2, label='Median line')
plt.title('Scatter plot with year and length of movies')
plt.xlabel('Year')
plt.ylabel('Length of movie')
plt.xlim(1890, 2010)
plt.ylim(-10,300)
plt.savefig('images/scatterplot_year_length')
plt.clf()


# Plot histogram for movie lengths
lengths_x_axis = lengths_dict.keys()
lengths_y_axis = lengths_dict.values()

plt.bar(lengths_x_axis, lengths_y_axis, width=1, linewidth=0, align='center', color='blue')
plt.ticklabel_format(useOffset=False)
plt.title("Histogram of movie lengths", fontsize=12)
plt.xlabel("Length", fontsize=10)
plt.ylabel("No. of movies", fontsize=10)
plt.tick_params(axis='both', which='major', labelsize=10)
plt.xticks(range(0,200, 10))
plt.xlim(-10, 200)
plt.ylim(-10,2000)
plt.savefig('images/length_dist.png')
plt.clf()


# Plot hisgoram for ratings
ratings_x_axis = ratings_dict.keys()
ratings_y_axis = ratings_dict.values()

plt.bar(ratings_x_axis, ratings_y_axis, width=0.07, linewidth=0, align='center', color='blue')
plt.ticklabel_format(useOffset=False)
plt.title('Movie ratings', fontsize=12)
plt.xlabel('Rating', fontsize=10)
plt.ylabel('No. of movies', fontsize=10)
plt.tick_params(axis='both', which='major', labelsize=10)
plt.xticks(range(1,11))
plt.savefig('images/ratings_dist.png')
plt.clf()


# Plot histogram for title lengths
title_len_x_axis = title_lengths.keys()
title_len_y_axis = title_lengths.values()

plt.bar(title_len_x_axis, title_len_y_axis, width=0.7, linewidth=0, align='center', color='blue')
plt.ticklabel_format(useOffset=False)
plt.title('Length of title', fontsize=12)
plt.xlabel('Char length', fontsize=10)
plt.ylabel('No. of movies', fontsize=10)
plt.tick_params(axis='both', which='major', labelsize=10)
plt.xticks(range(0,60, 5))
plt.savefig('images/title_length_distrib.png')
plt.clf()


# Plot histogram for release years
years_x_axis = years_dict.keys()
years_y_axis = years_dict.values()


plt.bar(years_x_axis, years_y_axis, width=0.7, linewidth=0, align='center', color='blue')
plt.ticklabel_format(useOffset=False)
plt.title('Distribution of movie releases by year', fontsize=12)
plt.xlabel('Years', fontsize=10)
plt.ylabel('No. of movies', fontsize=10)
plt.tick_params(axis='both', which='major', labelsize=10)
plt.xticks(range(1890,2010, 10), rotation=45)
plt.savefig('images/years_distrib.png')
plt.clf()

