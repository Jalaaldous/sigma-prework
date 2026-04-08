import datetime as dt

today = dt.date.today()

input_year = input("Please enter a date (day/month/year) ")
year_formatted = dt.datetime.strptime(input_year, "%d/%m/%Y").date()

age = today.year - year_formatted.year

if (today.month, today.day) < (year_formatted.month, year_formatted.day):
    age -= 1

print(age)
