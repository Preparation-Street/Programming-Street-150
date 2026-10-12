def gcd(a,b):
    while b != 0:
        a, b = b, a%b
    return a

try:
    num1 = int(input("Enter the first non-negative integer : "))
    num2 = int(input("Enter the second non-negative integer :"))
    result = gcd(num1, num2)

    if num1 < 0 or num2 < 0:
        print("Please, enter non-negative integers only....")
    else: 
        print(f"The Greatest Common Divisor of {num1} and {num2} is {result}")
except ValueError:
    print("Invalid input. Please, enter valid non-negative integers....")
