import java.util.*;
class sortArray  {
    public static int[] sort_array(int[] arr){
        // Bubble sort alogorithm
        for(int i = 0; i < arr.length - 1; i++){
            for(int j = 0; j < arr.length - i - 1; j++){
                if(arr[j] > arr[j + 1]){
                    // Swap arr[j] and arr[j + 1]
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
        return arr;
    }

    public static void main(String[] args) {
        Scanner sc  = new Scanner(System.in);

        System.out.println("Enter Array length");
        int n = sc.nextInt();

        int[] arr = new int[n];
        
        for(int i = 0; i < n; i++){
            arr[i] = sc.nextInt();
        }

        int[] result  = new int[n];

        result  = sort_array(arr);

        System.out.println(Arrays.toString(result));
        sc.close();
    }
}
