import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 1;
        Queue<int[]> queue = new LinkedList<>();
        PriorityQueue<Integer> priorityQueue = new PriorityQueue<>(Collections.reverseOrder());

        for (int i = 0; i < priorities.length; i++) {
            queue.offer(new int[]{i, priorities[i]});
            priorityQueue.offer(priorities[i]);
        }
        
        while(!queue.isEmpty()) {
            int[] current = queue.poll();
            
            if(current[1] == priorityQueue.peek()){
                if (current[0] == location) {
                    return answer;
                } 
                priorityQueue.poll();
                answer++;
            } else {
                queue.offer(current);
            }
            
        }

        return -1;
    }
}