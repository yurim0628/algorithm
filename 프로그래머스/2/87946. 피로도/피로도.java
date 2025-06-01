import java.util.*;

class Solution {
    private int answer = 0;
    
    public int solution(int k, int[][] dungeons) {
        int[] visited = new int[dungeons.length];
        dfs(k, dungeons, visited, 0);
        return answer;
    }
    
    public void dfs(int k, int[][] dungeons, int[] visited, int count) {
        answer = Math.max(answer, count);
            
        for(int i=0; i<dungeons.length; i++) {
            if(visited[i] != 1 && k >= dungeons[i][0]) {
                visited[i] = 1;
                dfs(k - dungeons[i][1], dungeons, visited, count + 1);
                visited[i] = 0;
            }
        }
    }
}