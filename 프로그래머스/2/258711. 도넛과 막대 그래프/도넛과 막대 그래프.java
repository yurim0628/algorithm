import java.util.*;

class Solution {
    public int[] solution(int[][] edges) {
        int[] result = new int[4];

        Set<Integer> nodeSet = new HashSet<>();
        Map<Integer, List<Integer>> outgoingMap = new HashMap<>();
        Map<Integer, List<Integer>> incomingMap = new HashMap<>();

        buildGraph(edges, nodeSet, outgoingMap, incomingMap);

        int maxNode = Collections.max(nodeSet);
        boolean[] visited = new boolean[maxNode + 1];

        int rootNode = findRootNode(nodeSet, outgoingMap, incomingMap, visited);
        result[0] = rootNode;

        result[2] = countEndNodes(nodeSet, outgoingMap, visited);
        result[3] = countFigureEightGraphs(nodeSet, outgoingMap, incomingMap, visited);
        result[1] = countCycleGraphs(nodeSet, outgoingMap, visited);

        return result;
    }

    private void buildGraph(int[][] edges, Set<Integer> nodeSet,
                            Map<Integer, List<Integer>> outgoingMap,
                            Map<Integer, List<Integer>> incomingMap) {
        for (int[] edge : edges) {
            int from = edge[0];
            int to = edge[1];

            nodeSet.add(from);
            nodeSet.add(to);

            outgoingMap.computeIfAbsent(from, k -> new ArrayList<>()).add(to);
            incomingMap.computeIfAbsent(to, k -> new ArrayList<>()).add(from);
        }
    }

    private int findRootNode(Set<Integer> nodeSet,
                             Map<Integer, List<Integer>> outgoingMap,
                             Map<Integer, List<Integer>> incomingMap,
                             boolean[] visited) {
        for (int node : nodeSet) {
            int out = outgoingMap.getOrDefault(node, Collections.emptyList()).size();
            int in = incomingMap.getOrDefault(node, Collections.emptyList()).size();

            if (out >= 2 && in == 0) {
                visited[node] = true;
                for (int child : outgoingMap.get(node)) {
                    incomingMap.get(child).remove((Integer) node);
                }
                return node;
            }
        }
        return -1;
    }

    private int countEndNodes(Set<Integer> nodeSet,
                              Map<Integer, List<Integer>> outgoingMap,
                              boolean[] visited) {
        int count = 0;
        for (int node : nodeSet) {
            if (outgoingMap.getOrDefault(node, Collections.emptyList()).isEmpty()) {
                visited[node] = true;
                count++;
            }
        }
        return count;
    }

    private int countFigureEightGraphs(Set<Integer> nodeSet,
                                       Map<Integer, List<Integer>> outgoingMap,
                                       Map<Integer, List<Integer>> incomingMap,
                                       boolean[] visited) {
        int count = 0;
        for (int node : nodeSet) {
            int out = outgoingMap.getOrDefault(node, Collections.emptyList()).size();
            int in = incomingMap.getOrDefault(node, Collections.emptyList()).size();

            if (out == 2 && in == 2 && !visited[node]) {
                visited[node] = true;
                for (int next : outgoingMap.get(node)) {
                    traverse(next, outgoingMap, visited);
                }
                count++;
            }
        }
        return count;
    }

    private int countCycleGraphs(Set<Integer> nodeSet,
                                 Map<Integer, List<Integer>> outgoingMap,
                                 boolean[] visited) {
        int count = 0;
        for (int node : nodeSet) {
            if (!visited[node] &&
                outgoingMap.getOrDefault(node, Collections.emptyList()).size() == 1) {
                if (isCycle(node, outgoingMap, visited)) {
                    count++;
                }
            }
        }
        return count;
    }

    private boolean isCycle(int start, Map<Integer, List<Integer>> outgoingMap, boolean[] visited) {
        int current = start;
        while (!visited[current]) {
            visited[current] = true;
            List<Integer> nextList = outgoingMap.getOrDefault(current, Collections.emptyList());
            if (nextList.isEmpty()) return false;
            current = nextList.get(0);
        }
        return current == start;
    }

    private void traverse(int node, Map<Integer, List<Integer>> outgoingMap, boolean[] visited) {
        while (!visited[node]) {
            visited[node] = true;
            List<Integer> nextList = outgoingMap.getOrDefault(node, Collections.emptyList());
            if (nextList.isEmpty()) break;
            node = nextList.get(0);
        }
    }
}
