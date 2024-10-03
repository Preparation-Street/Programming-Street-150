import java.util.*;

class Armstrong{
    public static void checkArmstrong(int n){
        int temp = n ;
        int sum  = 0;
        while(n>0){
            int digit = n % 10;
            n = n / 10;

            sum = sum + (digit*digit*digit); 
        }

        if(sum  == temp){
            System.out.println("Armstrong Number");
        }else{
            System.out.println("Not an Armstrong Number");
        }
    } 

    public static void main(String args[]){
        Scanner sc  = new Scanner(System.in);
        int n  = sc.nextInt();

        checkArmstrong(n);

        sc.close();
    }
}

