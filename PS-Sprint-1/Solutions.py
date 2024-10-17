# Problem 1: Odd/Even Number
def odd_even(n):
    """
    Checks if a number is even or odd.

    Parameters
    ----------
    n : int
        Number to check for even or odd.

    Returns
    -------
    bool
        True if n is even, False if n is odd.
    """
    if n % 2 == 0:
        # Return True if n is divisible by 2 (even)
        return True
    else:
        # Return False if n is not divisible by 2 (odd)
        return False
    
# Problem 2: Prime Number
def prime_number(n):
    """
    Checks if a number is prime.

    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

    Parameters
    ----------
    n : int
        Number to check for primality.

    Returns
    -------
    bool
        True if n is prime, False if not.
    """
    # Handle numbers less than or equal to 1 (not prime)
    if n <= 1:
        return False
    
    # Special case for 2 (the only even prime)
    elif n == 2:
        return True

    # Check divisibility by numbers from 2 to the square root of n
    for i in range(2, int(n**0.5) + 1):
        # If n is divisible by i, it's not prime
        if n % i == 0:
            return False
    
    # If no divisors found up to the square root, n is prime
    return True

# Problem 3: Leap Year
def is_leap(y):
    """
    Checks if a year is a leap year.

    Leap years are divisible by 4 except for end-of-century years which must be divisible by 400. This means that the year 2000 was a leap year, but the year 1900 was not.

    Parameters
    ----------
    y : int
        Year to check for leap year status.

    Returns
    -------
    bool
        True if y is a leap year, False if not.
    """
    # Condition 1: Divisible by 4 but not 100
    cond1 = y % 4 == 0 and y % 100 != 0
    # Condition 2: Divisible by 400
    cond2 = y % 400 == 0

    # If either condition is true, it's a leap year
    if (cond1 or cond2):
        return True
    # Else not a leap year
    else:
        return False

# Problem 4: Armstrong Number
def armstrong_number(num):

    """
    Checks if a number is an Armstrong number.

    An Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.

    Parameters
    ----------
    num : int
        Number to check for Armstrong number status.

    Returns
    -------
    bool
        True if num is an Armstrong number, False if not.
    """
    # Count the number of digits
    dig_count = 0
    temp = num
    while temp != 0:
        dig_count += 1
        temp = temp // 10
    
    # Calculate the sum of digits raised to the power of dig_count
    temp = num
    arm_num = 0
    while temp != 0:
        dig = temp % 10
        arm_num += dig ** dig_count
        temp = temp // 10
    
    # Check if the sum is equal to the original number
    return arm_num == num

# Problem 5: Fibonacci Series
def fibo_seq(n):
    """
    Generates the Fibonacci sequence up to the nth term.

    Parameters
    ----------
    n : int
        The number of terms in the Fibonacci sequence to generate.

    Returns
    -------
    list
        A list of the first n terms of the Fibonacci sequence, starting with 0 and 1.
    """
    # Initialize the first term to 0
    f_term = 0
    # Initialize the second term to 1
    s_term = 1
    # Create a list to store the sequence
    res_arr = [f_term, s_term]
    
    # Handle cases where n is less than or equal to 2
    if n <= 2:
        return res_arr
    
    # Generate the remaining terms using a while loop
    while n > 0:
        # Calculate the next term
        n_term = f_term + s_term
        # Append the next term to the list
        res_arr.append(n_term)
        # Update the first and second terms
        f_term, s_term = s_term, n_term
        # Decrement the counter
        n -= 1
    
    return res_arr

# Problem 6: Identify Palimdrome
def is_palimdrome(ele):
    """
    Checks if a given number or string is a palindrome.

    Parameters
    ----------
    ele : int or str
        The number or string to check.

    Returns
    -------
    bool
        True if the given element is a palindrome, False otherwise.
    """
    # Check if the element is an integer
    if type(ele) == int:
        temp = ele
        rev_num = 0
        
        # Continue the loop until all digits have been processed
        while temp != 0:
            # Extract the last digit of temp
            dig = temp % 10
            # Append the extracted digit to the reversed number
            rev_num = rev_num * 10 + dig
            # Remove the last digit from temp
            temp = temp // 10
        
        # Compare the original and reversed numbers
        return rev_num == ele
    
    # Check if the element is a string
    elif type(ele) == str:
        # Initialize an empty string to store the reversed characters
        rev_str = ""
        
        # Iterate over the characters in reverse order
        for i in range(len(ele)-1, -1, -1):
            # Append the current character to the reversed string
            rev_str += ele[i]
        
        # Compare the original and reversed strings
        return rev_str == ele

# Problem 7: Print star pattern
def pyramid_print(patternType, height):
    """
    Prints a pyramid pattern based on the given type and height.

    Parameters
    ----------
    patternType : str
        The type of pyramid pattern to print. Can be either "pyramid" or "diamond".
    height : int
        The height of the pyramid pattern.

    """
    def erect_pyramid(height):
        # Outer loop for rows
        for i in range(height):
            # Print spaces before stars
            for j in range(height - i - 1):
                print(" ", end="")
            # Print stars
            for j in range(2 * i + 1):
                print("*", end="")
            # Print spaces after stars
            for j in range(height - i - 1):
                print(" ", end="")
            print()  # Move to the next line
            
    def inverted_pyramid(height):
        # Outer loop for rows
        for i in range(height):
            # Print spaces before stars
            for j in range(i):
                print(" ", end="")
            # Print stars
            for j in range(2 * height - (2 * i + 1)):
                print("*", end="")
            # Print spaces after stars
            for j in range(i):
                print(" ", end="")
            print()  # Move to the next line

    if patternType == "pyramid":
        erect_pyramid(height)
    
    elif patternType == "diamond":
        erect_pyramid(height)
        inverted_pyramid(height)

# Problem 8: Find factorial
def factorial(num):
    """
    This function calculates the factorial of a given number.
    
    Parameters:
    num (int): The number to calculate the factorial of.
    
    Returns:
    int: The factorial of num.
    
    Edge cases:
    - If num is negative, it returns None.
    - If num is zero, it returns 1.
    """
    if num < 0:
        return None
    
    if num == 0:
        return 1
    
    # Initialize factorial to 1
    fact = 1
    # Loop until num becomes 0
    while num != 0:
        # Multiply factorial by num
        fact *= num
        # Decrement num
        num = num - 1
    
    return fact

# Problem 9: Summing Digits of a number
def digit_sum(num):
    """
    This function calculates the sum of digits of a given number.
    
    Parameters:
    num (int): The number to calculate the sum of digits of.
    
    Returns:
    int: The sum of the digits of num.
    """

    # Initialize the sum to 0
    dig_sum = 0

    # Loop until all digits are processed
    while num != 0:
        # Extract the last digit
        dig = num % 10
        # Add the digit to the sum
        dig_sum += dig
        # Remove the last digit from the number
        num = num // 10
    
    # Return the calculated sum
    return dig_sum

# Problem 10: GCD
def find_gcd(a, b):
    """
    This function finds the greatest common divisor (gcd) of two numbers.
    
    Parameters:
    a (int): The first number.
    b (int): The second number.
    
    Returns:
    int: The greatest common divisor of a and b.
    """
    # Initialize the GCD to 1
    gcd = 1
    # Iterate from 1 to the minimum of a and b
    for i in range(1, min(a, b) + 1):
        # Check if i divides both a and b
        if a % i == 0 and b % i == 0:
            # Update the GCD if i is a common divisor
            gcd = i
    
    return gcd

# Problem 11: LCM
def find_lcm(a, b):
    """
    This function finds the least common multiple (lcm) of two numbers.
    
    Parameters:
    a (int): The first number.
    b (int): The second number.
    
    Returns:
    int: The least common multiple of a and b.
    """
    # Find the greater of a and b
    greater = max(a, b)
    # Find the smaller of a and b
    smallest = min(a, b)
    # Iterate from the greater number to the product of a and b, incrementing by the greater number    
    for i in range(greater, a*b+1, greater):
        # Check if i is divisible by the smaller number    
        if i % smallest == 0:
            return i