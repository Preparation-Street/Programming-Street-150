"""
3. **Validating Leap Years**  
   **Difficulty**: Easy  
   **Topics**: Basic Programming, Date Handling  
   **Description**: Write a program to check if a given year is a leap year.  
   **Example**:  
   Input: `year = 2020`  
   Output: `Leap Year`  
   Explanation: 2020 is divisible by 4 but not by 100, or it is divisible by 400, so it is a leap year.
"""

def leap_year(year):
    if (year %4 ==0 and year % 100 !=0) or (year % 400 == 0):
        return "Leap Year"
    else:
        return "Not a Leap Year"
year = int(input("Enter Year: "))
print(leap_year(year))    