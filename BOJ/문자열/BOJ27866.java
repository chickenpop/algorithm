package BOJ.문자열;

import java.io.*;

public class BOJ27866 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] S = br.readLine().split("");
        int i = Integer.parseInt(br.readLine());

        System.out.println(S[i-1]);

    }
}
