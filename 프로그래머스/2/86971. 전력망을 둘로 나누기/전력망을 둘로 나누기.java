import java.util.*;

class Solution {
    int answer = Integer.MAX_VALUE;
    
    public int solution(int n, int[][] wires) {
        List<Integer>[] graph = new ArrayList[n + 1];
        
        for(int i = 0; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }
       
        for(int[] wire : wires) {
            graph[wire[0]].add(wire[1]);
            graph[wire[1]].add(wire[0]);
        }
        
        for(int[] wire : wires) {
            int start = wire[0];
            int end = wire[1];
            
            graph[start].remove(Integer.valueOf(end));
            graph[end].remove(Integer.valueOf(start));
            
            answer = Math.min(answer, Math.abs(bfs(start, graph, n) - bfs(end, graph, n)));
            
            graph[end].add(start);
            graph[start].add(end);
        }
        
        return answer;
    }
    
    public int bfs(int start, List<Integer>[] graph, int n) {
        int count = 1;
        Deque<Integer> queue = new ArrayDeque<>();
        int[] visited = new int[n + 1];
       
        queue.offer(start);
        visited[start] = 1;
        
        while(!queue.isEmpty()) {
            int current = queue.poll();
              visited[current] = 1;
                   
            
            for(int next : graph[current]) {
                if(visited[next] != 1) {
                   queue.offer(next);
                    count ++;
                }
            }
        }
        
        return count;
    }
}