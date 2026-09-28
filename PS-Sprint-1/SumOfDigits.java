import java.util.*;
public class SumOfDigits {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number: ");
        int n = sc.nextInt();
        
        int sum = 0;
        int digit = 0;

        while(n > 0){
            digit = n % 10;
            sum = sum + digit;
            n = n / 10;
        }
        System.out.println("The sum of the digits: " + sum);
        sc.close();
    }
}
