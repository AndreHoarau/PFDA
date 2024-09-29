#Modify this program so we can deal with the header line seperately
#Author Andre Hoarau
import csv
filename="data.csv"
with open (filename,"rt") as fp:
    reader= csv.reader(fp, delimiter = ",")
    linecount = 0
    for line in reader:
        if linecount == 0:
            print(f'This is the first line')
        else: 
            print (line)
        linecount +=1