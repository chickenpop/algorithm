package BOJ.배열;

import java.io.*;
import java.util.*;

public class BOJ5597 {

    public static void main(String[] args) throws IOException {
        
        boolean[] student = new boolean[30];
        Scanner sc = new Scanner(System.in);

        for(int i=0; i<28; i++){
            student[Integer.parseInt(sc.nextLine())-1] =  true;
        }

        for(int i=0; i<30; i++){
            if(!student[i]) System.out.println(i+1);
        }
    }

}