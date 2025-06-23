package java.dfs_bfs.bfs;

import java.io.*;
import java.util.*;

public class BOJ2667 {

        static int N, cnt=0;
        static boolean[][] visited;
        static int[][] map;
        static int[] dx = {0, 0, 1, -1};
        static int[] dy = {1, -1, 0, 0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        List<Integer> list = new ArrayList<>();

        N = Integer.parseInt(br.readLine());
        map = new int[N][N];
        visited = new boolean[N][N];
        for(int i=0; i<N; i++){
            String s = br.readLine();
            for(int j=0;j<N;j++){
                map[i][j] = s.charAt(j) - '0';
            }
        }

        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                if(!visited[i][j] && map[i][j] == 1){
                    dfs(i, j);
                    list.add(cnt);
                    cnt=0;
                }
            }
        }

        Collections.sort(list);
        System.out.println(list.size());
        for(int l : list){
            System.out.println(l);
        }

    }

    public static void dfs(int x, int y){
        visited[x][y] = true;
        cnt++;

        for(int i=0; i<4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            if(nx >= 0 && ny >= 0 && nx < N && ny < N){
                if(!visited[nx][ny] && map[nx][ny]== 1){
                    dfs(nx, ny);
                }
            }

        }
    }
    
}
