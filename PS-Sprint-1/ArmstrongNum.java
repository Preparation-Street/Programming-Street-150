import java.util.*;
public class ArmstrongNum{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int n = sc.nextInt();
        int original = n;
        int sum = 0;

        while(n>0){
            int digit = n % 10;
            sum = sum + digit*digit*digit;
            n=n/10;
        }
        if(sum == original){
            System.out.println("Armstrong Number");
        } else {
            System.out.println("Not a Armstrong Number");
        }
        sc.close();
    }
}