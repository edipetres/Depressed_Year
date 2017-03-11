## Questions we investigated: ##
1. Which platform is the most popular in the regions NA, EU and Japan? **Plamen Getsov**
2. How big a share of the global sales does the US sales cover? **Edmond Petres**
3. Which game genre is the most popular in 2012? **Emil Klausen**
4. Which publisher has the most titles in top 100? **Lucas Meulengracht Fredmark**


## Question No.1 ##
> Which platform is the most popular in the regions NA, EU and Japan?

```python
import csv
from collections import Counter

filename = "vgsales.csv"

with open(filename) as f:
reader = csv.reader(f)
header_row = next(reader)
platform_counter = 0

#    NAcheck = None
#    EUcheck = None
#    JPcheck = None

#us_sales = row[6]
#eu_sales = row[7]
#jp_sales = row[8]
#print(us_sales)

#    if (us_sales > eu_sales and us_sales > jp_sales):
#        NAcheck = True
#    if (eu_sales > us_sales and eu_sales > jp_sales):
#        EUcheck = True
#    if (jp_sales > us_sales and jp_sales > eu_sales):
#        JPcheck = True

platform = (row[2] for row in csv.reader(f))
print("Most used platform: {0}".format(Counter(platform).most_common()[0][0]))
```


## Question No.2 ##
> How big a share of the global sales does the US sales cover?

```python
import csv

filename = "vgsales.csv"

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    global_sales = 0.0
    us_sales = 0.0
    for row in reader:
        global_sales += float(row[10])
        us_sales += float(row[6])
    
    us_share = (us_sales * 100) / global_sales

    print('\n\nWhat is the proportion of US sales compared to global statistics?\n')
    print("Global sales: \t " + '%.3f' % global_sales)
    print("US sales: \t " + '%.3f' % us_sales)
    print("US share: \t" + "%.2f" % us_share + "% of global sales")
```

which prints:

```
What is the proportion of US sales compared to global statistics?

Global sales:    8920.440
US sales:        4392.950
US share:       49.25% of global sales
```


## Question No.3 ##
> Which game genre is the most popular in 2012?

```python
import pandas as pd

filename = 'vgsales.csv'

bef_stats_df = pd.read_csv(filename)
dd = bef_stats_df.as_matrix()

count = {};
for mylist in dd[:,4]:
    count.setdefault(mylist, 0)
    count[mylist] += 1;

print(count)
```

which prints:

```
{'Sports': 2346, 'Puzzle': 582, 'Simulation': 867, 'Shooter': 1310, 'Platform': 886, 'Adventure': 1286, 'Strategy': 681, 'Role-Playing': 1488, 'Racing': 1249, 'Action': 3316, 'Misc': 1739, 'Fighting': 848}
```


## Question No.4 ##
> Which publisher has the most titles in top 100?

```python
import csv

filename = 'vgsales.csv' # download file from url instead

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
```

which prints:

```
Nintendo has 52 game(s) in the top 100
Activision has 14 game(s) in the top 100
Take-Two Interactive has 9 game(s) in the top 100
Sony Computer Entertainment has 8 game(s) in the top 100
Microsoft Game Studios has 6 game(s) in the top 100
Electronic Arts has 5 game(s) in the top 100
Ubisoft has 2 game(s) in the top 100
SquareSoft has 1 game(s) in the top 100
Atari has 1 game(s) in the top 100
Sega has 1 game(s) in the top 100
Bethesda Softworks has 1 game(s) in the top 100

Nintendo has the most games in the top 100
```
