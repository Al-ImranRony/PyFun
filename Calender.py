# Default calendar show in python

import calendar

year = 2020
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for month in months:
    print(calendar.month(year, month))