package java.dfs_bfs.dfs;

import java.io.*;
import java.util.*;
import java.awt.Point;

public class BOJ10026 {
    static int N;
    static String[][] map;
    static String[][] mapRG;
    static boolean[][] visited;
    static boolean[][] visitedRG;
    static int[] dx = {0, 0, 1, -1};
    static int[] dy = {1, -1, 0, 0};
    static int rgb = 0, rg = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        N = Integer.parseInt(br.readLine());
        map = new String[N][N];
        visited = new boolean[N][N];
        mapRG = new String[N][N];
        visitedRG = new boolean[N][N];
        for(int i=0; i<N; i++){
            String[] tmpRgb = br.readLine().split("");
            for(int j=0; j<N; j++){
                map[i][j] = tmpRgb[j];
                if(tmpRgb[j].equals("G")){
                    mapRG[i][j] = "R";
                } else {
                    mapRG[i][j] = tmpRgb[j];
                }
            }
        }

        for(int i=0;i<N; i++){
            for(int j=0; j<N; j++){
                rgb += bfs(i, j, map, visited);
                rg += bfs(i, j, mapRG, visitedRG);
            }
        }
        
        System.out.println(rgb + " " + rg);

    }

    public static int bfs(int x, int y, String[][] maps, boolean[][] visiteds){
        if(visiteds[x][y]) return 0;
        
        Queue<Point> q = new LinkedList<>();
        q.add(new Point(x, y));
        visiteds[x][y] = true;
        String queueRgb = maps[x][y];

        while(!q.isEmpty()){
            Point p = q.poll();
            for(int i=0; i<4; i++){
                int nx = p.x + dx[i];
                int ny = p.y + dy[i];
                if(nx >= 0 && ny >= 0 && nx < N && ny <N){
                    if(queueRgb.equals(maps[nx][ny]) && !visiteds[nx][ny]){
                        q.add(new Point(nx, ny));
                        visiteds[nx][ny] = true;
                    }
                
                }
            }
        }
        return 1;

    }

}
