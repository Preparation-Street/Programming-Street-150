import java.util.*;

class fibonacciSeries{
    public static List<Integer> printFibo(int limit){
        List<Integer> fibIntegers = new ArrayList<>();

        int a = 0;
        int b = 1;
        if(a >= limit) fibIntegers.add(a);
        if(b >= limit) fibIntegers.add(b);

        while(true){
            int next  = a + b;
            if(next > limit) break;
            fibIntegers.add(next);

            a = b;
            b = next; 
        }

        return fibIntegers;
    }

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int limit = sc.nextInt();
        List<Integer> fIntegers = printFibo(limit);

        System.out.println(fIntegers);

        sc.close();
    }
}