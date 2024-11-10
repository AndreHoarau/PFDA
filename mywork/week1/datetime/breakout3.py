# Following jupyter notebook 1
#Breakout 3
# Create a time object with 5 microseconds and 39 minutes.
import datetime
#Breakout 3
#Create an arbitrary date object and add five weeks. Print the new date.

date1= datetime.date.today()
increment = datetime.timedelta(weeks= 5)
newdate =date1 + increment
print(newdate)