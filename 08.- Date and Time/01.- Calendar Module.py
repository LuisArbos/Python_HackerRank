"""
Calendar Module

The calendar module allows you to output calendars and provides additional useful functions for them.

class calendar.TextCalendar([firstweekday])

This class can be used to generate plain text calendars.

Task

You are given a date. Your task is to find what the day is on that date.

Input Format

A single line of input containing the space separated month, day and year, respectively, in MM DD YYYY
format.

"""
#Python 3:

# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

MM, DD, YYYY = map(int, input().split())

Cal = calendar.Calendar(firstweekday=0).itermonthdays4(YYYY, MM)

date_tuple = next((t for t in Cal if t[:3] == (YYYY, MM, DD)), None)
days_of_week = {
    0: "MONDAY",
    1: "TUESDAY",
    2: "WEDNESDAY",
    3: "THURSDAY",
    4: "FRIDAY",
    5: "SATURDAY",
    6: "SUNDAY"
}
print(days_of_week.get(date_tuple[3]))
    