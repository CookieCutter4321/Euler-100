"""
You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?


Mon Tues Wed Thurs Fri Sat Sun

Let's keep a pointer every time we go up a day and bruteforce
"""

days_in_months = {
    1: 31,
    2: 28, # on leap years this turns into 29
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}
#Q: How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
res = 0
# 1 Jan 1900 is Monday
day = 1 
month = 1 
year = 1900

day_of_week = 1 # 1 = mon, 2 = tues, 3 = wed, 4 = thurs, 5 = fri, 6 = sat, 7 = sun. We are looking for multiples of seven

while year <= 2000:
    
    if day == 1 and day_of_week % 7 == 0 and year >= 1901:
        res += 1

    # calculate next date after increment
    is_leap_year = year % 400 == 0 if year % 100 == 0 else year % 4 == 0
    month_limit = days_in_months[month]
    if month == 2 and is_leap_year:
        month_limit = 29 # special case for leap years in which February has 29 days

    day += 1
    day_of_week += 1
    if day > month_limit: # move to the newer month
        day = 1
        month += 1
    if month > 12: # new year
        month = 1
        year += 1
print(res)