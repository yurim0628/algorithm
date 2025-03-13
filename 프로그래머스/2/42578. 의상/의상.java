import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        Map<String, Integer> clothesMap = new HashMap<>();
        
        for (String[] cloth : clothes) {
            clothesMap.put(cloth[1], clothesMap.getOrDefault(cloth[1], 0) + 1);
        }
        
        for (int count : clothesMap.values()) {
            answer = answer * (count + 1);
        }
        
        return answer - 1;
    }
}

