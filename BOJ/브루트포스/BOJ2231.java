package BOJ.브루트포스;

import java.io.IOException;
import java.util.Scanner;

public class BOJ2231 {

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        
        int N = Integer.parseInt(sc.nextLine());
        System.out.println(sumDivision(N));
        sc.close();
    }

    public static int sumDivision(int N){
        for(int i=0; i<N; i++){
            String s = String.valueOf(i);
            int sum = 0;
            for(int j=0; j<s.length(); j++){
                sum += s.charAt(j) - '0';
            }
            int M = Integer.parseInt(s);
            if(M+sum == N) {
                return M;
            }
        }
        return 0;
    }
}