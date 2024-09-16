age = input("What is your current age? ")

years_left = 90 - int(age)
days_left = years_left * 365
# weeks_left = days_left // 7
# months_left = days_left // 30

weeks_left = years_left * 52
months_left = years_left * 12

message = f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left to living like larry!"

print(message)
