package BOJ.dfs_bfs.bfs;

import java.util.*;
import java.io.*;
import java.awt.Point;

public class BOJ1012 {

    static int T, M, N, K; // T: 테스트케이스, M: 밭의 가로길이, N: 밭의 세로길이, K: 배추가 심어져있는 수
    static int[][] map; // 배추의 위치 
    static boolean[][] visited;
    static List<Integer> list = new ArrayList<>(); 
    static int[] dx = {0, 0, 1, -1};
    static int[] dy = {1, -1, 0, 0};
    static int result = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        T = Integer.parseInt(br.readLine());

        for(int k=0; k<T; k++){
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            M = Integer.parseInt(st.nextToken());
            N = Integer.parseInt(st.nextToken());
            K = Integer.parseInt(st.nextToken());

            map = new int[M][N];
            visited = new boolean[M][N];
            for(int i=0; i<K; i++){
                st = new StringTokenizer(br.readLine(), " ");
                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());
                map[x][y] = 1;
            }

            for(int i=0; i<M; i++){
                for(int j=0; j<N; j++){
                    result += bfs(i, j);
                }
            }
            System.out.println(result);
            result = 0;
        }
    }

    public static int bfs(int x, int y){
        if(map[x][y] != 1 || visited[x][y]) return 0;
        Queue<Point> q = new LinkedList<>();
        q.add(new Point(x, y));
        visited[x][y] = true;

        while (!q.isEmpty()) {
            Point tmp = q.poll();
            for(int i=0; i<4; i++){
                int nx = tmp.x + dx[i];  
                int ny = tmp.y + dy[i];
                if(nx >= 0 && ny >= 0 && nx < M && ny < N){
                    if(!visited[nx][ny] && map[nx][ny] == 1){
                        q.add(new Point(nx, ny));
                        visited[nx][ny] = true;
                    }
                }
            }

        }
        return 1;

    }

}
