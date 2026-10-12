def check_prime_num(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            return False
    return True
try:
    num = int(input("Enter a integer number to check if it is a prime number : "))
    if check_prime_num(num):
        print(f"{num} is a prime number....")
    else:
        print(f"{num} is not a prime number....")
except ValueError:
    print("Invalid input. Please, enter a valid integer number.....")
