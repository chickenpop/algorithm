package BOJ.배열2;

import java.io.*;
import java.util.StringTokenizer;

public class BOJ2566 {

    static int x = 0, y = 0, max = 0;
    
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int[][] arr = new int[9][9];
        for(int i=0;i<9;i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int j=0;j<9;j++){
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for(int i=0;i<9;i++){
            for(int j=0;j<9;j++){
                if(max<=arr[i][j]){ // 최댓갑이 0인 경우도 포함되어야함(<=)
                    max = arr[i][j];
                    x = i+1;
                    y = j+1;
                }
            }
        }

        System.out.println(max); 
        System.out.println(x + " " + y);

    }
    
}
