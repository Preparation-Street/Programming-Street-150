import java.util.Scanner;

class palindromeNumber {
    public static String checkPalindrome(String original) {
        String reversed = "";
        
        // Reversing the string by adding characters in reverse order
        for (int i = original.length() - 1; i >= 0; i--) {
            reversed += original.charAt(i);
        }

        // Comparing original and reversed strings
        if (original.equals(reversed)) {
            return "Palindrome";
        } else {
            return "Not a Palindrome";
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String original = sc.nextLine();

        String result = checkPalindrome(original);

        System.out.println(result);
        sc.close();
    }
}
