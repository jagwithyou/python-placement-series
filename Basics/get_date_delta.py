
# Write a Python program to calculate number of days between two dates.
from datetime import date
def main(input_start_date, input_end_date):
    start_date = date(*input_start_date)
    end_date = date(*input_end_date)
    delta = end_date-start_date
    print(delta.days)

if __name__ == "__main__":
    start_date = (2022, 7, 2)
    end_date = (2022, 8, 2)
    main(start_date, end_date)

