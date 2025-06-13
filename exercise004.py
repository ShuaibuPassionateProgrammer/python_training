import datetime
import time
import calendar

print("1. Get current time: ")
print("2. Get current date: ")
print("3. Get calendar: ")
option = input("Select one of the following options above: ")

if option == "1":
    print("Current Time: " + time.strftime("%H:%M:%S"))
elif option == "2":
    print("Current Date: " + time.strftime("%d/%m/%Y"))
elif option == "3":
    month = int(input("Enter month (1-12): "))
    year = int(input("Enter year: "))

    print(calendar.month(year, month))
