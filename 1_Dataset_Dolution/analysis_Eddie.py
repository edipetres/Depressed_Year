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

