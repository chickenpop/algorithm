package BOJ.Math;

import java.io.*;
import java.util.*;

public class BOJ2745 {
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        String B = st.nextToken();
        int N = Integer.parseInt(st.nextToken());
        int result = 0;

        int i = 1;
        for(Character c : B.toCharArray()){
            int tmp;
            if(Character.isDigit(c)){
                tmp = c - '0'; 
            } else {
                tmp = c - 'A' + 10;
            }
            result += tmp * (Math.pow(N, B.length() - i++));
        }

        System.out.println(result);

    }
}
