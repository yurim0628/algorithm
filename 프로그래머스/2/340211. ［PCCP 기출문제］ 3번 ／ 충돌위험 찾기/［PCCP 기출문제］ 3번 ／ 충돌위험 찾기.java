import java.util.*;

class Solution {
    private Map<Integer, Map<String, Integer>> timeLineMap = new HashMap<>();

    public int solution(int[][] points, int[][] routes) {
        for (int[] route : routes) {
            Robot robot = new Robot(points, route, timeLineMap);
            robot.moveAll();
        }

        return getTotalDangerCount();
    }

    private int getTotalDangerCount() {
        return (int) timeLineMap.values().stream()
            .flatMap(positionMap -> positionMap.values().stream())
            .filter(dangerCount -> dangerCount > 1)
            .count();
    }
}

class Robot {
    private int timestamp = 0;
    private int x, y;
    private int[][] points;
    private int[] route;
    private Map<Integer, Map<String, Integer>> timeLineMap;

    public Robot(int[][] points, int[] route, Map<Integer, Map<String, Integer>> timeLineMap) {
        this.points = points;
        this.route = route;
        this.timeLineMap = timeLineMap;
    }

    public void moveAll() {
        for (int i = 0; i < route.length - 1; i++) {
            int[] start = points[route[i] - 1];
            int[] end = points[route[i + 1] - 1];
            move(start, end, i == 0);
        }
    }

    private void move(int[] start, int[] end, boolean isFirst) {
        int sx = start[0], sy = start[1];
        int ex = end[0], ey = end[1];

        if (isFirst) {
            this.x = sx;
            this.y = sy;
            recordPosition();
        }

        int dx = Integer.compare(ex, sx);
        while (x != ex) {
            x += dx;
            recordPosition();
        }

        int dy = Integer.compare(ey, sy);
        while (y != ey) {
            y += dy;
            recordPosition();
        }
    }

    private void recordPosition() {
        String pos = x + "," + y;
        timeLineMap
            .computeIfAbsent(timestamp, k -> new HashMap<>())
            .merge(pos, 1, Integer::sum);
        timestamp++;
    }
}
