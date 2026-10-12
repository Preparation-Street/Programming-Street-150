def check_even_odd(num):
    if num%2 == 0:
        return "This is an Even Number...."
    else:
        return "This is an Odd Number...."
try:
    num = int(input("Enter a number to determine Even or Odd : "))       
    result = check_even_odd(num)
    print(result)
except ValueError:
    print("Invalid Input. Please enter a valid integer....")
