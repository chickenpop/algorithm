package BOJ.브루트포스;

import java.io.*;
import java.util.*;

public class BOJ1436 {
    static long N = 0;
    static long cntEnd = 0;
    static long End = 0;
    static long firstEnd = 666;
    public static void main(String[] args) throws IOException {
    
        Scanner sc = new Scanner(System.in);
        N = Integer.parseInt(sc.nextLine());
        
        while (N != cntEnd) {
            String end = String.valueOf(firstEnd);
            if(end.contains("666")){
                cntEnd++;
                End = Long.valueOf(end);
            }
            firstEnd++;
        }    
        
        System.out.println(End);
        sc.close(); 
   } 


}
