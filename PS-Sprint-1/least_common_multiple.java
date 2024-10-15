import java.util.Scanner;
class least_common_multiple {
    int lcm(int a, int b){
        int gcd = gcd(a, b);
        return Math.abs(a*b)/gcd;
    }

    int gcd(int a, int b){
        if(b == 0){
            return a;
        }

        while(b!=0){
            int temp = b;
            b = a%b;
            a = temp;
        }
        return a;
    }

    public static void main(String[] args) {
        least_common_multiple lcm = new least_common_multiple();
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the first number: ");
        int a = sc.nextInt();
        System.out.println("Enter the second number: ");
        int b = sc.nextInt();
        System.out.println("Least Common Multiple of " + a + " and " + b + " is " + lcm.lcm(a, b));
        sc.close();
    }
}
