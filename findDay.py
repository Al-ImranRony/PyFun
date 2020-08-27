# What was the day when you born ?

import datetime
import calendar

def findDayName(date):
    born = datetime.datetime.strptime(date, '%d %m %Y').weekday()

    return (calendar.day_name[born])

birthDate = '17 04 2020'
print(f'"{birthDate}" is: ', findDayName(birthDate))