# Author Andre Hoarau
# Following jupyter notebook 1
# Breakout 4
# Write a function (named number_days_between) that:

# Takes two arguments that are 8-digit integers of the form YYYYMMDD (actually a date), and
# Returns the number of days between the two dates.
# For instance:

   # number_days_between(20200617, 20200619) = 2
   # number_days_between(20200619, 20100219) = 3773

import datetime

date1= input("Input date one in format YYYYMMDD: ")
date2= input("Input date two in format YYYYMMDD: ")


def number_days_between (date1,date2):
   format = "%Y%m%d"
   date1 =datetime.datetime.strptime(date1, format)
   date2 =datetime.datetime.strptime(date2, format)
   difference = (date1 - date2).days
   return difference

days_between= number_days_between(date1,date2)
print(f"Number of days between the two dates: {days_between}")
