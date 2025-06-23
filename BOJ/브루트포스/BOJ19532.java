package BOJ.브루트포스;

import java.io.*;
import java.util.*;

public class BOJ19532 {

    static long a, b, c, d, e, f;
    
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        a = Integer.parseInt(st.nextToken());
        b = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        d = Integer.parseInt(st.nextToken());
        e = Integer.parseInt(st.nextToken());
        f = Integer.parseInt(st.nextToken());

        bruteForce();
    }

    public static void bruteForce(){
        for(int x=-999; x<1000; x++){
            for(int y=-999; y<1000; y++){
                if(a*x + b*y == c && d*x + e*y == f){
                    System.out.println(x + " " + y);
                }
            }
        }
    }

}
