import java.util.Scanner;

class greatest_common_divisor {
    int gcd(int a, int b){
        if(b == 0){
            return a;
        }

        while(b!=0){
            int temp = b;
            b = a %b;
            a = temp;
        }

        return a;
    }

    public static void main(String[] args) {

        greatest_common_divisor g = new greatest_common_divisor();  
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the first number: ");
        int a = sc.nextInt();
        System.out.println("Enter the second number: ");
        int b = sc.nextInt();
        System.out.println("Greatest Common Divisor of " + a + " and " + b + " is " + g.gcd(a, b));
        sc.close();
        
    }
}
