def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(yr, mnth):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month > 12 and month < 1:
        return "Invalid Month"

    if leap_year(year) and month == 2:
        return 29
    else:
        return f"The days in month you choose is {month_days[month -1]}"

year = int(input("Enter a year you want to check: "))
month = int(input("Enter a month you want to check: "))

days = days_in_month(year, month)
print(days)