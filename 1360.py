# Input: date1 = "2020-01-15", date2 = "2019-12-31"
# Output: 15

from datetime import date


def daysBetweenDates(date1,date2):
    date1=date(date1)
    date2=date(date2)
    return (date2-date1)

date1 = "2020-01-15"
date2 = "2019-12-31"
print(daysBetweenDates(date1,date2))
