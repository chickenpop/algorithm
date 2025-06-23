package java.브루트포스;

import java.util.*;
import java.io.*;

public class BOJ2798 {
    static int N, M;
    static int[] arr;
    static int result = 0;
    public static void main(String[] args) throws IOException{
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        
        arr = new int[N];
        st = new StringTokenizer(br.readLine(), " ");
        for(int i=0; i<N; i++){
            arr[i] = Integer.parseInt(st.nextToken());            
        }
        
        blackJack();
    
    }
    
    public static void blackJack(){
        for(int i=0; i<N; i++){
            for(int j=i+1; j<N; j++){
                for(int k=j+1; k<N; k++){
                    int cardSum = arr[i] + arr[j] + arr[k];
                    if(cardSum == M){
                        System.out.println(cardSum);
                        return;
                    } 
                    if(cardSum < M && result < cardSum){
                        result = cardSum;
                    }
                }
            }
        }
        System.out.println(result);
        return;
    }
    
}
