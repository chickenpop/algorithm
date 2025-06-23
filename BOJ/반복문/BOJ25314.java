package BOJ.반복문;

import java.util.*;
import java.io.*;

public class BOJ25314 {
   
    public static void main(String[] args) throws IOException {
    
        Scanner sc = new Scanner(System.in);
        long N = Long.parseLong(sc.nextLine());
        
        long divisionN = N/4;
        for(int i=0; i<divisionN; i++){
            System.out.print("long ");
        }

        System.out.print("int");
        sc.close();
    } 
}
