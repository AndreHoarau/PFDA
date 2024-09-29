# Program to read in CSV and input each line as a list.
# Author Andre Hoarau
import csv
filename="data.csv"
with open (filename,"rt") as fp:
    reader= csv.reader(fp, delimiter = ",")
    for line in reader:
        print (line)
