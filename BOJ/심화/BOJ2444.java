package BOJ.심화;

import java.util.Scanner;

public class BOJ2444 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = Integer.parseInt(sc.nextLine());
        int time = 2*N;

        for(int i=1; i<time; i++){
            if(i<=N){
                for(int j=0; j<N-i; j++){
                    System.out.print(" ");
                }
                for(int k=0; k<2*i-1; k++){
                    System.out.print("*");
                }
            } else {
                for(int j=0; j<i-N; j++){
                    System.out.print(" ");
                }
                for(int k=0; k<2*(2*N-i)-1; k++){
                    System.out.print("*");
                }
            }
            System.out.println();
        }
    }
}
