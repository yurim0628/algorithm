import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        Map<String, Integer> dict = new HashMap<>();
        for(String[] c : clothes) {
            dict.put(c[1], dict.getOrDefault(c[1], 0) + 1);
        }
        for(int d : dict.values()) {
            answer *= (d + 1);
        }
        
        return answer - 1;
    }
}