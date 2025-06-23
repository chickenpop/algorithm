package BOJ.dfs_bfs.dfs;

import java.util.*;
import java.io.*;

public class BOJ2644 {
    static int N; // 전체 인원수
    static int x, y; // 촌수 비교할 사람(번호)
    static int M; // 부모 자식 관계수
    static int[][] graph; // 부모 자식 관계
    static boolean[] visited; // 관계 방문 여부
    static boolean zero = true; // 비교할 두사람 관계여부
    static int cnt = 0; // 비교할 두 사람의 관계수

    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    
        N = Integer.parseInt(br.readLine());
        graph = new int[N+1][N+1];
        visited = new boolean[N+1];

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        x = Integer.parseInt(st.nextToken());
        y = Integer.parseInt(st.nextToken());

        M = Integer.parseInt(br.readLine());
        for(int i=0; i<M; i++){
            st = new StringTokenizer(br.readLine(), " ");
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            graph[u][v] = graph[v][u] = 1;
        }

        System.out.println(dfs(x, y, cnt));


    }

    public static int dfs(int start, int end, int cnt){
       
        if(start == end) return cnt;
        visited[start] = true;

        for(int i=1; i<N+1; i++){
            if(!visited[i] && graph[start][i] == 1){
                System.out.print(start + "->" + i+" ");
                int temp = dfs(i, end, cnt+1);
                if(temp != -1) return temp;
            }
        }
        return -1;
        
    }

}
