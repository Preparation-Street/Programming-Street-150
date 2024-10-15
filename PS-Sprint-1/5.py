"""
5. **Generating the Fibonacci Series**  
   **Difficulty**: Easy  
   **Topics**: Basic Programming, Sequences  
   **Description**: Write a program to generate the Fibonacci series up to a given number.  
   **Example**:  
   Input: `limit = 10`  
   Output: `[0, 1, 1, 2, 3, 5, 8]`  
   Explanation: The Fibonacci series up to 10 is generated as [0, 1, 1, 2, 3, 5, 8].
"""

def fib(num):
    a=0
    b=1
    if num ==1:
        print(a)
    else:
        print(a , end = " ")    
        print(b , end = " ")
        
        for i in range (2,num):
            c=a+b
            print(c, end = " ")
            a=b
            b=c
num= int(input("Enter the Number: "))
fib(num)            