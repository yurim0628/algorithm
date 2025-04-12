import java.util.*;

class Solution {
    public int solution(int x, int y, int n) {
        return bfs(x, y, n);
    }
    
    private int bfs(int x, int y, int n) {
        Deque<int[]> queue = new ArrayDeque<>();
        Set<Integer> operationResult = new HashSet<>();
        
        queue.offer(new int[]{x, 0});
        operationResult.add(x);
        
        while(!queue.isEmpty()){
            int[] current = queue.poll();
            
            int num = current[0];
            int steps = current[1];
            
            if(num == y) return steps;
            
            int[] operations = new int[]{num + n, num * 2, num * 3};
            for(int operation : operations) {
                if(operation <= y && !operationResult.contains(operation)){
                    queue.offer(new int[]{operation, steps + 1});
                    operationResult.add(operation);
                }
            }
        }
        
        return -1;
    }
}