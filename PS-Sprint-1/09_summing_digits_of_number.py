def sum_of_digits(num):
    total = 0
    while num > 0:
        digit = num % 10
        total += digit
        num //= 10
    return total

try:
    num = int(input("Enter a non-negative number to calculate the sum of digits of it : "))
    result = sum_of_digits(num)
    if num >= 0:
        print(f"The sum of digits of {num} is {result}.")
    else:
        print("Please, enter a non-negative number.")
except ValueError:
    print("Invalid input. Please, enter a valid non-negative integer....")
