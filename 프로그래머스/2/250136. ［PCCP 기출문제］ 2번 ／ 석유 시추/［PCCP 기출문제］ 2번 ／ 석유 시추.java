import java.util.*;

class Solution {
    boolean[][] visited;

    public int solution(int[][] land) {
        int maxOil = 0;

        int rows = land.length;
        int cols = land[0].length;
        visited = new boolean[rows][cols];
        int[] oilPerColumn = new int[cols]; 

        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                if (land[row][col] > 0 && !visited[row][col]) {
                    int[] oilInfo = bfs(land, row, col);
                    int minCol = oilInfo[0];
                    int maxCol = oilInfo[1];
                    int oilAmount = oilInfo[2];

                    for (int c = minCol; c <= maxCol; c++) {
                        oilPerColumn[c] += oilAmount;
                    }
                }
            }
        }

        for (int oil : oilPerColumn) {
            maxOil = Math.max(oil, maxOil);
        }

        return maxOil;
    }

    private int[] bfs(int[][] land, int startX, int startY) {
        int oilCount = 1;
        int minCol = Integer.MAX_VALUE;
        int maxCol = 0;

        int rows = land.length;
        int cols = land[0].length;

        Deque<int[]> queue = new ArrayDeque<>();
        queue.offer(new int[]{startX, startY});
        visited[startX][startY] = true;

        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int currX = current[0];
            int currY = current[1];

            minCol = Math.min(minCol, currY);
            maxCol = Math.max(maxCol, currY);

            int[][] directions = {{0, -1}, {0, 1}, {-1, 0}, {1, 0}};
            for (int[] dir : directions) {
                int nextX = currX + dir[0];
                int nextY = currY + dir[1];

                if (nextX >= 0 && nextX < rows && nextY >= 0 && nextY < cols &&
                    !visited[nextX][nextY] && land[nextX][nextY] > 0) {
                    queue.offer(new int[]{nextX, nextY});
                    visited[nextX][nextY] = true;
                    oilCount++;
                }
            }
        }

        return new int[]{minCol, maxCol, oilCount};
    }
}