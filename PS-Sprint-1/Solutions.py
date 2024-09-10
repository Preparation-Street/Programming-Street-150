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
        return True
    else:
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
    if n <= 1:
        return False
    
    elif n == 2:
        return True

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
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
    cond1 = y % 4 == 0 and y % 100 != 0
    cond2 = y % 400 == 0

    if (cond1 or cond2):
        return True
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
    dig_count = 0
    temp = num
    
    while temp != 0:
        dig_count += 1
        temp = temp // 10
    
    temp = num
    arm_num = 0
    while temp != 0:
        dig = temp % 10
        arm_num += dig ** dig_count
        temp = temp // 10
    
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
    f_term = 0
    s_term = 1
    res_arr = [f_term, s_term]

    if n <= 2:
        return res_arr
    
    while n > 0:
        n_term = f_term + s_term
        res_arr.append(n_term)
        f_term, s_term = s_term, n_term
        n -= 1
    
    return res_arr

# Problem 6: Identify Palimdrome
def palimdrome(ele):
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
    if type(ele) == int:
        temp = ele
        rev_num = 0
        while temp != 0:
            dig = temp % 10
            rev_num = rev_num * 10 + dig
            temp = temp // 10
        
        return rev_num == ele
    
    elif type(ele) == str:
        rev_str = ""
        for i in range(len(ele)-1, -1, -1):
            rev_str += ele[i]
        
        return rev_str == ele

# Problem 7: Print star pattern