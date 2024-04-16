import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        Map<String, Boolean> map = new HashMap<String, Boolean>();
        
        Arrays.sort(phone_book, (o1, o2) -> Integer.compare(o1.length(), o2.length()));
    
        for (String phone : phone_book) {
            String tmp = "";
            
            for (int i = 0; i < phone.length(); i++) {
                tmp += phone.charAt(i);
                if (map.get(tmp) != null) {
                    return false;
                }
            }
            
            map.put(phone, true);
        }
        
        return true;
    }
}