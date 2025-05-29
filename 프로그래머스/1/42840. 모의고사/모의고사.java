import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        int[] score = new int[]{0, 0, 0};
        
        int[] numberOne = {1, 2, 3, 4, 5};
        int[] numberTwo = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] numberThree = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        
      
        for (int i = 0; i < answers.length; i++) {
            if (answers[i] == numberOne[i % numberOne.length]) {
                score[0]++;
            }
            if (answers[i] == numberTwo[i % numberTwo.length]) {
                score[1]++;
            }
            if (answers[i] == numberThree[i % numberThree.length]) {
                score[2]++;
            }
        }
        
    
        int max = Math.max(score[0], Math.max(score[1], score[2]));
      
        List<Integer> topScorers = new ArrayList<>();
        for (int i = 0; i < 3; i++) {
            if (score[i] == max) {
                topScorers.add(i + 1);  
            }
        }
        
       
        return topScorers.stream().mapToInt(i -> i).toArray();
    }
}
