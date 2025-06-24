package BOJ.심화;

import java.io.*;
import java.util.*;

public class BOJ25206 {

    static Map<String, Float> score = new HashMap<>();
    public static void main(String[] args) throws IOException {

        score.put("A+", 4.5f);
        score.put("A0", 4.0f);
        score.put("B+", 3.5f);
        score.put("B0", 3.0f);
        score.put("C+", 2.5f);
        score.put("C0", 2.0f);
        score.put("D+", 1.5f);
        score.put("D0", 1.0f);
        score.put("F", 0.0f);

        Float scoreSum = 0.0f;
        Float unitSum = 0.0f;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        for(int i=0; i<20; i++){
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            String subject = String.valueOf(st.nextToken());
            Float unit = Float.parseFloat(st.nextToken());
            String scoreInput = st.nextToken();
            if(!scoreInput.equals("P")){
                unitSum += unit;
                scoreSum += unit * score.get(scoreInput);
            }
        }

        System.out.printf("%.6f", scoreSum/unitSum);
        
    }
}
