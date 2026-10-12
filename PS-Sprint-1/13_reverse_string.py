def reverse_str(string):
    return string[::-1]

try:
    string = input("Enter a string to reverse : ")
    result = reverse_str(string)
    print(f"Reversed string : {result}")
except Exception as e:
    print(f"An error occurred: {e}")