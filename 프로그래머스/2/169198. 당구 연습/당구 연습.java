import java.util.*;

class Solution {
    public static int[] solution(int m, int n, int startX, int startY, int[][] balls) {
        int[] answer = new int[balls.length];

        Point board = new Point(m, n);
        Point start = new Point(startX, startY);

        for (int i = 0; i < balls.length; i++) {
            Point ball = new Point(balls[i][0], balls[i][1]);
            List<Point> symPoints = symmetricTransposition(board, start, ball);

            int minDistance = Integer.MAX_VALUE;
            for (Point sym : symPoints) {
                int dist = calculationDistance(start, sym);
                if (dist < minDistance) {
                    minDistance = dist;
                }
            }
            answer[i] = minDistance;
        }

        return answer;
    }

    private static List<Point> symmetricTransposition(Point board, Point start, Point ball) {
        List<Point> syms = new ArrayList<>();

        int bx = ball.x, by = ball.y;
        int sx = start.x, sy = start.y;

        if (!(sx == bx && sy > by)) syms.add(new Point(bx, -by));
        if (!(sx == bx && sy < by)) syms.add(new Point(bx, 2 * board.y - by));
        if (!(sx < bx && sy == by)) syms.add(new Point(2 * board.x - bx, by));
        if (!(sx > bx && sy == by)) syms.add(new Point(-bx, by));

        return syms;
    }

    private static int calculationDistance(Point p1, Point p2) {
        int dx = p1.x - p2.x;
        int dy = p1.y - p2.y;
        return dx * dx + dy * dy;
    }

    private static class Point {
        int x, y;
        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}
