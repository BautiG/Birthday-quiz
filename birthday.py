"""
birthday.py
Author: Bauti G
Credit: Vinzent and Liam S.
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
name=str(input("Hello, what is your name? "))
month=str(input("Hi {0}, what was the name of the month you were born in? ".format(name)))
year=int(input("And what year were you born in, {0}? ".format(name))
day=int(input("And the day? "))

from datetime import datetime
from calendar import month_name
todaymonth = datetime.today().month
todaydate = datetime.today().day
exc = 0
if month == "October" and day == 31:
    print("You were born on Halloween!")
    exc = 1

if month == "January":
    month = 1
if month == "February":
    month = 2
if month == "March":
    month = 3
if month == "April":
    month = 4
if month == "May":
    month = 5
if month == "June":
    month = 6
if month == "July":
    month = 7
if month == "August":
    month = 8
if month == "September":
    month = 9
if month == "October":
    month = 10
if month == "November":
    month = 11
if month == "December":
    month = 12
    
if month == todaymonth and todaydate == day:
    print("Happy birthday!")
    exc = 1
    
if year < 1980:
    time="Stone Age"
if year >= 1980 and year < 1990:
    time="eighties"
if year >= 1990 and year < 2000:
    time="nineties"
if year >= 2000:
    time="two thousands"
if exc == 0:
    if month == 12 or month == 1 or month == 2:
        monthbaby="winter baby"
    if month == 3 or month == 4 or month == 5:
        monthbaby="spring baby"
    if month == 6 or month == 7 or month == 8:
        monthbaby="summer baby"
    if month == 9 or month == 10 or month == 11:
        monthbaby="fall baby"
    print("{0}, you are a {1} of the {2}.".format(name, monthbaby, time))
