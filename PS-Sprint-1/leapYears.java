import java.util.*;

class leapYears{
    public static String leap_Years(int year){
        if (year % 400 == 0) {
            return "Leap Year"; // Divisible by 400, it's a leap year
        } else if (year % 100 == 0) {
            return "Not a Leap Year"; // Divisible by 100 but not by 400, not a leap year
        } else if (year % 4 == 0) {
            return "Leap Year"; // Divisible by 4 but not by 100, it's a leap year
        } else {
            return "Not a Leap Year"; // Not divisible by 4, it's not a leap year
        }
    } 

    public static void main(String args[]){
        Scanner sc  = new Scanner(System.in);
        int n  = sc.nextInt();

        String x = leap_Years(n);

        System.out.println(x);

        sc.close();
    }
}


