# Qno.47
# Check if year is leap year.
# Difficult words:
# - leap year: year with 366 days

year = int(input("Enter year: "))

is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print("Leap year" if is_leap else "Not leap year")
