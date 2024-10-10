import java.util.*;

class vowelConsonants {
    public static boolean isVowel(char c){
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ;
    }


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String input = sc.nextLine().toLowerCase();
        
        int vowelCount = 0;
        int consonantCount  = 0;

        for(char c: input.toCharArray()){
            if(c >= 'a' && c <= 'z'){
                if(isVowel(c)){
                    vowelCount += 1;
                }else{
                    consonantCount += 1;
                }
            }
        }

        System.out.println("Vowels: " + vowelCount);
        System.out.println("Consonants: " + consonantCount);

        sc.close();
    }
}
