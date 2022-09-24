
# Write a Python program to print the calendar of a given month and year.
import calendar

def main(month, year):
    print(calendar.month(year,month))

if __name__ == "__main__":
    month = 1
    year = 2022
    main(month, year)

