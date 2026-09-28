import java.util.*;
public class LeapYear{
    public static void main(String []args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the year: ");
        int year = sc.nextInt();
        //Check if Leap Year
        if(year % 4 == 0 && year % 100 != 0 || year % 400 ==0 ) {
            System.out.println("Leap Year");
        } else {
            System.out.println("Not a Leap Year");
        }
        sc.close();
    }
}