package BOJ.Math;

import java.util.*;
import java.io.*;

public class BOJ11005 {

    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        long B = Long.parseLong(st.nextToken());
        long N = Long.parseLong(st.nextToken());
        List<String> list = new ArrayList<>();

        while(B>0){
            long tmp = B%N;
           
            String s;
            if(tmp>=10){
                Character c = (char)('A' + (tmp - 10));
                s = c.toString();
            } else {
                s = String.valueOf(tmp);
            }
            list.add(s);
           
            B = B/N;
        }

        Collections.reverse(list);
        for(String s : list){
            System.out.print(s);
        }

    }
}