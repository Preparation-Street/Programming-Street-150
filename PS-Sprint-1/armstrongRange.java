import java.util.*;


public class armstrongRange {
    public static int[] rangeArmstrong(ArrayList<Integer> list) {
        int lower = list.get(0);
        int higher = list.get(1);
        ArrayList <Integer> arr = new ArrayList<>(); 

        for(int i=lower; i<=higher; i++) {
            int temp = i;
            int sum = 0;

            while (temp > 0) {
                int digit = temp % 10;
                sum += (digit * digit * digit);
                temp /= 10;
            }

            if(sum == i) {
                arr.add(i);
            }
        }


        int[] result = new int[arr.size()];
        for (int j = 0; j < arr.size(); j++) {
            result[j] = arr.get(j);
        }

        return result;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        ArrayList<Integer> range = new ArrayList<>();
        System.out.println("Enter Lower Range");
        int lower = sc.nextInt();

        System.out.println("Enter Higher Range");
        int higher = sc.nextInt();

        if(lower < higher) {
            range.add(lower);
            range.add(higher);

            range.trimToSize();

            int[] armstrongNumbers = rangeArmstrong(range);
            List<Integer> armstrongList = new ArrayList<>();

            for (int num : armstrongNumbers) {
                armstrongList.add(num);
            }
            
            // Print the Armstrong numbers found in the range
            System.out.println(armstrongList);
        }else {
            System.out.println("lower range cannot be higher than higher range.");
        }
    }
}
