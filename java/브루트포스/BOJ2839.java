package java.브루트포스;

import java.io.*;
import java.util.*;

public class BOJ2839 {
   public static void main(String[] args) throws IOException {

      Scanner sc = new Scanner(System.in);
      int N = Integer.parseInt(sc.nextLine());
      int cnt = 0;
      
      while(N>0){
         if(N%5==0){
            cnt += N/5;
            N=0;
         } else {
            N-=3;
            cnt++;
         }
      }
      
      if(N<0) System.out.println(-1);
      else System.out.println(cnt);
      sc.close(); 
   } 
}
