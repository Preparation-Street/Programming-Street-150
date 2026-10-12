def check_leap_year(year):
    if (year%4 == 0 and year%100 != 0) or year%400 == 0:
        return f"{year} is a leap year...."
    else:
        return f"{year} is a common year...."
try:
    year = int(input("Enter a year to check if it is a leap year or a common year : "))
    result = check_leap_year(year)
    print(result)
except ValueError:
    print("Invalid input. Please enter a valid year....")
