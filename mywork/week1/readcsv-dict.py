#Simple program to read in a csv file  as a dict
#Author andre hoarau

import csv

FILENAME = "data.csv"

with open (FILENAME, "rt") as fp:
    reader =csv.DictReader(fp, delimiter= "," , quoting= csv.QUOTE_NONNUMERIC)
    total = 0
    for line in reader:
        total += line['id']
        print (line)
        print (total)
