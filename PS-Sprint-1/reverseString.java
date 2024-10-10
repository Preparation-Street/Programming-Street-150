import java.util.*;

class reverseString {
    public static String reverse_string(String original){
        StringBuilder reversed = new StringBuilder();

        // Loop through the original string in reverse order
        for (int i = original.length() - 1; i >= 0; i--) {
            reversed.append(original.charAt(i));  // Append each character in reverse order
        }

        return reversed.toString();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String original = sc.nextLine();

        String revString = reverse_string(original);

        System.out.println(revString);
        sc.close();
    }
}
