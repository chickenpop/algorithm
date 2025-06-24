package BOJ.심화;

import java.io.*;
import java.util.*;

public class BOJ3003 {
    public static void main(String[] args) throws IOException {
        int[] chess = {1, 1, 2, 2, 2, 8};
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        for(int i=0; i<6; i++){
            chess[i] = chess[i] - Integer.parseInt(st.nextToken());
        }

        for(int i: chess){
            System.out.print(i+" ");
        }

    } 
}
