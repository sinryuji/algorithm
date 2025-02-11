class Solution {
    private int getDivisorCount(int n) {
        int cnt = 0;
        for (int i = 1; i <= n; i++) {
            if (n % i == 0) {
                cnt++;
            }
        }
        return cnt;
    }
    
    public int solution(int left, int right) {
        int answer = 0;
        
        for (int i = left; i <= right; i++) {
            int cnt = getDivisorCount(i);
            answer += cnt % 2 == 0 ? i : -i;
        }
        
        return answer;
    }
}