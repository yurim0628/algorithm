from collections import deque

def bfs(sx, sy, graph, visited):
    queue = deque([(sx, sy)])
    visited[sx][sy] = True
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]) and not visited[nx][ny] and graph[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = True

T = int(input())
results = []
for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * N for _ in range(M)]
    visited = [[False] * N for _ in range(M)]

    for _ in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1

    count = 0
    for sx in range(M):
        for sy in range(N):
            if graph[sx][sy] == 1 and not visited[sx][sy]:
                bfs(sx, sy, graph, visited)
                count += 1

    results.append(count)

print('\n'.join(map(str, results)))
