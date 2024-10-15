import java.util.Scanner;

class sumDigits {
     int sum_digits(int n){
        int sum  = 0;
        while(n>0){
            int digit = n%10;
            sum += digit;
            n = n/10;
        }

        return sum;
    }

    public static void main(String[] args) {
        sumDigits sd = new sumDigits();
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number: ");
        int n = sc.nextInt();
        System.out.println("Sum of digits of " + n + " is " + sd.sum_digits(n));
        sc.close();
    }
}
