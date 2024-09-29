#Simple program to read in a csv file 
#Author andre hoarau

import csv

FILENAME = "data.csv"

with open (FILENAME, "rt") as fp:
    reader =csv.reader(fp, delimiter= "," , quoting= csv.QUOTE_ALL)
    linecount = 0
    total = 0
    for line in reader:
        if not linecount: #first row ie header row.
            print (f"{line} \n ---------") 
            #first row
        else: # all subsequnt rows
            total += int(line[0])
            print (line)
        linecount +=1
