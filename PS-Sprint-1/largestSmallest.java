import java.util.*;

class largestSmallest {
    public static int[] largest_smallest(int[] arr){

        int[] number = new int[2];  // Declares an array of 5 integers

        int largest = arr[0];
        int smallest = arr[0];

        for(int i = 0; i < arr.length; i++){
            if(arr[i] > largest){
                largest = arr[i];
            }
        }

        for(int i = 0; i < arr.length; i++){
            if(arr[i] < smallest){
                smallest = arr[i];
            }
        }

        number[0] = largest;
        number[1] = smallest;

        return number;
    }

    public static void main(String[] args) {
        Scanner sc  = new Scanner(System.in);

        System.out.println("Enter Array length");
        int n = sc.nextInt();

        int[] arr = new int[n];
        
        for(int i = 0; i < n; i++){
            arr[i] = sc.nextInt();
        }

        int[] result = largest_smallest(arr);

        System.out.println("largest: "+ result[0]);
        System.out.println("Smallest: "+ result[1]);
    }
}
