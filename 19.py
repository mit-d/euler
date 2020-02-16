# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

from datetime import date, timedelta

day = date(1900, 1, 1)
ct = 0

while day < date(2000, 1, 1):
    if day.weekday() == 6 and day.day == 1:
        ct = ct + 1
    day = day + timedelta(1)
print(ct)
