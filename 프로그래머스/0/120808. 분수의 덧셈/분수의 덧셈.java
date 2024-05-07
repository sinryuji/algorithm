class Solution {
    private int gcd(int a, int b) {
        while (b > 0) {
            int tmp = a;
            a = b;
            b = tmp % b;
        }
        return a;
    }
    
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        int[] answer = new int[2];
        
        int numer = numer1 * denom2 + numer2 * denom1;
        int denom = denom1 * denom2;
        
        int g = gcd(numer, denom);
        answer[0] = numer / g;
        answer[1] = denom / g;
        
        return answer;
    }
}