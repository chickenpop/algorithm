package BOJ.반복문;

import java.util.*;
import java.io.*;

public class BOJ25304 {
    static int totalPrice = 0;
    static int item = 0;
    static int buyPrice = 0;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        totalPrice = Integer.parseInt(br.readLine());
        item = Integer.parseInt(br.readLine());

        for(int i=0; i<item; i++){
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            int price = Integer.parseInt(st.nextToken());
            int num = Integer.parseInt(st.nextToken());
            buyPrice += price * num;
        }

        if(totalPrice == buyPrice) System.out.println("Yes");
        else System.out.println("No");
    } 
}
