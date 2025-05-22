import java.util.*;

class Solution {
    boolean solution(String s) {
        List<Character> stack = new ArrayList<>();
        
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            
            if (c == '(') {
                stack.add(c);
            } 
            else if (c == ')') {
                if (stack.isEmpty()) {
                    return false;
                }
                stack.remove(stack.size() - 1);
            }
        }
        
        return stack.isEmpty();
    }
}
