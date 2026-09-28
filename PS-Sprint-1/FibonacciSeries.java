import java.util.*;
public class FibonacciSeries{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Limit = ");
        int limit = sc.nextInt();
        int a = 0;
        int b = 1;

        while(a <= limit){
            System.out.print(a + " ");

            int c = a + b;
            a = b;
            b = c;
        }
        sc.close();
    }
}
