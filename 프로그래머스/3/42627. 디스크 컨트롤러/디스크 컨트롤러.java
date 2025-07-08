import java.util.*;

class Solution {
    public int solution(int[][] jobs) {
        int totalWaitTime = 0;
        
        Arrays.sort(jobs, (a, b) -> a[0] - b[0]);
        
        PriorityQueue<int[]> minHeap = new PriorityQueue<>((a, b) -> {
            if (a[1] == b[1]) {
                return a[0] - b[0]; 
            }
            return a[1] - b[1];  
        });
        
        int currentIndex = 0;
        int currentTime = 0;
        
        while (currentIndex < jobs.length || !minHeap.isEmpty()) {
            while (currentIndex < jobs.length && jobs[currentIndex][0] <= currentTime) {
                minHeap.add(new int[]{jobs[currentIndex][0], jobs[currentIndex][1]});
                currentIndex++;
            }
            
            if (!minHeap.isEmpty()) {
                int[] job = minHeap.poll();
                int startTime = job[0];
                int remainingTime = job[1];
                
                currentTime += remainingTime;
                totalWaitTime += (currentTime - startTime);
            } else {
                currentTime++;
            }
        }
        
        return totalWaitTime / jobs.length;
    }
}
