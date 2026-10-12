def gcd(a,b):
    while b != 0:
        a, b = b, a%b
    return a

def lcm(a,b):
    if a == 0 or b == 0:
        return 0
    return (a*b) / gcd(a,b)

try:
    num1 = int(input("Enter the first non-negative integer number : "))
    num2 = int(input("Enter the second non-negative integer number : "))
    result = lcm(num1,num2)

    if num1 < 0 or num2 < 0:
        print("Please, enter non-negative numbers....")
    else:
        print(f"The Least Common Multiple of {num1} and {num2} is {result}")
except ValueError:
    print("Invalid input. Please, enter valid non-negative integers....")