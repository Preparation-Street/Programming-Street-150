import java.util.*;

class checkPrime{
    public static boolean check_Prime(int n){
        if (n <= 1) {
            return false; // numbers less than or equal to 1 are not prime
        }

        // Checking divisibility from 2 to sqrt(n)
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                return false; // n is divisible by i, so it's not prime
            }
        }

        return true; // n is prime
    } 

    public static void main(String args[]){
        Scanner sc  = new Scanner(System.in);
        int n  = sc.nextInt();

        boolean x = check_Prime(n);

        System.out.println(x);

        sc.close();
    }
}


