import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        int total_weight = 0;
        Queue<Integer> queue = new LinkedList<>();
        int index = 0;
        while(index < truck_weights.length) {
            if(bridge_length == queue.size()) {
                total_weight -= queue.poll();
            }
            if(total_weight + truck_weights[index] <= weight) {
                total_weight += truck_weights[index];
                queue.offer(truck_weights[index]);
                index ++;
            } else {
                queue.offer(0);
            }
            answer += 1;
            
                
        }
        return answer + bridge_length;
    }
}
