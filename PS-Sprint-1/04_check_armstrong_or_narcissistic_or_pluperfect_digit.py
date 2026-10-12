def check_armstrong_num(num):
    digits = str(num)
    num_digits = len(digits)
    total = sum(int(digit)**num_digits for digit in digits)
    if total == num:
        return f"{num} is an Armstrong Number...."
    else:
        return f"{num} is not an Armstrong Number...."

try:
    num = int(input("Enter a number to check if it is a Armstrong Number : "))
    result =  check_armstrong_num(num)
    print(result)
except ValueError:
    print("Invalid input. Please enter a valid integer....")
