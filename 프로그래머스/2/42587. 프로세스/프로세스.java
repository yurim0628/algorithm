import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 1;
        
        PriorityQueue<Integer> priorityQueue = new PriorityQueue<>(Collections.reverseOrder());
        Deque<int[]> queue = new ArrayDeque<>();
        
        for(int i=0; i<priorities.length; i++) {
            queue.offer(new int[]{i, priorities[i]});
            priorityQueue.offer(priorities[i]);
        }
        
        while(!priorityQueue.isEmpty()) {
            int[] info = queue.poll();
            
            if(info[1] == priorityQueue.peek()) {
                if(info[0] == location) {
                    return answer;
                } else {
                    answer += 1;
                    priorityQueue.poll();
                }
            } else {
                queue.offer(info);
            }
            
        }
        
        return answer;
    }
}