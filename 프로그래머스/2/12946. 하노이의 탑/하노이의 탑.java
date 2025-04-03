import java.util.*;

class Solution {
    List<int[]> moveList = new ArrayList<>();
    
    public int[][] solution(int n) {
        hanoi(n, 1, 3, 2);
        
        int countMove = moveList.size();
        int[][] answer = new int[countMove][2];
        
        for(int i = 0; i < countMove; i++) {
            int[] move = moveList.get(i);
            answer[i][0] = move[0];
            answer[i][1] = move[1];
        }
        
        return answer;
    }
    
    private void hanoi(int number, int start, int end, int mid) {
        if(number == 1) {
            moveList.add(new int[]{start, end});
        } else {
            hanoi(number - 1, start, mid, end);
            moveList.add(new int[]{start, end});
            hanoi(number - 1, mid, end, start);
        }
    }
}