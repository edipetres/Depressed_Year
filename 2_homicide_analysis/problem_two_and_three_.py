import csv
import pprint
import operator

filename = 'database.csv'

with open(filename) as file_object:
    reader = csv.reader(file_object)
    header_row = next(reader)

    for i, v in enumerate(header_row):
        first_row = next(reader)
        #print(i, v, first_row[i])
      
    weaponsmale = {}
    weaponsfemale = {}
    print("Going looping: ")
    for row in reader:
        if(str(row[15]) == 'Male'):
            if(str(row[20])) in weaponsmale.keys():
                weaponsmale[row[20]] = weaponsmale[row[20]] + 1
            else:
                weaponsmale[row[20]] = 1
        if(str(row[15]) == 'Female'):
            if(str(row[20])) in weaponsfemale.keys():
                weaponsfemale[row[20]] = weaponsfemale[row[20]] + 1
            else:
                weaponsfemale[row[20]] = 1    
                
    sorted_x = sorted(weaponsmale.items(), key=operator.itemgetter(1))
    sorted_y = sorted(weaponsfemale.items(), key=operator.itemgetter(1))
    print("Male")
    pprint.pprint(sorted_x)
    print("Women")
    pprint.pprint(sorted_y)
    
    print("The weapon mostly used by MALES are: " + max(weapons, key=weapons.get))
    print("The weapon mostly used by FEMALES are: " + max(weapons, key=weapons.get))
    
