def check_palindrome(value):
    value_str = str(value)
    if value_str == value[::-1]:
        return f"{value} is a palindrome...."
    else:
        return f"{value} is not a palindrome...."
    
try:
    value = input("Enter a string or number to check if it is a Palindrome : ")
    result = check_palindrome(value)
    print(result)
except Exception as e:
    print("An error occurred: ", e)
