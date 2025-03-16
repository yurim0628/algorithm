import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {            
        int row = commands.length;
        int[] answer = new int[row]; 
        
        for(int i=0; i<row; i++) {
            int start = commands[i][0];
            int end = commands[i][1];
            int number = commands[i][2];
            
            int[] subArray = Arrays.copyOfRange(array, start - 1, end);
            Arrays.sort(subArray);
            answer[i] = subArray[number - 1];
        }
        
        return answer;
    }
}