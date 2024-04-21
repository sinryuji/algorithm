import java.util.*;
import java.io.*;

public class Main {
    static class Node {
        int x, y, cnt;

        Node(int x, int y, int cnt) {
            this.x = x;
            this.y = y;
            this.cnt = cnt;
        }
    }

    static int[][] board;
    static boolean[][] visited;
    static int N;
    static int M;

    public static int bfs() {
        PriorityQueue<Node> q = new PriorityQueue<>(Comparator.comparingInt(o -> o.cnt));
        int[] dx = {1, -1, 0, 0};
        int[] dy = {0, 0, 1, -1};

        q.offer(new Node(0, 0, 0));
        visited[0][0] = true;

        while (!q.isEmpty()) {
            Node curNode = q.poll();

            if (curNode.x == M - 1 && curNode.y == N - 1) {
                return curNode.cnt;
            }

            for (int i = 0; i < 4; i++) {
                int nx = dx[i] + curNode.x;
                int ny = dy[i] + curNode.y;

                if (nx < 0 || nx >= M || ny < 0 || ny >= N || visited[ny][nx]) {
                    continue;
                }

                visited[ny][nx] = true;
                if (board[ny][nx] == 0) {
                    q.offer(new Node(nx, ny, curNode.cnt));
                } else {
                    q.offer(new Node(nx, ny, curNode.cnt + 1));
                }
            }
        }

        return 0;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String str = br.readLine();
        StringTokenizer st = new StringTokenizer(str, " ");

        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());


        board = new int[N][M];
        for (int y = 0; y < N; y++) {
            char[] line = br.readLine().toCharArray();
            for (int x = 0; x < M; x++) {
                board[y][x] = line[x] - 48;
            }
        }

        visited = new boolean[N][M];

        System.out.println(bfs());
    }
}