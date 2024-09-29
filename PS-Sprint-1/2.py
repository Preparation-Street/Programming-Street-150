"""
2. **Checking for Prime Numbers**  
   **Difficulty**: Easy  
   **Topics**: Basic Programming, Number Theory  
   **Description**: Write a program to determine if a number is prime.  
   **Example**:  
   Input: `number = 7`  
   Output: `Prime`  
   Explanation: 7 has no divisors other than 1 and itself, so it is a prime number."""
   
number = int(input("Enter a Number : "))
if number == 1 or number ==0:
    print ("Number is not a Prime Number")
    
for i in range (2,number):
    if (number % i) == 0:
        print ("Number is not a Prime Number")
        break
else:
    print ("Number is a Prime Number")        
       