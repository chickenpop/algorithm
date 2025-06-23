package BOJ.dfs_bfs.bfs;

import java.io.*;
import java.util.*;

public class BOJ2606 {
    
    static int N, M, cnt;
    static boolean[] visited;
    static int[][] network;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        M = Integer.parseInt(br.readLine());
        network = new int[N+1][N+1];
        visited = new boolean[N+1];

        for(int i=0; i<M; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            network[u][v] = network[v][u] = 1;
        }

        dfs(1);
        System.out.println(cnt-1);
    }

    public static void dfs(int v){
        visited[v] = true;
        cnt++;

        for(int i=1; i<N+1; i++){
            if(!visited[i] && network[i][v] == 1){
                dfs(i);
            }
        }

    }

}
