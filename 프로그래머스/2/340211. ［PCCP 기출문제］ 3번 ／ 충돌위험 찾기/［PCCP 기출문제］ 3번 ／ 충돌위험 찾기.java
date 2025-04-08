import java.util.*;

class Solution {
    private Map<Integer, Map<String, Integer>> timeLineMap = new HashMap<>();
    private int time;
   
    public int solution(int[][] points, int[][] routes) {
        int totalDangerCount = 0;
        int targetPointCount = routes[0].length;
        
        for (int[] route : routes) {
             time = 0;
             int count = 0;
             for (int i = 0; i < targetPointCount - 1; i++) {
                int[] startPoint = points[route[i] - 1];
                int[] endPoint = points[route[i + 1] - 1];

                int sx = startPoint[0], sy = startPoint[1];
                int ex = endPoint[0], ey = endPoint[1];

                move(count, sx, sy, ex, ey);
                count ++;
            }
        }

        return getDangerCount();
    }

    private void move(int count, int sx, int sy, int ex, int ey) {
        if(count == 0) {
            Map<String, Integer> positionMap = timeLineMap
                .computeIfAbsent(time, k -> new HashMap<>());
            String position = sx + "," + sy;
            positionMap.put(position, positionMap.getOrDefault(position, 0) + 1);
            time++;
        }
        
        int xMoveCount = Math.abs(ex - sx);
        int xDirection = Integer.compare(ex, sx);

        for (int i = 0; i < xMoveCount; i++) {
            sx += xDirection;
            Map<String, Integer> posMap = timeLineMap
                .computeIfAbsent(time, k -> new HashMap<>());
            String pos = sx + "," + sy;
            posMap.put(pos, posMap.getOrDefault(pos, 0) + 1);
            time++;
        }

        int yMoveCount = Math.abs(ey - sy);
        int yDirection = Integer.compare(ey, sy); 

        for (int i = 0; i < yMoveCount; i++) {
            sy += yDirection;
            Map<String, Integer> posMap = timeLineMap
                .computeIfAbsent(time, k -> new HashMap<>());
            String pos = sx + "," + sy;
            posMap.put(pos, posMap.getOrDefault(pos, 0) + 1);
            time++;
        }
    }

    private int getDangerCount() {
        int dangerCount = 0;

        for (Map<String, Integer> positionMap : timeLineMap.values()) {
            for (Map.Entry<String, Integer> entry : positionMap.entrySet()) {
                if (entry.getValue() > 1) {
                    dangerCount++;
                }
            }
        }

        return dangerCount;
    }
}
