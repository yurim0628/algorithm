import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int mixCount = 0;  
        PriorityQueue<Integer> spicyHeap = new PriorityQueue<>();  

        for (int scovilleIndex : scoville) {
            spicyHeap.add(scovilleIndex);
        }
    
        while (spicyHeap.peek() < K && spicyHeap.size() > 1) {
            int leastSpicy = spicyHeap.poll();  
            int secondLeastSpicy = spicyHeap.poll(); 
            
            int combinedSpicy = leastSpicy + (secondLeastSpicy * 2);  
            spicyHeap.offer(combinedSpicy);
            
            mixCount++;  
        }
            
        return spicyHeap.peek() >= K ? mixCount : -1;
    }
}
