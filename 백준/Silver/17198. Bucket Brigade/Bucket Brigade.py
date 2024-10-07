from collections import deque

def bfs(sx, sy, graph, visited):
    queue = deque([(sx, sy)])  
    visited[sx][sy] = 1
    while queue:
        cx, cy = queue.popleft()
        if graph[cx][cy] == 'L':
            return visited[cx][cy] - 2
        for dx, dy in ([0, -1], [0, 1], [-1, 0], [1, 0]):
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < 10 and 0 <= ny < 10 and not visited[nx][ny] and graph[nx][ny] != 'R':
                queue.append((nx, ny))
                visited[nx][ny] = visited[cx][cy] + 1

graph = [list(input()) for _ in range(10)]  
visited = [[0] * 10 for _ in range(10)]

for i in range(10):
    for j in range(10):
        if graph[i][j] == 'B':
            print(bfs(i, j, graph, visited)) 
