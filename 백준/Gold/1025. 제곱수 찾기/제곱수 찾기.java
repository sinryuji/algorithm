import java.util.*;
import java.io.*;

public class Main{
    public static boolean isPerfectSquareNumber(int n) {
        int sqrt = (int) Math.sqrt(n);
        return sqrt * sqrt == n;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String line = br.readLine();
        StringTokenizer st = new StringTokenizer(line, " ");

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[][] board = new int[N][M];

        for (int i = 0; i < N; i++) {
            char[] chars = br.readLine().toCharArray();
            for (int j = 0; j < M; j++) {
                board[i][j] = chars[j] - 48;
            }
        }

        int answer = -1;

        for (int row = 0; row < N; row++) {
            for (int col = 0; col < M; col++) {
                for (int rowD = -N; rowD < N; rowD++) {
                    for (int colD = -M; colD < M; colD++){
                        if (rowD == 0 && colD == 0) {
                            continue;
                        }

                        int tmp = 0;
                        int newRow = row;
                        int newCol = col;

                        while (newRow >= 0 && newRow < N && newCol >= 0 && newCol < M) {
                            tmp = tmp * 10 + board[newRow][newCol];

                            if (isPerfectSquareNumber(tmp)) {
                                answer = Math.max(answer, tmp);
                            }

                            newRow += rowD;
                            newCol += colD;
                        }
                    }
                }
            }
        }

        System.out.println(answer);
    }
}