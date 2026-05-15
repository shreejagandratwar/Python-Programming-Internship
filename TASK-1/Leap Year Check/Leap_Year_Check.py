def check_leap_year(year):
    # Leap year condition: divisible by 4 and (not divisible by 100 OR divisible by 400)
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False


# Execution block
try:
    target_year = int(input("Enter a year to check: "))

    if check_leap_year(target_year):
        print(f"{target_year} is a leap year.")
    else:
        print(f"{target_year} is not a leap year.")
except ValueError:
    print("Please enter a valid whole number for the year.")
