package java.브루트포스;

import java.io.*;
import java.util.*;

public class BOJ1018 {

    static int M, N;
    static Character[][] chess;   
    static boolean[][] chessTF; 
    static int MIN = 64; // 체스판이 최대로 뒤바뀔 수 있는 수 8*8
    
   public static void main(String[] args) throws IOException {
    
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine(), " ");

    M = Integer.parseInt(st.nextToken());
    N = Integer.parseInt(st.nextToken());
    chess = new Character[M][N];
    chessTF = new boolean[M][N];
    for(int i=0;i<M;i++){
        String s = br.readLine();
        for(int j=0; j<N; j++){
            chess[i][j] = s.charAt(j);
            if(chess[i][j] == 'W'){
                chessTF[i][j] = true;
            } 
        }
    }

    // 순환할 체스판 범위 8*8 크기로 한칸씩 이동 
    for(int i=0; i<M-7; i++){ // 아래로
        for(int j=0; j<N-7; j++){ // 옆으->
            chess(i, j);
        }
    }

    System.out.println(MIN);
   
   } 

   public static void chess(int x, int y){
        int end_x = x+8;
        int end_y = y+8;
        
        boolean firstTF = chessTF[x][y]; // 체스판의 첫번째 글자
        int cnt=0;

        for(int i=x; i<end_x; i++){
            for(int j=y; j<end_y; j++){
                if(firstTF != chessTF[i][j]){ 
                    cnt++;
                }
                firstTF = !firstTF;
            }
            firstTF = !firstTF;
        }
        /*
         * 첫 번째 칸을 기준으로 할 떄의 색칠 할 개수(cnt)와
         * 반대되는 색을 기준으로 할때의 개수(64-cnt) 중 최솟값을 cnt에 저장
         */
        cnt = Math.min(cnt, 64-cnt);
        // 이전값보다 작은 경우 최솟값 갱신
        if(cnt<MIN) MIN = cnt;

   }
}
