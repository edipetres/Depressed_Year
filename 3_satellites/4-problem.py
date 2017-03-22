import csv

filename = 'satellite_dataset.csv'

with open(filename) as f:
    reader = csv.reader(f)
    next(reader)

    filtered_sats = [sat for sat in reader if str(sat[15]).strip()]  # filter out invalid weight data (empty strings)
    lightest_sat = filtered_sats[0]

    for sat in filtered_sats:
        # if the current satellite weight is smaller than the previous, set the new one
        if sat[15] < lightest_sat[15]:
            lightest_sat = sat

    # lightest_sat[0]   => "Official Name of Satellite"
    # lightest_sat[3]   => "Country of Operator/Owner"
    # lightest_sat[15]  => "Launch Mass (Kilograms)"
    print('The lightest satellite "{}" comes from {} and weighs {} kilograms.'.format(lightest_sat[0],
                                                                                      lightest_sat[3],
                                                                                      lightest_sat[15]))
