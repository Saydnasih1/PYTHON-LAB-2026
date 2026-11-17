import datetime

def display():
    d = datetime.datetime.now()
    print("Date and Time:", d)
    print("Year:", d.year)
    print("Month:", d.month)
    print("Week Number:", d.strftime("%U"))
    print("Weekday:", d.strftime("%A"))
    print("Day of Year:", d.strftime("%j"))
    print("Day of Month:", d.day)
    print("Day of Week:", d.weekday())

display()
