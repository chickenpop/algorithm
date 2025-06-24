package BOJ.배열;

import java.util.*;
import java.io.*;

public class BOJ2566 {
    public static void main(String[] args) throws IOException { 
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int[][] map = new int[9][9];
        int maxValue = 0;
        int x = 0;
        int y = 0;

        for(int i=0; i<9; i++){
            st = new StringTokenizer(br.readLine(), " ");
            for(int j=0; j<9; j++){
                int value = Integer.parseInt(st.nextToken());
                map[i][j] = value;
                if(maxValue < value){
                    maxValue = value;
                    x = i+1; y = j+1;
                }
            }
        }

        System.out.println(maxValue);
        System.out.println(x + " " + y);

    }
}
