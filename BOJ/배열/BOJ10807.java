package BOJ.배열;

import java.util.*;
import java.io.*;

public class BOJ10807 {
    
    public static void main(String[] args) throws IOException {
        int N = 0, v = 0;
        List<Integer> list = new ArrayList<Integer>();

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");        
        for(int i=0; i<N; i++){
            list.add(Integer.parseInt(st.nextToken()));
        }        
        
        v = Integer.parseInt(br.readLine());
        int cnt = 0;
        for(int i=0; i<N; i++){
            if(list.get(i) == v) cnt++;
        }
        System.out.println(cnt);
    }
}
