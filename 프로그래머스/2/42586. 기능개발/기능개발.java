import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> list = new ArrayList<>();
        
        int currentDay = calculateDays(progresses[0], speeds[0]);
        int count = 1;
        
        for(int i=1; i<progresses.length; i++) {
            int nextDay = calculateDays(progresses[i], speeds[i]);
            if(currentDay >= nextDay) {
                count ++;
            } else {
                list.add(count);
                count = 1;
                currentDay = nextDay;
            }
        }
        
        list.add(count);
        
        return list.stream().mapToInt(i -> i).toArray();
    }
    
    public int calculateDays(int progress, int speed) {
        int remainingProgress = 100 - progress;
        return (int) Math.ceil(remainingProgress / (double) speed); 
    }
}