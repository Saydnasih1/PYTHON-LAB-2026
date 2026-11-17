import calendar
def leap_year(year):
 if calendar.isleap(year):
  print ("Leap year")
 else:
  print ("Not a leap year")
y=int(input("Enter year: "))
leap_year(y)
