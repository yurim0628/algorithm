import java.util.*;

class Solution {
    public int solution(int n, int[][] wires) {
        List<Integer>[] graph = new ArrayList[n + 1];
        
        for (int i = 0; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }
        
        for(int[] wire : wires) {
            graph[wire[0]].add(wire[1]);
            graph[wire[1]].add(wire[0]);
        }
        
        int minDiff = Integer.MAX_VALUE;
        
         for(int[] wire : wires) {
            int a = wire[0];
            int b = wire[1];
             
            graph[a].remove(Integer.valueOf(b));
            graph[b].remove(Integer.valueOf(a));
            
            minDiff = Math.min(minDiff, Math.abs(bfs(a, n, graph) - bfs(b, n, graph)));
            
            graph[a].add(b);
            graph[b].add(a);
        }
        
        return minDiff;
    }
    
    public int bfs(int start, int n, List<Integer>[] graph) {
        int count = 1;
        
        Deque<Integer> queue = new ArrayDeque<>();
        int[] visited = new int[n + 1];
        
        queue.offer(start);
        visited[start] = 1;
        
        while(!queue.isEmpty()) {
            int current = queue.poll();
            
            for(int next : graph[current]) {
                if(visited[next] != 1) {
                    visited[next] = 1;
                    queue.offer(next);
                    count ++;
                }
            }
        }
        
        return count;
    }
}