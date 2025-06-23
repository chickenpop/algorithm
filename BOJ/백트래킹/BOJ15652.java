package BOJ.백트래킹;

import java.util.*;
import java.io.*;

public class BOJ15652 {
    
    static int N, M;
    static int[] arr;
    static StringBuilder sb = new StringBuilder();
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        
        arr = new int[M];
        
        dfs(0, 0);
        System.out.println(sb); 
    }
    
    public static void dfs(int at, int depth){
        if(depth == M){
            for(int val : arr){
                sb.append(val).append(' ');
            }    
            sb.append('\n');    
            return;
        }
        for(int i=at; i<N; i++){
            arr[depth] = i + 1;             
            dfs(i, depth+1);
        }

    }
}