def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        result = 1
        for i in range(2, num + 1):
            result *= i
        return result

try:
    num = int(input("Enter a non-negative integer number to compute its factorial : "))
    result = factorial(num)
    if num > 0:
        print(f"The Factorial of {num} is {result}")
    else:
        print("Factorial is not defined for negative numbers....")
except ValueError:
    print("Invalid input. Please, enter a non-negative integer....")
