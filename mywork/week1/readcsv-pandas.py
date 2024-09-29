#Reading in the csv as a panadas table
# Author Andre Hoarau

FILENAME = "data.csv"
import pandas
df=pandas.read_csv(FILENAME)
print (df)