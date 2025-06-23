package BOJ.dfs_bfs.dfs;

import java.awt.Point;
import java.io.*;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ7576 {
    
        static int[][] map;
        static int[] dx = {0, 0, 1, -1};
        static int[] dy = {1, -1, 0, 0};
        static int totalTomato = 0;
        static Queue<Point> q = new LinkedList<>();;
        static int N, M;
        static int date = 0 ;

    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        map = new int[N][M];
        for(int i=0; i<N; i++){
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<M; j++){
                map[i][j] = Integer.parseInt(st.nextToken());
                if(map[i][j] == 0) totalTomato++;
                else if(map[i][j] == 1) q.add(new Point(i, j));
            }
        }

        if(totalTomato == 0) {
            System.out.println(0);
            return;
        }

        dfs();
        if(totalTomato>0){
            System.out.println(-1);
        } else {
            System.out.println(date);
        }
        
    }

    public static void dfs(){

        while(!q.isEmpty()){
            Point tmp = q.poll();
            date++;
            for(int i=0; i<4; i++){
                int nx = tmp.x + dx[i];
                int ny = tmp.y + dy[i];
                if(nx >= 0 && ny >=0 && nx <N && ny < M){
                    if(map[nx][ny] == 0){
                        totalTomato--;
                        q.add(new Point(nx, ny));
                    }
                }
            }

        }

    }

}
