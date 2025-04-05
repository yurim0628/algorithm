import java.util.*;
import java.util.function.BiPredicate; 

class Solution {
    private static final int FRIEND_COUNT = 8;
    private int answer = 0;
    private final char[] friends = {'A', 'C', 'F', 'J', 'M', 'N', 'R', 'T'};
    private boolean[] visited;
    private String[] data;

    public int solution(int n, String[] data) {
        this.data = data;
        visited = new boolean[FRIEND_COUNT];
        dfs("");
        return answer;
    }
    
    private void dfs(String currentLine) {
        if (currentLine.length() == FRIEND_COUNT) {
            if (isValidLine(currentLine)) {
                answer++;
            }
            return; 
        }
        
        for (int i = 0; i < FRIEND_COUNT; i++) {
            if (!visited[i]) {
                visited[i] = true;
                dfs(currentLine + friends[i]);
                visited[i] = false;
            }
        }
    }
    
    private boolean isValidLine(String currentLine) {
        for (String d : data) {
            char friendA = d.charAt(0);
            char friendB = d.charAt(2);
            char condition = d.charAt(3);
            int desiredGap = d.charAt(4) - '0';

            int posA = currentLine.indexOf(friendA);
            int posB = currentLine.indexOf(friendB);
            int actualGap = Math.abs(posA - posB) - 1;
            
            if (!ConditionChecker.compare(condition, actualGap, desiredGap)) {
                return false; 
            }
        }
        
        return true;
    }
}

class ConditionChecker {
    private static final Map<Character, BiPredicate<Integer, Integer>> conditions = new HashMap<>();

    static {
        conditions.put('=', (a, b) -> a == b);
        conditions.put('>', (a, b) -> a > b);
        conditions.put('<', (a, b) -> a < b);
    }

    public static boolean compare(char condition, int num1, int num2) {
        return conditions.get(condition).test(num1, num2);
    }
}