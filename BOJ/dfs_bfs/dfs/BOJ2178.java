
package BOJ.dfs_bfs.dfs;

import java.util.*;
import java.io.*;
import java.awt.Point;

public class BOJ2178 {

    static int[][] map;
    static boolean[][] visited;
    static int dx[] = {0, 0, 1, -1};
    static int dy[] = {1, -1, 0, 0};
    static int N, M;
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        map = new int[N][M];
        visited = new boolean[N][M];
        for(int i=0; i<N; i++){
            String s  = br.readLine();
            for(int j=0; j<M; j++){
                map[i][j] = s.charAt(j) - '0';
            }
        }

        bfs(0, 0);
        System.out.println(map[N-1][M-1]);

    }

    public static void bfs(int x, int y){
        visited[x][y] = true;
        Queue<Point> q = new LinkedList<>();
        q.add(new Point(x, y));

        while (!q.isEmpty()) {
            Point p = q.poll();
            for(int i=0; i<4; i++){
                int nx = p.x + dx[i];
                int ny = p.y + dy[i];
                if(nx >= 0 && ny >= 0 && nx < N && ny <M){
                    if(!visited[nx][ny] && map[nx][ny] == 1){
                        visited[nx][ny] = true;
                        q.add(new Point(nx, ny));
                        map[nx][ny] = map[p.x][p.y] + 1;
                    }
                }
            }
        }
    }
    
}