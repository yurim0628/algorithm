import java.util.*;

class Solution {

    public int solution(String[] storage, String[] requests) {
        int n = storage.length;
        int m = storage[0].length();
        
        int totalContainersLeft = n * m;
        
        char[][] storageArray = new char[n][m];
        for (int i = 0; i < n; i++) {
            storageArray[i] = storage[i].toCharArray();
        }

        for (String request : requests) {
            char targetContainer = request.charAt(0);  
            
            EquipmentManager manager = EquipmentManager.find(request.length());  
            Equipment equipment = manager.createEquipment();  
            
            int removedContainersCount = equipment.removeContainers(storageArray, n, m, targetContainer);
            totalContainersLeft -= removedContainersCount;
        }

        return totalContainersLeft;
    }
}

enum EquipmentManager {
    FORKLIFT(1, Forklift::new),
    CRANE(2, Crane::new);

    private final int length;
    private final EquipmentCreator creator;

    EquipmentManager(int length, EquipmentCreator creator) {
        this.length = length;
        this.creator = creator;
    }

    @FunctionalInterface
    public interface EquipmentCreator {
        Equipment create();
    }

    public static EquipmentManager find(int length) {
        return Arrays.stream(EquipmentManager.values())
                .filter(e -> e.length == length)
                .findFirst()
                .orElseThrow(() -> new IllegalArgumentException("존재하지 않는 장비 타입입니다."));
    }

    public Equipment createEquipment() {
        return creator.create();
    }
}

interface Equipment {
    int removeContainers(char[][] storageArray, int n, int m, char targetContainer);
}

class Crane implements Equipment {

    @Override
    public int removeContainers(char[][] storageArray, int n, int m, char targetContainer) {
        int removedContainersCount = 0;
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (storageArray[i][j] == targetContainer) {
                    storageArray[i][j] = ' '; 
                    removedContainersCount++; 
                }
            }
        }
        
        return removedContainersCount; 
    }
}

class Forklift implements Equipment {

    @Override
    public int removeContainers(char[][] storageArray, int n, int m, char targetContainer) {
        Deque<int[]> positionsToRemove = new ArrayDeque<>();
        int removedContainersCount = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (storageArray[i][j] == targetContainer) {
                    boolean isRemoved = bfs(storageArray, i, j, n, m);
                    if (isRemoved) {
                        positionsToRemove.offer(new int[]{i, j});
                    }
                }
            }
        }

        while (!positionsToRemove.isEmpty()) {
            int[] position = positionsToRemove.poll(); 
            storageArray[position[0]][position[1]] = ' ';  
            removedContainersCount++;
        }
        
        return removedContainersCount;
    }

    private boolean bfs(char[][] storage, int sx, int sy, int n, int m) {
        Deque<int[]> queue = new ArrayDeque<>();
        boolean[][] visited = new boolean[n][m];

        queue.offer(new int[]{sx, sy});
        visited[sx][sy] = true;

        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int cx = current[0];
            int cy = current[1];

            int[][] directions = {{0, -1}, {0, 1}, {-1, 0}, {1, 0}};
            for (int[] direction : directions) {
                int nx = cx + direction[0];
                int ny = cy + direction[1];
                
                if (nx < 0 || nx >= n || ny < 0 || ny >= m)  {
                    return true; 
                }

                if (!visited[nx][ny] && storage[nx][ny] == ' ') {
                    visited[nx][ny] = true;
                    queue.offer(new int[]{nx, ny});
                }
            }
        }
        
        return false;
    }
}