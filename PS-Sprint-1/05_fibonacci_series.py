def fibonacci_series(num):
    series = []
    a,b = 0,1
    while a <= num:
        series.append(a)
        a,b = b,a+b
    return series

try:
    num = int(input("Enter a number to generate the Fibonacci Sequence up to that number : "))
    result = fibonacci_series(num)
    if num<0:
        print("Please enter a non-negative number....")
    else:
        print("The Fibonacci Series is : ", result)
except ValueError:
    print("Invalid input. Please, enter a valid integer number....")
