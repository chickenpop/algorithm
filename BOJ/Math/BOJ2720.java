package BOJ.Math;

import java.util.*;

public class BOJ2720 {
    
    static double quarter = 25;
    static double dime = 10;
    static double nickel = 5;
    static double penny = 1;
    static int q=0, d=0, n=0, p=0;
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int T = Integer.parseInt(sc.nextLine());
        double testCase = 0;
        for(int i=0; i<T; i++){
            testCase = Integer.parseInt(sc.nextLine());

            while(testCase>0){
                if(testCase>=quarter){
                    testCase -= quarter;
                    q++;
                } else if(testCase>=dime){
                    testCase -= dime;
                    d++;
                } else if(testCase>=nickel){
                    testCase -= nickel;
                    n++;
                } else {
                    testCase -= penny;
                    p++;
                }
            }

            System.out.println(q + " " + d + " " + n + " " + p);
            q = 0; d = 0; n = 0; p = 0;
        }
    }

}
