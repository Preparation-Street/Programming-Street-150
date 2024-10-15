import java.util.*;

class evenOdd{
    public static void even_Odd(int n){
        if(n%2 == 0){
            System.out.println("Even");
        }else{
            System.out.println("Odd");
        }
    } 

    public static void main(String args[]){
        Scanner sc  = new Scanner(System.in);
        int n  = sc.nextInt();

        even_Odd(n);

        sc.close();
    }
}

