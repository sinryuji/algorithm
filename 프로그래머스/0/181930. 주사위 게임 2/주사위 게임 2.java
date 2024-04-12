import java.util.Set;
import java.util.stream.Stream;
import java.util.stream.Collectors;

class Solution {
    public int solution(int a, int b, int c) {
        Set<Integer> set = Stream.of(a, b, c).collect(Collectors.toSet());
        
        if (set.size() == 3) {
            return a + b + c;
        } else if (set.size() == 2) {
            return (a + b + c) * (int)(Math.pow(a, 2) + Math.pow(b, 2) + Math.pow(c, 2));
        }
        return (a + b + c) * (int)(Math.pow(a, 2) + Math.pow(b, 2) + Math.pow(c, 2)) * (int)(Math.pow(a, 3) + Math.pow(b, 3) + Math.pow(c, 3));
    }
}