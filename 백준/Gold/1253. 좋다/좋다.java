import java.util.*;
import java.io.*;

public class Main {
    static int[] nums;
    static int N;

    public static boolean twoPoint(int idx) {
        int left = idx == 0 ? 1 : 0;
        int right = idx == N - 1 ? N - 2 : N - 1;
        int target = nums[idx];

        int sum;
        while (left < right) {
            sum = nums[left] + nums[right];

            if (sum == target) {
                return true;
            } else if (sum < target) {
                left++;
                if (left == idx) {
                    left++;
                }
            } else {
                right--;
                if (right == idx) {
                    right--;
                }
            }
        }

        return false;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        nums = new int[N];

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        for (int idx = 0; idx < N; idx++) {
            nums[idx] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(nums);

        int answer = 0;
        for (int idx = 0; idx < N; idx++) {
            if (twoPoint(idx)) {
                answer++;
            }
        }

        System.out.println(answer);
    }
}