import java.util.*;

class Solution {
    public int solution(int n, int[][] costs) {
        List<List<int[]>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }

        for (int[] edge : costs) {
            int from = edge[0];
            int to = edge[1];
            int cost = edge[2];
            graph.get(from).add(new int[]{to, cost});
            graph.get(to).add(new int[]{from, cost});
        }

        boolean[] visited = new boolean[n];
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[1]));
        int totalCost = 0;

        visited[0] = true;
        for (int[] neighbor : graph.get(0)) {
            pq.offer(neighbor);
        }

        while (!pq.isEmpty()) {
            int[] current = pq.poll();
            int to = current[0];
            int cost = current[1];

            if (visited[to]) continue;

            visited[to] = true;
            totalCost += cost;

            for (int[] neighbor : graph.get(to)) {
                if (!visited[neighbor[0]]) {
                    pq.offer(neighbor);
                }
            }
        }

        return totalCost;
    }
}
