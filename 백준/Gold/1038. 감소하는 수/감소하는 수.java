import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static List<Long> list = new ArrayList<>();

    public static void dfs(long num) {
        list.add(num);

        long remainder = num % 10;
        if (remainder == 0) {
            return;
        }

        for (long i = remainder - 1; i >= 0; i--) {
            dfs(num * 10 + i);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        if (N < 10) {
            System.out.println(N);
        } else if (N >= 1023) {
            System.out.println(-1);
        } else {
            for (int i = 0; i < 10; i++) {
                dfs(i);
            }

            Collections.sort(list);
            System.out.println(list.get(N));
        }
    }
}