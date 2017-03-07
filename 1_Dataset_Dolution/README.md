## Questions we investigated: ##
1. Which platform is the most popular in the regions NA, EU and Japan? **Plamen Getsov**
2. How big a share of the global sales does the US sales cover? **Edmond Petres**
3. Which game genre is the most popular in 2012? **Emil Klausen**
4. Which publisher has the most titles in top 100? **Lucas Meulengracht Fredmark**


## Question No.2 ##
>How big a share of the global sales does the US sales cover?

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
