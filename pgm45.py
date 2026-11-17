import datetime

def dates():
    d = datetime.datetime.strptime(input("Enter date (DD-MM-YYYY): "), "%d-%m-%Y")

    print("Yesterday:", d - datetime.timedelta(days=1))
    print("Today:", d)
    print("Tomorrow:", d + datetime.timedelta(days=1))

dates()
