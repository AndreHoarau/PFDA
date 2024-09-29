#Modify the program to calculate the average age
# Author Andre Hoarau
import csv
filename="data.csv"
with open (filename,"rt") as fp:
    reader= csv.reader(fp, delimiter = ",")
    linecount = 0
    total = 0
    for line in reader:
        if linecount == 0:
            print(f'This is the first line')
        else: 
            total += int(line[1])
        linecount +=1
    print(f'average is {total/(linecount-1)}')
# alternative 
'''with open (DATADIR + FILENAME, "rt") as fp:
reader = csv.reader(fp, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
linecount = 0
total = 0
for line in reader:
if not linecount: # first row ie header row
pass
else: # all subsequent rows
total += line[1] # why 1
linecount += 1
print (f"average is {total/(linecount-1)}") # why -1 ?'''