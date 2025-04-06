import java.util.*;

class Solution {
    int[][] picture;
    boolean[][] visited;
    int[] dx = {-1, 1, 0, 0};
    int[] dy = {0, 0, -1, 1};
    
    public int[] solution(int m, int n, int[][] picture) {
        this.picture = picture;
        visited = new boolean[m][n]; 
        int numberOfArea = 0; 
        int maxSizeOfOneArea = 0;  

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (picture[i][j] != 0 && !visited[i][j]) {
                    numberOfArea++;
                    int areaSize = bfs(i, j, picture[i][j], m, n);
                    maxSizeOfOneArea = Math.max(maxSizeOfOneArea, areaSize); 
                }
            }
        }
        
        return new int[]{numberOfArea, maxSizeOfOneArea};
    }

    private int bfs(int x, int y, int color, int m, int n) {
        Deque<int[]> queue = new ArrayDeque<>();
        queue.offer(new int[]{x, y});
        visited[x][y] = true;
        int areaSize = 1;

        while (!queue.isEmpty()) {
            int[] position = queue.poll();
            int cx = position[0];
            int cy = position[1];

            for (int i = 0; i < 4; i++) {
                int nx = cx + dx[i];
                int ny = cy + dy[i];
                
                if (nx >= 0 && nx < m && ny >= 0 && ny < n && !visited[nx][ny] && picture[nx][ny] == color) {
                    visited[nx][ny] = true;
                    queue.add(new int[]{nx, ny});
                    areaSize++;
                }
            }
        }

        return areaSize;
    }
}