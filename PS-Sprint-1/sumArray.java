import java.util.*;

class sumArray {
    public static int sum_array(int[] arr) {
        int sum = 0;
        for(int i = 0; i < arr.length; i++) {
            sum += arr[i];
        }

        return sum;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter Array length");
        int n = sc.nextInt();

        int[] arr = new int[n];
        
        for(int i = 0; i < n; i++){
            arr[i] = sc.nextInt();
        }

        int result = sum_array(arr);

        System.out.println(result);
    }
}
