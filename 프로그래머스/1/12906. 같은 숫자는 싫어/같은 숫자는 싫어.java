import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        List<Integer> list = new ArrayList<>();
        int prev = -1;
        for(int a : arr) {
            if(prev != a) {
                list.add(a);
            } 
            prev = a;
        }
        
        return list.stream().mapToInt(i -> i).toArray();
    }
}