import java.util.Scanner;

class pattern {
    public static void printPyramid(int height) {
        for (int i = 1; i <= height; i++) {
            // Print leading spaces
            for (int j = 1; j <= height - i; j++) {
                System.out.print(" ");
            }
            
            // Print stars
            for (int k = 1; k <= 2 * i - 1; k++) {
                System.out.print("*");
            }
            
            // Move to the next line after printing each row
            System.out.println();
        }
    }

    public static void printDiamond(int height){
        for (int i = 1; i <= height; i++) {
            // Print leading spaces
            for (int j = 1; j <= height - i; j++) {
                System.out.print(" ");
            }
            
            // Print stars
            for (int k = 1; k <= 2 * i - 1; k++) {
                System.out.print("*");
            }
            
            // Move to the next line after printing each row
            System.out.println();
        }

        for(int i = height - 1; i >= 1; i--){

            for(int j = 1; j <= height - i; j++){
                System.out.print(" ");
            }

            for(int k = 1; k <= 2 * i - 1; k++){
                System.out.print("*");
            }

            System.out.println();
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter pattern type (pyramid or diamond): ");
        String patternType = sc.nextLine();
        
        if (patternType.equalsIgnoreCase("pyramid")) {
            System.out.print("Enter height of the pyramid: ");
            int height = sc.nextInt();
            printPyramid(height);
        } else if(patternType.equalsIgnoreCase("diamond")){
            System.out.print("Enter height of the Diamond: ");
            int height = sc.nextInt();
            printDiamond(height);
        } else{
            System.out.println("Invalid");
        }

        sc.close();
    }
}
