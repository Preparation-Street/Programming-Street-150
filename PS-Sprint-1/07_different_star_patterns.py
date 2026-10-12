def pyramid(num):
    print("Pyramid Pattern: ")
    for i in range(num):
        print(" " * (num - (i + 1)), end="")
        print("* " * (i + 1))

def diamond(num):
    print("Diamond Pattern: ")
    for i in range (num):
        print(" " * (num - (i + 1)), end="")
        print("* " * (i + 1))
    for i in range(num):
        print(" " * (i + 1), end="")
        print("* " * (num - (i + 1)))

print("Choose a pattern to print : ")
print("1. Pyramid")
print("2. Diamond")

try:
    choice = int(input("Enter your choice(1 or 2) : "))
    num = int (input("Enter the number of row or height : "))
    if choice == 1:
        pyramid(num)
    elif choice == 2:
        diamond(num)
    else:
        print("Invalid choice. Please, enter 1 or 2....")
except Exception as e:
    print("An error occurred: ", e)
