package BOJ.배열;

import java.io.*;
import java.util.*;

public class BOJ10813 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());        

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        List<Integer> list = new ArrayList<Integer>(N);

        for(int i=0; i<N; i++){
            list.add(i+1);
        }        
        
        for(int k=0; k<M; k++){
            st = new StringTokenizer(br.readLine());
            int i = Integer.parseInt(st.nextToken()) - 1;
            int j = Integer.parseInt(st.nextToken()) - 1;
            int tmp = list.get(i);
            list.set(i,list.get(j));
            list.set(j, tmp);
        }

        for(int k : list){
            System.out.print(k + " ");
        }

        
    }
}
