# Program to check whether a number is an Armstrong number or not

num = int(input("Enter the number: "))

sum = 0
temp = num
digits = len(str(num))

while temp > 0:
    digit = temp % 10
    sum += digit ** digits
    temp //= 10

if sum == num:
    print(num, "is an Armstrong Number")
else:
    print(num, "is not an Armstrong Number")