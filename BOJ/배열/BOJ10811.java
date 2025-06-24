package BOJ.배열;

import java.util.*;
import java.io.*;

public class BOJ10811 {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] basket = new int[N+1];
        for(int i=0; i<N+1; i++){
            basket[i] = i;
        }

        for(int k=0; k<M; k++){
            st = new StringTokenizer(br.readLine());
            int i = Integer.parseInt(st.nextToken());
            int j = Integer.parseInt(st.nextToken());

            for(int l=0; l<(j-i)/2 + (j-i)%2; l++){
                int tmp = basket[i+l];
                basket[i+l] = basket[j-l];
                basket[j-l] = tmp;               
            }

        }
        
        for(int i=0; i<N; i++){
            System.out.print(basket[i+1] + " ");
        }
    }
}
