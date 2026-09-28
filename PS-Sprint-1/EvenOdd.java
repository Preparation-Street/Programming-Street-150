import java.util.*;
public class EvenOdd{
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the number: ");
        int n = sc.nextInt();

        //check if no. is Even/Odd
        if(n % 2 == 0){
            System.out.println("Even Number");
        } else {
            System.out.println("Odd Number");
        }
        sc.close();
    }
}
