"""
4. **Calculating Armstrong Numbers**  
   **Difficulty**: Easy  
   **Topics**: Basic Programming, Number Theory  
   **Description**: Write a program to check if a number is an Armstrong number.  
   **Example**:  
   Input: `number = 153`  
   Output: `Armstrong Number`  
   Explanation: 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153. 
"""
def armstrong(num):

    temp = num
    sum= 0
    while temp>0:
        digit=temp%10
        cube = digit ** len(str(num))
        sum= sum+cube
        temp//=10
    if sum == num:
        return "Number is Armstrong"
    else:
        return "Number is not Armstrong"
num = int(input("Enter the number : "))
print(armstrong(num))       