array = []

while True:
    num = input("Enter a number OR write 'done' to finish : ")
    if num.lower() == 'done':
        break
    else:
        try:
            array.append(int(num))
        except ValueError:
            print("Invalid input. Please enter a number or 'done' to finish....")
if array:
    largest = max(array)
    smallest =min(array) 
    print(f"The maximum number is {largest}")
    print(f"The minimum number is {smallest}")
else:
    print("No numbers were entered....")