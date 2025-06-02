import java.util.*;

class Solution {
    int answer = 0;
    public int solution(String word) {
        StringBuilder currentWord = new StringBuilder();
        char[] alphabet = new char[]{'A', 'E', 'I', 'O', 'U'};
        dfs(word, currentWord, alphabet);
        return answer;
    }
    
    private boolean dfs(String word, StringBuilder currentWord, char[] alphabet) {
        System.out.println(currentWord);
        if(word.equals(currentWord.toString())) {
            return true;
        }
        if(currentWord.length() == 5) {
            return false;
        }
        
        
        for(char a : alphabet) {
            currentWord.append(a);
            answer++;
            if(dfs(word, currentWord, alphabet)){
                return true;
            };
            currentWord.deleteCharAt(currentWord.length() - 1);
        }
        
        return false;
    }
}