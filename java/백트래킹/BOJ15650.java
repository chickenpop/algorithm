package java.백트래킹;

import java.io.*;
import java.util.*;

public class BOJ15650 {
   
    static int[] map;
    static int N, M;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        
        map = new int[M];

        backtracking(0, 0);

        System.out.println(sb);
    } 

    public static void backtracking(int depth, int plus){
        if(depth == M){
            for(int val : map){
                sb.append(val).append(' ');
            }
            sb.append('\n');
            return;
        }
        for(int i=plus; i<N; i++){
            map[depth] = i+1;
            backtracking(depth+1, i+1);
        }
    }

}
