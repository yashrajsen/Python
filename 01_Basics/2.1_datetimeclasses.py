# Working with data and time

# import the standard library of data time to access the date and time classes

from datetime import date
from datetime import time
from datetime import datetime

def main():
    #print today's date
    today = date.today()
    print("Today's date is ", today)

    # print individual components of today's date
    print("Date Components:", today.day," ", today.month," ", today.year)

    # retrieve today's weekday
    print("Weekday Number is:", today.weekday())
    days = ["Mon","Tues", "Wed","Thu","Fri","Sat","Sun"]
    print("Weekday is ", days[today.weekday()])

    #Datetime objects
    today = datetime.now()
    print("current date and time is", today)

    # get the time component
    t = datetime.time(datetime.now())
    print(t)


if __name__ == "__main__":
    main()

