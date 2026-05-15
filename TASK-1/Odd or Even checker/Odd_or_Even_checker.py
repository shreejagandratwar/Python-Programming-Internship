# Take input from the user and convert to an integer
number = int(input("Enter a number: "))

# Check if the remainder is 0
if number % 2 == 0:
    print(f"{number} is an Even number.")
else:
    print(f"{number} is an Odd number.")
