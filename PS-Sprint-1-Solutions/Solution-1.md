#PS-Sprint-1-Solution

## 1. Determining Even/Odd Numbers

```java

public class EvenOdd {
    public static void main(String[] args) {
        int number = 4;
        if (number % 2 == 0) {
            System.out.println("Even");
        } else {
            System.out.println("Odd");
        }
    }
}

```

## 2. Checking for Prime Numbers

```java
public class PrimeNumber {
    public static void main(String[] args) {
        int number = 7;
        boolean isPrime = true;
        for (int i = 2; i <= Math.sqrt(number); ; i++) { 
            if (number % i == 0) {
                isPrime = false;
                break;
            }
        }
        if (isPrime) {
            System.out.println("Prime");
        } else {
            System.out.println("Not Prime");
        }
    }
}

```

## 3. Validating Leap Years

```java

public class LeapYear {
    public static void main(String[] args) {
        int year = 2020;
        if (year % 4 == 0 && (year % 100 != 0 || year % 400 == 0)) {
            System.out.println("Leap Year");
        } else {
            System.out.println("Not a Leap Year");
        }
    }
}

```

## 4. Calculating Armstrong Numbers

```java
public class ArmstrongNumber {
    public static void main(String[] args) {
        int number = 153, original = number, result = 0;
        while (original != 0) {
            int digit = original % 10;
            result += Math.pow(digit, 3);
            original /= 10;
        }
        if (result == number) {
            System.out.println("Armstrong Number");
        } else {
            System.out.println("Not an Armstrong Number");
        }
    }
}


```

## 5. Generating the Fibonacci Series

```java
public class FibonacciSeries {
    public static void main(String[] args) {
        int limit = 10;
        int a = 0, b = 1;
        while (a <= limit) {
            System.out.print(a + " ");
            int next = a + b;
            a = b;
            b = next;
        }
    }
}

```

## 6. Identifying Palindromes

```java
public class Palindrome {
    public static void main(String[] args) {
        String str = "radar";
        String rev = new StringBuilder(str).reverse().toString();
        if (str.equals(rev)) {
            System.out.println("Palindrome");
        } else {
            System.out.println("Not a Palindrome");
        }
    }
}


```

## 7. Crafting Star Patterns (Pyramid)

```java
public class StarPattern {
    public static void main(String[] args) {
        int height = 5;
        for (int i = 1; i <= height; i++) {
            for (int j = 1; j <= height - i; j++) {
                System.out.print(" ");
            }
            for (int k = 1; k <= (2 * i - 1); k++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}

```

## 8. Finding the Factorial of a Number

```java
public class Factorial {
    public static void main(String[] args) {
        int number = 5;
        int factorial = 1;
        for (int i = 1; i <= number; i++) {
            factorial *= i;
        }
        System.out.println(factorial);
    }
}

```

## 9. Summing Digits of a Number

```java
public class SumOfDigits {
    public static void main(String[] args) {
        int number = 1234, sum = 0;
        while (number != 0) {
            sum += number % 10;
            number /= 10;
        }
        System.out.println(sum);
    }
}


```

## 10. Finding the Greatest Common Divisor (GCD)

```java
public class GCD {
    public static void main(String[] args) {
        int a = 48, b = 18;
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        System.out.println(a);
    }
}

```

## 11. Finding the Least Common Multiple (LCM)

```java
public class LCM {
    public static void main(String[] args) {
        int a = 12, b = 15;
        int lcm = (a * b) / gcd(a, b);
        System.out.println(lcm);
    }

    private static int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
}

```

## 12. Counting Vowels and Consonants in a String

```java
public class VowelConsonantCounter {
    public static void main(String[] args) {
        String str = "hello world";
        int vowelCount = 0, consonantCount = 0;

        str = str.toLowerCase();  // Convert the string to lowercase for easier comparison

        for (int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);
            if (ch >= 'a' && ch <= 'z') {  // Check if it's an alphabetic character
                if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u') {
                    vowelCount++;
                } else {
                    consonantCount++;
                }
            }
        }

        System.out.println("Vowels: " + vowelCount);
        System.out.println("Consonants: " + consonantCount);
    }
}

```

## 13. Reversing a String

```java
public class ReverseString {
    public static void main(String[] args) {
        String str = "programming";
        String reversed = "";

        for (int i = str.length() - 1; i >= 0; i--) {
            reversed += str.charAt(i);
        }

        System.out.println("Reversed String: " + reversed);
    }
}

```

## 14. Finding the Largest and Smallest Numbers in an Array

```java
import java.util.Arrays;

public class LargestSmallestInArray {
    public static void main(String[] args) {
        int[] array = {4, 7, 1, 8, 5};
        int smallest = array[0];
        int largest = array[0];

        for (int num : array) {
            if (num > largest) {
                largest = num;
            }
            if (num < smallest) {
                smallest = num;
            }
        }

        System.out.println("Largest: " + largest + ", Smallest: " + smallest);
    }
}

```

## 15. Sorting an Array

```java
import java.util.Arrays;

public class SortArray {
    public static void main(String[] args) {
        int[] array = {3, 1, 4, 1, 5, 9};
        Arrays.sort(array);

        System.out.println("Sorted Array: " + Arrays.toString(array));
    }
}


```

## 16. Finding the Sum of Elements in an Array

```java
public class SumOfArrayElements {
    public static void main(String[] args) {
        int[] array = {1, 2, 3, 4, 5};
        int sum = 0;

        for (int num : array) {
            sum += num;
        }

        System.out.println("Sum of Elements: " + sum);
    }
}

```

## 17. Checking for Armstrong Numbers in a Range

```java
public class ArmstrongInRange {
    public static void main(String[] args) {
        int lower = 1, upper = 500;

        for (int num = lower; num <= upper; num++) {
            int sum = 0, temp = num, digits = String.valueOf(num).length();

            while (temp != 0) {
                int digit = temp % 10;
                sum += Math.pow(digit, digits);
                temp /= 10;
            }

            if (sum == num) {
                System.out.println(num + " is an Armstrong number.");
            }
        }
    }
}
```

## 18. Generating Multiplication Tables

```java
public class MultiplicationTable {
    public static void main(String[] args) {
        int number = 4;

        for (int i = 1; i <= 10; i++) {
            System.out.println(number + " x " + i + " = " + number * i);
        }
    }
}
```

## 19. Finding Prime Numbers in a Range

```java
public class PrimeInRange {
    public static void main(String[] args) {
        int lower = 10, upper = 30;

        for (int num = lower; num <= upper; num++) {
            boolean isPrime = true;

            if (num == 1) continue;  // Skip 1 as it's neither prime nor composite

            for (int i = 2; i <= num / 2; i++) {
                if (num % i == 0) {
                    isPrime = false;
                    break;
                }
            }

            if (isPrime) {
                System.out.println(num + " is a prime number.");
            }
        }
    }
}
```

## 20. Checking for Perfect Numbers

```java
public class PerfectNumber {
    public static void main(String[] args) {
        int num = 28;
        int sum = 0;

        for (int i = 1; i < num; i++) {
            if (num % i == 0) {
                sum += i;
            }
        }

        if (sum == num) {
            System.out.println(num + " is a perfect number.");
        } else {
            System.out.println(num + " is not a perfect number.");
        }
    }
}
```

## 21. Calculating the Sum of Even Numbers in a Range

```java
public class SumEvenInRange {
    public static void main(String[] args) {
        int lower = 1, upper = 10;
        int sum = 0;

        for (int i = lower; i <= upper; i++) {
            if (i % 2 == 0) {
                sum += i;
            }
        }

        System.out.println("Sum of even numbers: " + sum);
    }
}
```

## 22. Calculating the Sum of Odd Numbers in a Range

```java
public class SumOddNumbers {
    public static void main(String[] args) {
        int start = 1, end = 10;
        int sum = 0;
        for (int i = start; i <= end; i++) {
            if (i % 2 != 0) {
                sum += i;
            }
        }
        System.out.println("Sum of odd numbers: " + sum);
    }
}
```

## 23. Finding the Fibonacci Number at a Specific Position

```java
public class FibonacciNumber {
    public static void main(String[] args) {
        int position = 5;
        System.out.println("Fibonacci number at position " + position + " is: " + fibonacci(position));
    }

    public static int fibonacci(int n) {
        if (n <= 1) return n;
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
}
```

## 24. Printing Prime Numbers Less Than a Given Number

```java
public class PrimeNumbers {
    public static void main(String[] args) {
        int limit = 20;
        for (int i = 2; i < limit; i++) {
            if (isPrime(i)) {
                System.out.print(i + " ");
            }
        }
    }

    public static boolean isPrime(int num) {
        if (num <= 1) return false;
        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) return false;
        }
        return true;
    }
}
```

## 25. Finding the Number of Digits in a Number

```java
public class NumberOfDigits {
    public static void main(String[] args) {
        int number = 12345;
        System.out.println("Number of digits: " + Integer.toString(number).length());
    }
}
```

## 26. Checking if a Number is a Narcissistic Number

```java
public class NarcissisticNumber {
    public static void main(String[] args) {
        int number = 153;
        System.out.println(number + " is a Narcissistic Number: " + isNarcissistic(number));
    }

    public static boolean isNarcissistic(int num) {
        int sum = 0, temp = num, digits = Integer.toString(num).length();
        while (temp > 0) {
            int digit = temp % 10;
            sum += Math.pow(digit, digits);
            temp /= 10;
        }
        return sum == num;
    }
}
```

## 27. Generating a Pattern of Numbers

```java
public class NumberPattern {
    public static void main(String[] args) {
        int rows = 3;
        int num = 1;
        for (int i = 1; i <= rows; i++) {
            for (int j = 1; j <= i; j++) {
                System.out.print(num++ + " ");
            }
            System.out.println();
        }
    }
}
```

## 28. Finding the Sum of the Digits of the Factorial of a Number

```java

import java.math.BigInteger;

public class SumOfFactorialDigits {
    public static void main(String[] args) {
        int number = 4;
        BigInteger factorial = factorial(number);
        System.out.println("Sum of the digits of " + number + "! is: " + sumOfDigits(factorial));
    }

    public static BigInteger factorial(int n) {
        BigInteger result = BigInteger.ONE;
        for (int i = 2; i <= n; i++) {
            result = result.multiply(BigInteger.valueOf(i));
        }
        return result;
    }

    public static int sumOfDigits(BigInteger number) {
        int sum = 0;
        String str = number.toString();
        for (char c : str.toCharArray()) {
            sum += Character.getNumericValue(c);
        }
        return sum;
    }
}
```

## 29. Finding the Largest Palindrome in a String

```java
public class LargestPalindrome {
    public static void main(String[] args) {
        String string = "babad";
        System.out.println("Largest palindrome: " + longestPalindrome(string));
    }

    public static String longestPalindrome(String s) {
        if (s == null || s.length() < 1) return "";
        int start = 0, end = 0;
        for (int i = 0; i < s.length(); i++) {
            int len1 = expandAroundCenter(s, i, i);
            int len2 = expandAroundCenter(s, i, i + 1);
            int len = Math.max(len1, len2);
            if (len > end - start) {
                start = i - (len - 1) / 2;
                end = i + len / 2;
            }
        }
        return s.substring(start, end + 1);
    }

    private static int expandAroundCenter(String s, int left, int right) {
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }
        return right - left - 1;
    }
}
```

## 30. Finding Missing Numbers in a Sequence

```java
import java.util.HashSet;

public class MissingNumbers {
    public static void main(String[] args) {
        int[] sequence = {1, 2, 4, 5};
        System.out.println("Missing numbers: " + findMissingNumbers(sequence, 5));
    }

    public static HashSet<Integer> findMissingNumbers(int[] arr, int n) {
        HashSet<Integer> numbers = new HashSet<>();
        for (int num : arr) {
            numbers.add(num);
        }
        HashSet<Integer> missingNumbers = new HashSet<>();
        for (int i = 1; i <= n; i++) {
            if (!numbers.contains(i)) {
                missingNumbers.add(i);
            }
        }
        return missingNumbers;
    }
}
```

## 31. Generating Pascal’s Triangle

```java
import java.util.ArrayList;
import java.util.List;

public class PascalsTriangle {
    public static void main(String[] args) {
        int rows = 4;
        List<List<Integer>> triangle = generate(rows);
        for (List<Integer> row : triangle) {
            System.out.println(row);
        }
    }

    public static List<List<Integer>> generate(int numRows) {
        List<List<Integer>> triangle = new ArrayList<>();
        for (int i = 0; i < numRows; i++) {
            List<Integer> row = new ArrayList<>();
            row.add(1);
            for (int j = 1; j < i; j++) {
                row.add(triangle.get(i - 1).get(j - 1) + triangle.get(i - 1).get(j));
            }
            if (i > 0) row.add(1);
            triangle.add(row);
        }
        return triangle;
    }
}
```

## 32. Finding the Median of an Array

```java
import java.util.Arrays;

public class MedianOfArray {
    public static void main(String[] args) {
        int[] array = {3, 1, 2, 4, 5};
        System.out.println("Median: " + findMedian(array));
    }

    public static double findMedian(int[] nums) {
        Arrays.sort(nums);
        int length = nums.length;
        if (length % 2 == 0) {
            return (nums[length / 2 - 1] + nums[length / 2]) / 2.0;
        } else {
            return nums[length / 2];
        }
    }
}
```

## 33. Calculating the Power of a Number

```java
public class PowerOfNumber {
    public static void main(String[] args) {
        int base = 2, exponent = 3;
        System.out.println(base + " raised to the power of " + exponent + " is: " + Math.pow(base, exponent));
    }
}


```

## 34. Checking for an Anagram

```java
import java.util.Arrays;

public class AnagramCheck {
    public static void main(String[] args) {
        String string1 = "listen", string2 = "silent";
        System.out.println("Are anagrams: " + areAnagrams(string1, string2));
    }

    public static boolean areAnagrams(String s1, String s2) {
        char[] array1 = s1.toCharArray();
        char[] array2 = s2.toCharArray();
        Arrays.sort(array1);
        Arrays.sort(array2);
        return Arrays.equals(array1, array2);
    }
}
```

## 35. Finding the Sum of Prime Numbers in a Range

```java
public class SumPrimeNumbers {
    public static void main(String[] args) {
        int start = 1, end = 10;
        System.out.println("Sum of prime numbers: " + sumOfPrimes(start, end));
    }

    public static int sumOfPrimes(int start, int end) {
        int sum = 0;
        for (int i = start; i <= end; i++) {
            if (isPrime(i)) {
                sum += i;
            }
        }
        return sum;
    }

    public static boolean isPrime(int num) {
        if (num <= 1) return false;
        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) return false;
        }
        return true;
    }
}
```

## 36. Finding the N-th Triangular Number

```java
public class TriangularNumber {
    public static void main(String[] args) {
        int N = 4;
        System.out.println("The " + N + "-th triangular number is: " + triangularNumber(N));
    }

    public static int triangularNumber(int N) {
        return N * (N + 1) / 2;
    }
}
```

## 37. Checking for Perfect Squares

```java
public class PerfectSquareCheck {
    public static void main(String[] args) {
        int number = 16;
        System.out.println(number + " is a perfect square: " + isPerfectSquare(number));
    }

    public static boolean isPerfectSquare(int num) {
        int sqrt = (int) Math.sqrt(num);
        return num == sqrt * sqrt;
    }
}
```

## 38. Finding the Sum of Squares of Digits

```java
public class SumOfSquaresOfDigits {
    public static void main(String[] args) {
        int number = 123;
        System.out.println("Sum of squares of digits: " + sumOfSquares(number));
    }

    public static int sumOfSquares(int num) {
        int sum = 0;
        while (num > 0) {
            int digit = num % 10;
            sum += digit * digit;
            num /= 10;
        }
        return sum;
    }
}
```

## 39. Generating a Square Matrix of a Given Size

```java
public class SquareMatrixGenerator {
    public static void main(String[] args) {
        int size = 3;
        generateMatrix(size);
    }

    public static void generateMatrix(int size) {
        int num = 1;
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                System.out.print(num++ + " ");
            }
            System.out.println();
        }
    }
}
```

## 40. Calculating the Sum of Digits of a Number Until Single Digit

```java
public class SumDigitsUntilSingleDigit {
    public static void main(String[] args) {
        int number = 9875;
        System.out.println("Sum of digits until single digit: " + sumUntilSingleDigit(number));
    }

    public static int sumUntilSingleDigit(int num) {
        while (num >= 10) {
            int sum = 0;
            while (num > 0) {
                sum += num % 10;
                num /= 10;
            }
            num = sum;
        }
        return num;
    }
}
```

## 41. Finding the Count of Specific Digits in a Number

```java
public class CountSpecificDigit {
    public static void main(String[] args) {
        int number = 122333;
        int digit = 3;
        System.out.println("Count of digit " + digit + ": " + countDigit(number, digit));
    }

    public static int countDigit(int num, int digit) {
        int count = 0;
        while (num > 0) {
            if (num % 10 == digit) {
                count++;
            }
            num /= 10;
        }
        return count;
    }
}
```

## 42. Generating a Fibonacci Sequence Using Recursion

```java
import java.util.ArrayList;
import java.util.List;

public class RecursiveFibonacci {
    public static void main(String[] args) {
        int number = 5;
        List<Integer> fibonacciSequence = new ArrayList<>();
        for (int i = 0; i < number; i++) {
            fibonacciSequence.add(fibonacci(i));
        }
        System.out.println("Fibonacci sequence up to " + number + ": " + fibonacciSequence);
    }

    public static int fibonacci(int n) {
        if (n <= 1) return n;
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
}
```

## 43. Finding All Divisors of a Number

```java
import java.util.ArrayList;
import java.util.List;

public class DivisorsFinder {
    public static void main(String[] args) {
        int number = 12;
        System.out.println("Divisors of " + number + ": " + findDivisors(number));
    }

    public static List<Integer> findDivisors(int num) {
        List<Integer> divisors = new ArrayList<>();
        for (int i = 1; i <= num; i++) {
            if (num % i == 0) {
                divisors.add(i);
            }
        }
        return divisors;
    }
}
```

## 44. Finding the Average of Numbers in an Array

```java
public class AverageOfArray {
    public static void main(String[] args) {
        int[] array = {1, 2, 3, 4, 5};
        System.out.println("Average: " + calculateAverage(array));
    }

    public static double calculateAverage(int[] array) {
        int sum = 0;
        for (int num : array) {
            sum += num;
        }
        return (double) sum / array.length;
    }
}
```

## 45. Finding the Mode of Numbers in an Array

```java
import java.util.HashMap;
import java.util.Map;

public class ModeFinder {
    public static void main(String[] args) {
        int[] array = {1, 2, 2, 3, 4, 4, 4};
        System.out.println("Mode: " + findMode(array));
    }

    public static int findMode(int[] array) {
        Map<Integer, Integer> frequencyMap = new HashMap<>();
        int maxCount = 0, mode = -1;

        for (int num : array) {
            int count = frequencyMap.getOrDefault(num, 0) + 1;
            frequencyMap.put(num, count);
            if (count > maxCount) {
                maxCount = count;
                mode = num;
            }
        }
        return mode;
    }
}
```

## 46. Determining the Length of a String Without Using Built-In Functions4

```java
public class StringLength {
    public static void main(String[] args) {
        String str = "hello";
        System.out.println("Length of the string: " + findLength(str));
    }

    public static int findLength(String str) {
        int length = 0;
        for (char c : str.toCharArray()) {
            length++;
        }
        return length;
    }
}
```

## 47. Generating a Number Pyramid

```java
public class NumberPyramid {
    public static void main(String[] args) {
        int rows = 4;
        generatePyramid(rows);
    }

    public static void generatePyramid(int rows) {
        for (int i = 1; i <= rows; i++) {
            for (int j = 1; j <= i; j++) {
                System.out.print(j);
            }
            System.out.println();
        }
    }
}

```

## 48. Finding the Sum of Prime Factors of a Number

```java
public class SumOfPrimeFactors {
    public static void main(String[] args) {
        int number = 12;
        System.out.println("Sum of prime factors: " + sumOfPrimeFactors(number));
    }

    public static int sumOfPrimeFactors(int num) {
        int sum = 0;
        for (int i = 2; i <= num; i++) {
            if (num % i == 0 && isPrime(i)) {
                sum += i;
                while (num % i == 0) {
                    num /= i;
                }
            }
        }
        return sum;
    }

    public static boolean isPrime(int n) {
        if (n <= 1) return false;
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) return false;
        }
        return true;
    }
}
```

## 49. Finding the Second Largest Number in an Array

```java
public class SecondLargestNumber {
    public static void main(String[] args) {
        int[] array = {10, 20, 4, 45, 99};
        System.out.println("Second largest number: " + findSecondLargest(array));
    }

    public static int findSecondLargest(int[] array) {
        int largest = Integer.MIN_VALUE;
        int secondLargest = Integer.MIN_VALUE;

        for (int num : array) {
            if (num > largest) {
                secondLargest = largest;
                largest = num;
            } else if (num > secondLargest && num < largest) {
                secondLargest = num;
            }
        }
        return secondLargest;
    }
}
```

## 50. Finding the Longest Substring Without Repeating Characters

```java
import java.util.HashSet;

public class LongestSubstringWithoutRepeating {
    public static void main(String[] args) {
        String string = "abcabcbb";
        System.out.println("Longest substring without repeating characters: " + longestSubstring(string));
    }

    public static String longestSubstring(String s) {
        int start = 0, maxLength = 0, maxStart = 0;
        HashSet<Character> set = new HashSet<>();

        for (int end = 0; end < s.length(); end++) {
            while (set.contains(s.charAt(end))) {
                set.remove(s.charAt(start));
                start++;
            }
            set.add(s.charAt(end));
            if (end - start + 1 > maxLength) {
                maxLength = end - start + 1;
                maxStart = start;
            }
        }
        return s.substring(maxStart, maxStart + maxLength);
    }
}
```
