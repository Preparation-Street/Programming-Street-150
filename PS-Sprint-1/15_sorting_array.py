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
    array.sort()
    print(f"The array sorted in ascending order is {array}.")
else:
    print("No numbers were entered....")