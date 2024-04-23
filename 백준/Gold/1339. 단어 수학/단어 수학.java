import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String[] words = new String[N];
        Integer[] alpha = new Integer[26];
        Arrays.fill(alpha, 0);
        for (int i = 0; i < N; i++) {
            words[i] = br.readLine();
        }

        for (int i = 0; i < N; i++) {
            int tmp = (int)Math.pow(10, words[i].length() - 1);
            for (int j = 0; j < words[i].length(); j++) {
                alpha[(int)(words[i].charAt(j)-'A')] += tmp;
                tmp /= 10;
            }
        }

        Arrays.sort(alpha, Collections.reverseOrder());

        int n = 9;
        int answer = 0;
        for (int i = 0; true; i++) {
            if (alpha[i] == 0) {
                break;
            }
            answer += alpha[i] * n;
            n--;
        }

        System.out.println(answer);
    }
}